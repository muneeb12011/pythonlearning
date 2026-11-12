import time, random
import numpy as np   # pip install numpy

N = 5_000_000
lst = list(range(N))
shuf = lst[:]
random.shuffle(shuf)
arr = np.arange(N, dtype=np.int64)

def t(label, f):
    s = time.perf_counter(); f()
    print(f"{label}: {time.perf_counter() - s:.3f} s")

t("list in order ", lambda: sum(lst))
t("list shuffled ", lambda: sum(shuf))
t("numpy array   ", lambda: arr.sum())

m = np.zeros((4000, 4000), dtype=np.int64)   # ~128 MB
t("2D by rows    ", lambda: sum(m[i, :].sum() for i in range(4000)))
t("2D by columns ", lambda: sum(m[:, j].sum() for j in range(4000)))