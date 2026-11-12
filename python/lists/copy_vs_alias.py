a = [1, 2, 3]
b = a

a.append(4)

print(a)
print(b)
print(a is b)

a = [1, 2, 3]
b = a.copy()

a.append(4)

print(a)
print(b)
print(a is b)



a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)
print(b)
print(a is b)
print(a[0] is b[0])


import copy  

a = [[1, 2, 3], [4, 5, 6]]

#creating a shallow copy of the nested list 
b = copy.copy(a) #deepcopy() 

# modifying an element in the shallow copied list
b[0][0] = 99

# Printing the original and shallo wcopied lists  
print("b: ", b) 
print("a: ", a)

a = [1, 2, 3]
b = a

a.append(4)

print(a)
print(b)
print(a is b)

a = [1, 2, 3]
b = a.copy()

a.append(4)

print(a)
print(b)
print(a is b)

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)
print(b)
print(a is b)
print(a[0] is b[0])

x = 10
y = x

x = 20

print(y)


print("x:", x)
print("y:", y)
