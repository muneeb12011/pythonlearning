a = [1, 2, 3]
print(id(a))     

a.append(4)      
a[0] = 99
print(id(a))         # sme address as before proof it is the same object....just changed
print(a)       

a = [1, 2, 3]
b = a

print(id(a))      
print(id(b))        
print(a is b)          

a = [1, 2, 3]
print(id(a)) 
a.append(4)
print(id(a))      
print(a)      