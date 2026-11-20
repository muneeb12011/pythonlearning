import tracemalloc, os, psutil

tracemalloc.start()
p = psutil.Process(os.getpid())

cache = []                       #   leak grows forever
def handle_request(i):
    cache.append("x" * 100_000)  # keeps 100 KB perr request never freed

snap1 = tracemalloc.take_snapshot()
for i in range(2000):
    handle_request(i)
snap2 = tracemalloc.take_snapshot()

print("process RSS:", p.memory_info().rss / 1e6, "MB")
for stat in snap2.compare_to(snap1, "lineno")[:3]:
    print(stat)                  # shows WHICH line grew