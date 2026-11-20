a = [10, 20, 30, 40, 50]

print(a[0])
print(a[-1])
print(a[1:4])
print(a[:3])
print(a[3:])
print(a[::-1])

# is slicing a new object?
b = a[:]
print(a is b)  

# is it shallow?
nested = [[1, 2], [3, 4]]
shallow = nested[:]
shallow[0].append(99)
print(nested)   # first inner list changed too