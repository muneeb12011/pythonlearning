import sys
import tracemalloc
from array import array

N = 5_000_000

tracemalloc.start()
a = list(range(N))
cur, _ = tracemalloc.get_traced_memory()
print(f"list of ints: {cur / 1e6:.0f} MB (pointer array alone: {sys.getsizeof(a) / 1e6:.0f} MB)")
tracemalloc.stop()

tracemalloc.start()
b = array("q", range(N))
cur, _ = tracemalloc.get_traced_memory()
print(f"array('q'):   {cur / 1e6:.0f} MB")
tracemalloc.stop()

# Watch the over-allocation pattern during appends
c, last = [], -1
for i in range(100):
    c.append(i)
    size = sys.getsizeof(c)
    if size != last:
        print(f"len={len(c):>3}  bytes={size}")
        last = size