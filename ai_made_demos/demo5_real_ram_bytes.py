"""Look at the REAL bytes in RAM behind Python ints, lists and tuples.
Works on CPython 3.x, 64-bit. We read raw memory at the object's address with ctypes.
id(obj) in CPython is the address of the object in RAM (a virtual address)."""
import ctypes
import platform
import struct
import sys

assert platform.python_implementation() == "CPython", "id() is an address only in CPython"
assert struct.calcsize("P") == 8, "this demo assumes a 64-bit Python"
print("Python", sys.version.split()[0])


def raw(addr, n):
    return ctypes.string_at(addr, n)          # read n real bytes starting at addr


def hexs(b):
    return " ".join(f"{x:02x}" for x in b)    # bytes as hex, in the order stored in RAM


def Q(b, off=0):
    return struct.unpack_from("<Q", b, off)[0]  # 8 bytes -> unsigned number (little-endian)


def S(b, off=0):
    return struct.unpack_from("<q", b, off)[0]  # 8 bytes -> signed number


def title(t):
    print("\n" + "=" * 68 + f"\n{t}\n" + "=" * 68)


# ------------------------------------------------------------------
title("1. The int object 10 and 15: the real bytes")
for val in (10, 15):
    a = id(val)
    b = raw(a, 28)
    print(f"\nint {val} lives at address {a} ({hex(a)}), size {sys.getsizeof(val)} bytes")
    print(f"  bytes  0-7  : {hexs(b[0:8])}   reference count = {Q(b, 0)}")
    print(f"  bytes  8-15 : {hexs(b[8:16])}   pointer to the type 'int' = {Q(b, 8)}  (id(int) = {id(int)})")
    print(f"  bytes 16-23 : {hexs(b[16:24])}   size/sign word = {Q(b, 16)}")
    print(f"  bytes 24-27 : {hexs(b[24:28])}   THE NUMBER ITSELF = {struct.unpack_from('<I', b, 24)[0]}")
print("\nSo the number is only 4 of the 28 bytes. The rest is bookkeeping about the object.")


# ------------------------------------------------------------------
title("2. x = 10 then x = 15: arrows are counted INSIDE the object")


def refcount(addr):
    return Q(raw(addr, 8))


x = int("100000")                      # a fresh object, not a cached one
old = id(x)
print(f"x = 100000  -> object at {old}, its reference count (read from RAM) = {refcount(old)}")
y = x
print(f"y = x       -> same object, reference count = {refcount(old)}  (two names point to it)")
x = int("200000")
new = id(x)
print(f"x = 200000  -> x now points to {new}")
print(f"   old object's count = {refcount(old)}  (only y still points to it)")
print(f"   new object's count = {refcount(new)}")
del y
print(f"del y       -> the old object's count would now be 0 -> Python frees that memory.")
print("(We do not read the old address now: that memory has been given back.)")


# ------------------------------------------------------------------
title("3. A list: the header, and the separate array of pointers")


def list_header(lst):
    h = raw(id(lst), 40)
    return {"refcnt": Q(h, 0), "type": Q(h, 8), "len": S(h, 16), "items_ptr": Q(h, 24), "allocated": S(h, 32)}


def list_pointers(lst):
    h = list_header(lst)
    return list(struct.unpack(f"<{h['len']}Q", raw(h["items_ptr"], 8 * h["len"])))


lst = [10, 20, 30]
h = list_header(lst)
print(f"list object at {id(lst)}, size {sys.getsizeof(lst)} bytes")
print(f"  length (ob_size)      = {h['len']}")
print(f"  pointer to the array  = {h['items_ptr']}   <- the arrows live in a SEPARATE block of RAM")
print(f"  allocated slots       = {h['allocated']}")
ptrs = list_pointers(lst)
print("\nThe array at that address holds these 8-byte pointers:")
for i, (p, item) in enumerate(zip(ptrs, lst)):
    print(f"  slot {i}: {p}   id({item}) = {id(item)}   match: {p == id(item)}")

print("\nNow: lst[0] = 99")
before_items_ptr = h["items_ptr"]
lst[0] = 99
h2 = list_header(lst)
ptrs2 = list_pointers(lst)
print(f"  list object address : {id(lst)} (same)")
print(f"  array address       : {h2['items_ptr']} (same: {h2['items_ptr'] == before_items_ptr})")
print(f"  slot 0 pointer      : {ptrs[0]} -> {ptrs2[0]}   (now id(99) = {id(99)})")
print(f"  slots 1, 2          : unchanged: {ptrs[1:] == ptrs2[1:]}")
print("  Nothing was edited inside the object 10. One 8-byte pointer was overwritten.")

print("\nNow keep appending and watch the array move (the resize from your first lesson):")
last_ptr, last_alloc = h2["items_ptr"], h2["allocated"]
print(f"  len=3  allocated={last_alloc}  array at {last_ptr}")
for i in range(3, 14):
    lst.append(i)
    hh = list_header(lst)
    if hh["items_ptr"] != last_ptr or hh["allocated"] != last_alloc:
        print(f"  len={hh['len']:<2} allocated={hh['allocated']:<2} array at {hh['items_ptr']}  <- grew, array moved")
        last_ptr, last_alloc = hh["items_ptr"], hh["allocated"]
print(f"  The list object itself never moved: still {id(lst)}")


# ------------------------------------------------------------------
title("4. A tuple: the pointers sit INSIDE the object, right after the header")
t = (10, 20, 30)
b = raw(id(t), 24 + 8 * 3)
print(f"tuple at {id(t)}, size {sys.getsizeof(t)} bytes")
print(f"  length (ob_size) = {S(b, 16)}")
tptrs = list(struct.unpack_from("<3Q", b, 24))
for i, (p, item) in enumerate(zip(tptrs, t)):
    print(f"  pointer {i} at offset {24 + 8 * i}: {p}   id({item}) = {id(item)}   match: {p == id(item)}")
print("  No separate array, and no spare slots. That is why a tuple cannot grow or change.")


# ------------------------------------------------------------------
title("5. tuple -> list: which bytes get copied?")
l = list(t)
lh = list_header(l)
lptrs = list_pointers(l)
print(f"tuple at {id(t)}, its pointers start at {id(t) + 24}")
print(f"list  at {id(l)}, its pointer array is at {lh['items_ptr']}")
print(f"tuple pointers: {tptrs}")
print(f"list  pointers: {lptrs}")
print(f"identical pointer values: {tptrs == lptrs}")
print("-> a NEW header and a NEW pointer array were built. The objects 10, 20, 30 were NOT copied.")


# ------------------------------------------------------------------
title("6. Where in RAM is this? (your OS lesson: virtual addresses)")


def region(addr):
    try:
        with open("/proc/self/maps") as f:
            for line in f:
                span, perms, *rest = line.split()
                lo, hi = (int(v, 16) for v in span.split("-"))
                if lo <= addr < hi:
                    # fields: offset dev inode [path]; no path means anonymous memory
                    return f"{span} {perms} {rest[3] if len(rest) > 3 else '(anonymous memory)'}"
    except OSError:
        return "(needs Linux: /proc/self/maps)"
    return "(not found)"


print("list object   :", region(id(lst)))
print("its array     :", region(list_header(lst)["items_ptr"]))
print("int 10 object :", region(id(10)))
