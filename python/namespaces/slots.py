import tracemalloc

class A:
    def __init__(self):
        self.a = 1
        self.b = 2

class B:
    __slots__ = ("a", "b")
    def __init__(self):
        self.a = 1
        self.b = 2

for cls in (A, B):
    tracemalloc.start()
    items = [cls() for _ in range(100_000)]
    print(cls.__name__, tracemalloc.get_traced_memory()[0] // 1024, "KB")
    tracemalloc.stop()

print(hasattr(A(), "__dict__"), hasattr(B(), "__dict__"))
