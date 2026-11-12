"""Python's namespace is a real dictionary: name -> object."""
import builtins
import math

x = 10
print("1. type of the file's namespace:", type(globals()))
print("   'x' is a key in it:", "x" in globals(), "| value:", globals()["x"])
print("   same object as x:", globals()["x"] is x)

x = 15
print("\n2. after x = 15, the dictionary entry changed:", globals()["x"])

globals()["z"] = 99            # write straight into the dictionary...
print("\n3. I never wrote 'z = 99', but z works:", z)

print("\n4. math's box is a dictionary too:", type(math.__dict__), "| has sqrt:", "sqrt" in math.__dict__)

def f():
    y = 5
    print("\n5. inside a function, its own small box:", locals())
f()

print("\n6. built-in names (len, print...) live in another box:", builtins.len is len)