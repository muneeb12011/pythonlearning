a = [1, 2, 3]
b = a
a.append(4)

print(a)


a = [1, 2, 3]
b = a

a[0] = 99

print(a)
print(b)

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)
print(b)

list = [1, 2 , 4, 5 ,6 ,6]
