import os, psutil   # pip install psutil

p = psutil.Process(os.getpid())
print("before:", p.memory_info().rss / 1e6, "MB")
data = list(range(5_000_000))
print("after: ", p.memory_info().rss / 1e6, "MB")