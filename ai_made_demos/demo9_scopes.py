"""Which namespace does Python look in first? Order: Local, Enclosing, Global, Built-in (LEGB)."""

y = "global y"                      # G: this file's notebook

def outer():
    z = "enclosing z"               # E: the notebook of the function around inner
    def inner():
        w = "local w"               # L: inner's own notebook
        print("1. found by name:", w, "|", z, "|", y, "|", len)
        # w came from L, z from E, y from G, len from B (built-in)
    inner()

outer()

print("\n2. same name in 3 places, which one wins?")
x = "global x"
def a():
    x = "a's own x"
    def b():
        x = "b's own x"
        print("   inside b:", x)           # L wins
    b()
    print("   inside a:", x)               # a's own
a()
print("   outside:", x)                    # global

print("\n3. the classic trap:")
count = 0
def add_wrong():
    count = count + 1                      # Python sees an assignment -> count is LOCAL here
try:
    add_wrong()
except UnboundLocalError as e:
    print("   UnboundLocalError:", e)

def add_right():
    global count                           # say: use the FILE's notebook for count
    count = count + 1
add_right()
print("   with 'global count' ->", count)

print("\n4. nonlocal: change a variable of the enclosing function")
def counter():
    n = 0
    def up():
        nonlocal n
        n += 1
        return n
    up(); up()
    return n
print("   n after two calls:", counter())
