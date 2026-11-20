a = [1, 2, 3]
print(id(a))     # some address

a.append(4)        # mutate edits the sme object
a[0] = 99
print(id(a))         # SAME address as before proof it is the same object....just changed
print(a)                # [99, 2, 3, 4]

a = [1, 2, 3]
b = a

print(id(a))      
print(id(b))        
print(a is b)          

a = [1, 2, 3]
print(id(a))     # e.g. 1000
a.append(4)
print(id(a))       # 1000 -- SAME object, just edited
print(a)               # [1, 2, 3, 4]