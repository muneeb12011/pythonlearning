import tracemalloc
tracemalloc.start()

before = tracemalloc.take_snapshot()      # photo of memory now

cache = []
for i in range(1000):
    cache.append("x" * 100_000)           # each one is100 KB

after = tracemalloc.take_snapshot()       # photo of memory later

for stat in after.compare_to(before, "lineno")[:1]:
    print(stat)                           # which line grew the most