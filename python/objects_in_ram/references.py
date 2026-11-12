"""how variables, lists and tuples reallyy live in ram (CPython).
id(obj) = the memory address of the object. Same id = the sAME object in RAM."""
import sys


class Box:
    """A normal object that tells us when Python frees it."""
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"      >>> {self.name} was FREED from RAM (nothing pointed to it)")


def title(t):
    print("\n" + "=" * 60 + f"\n{t}\n" + "=" * 60)


# ---------------------------------------------------------------
title("1. x = 10, then x = 15  (what happens to the 10?)")
x = 10
print("x = 10  -> x points to object at", id(x))
x = 15
print("x = 15  -> x points to object at", id(x), "(a DIFFERENT object)")
print("the 10 is still alive at", id(10), "-> small ints (-5..256) are pre-made and kept forever")

print("\nSame thing with an object that is NOT cached, so we can see it die:")
x = Box("Box-A")
print("  x points to Box-A")
x = Box("Box-B")          # the last arrow to Box-A is removed here
print("  x now points to Box-B (the line above freed Box-A)")

# ---------------------------------------------------------------
title("2. Two names, one object (reference sharing)")
a = [1, 2, 3]
b = a                      # copies the ARROW, not the list
print("id(a) =", id(a), " id(b) =", id(b), " same object?", a is b)
b.append(4)
print("after b.append(4):  a =", a, " (a changed too!)")
c = a.copy()               # a real new list
print("c = a.copy() -> id(c) =", id(c), " same object?", a is c)
c.append(99)
print("after c.append(99): a =", a, " c =", c, " (a NOT affected)")

# ---------------------------------------------------------------
title("3. Changing a value INSIDE a list")
nums = [1, 2, 3]
print("list id before:", id(nums))
print("item ids before:", [id(i) for i in nums])
nums[0] = 99
print("nums[0] = 99")
print("list id after :", id(nums), "(SAME list object)")
print("item ids after :", [id(i) for i in nums], "(first arrow now points to 99)")
print("the list's array of pointers was edited; the list itself did not move")

# ---------------------------------------------------------------
title("4. Tuple: the arrows are locked")
t = (1, 2, 3)
print("tuple id:", id(t), " item ids:", [id(i) for i in t])
try:
    t[0] = 99
except TypeError as e:
    print("t[0] = 99  ->  TypeError:", e)

print("\nBut a tuple holding a LIST: the arrow is locked, the list is not")
t2 = ([1, 2], 3)
print("before:", t2, " id of inner list:", id(t2[0]))
t2[0].append(100)
print("after t2[0].append(100):", t2, " id of inner list:", id(t2[0]), "(same)")

# ---------------------------------------------------------------
title("5. tuple -> list (and back): what actually happens")
t = (10, 20, 30)
l = list(t)
print("tuple id:", id(t), "  new list id:", id(l), "-> a NEW object was created")
print("tuple item ids:", [id(i) for i in t])
print("list  item ids:", [id(i) for i in l], "-> the SAME items, not copied")
l[0] = 5
print("after l[0] = 5 -> list:", l, " tuple untouched:", t)
back = tuple(l)
print("tuple(l) -> another NEW object:", id(back), "!=", id(t))

# ---------------------------------------------------------------
title("6. Memory cost: list vs tuple (same 5 items)")
print("list :", sys.getsizeof([1, 2, 3, 4, 5]), "bytes (bigger header, because a list must be able to grow)")
print("tuple:", sys.getsizeof((1, 2, 3, 4, 5)), "bytes (smaller, it can never grow or change)")