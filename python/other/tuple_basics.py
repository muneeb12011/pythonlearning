t = (1, 2, 3)
print(t[0], t[-1], len(t))

try:
    t[0] = 99
except TypeError as e:
    print("error:", e)

# tuple holding a list: arrow locked, list inside not
t2 = ([1, 2], 3)
t2[0].append(100)
print(t2)

l = list(t)
l[0] = 99
print(l, t)
