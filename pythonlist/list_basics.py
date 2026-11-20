# LIST BASICS - 5 small steps
# Run this file and read the output under each step.


# ---------- Step 1: a list is a row of items in order ----------
fruits = ["apple", "banana", "mango"]
print("Step 1:", fruits)


# ---------- Step 2: get one item by position (starts at 0) ----------
print("Step 2:")
print(fruits[0])     # apple  (first item)
print(fruits[1])     # banana (second item)
print(fruits[-1])    # mango  (last item)


# ---------- Step 3: add and remove ----------
fruits.append("orange")    # add at the end
fruits.remove("banana")    # remove by name
print("Step 3:", fruits)   # ['apple', 'mango', 'orange']


# ---------- Step 4: change an item ----------
fruits[2] = "grapes"       # replace the item at whatever position you want by entering a new value in[]
print("Step 4:", fruits)   # ['grapes', 'mango', 'orange']


# ---------- Step 5: loop through it --------
print("Step 5:")
for f in fruits:
    print(f)


# ---------- Bonus: two tiny things you will use a lot ----------
print("How many items:", len(fruits))   # 3
print("Is mango in list?", "mango" in fruits)   
print("Is grapes in list?", "grapes" in fruits)   
print("Is orange in list?", "orange" in fruits)   
print("Is banana in list?", "banana" in fruits)   

a = [10, 20, 30]
b = a

b.append(40)

print(a)
print(b)
print(a is b)