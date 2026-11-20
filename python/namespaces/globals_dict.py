y = 5
print(globals()["y"])
globals()["z"] = 10
print(z)

def f():
    a = 1
    print(locals())

f()
