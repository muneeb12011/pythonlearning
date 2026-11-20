"""A real RAM map: how pointers LOOK in memory (CPython 3.12+, 64-bit).
Each row = real address | the real bytes stored there | what those bytes mean."""
import ctypes
import gc
import struct
import sys

gc.disable()


def raw(addr, n):
    return ctypes.string_at(addr, n)


def hexs(b):
    return " ".join(f"{x:02x}" for x in b)


def Q(b, off=0):
    return struct.unpack_from("<Q", b, off)[0]


# Three fresh int objects (created at runtime, so they live in normal heap RAM)
a = int("1000")
b = int("2000")
c = int("3000")
lst = [a, b, c]
t = (a, b, c)

names = {
    id(a): "int a (1000)", id(b): "int b (2000)", id(c): "int c (3000)",
    id(lst): "the list object", id(t): "the tuple object",
    id(int): "type 'int'", id(list): "type 'list'", id(tuple): "type 'tuple'",
}


def row(addr, nbytes, meaning):
    print(f"  {addr:#x} | {hexs(raw(addr, nbytes)):<23} | {meaning}")


def pointer_row(addr, label):
    value = Q(raw(addr, 8))
    target = names.get(value, "(something else)")
    print(f"  {addr:#x} | {hexs(raw(addr, 8)):<23} | {label}: pointer to {value:#x} = {target}")


def title(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


print("Reading: each pointer is just an 8-byte NUMBER = the address of the object it points to.")
print("Bytes are stored 'little-endian': the LAST digits of the address come FIRST.")

# ------------------------------------------------------------------
title("1. The three int objects")
for label, addr in (("a", id(a)), ("b", id(b)), ("c", id(c))):   # addresses only: no extra arrows
    print(f"\nint {label} at {addr:#x}  ({names[addr]})")
    row(addr, 8, "reference count (how many arrows point HERE)")
    pointer_row(addr + 8, "type")
    row(addr + 16, 8, "size/sign word")
    row(addr + 24, 4, f"THE NUMBER = {struct.unpack_from('<I', raw(addr + 24, 4))[0]}")

# ------------------------------------------------------------------
title("2. The LIST: header + a separate array of pointers")
addr = id(lst)
hdr = raw(addr, 40)
items = Q(hdr, 24)
print(f"\nlist object at {addr:#x}")
row(addr, 8, "reference count")
pointer_row(addr + 8, "type")
row(addr + 16, 8, f"length = {Q(hdr, 16)}")
pointer_row(addr + 24, "ob_item")   # shows where the array lives
row(addr + 32, 8, f"allocated slots = {Q(hdr, 32)}")
print(f"\nThe pointer array (a different block of RAM) at {items:#x}:")
for i in range(3):
    pointer_row(items + 8 * i, f"slot {i}")

# ------------------------------------------------------------------
title("3. The TUPLE: the pointers sit right after the header")
addr = id(t)
print(f"\ntuple object at {addr:#x}")
row(addr, 8, "reference count")
pointer_row(addr + 8, "type")
row(addr + 16, 8, f"length = {Q(raw(addr, 24), 16)}")
for i in range(3):
    pointer_row(addr + 24 + 8 * i, f"item {i}")

# ------------------------------------------------------------------
title("4. How many arrows point to each int? (read from RAM)")
for label, addr in (("a", id(a)), ("b", id(b)), ("c", id(c))):
    print(f"  int {label}: reference count = {Q(raw(addr, 8))}")
print("  (the name + the list slot + the tuple slot = 3 arrows for each)")

# ------------------------------------------------------------------
title("5. lst[0] = c  -> watch the bytes of slot 0 change")
slot0 = items
before_bytes = raw(slot0, 8)
rc_a, rc_c = Q(raw(id(a), 8)), Q(raw(id(c), 8))
lst[0] = c
after_bytes = raw(slot0, 8)
print(f"  slot 0 BEFORE: {hexs(before_bytes)}  -> {names[Q(before_bytes)]}")
print(f"  slot 0 AFTER : {hexs(after_bytes)}  -> {names[Q(after_bytes)]}")
print(f"  int a count: {rc_a} -> {Q(raw(id(a), 8))}      int c count: {rc_c} -> {Q(raw(id(c), 8))}")
print("  Only 8 bytes were overwritten. The int objects themselves did not change.")

# ------------------------------------------------------------------
title("6. Drawing of what you just saw (real addresses)")
print(f"""
  name a ───────────────────────────────→ [ int 1000 @ {id(a):#x} ]
  name b ───────────────────────────────→ [ int 2000 @ {id(b):#x} ]
  name c ───────────────────────────────→ [ int 3000 @ {id(c):#x} ]

  list @ {id(lst):#x}  ──ob_item──→  array @ {items:#x}
        slot 0 = {Q(raw(items, 8)):#x}   (now points to c)
        slot 1 = {Q(raw(items + 8, 8)):#x}   (b)
        slot 2 = {Q(raw(items + 16, 8)):#x}   (c)

  tuple @ {id(t):#x}   (pointers stored inside it)
        item 0 = {Q(raw(id(t) + 24, 8)):#x}   (a)
        item 1 = {Q(raw(id(t) + 32, 8)):#x}   (b)
        item 2 = {Q(raw(id(t) + 40, 8)):#x}   (c)
""")
