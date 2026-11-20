a = [1, 1, 2, 2, 3, 4, 5, 5, 6]
del a[1:5]
print(a)

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])


names = ["alice", "alice", "net", "john"]
print(list(set(names)))

names = [1, 1, 2, 3, 4, 4, 5]
print(list(set(names)))


list = [1, 2, 3, 4, 5]
list = list.pop(3)
print(list)

list = [1, 2, 3, 4, 5,]
list.remove(2)
print(list)

list = ["apple", "banana", "cherry"]
list.clear()
print(list)

#sor
list = ["cherry", "apple", "banana", "orange"]
list.sort()
print(list)

# del, delete used to remove an item from a list by index and also we can slice thee list to remove
list = ["cherry", "apple", "banana", "orange"]
del list[1:3]
print(list)


a = [10, 20, 30]

x = a.pop()

print(a)
print(x)