import sys
import tracemalloc

print("A. MODULE namespace")
import mymod                      # runs mymod.py once
import mymod                      # second import: NOT run again
print("   'value' is a key in mymod.__dict__:", "value" in mymod.__dict__)
print("   mymod is cached in sys.modules:", "mymod" in sys.modules)

from mymod import value           # copies the ARROW into my notebook
mymod.value = 2                   # change it inside mymod's notebook
print("   mymod.value =", mymod.value, "| my own value =", value, " (my arrow still points to the old 1)")

print("\nB. CLASS and OBJECT namespaces")
class Dog:
    species = "dog"
    def __init__(self, name):
        self.name = name
d = Dog("Rex")
print("   instance d.__dict__      :", d.__dict__)
print("   'species' in d.__dict__  :", "species" in d.__dict__)
print("   'species' in Dog.__dict__:", "species" in Dog.__dict__)
print("   d.species                :", d.species, " <- not in d's notebook, found in the class's")
d.species = "wolf"
print("   after d.species = 'wolf' -> d.__dict__:", d.__dict__, "| Dog.species still:", Dog.species)

print("\nC. Why __slots__ saves memory (no notebook per object)")
class WithDict:
    def __init__(self, i):
        self.id = i; self.name = "ali"; self.age = 22
class WithSlots:
    __slots__ = ("id", "name", "age")
    def __init__(self, i):
        self.id = i; self.name = "ali"; self.age = 22
print("   slots object has a __dict__:", hasattr(WithSlots(1), "__dict__"))
for cls in (WithDict, WithSlots):
    tracemalloc.start()
    keep = [cls(i) for i in range(100_000)]
    cur, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"   100k {cls.__name__:<9}: {cur / 1e6:6.1f} MB")
