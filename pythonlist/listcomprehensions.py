numbers = [1, 2, 3, 4]

# normal loop
squares = []
for x in numbers:
    squares.append(x * x)

# comprehension - same result, one line
squares = [x * x for x in numbers]

a = [1, 2, 3]
b = a
c = a.copy()

b.append(4)
c.append(5)

print(a)
print(b)
print(c)
print(a is b)
print(a is c)

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)              # [[1, 2, 99], [3, 4]]
print(b)              # [[1, 2, 99], [3, 4]]
print(a is b)          # False
print(a[0] is b[0])    # True