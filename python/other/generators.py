import sys

def squares_list(n):
    return [i * i for i in range(n)]

def squares_gen(n):
    for i in range(n):
        yield i * i

print("list :", sys.getsizeof(squares_list(1_000_000)), "bytes")
print("gen  :", sys.getsizeof(squares_gen(1_000_000)), "bytes")
print(sum(squares_gen(1_000_000)))
