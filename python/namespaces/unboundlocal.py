x = "global"

def f():
    print(x)
    x = "local"      # this line makess x local for tha whole function

try:
    f()
except UnboundLocalError as e:
    print("error:", e)

def g():
    global x
    print(x)
    x = "changed"

g()
print(x)
