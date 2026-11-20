"""Demo 2: leak vs spike, and how tracemalloc finds the guilty line."""
import tracemalloc

tracemalloc.start()


def mb(n):
    return f"{n / 1e6:7.1f} MB"


# ---------- LEAK: something keeps a reference forever ----------
cache = []  # global list = classic leak


def handle_request(i):
    result = "x" * 100_000  # pretend this is a response
    cache.append(result)  # BUG: never removed, so it can never be freed


snap_before = tracemalloc.take_snapshot()
print("LEAK: memory after every 500 requests (it only goes UP)")
for i in range(1, 2001):
    handle_request(i)
    if i % 500 == 0:
        current, _ = tracemalloc.get_traced_memory()
        print(f"  request {i:>4}: {mb(current)}")

snap_after = tracemalloc.take_snapshot()
print("\ntracemalloc says THIS line grew the most:")
for stat in snap_after.compare_to(snap_before, "lineno")[:1]:
    print(" ", stat)

cache.clear()  # the fix: stop holding references
current, _ = tracemalloc.get_traced_memory()
print(f"\nafter cache.clear(): {mb(current)}  (back down, so it was a leak)")

# ---------- SPIKE: one operation needs a lot at once ----------
tracemalloc.reset_peak()
big = list(range(3_000_000))  # one big load
current, peak = tracemalloc.get_traced_memory()
print(f"\nSPIKE: while loaded: current={mb(current)}, peak={mb(peak)}")
del big
current, peak = tracemalloc.get_traced_memory()
print(f"after del big    : current={mb(current)}, peak still remembers {mb(peak)}")
print("A spike goes up then comes back down. A leak never comes back down.")
