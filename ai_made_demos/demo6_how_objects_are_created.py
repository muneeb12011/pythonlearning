"""How Python objects get CREATED in RAM (CPython 3.12+, 64-bit)."""
import dis
import gc
import sys


def title(t):
    print("\n" + "=" * 66 + f"\n{t}\n" + "=" * 66)


title("1. What the bytecode does for each line")
for src in ["x = 10", "t = (10, 20, 30)", "t = (a, b, c)", "lst = [a, b, c]", "l = list(t)"]:
    print(f"\n--- {src}")
    dis.dis(compile(src, "<s>", "exec"))

title("2. Literals are made BEFORE the program runs (compile time)")
code = compile("x = 1000", "<s>", "exec")
print("constants kept inside the compiled code:", code.co_consts)
ns = {}
exec(code, ns)
print("x points to that very object:", ns["x"] is code.co_consts[0])
print("a literal tuple is also pre-built:", compile("t = (10, 20, 30)", "<s>", "exec").co_consts[0])

title("3. How many separate blocks of RAM does each creation need?")
gc.disable()
a, b, c = 10, 20, 30
N = 2000


def count(make):
    keep = [None] * N                 # pre-sized, so the keeper itself does not allocate
    n0 = sys.getallocatedblocks()
    for i in range(N):
        keep[i] = make()              # make N objects and keep them alive
    n1 = sys.getallocatedblocks()
    return n1 - n0, keep


tl, k1 = count(lambda: (a, b, c))
ll, k2 = count(lambda: [a, b, c])
print(f"tuple (a,b,c): {tl / N:.2f} block per object   (the pointers are inside it)")
print(f"list  [a,b,c]: {ll / N:.2f} blocks per object  (header + a separate pointer array)")
print("sizes reported:", sys.getsizeof(k1[0]), "bytes (tuple),", sys.getsizeof(k2[0]), "bytes (list)")

title("4. Python's own memory manager (small objects, 512 bytes or less)")
print("Printing Python's allocator report (the arena and pool lines are the important ones):\n")
sys._debugmallocstats()
