fruits = ["apple", "banana", "mango"]
print("Step 1:", fruits)

print("Step 2:")
print(fruits[0]) 
print(fruits[1])     
print(fruits[-1])    


fruits.append("orange") 
fruits.remove("banana")  
print("Step 3:", fruits)   

fruits[2] = "grapes"     
print("Step 4:", fruits) 


print("Step 5:")
for f in fruits:
    print(f)


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