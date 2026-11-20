# PYTHON DATA STRUCTURES - FAST PREP FOR SENIOR MEETING
# Read top to bottom. Then do the self-test at the end WITHOUT scrolling up.


# ============================================================
# 1. LIST
# ============================================================

# WHAT: ordered, changeable collection, allows duplicates
a = [10, 20, 30]

# WHY IT EXISTS: hold many related items as ONE variable, in order, that can grow/shrink
cart = []
cart.append("shirt")
cart.append("shoes")

# USE CASES:
# - shopping cart (order matters, duplicates ok)
# - sensor readings over time
# - results collected in a loop
# - any "sequence of steps/events"

# INTERNALS:
# - row of POINTERS in one memory block, not the actual values
# - keeps spare empty slots at the end for fast append
a = [10, 20, 30]
print(id(a[0]))   # pointer to the int object 10, list doesn't hold 10 "directly"

# COMPLEXITY:
# a[i]        O(1)   -> direct address calculation
# append()    O(1) avg -> writes into spare slot (rare resize = O(n), averaged out = "amortized O(1)")
# insert(0,x) O(n)   -> shifts everything right
# pop()       O(1)   -> removes from end, nothing shifts
# pop(0)      O(n)   -> shifts everything left
# x in a      O(n)   -> scans one by one, no shortcut
# remove(x)   O(n)   -> search (scan) + shift
# a[i:j]      O(k)   -> k = size of slice, builds new list, copies pointers

# MUTATE vs REBIND:
a = [1, 2, 3]
a.append(4)        # MUTATE - same object, id(a) unchanged
a = [9, 9, 9]       # REBIND - new object, id(a) changes

# REFERENCE SHARING:
a = [1, 2, 3]
b = a               # same object, b.append() affects a too
c = a.copy()         # NEW outer object, but shallow (nested items still shared)

# ALTERNATIVES:
# - need fast membership check -> set
# - need key->value -> dict
# - must never change -> tuple
# - need fast work at BOTH ends -> deque


# ============================================================
# 2. TUPLE
# ============================================================

# WHAT: ordered, UNCHANGEABLE collection, allows duplicates
point = (31.52, 74.35)

# WHY IT EXISTS: same as list, but with a HARD guarantee it can't be edited
# point[0] = 99   # TypeError - this is the entire point of using it

# USE CASES:
# - coordinates, fixed records (x, y)
# - dict keys (lists can't be keys, tuples can, because tuples are hashable)
# - returning multiple values from a function
def get_min_max(nums):
    return min(nums), max(nums)   # returns a tuple

low, high = get_min_max([3, 1, 4, 1, 5])   # unpacking

# INTERNALS: same pointer-array idea as list, just no methods that mutate it

# COMPLEXITY: indexing O(1), search O(n) -- SAME as list for these
# (tuple isn't faster at searching, only safer from being changed)

# ALTERNATIVES:
# - needs to change later -> list
# - needs fast lookup -> set/dict


# ============================================================
# 3. DICT
# ============================================================

# WHAT: key -> value pairs, unordered by meaning (but insertion order is kept since 3.7)
employee = {"id": 101, "name": "ali", "dept": "engineering"}

# WHY IT EXISTS: look something up by a MEANINGFUL LABEL, not by position
employees = {101: {"name": "ali"}, 102: {"name": "sara"}}
print(employees[101])        # instant, direct lookup by key

# USE CASES:
# - employee_id -> employee info
# - username -> account
# - counting things (word frequency)
# - config settings (key -> value)

# COUNTING EXAMPLE (very common interview pattern):
words = ["a", "b", "a", "c", "b", "a"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)   # {'a': 3, 'b': 2, 'c': 1}

# INTERNALS: hash table. key is hashed -> tells Python roughly where to store/find it
# that's WHY lookup is fast, no scanning needed

# COMPLEXITY:
# d[key]        O(1) avg  -> hash tells it where to look
# key in d       O(1) avg  -> same, hash-based
# d[key] = val    O(1) avg  -> same
# del d[key]       O(1) avg

# METHODS:
d = {"a": 1, "b": 2}
print(d.keys())      # dict_keys(['a', 'b'])
print(d.values())     # dict_values([1, 2])
print(d.items())       # dict_items([('a', 1), ('b', 2)])
print(d.get("c", 0))    # 0 -- safe lookup, no KeyError if missing
for k, v in d.items():
    print(k, v)

# ALTERNATIVES:
# - don't need labels, just a sequence -> list
# - only need existence check, no value attached -> set


# ============================================================
# 4. SET
# ============================================================

# WHAT: unordered, UNIQUE items only, no duplicates allowed
s = {1, 2, 3}

# WHY IT EXISTS: answer "is X in here?" FAST, and auto-remove duplicates
usernames = {"ali", "sara", "usman"}
print("sara" in usernames)   # O(1), instant even with millions of entries

# USE CASES:
# - checking membership on large data (usernames, blacklist, seen-before tracking)
# - removing duplicates from a list
emails = ["a@x.com", "b@x.com", "a@x.com"]
unique = set(emails)
print(unique)   # duplicates gone

# INTERNALS: hash table, same idea as dict but values only, no key->value pairing

# COMPLEXITY:
# x in s       O(1) avg  -> hashed, jumps straight there
# s.add(x)      O(1) avg
# s.remove(x)    O(1) avg

# NOTE: set has NO order, so no s[0], no indexing at all
# NOTE: set items must be hashable (immutable) -> can't put a list inside a set

# ALTERNATIVES:
# - need order -> list
# - need a value attached to each item, not just existence -> dict
# - must be locked/immutable -> frozenset


# ============================================================
# 5. DEQUE (from collections)
# ============================================================

from collections import deque

# WHAT: double-ended queue, fast at BOTH the front and the back
q = deque([10, 20, 30])

# WHY IT EXISTS: a list is only cheap at the END. deque is cheap at BOTH ends.
q.append(40)        # add to back    - O(1)
q.appendleft(5)       # add to front   - O(1)
q.pop()                # remove from back - O(1)
q.popleft()             # remove from front - O(1)
print(q)

# USE CASES:
# - task queues, message queues
# - sliding window problems
# - undo/redo with limited history (deque(maxlen=N))

# COMPLEXITY: O(1) both ends, vs list's O(n) at the front

# ALTERNATIVES:
# - only ever touch the END -> list is fine, no need for deque


# ============================================================
# QUICK DECISION TABLE
# ============================================================
# order + duplicates + changeable        -> list
# order + duplicates + LOCKED            -> tuple
# label -> value lookup                  -> dict
# unique items / fast "is it in here"    -> set
# fast work at BOTH ends                 -> deque


# ============================================================
# SELF-TEST -- cover everything above and answer these out loud
# ============================================================

# 1. Why is a[i] O(1) but x in a O(n)?
# 2. What makes append() "amortized" O(1) instead of plain O(1)?
# 3. b = a vs b = a.copy() -- what's the actual difference in memory?
# 4. Why is a.copy() called a SHALLOW copy? What problem can that cause?
# 5. Mutating vs rebinding -- one sentence each.
# 6. Why is dict/set lookup O(1) when list lookup is O(n)? (one word: ______)
# 7. Give one real scenario each for: list, tuple, dict, set, deque.
# 8. Your senior asks "why a list here instead of a set?" -- answer in the
#    requirement -> choice -> reason -> trade-off format.
# 9. Why can't a list be a dict key, but a tuple can?
# 10. a.insert(0, x) vs a.append(x) -- which is O(1) and why?


# ============================================================
# ANSWERS (don't peek until you've tried)
# ============================================================
# 1. a[i] calculates the exact memory address directly (position-based).
#    x in a has no shortcut for VALUES, so it must scan item by item.
# 2. Most appends just use a spare slot (O(1)). Occasionally the block is full
#    and Python copies everything to a bigger block (O(n)), but that happens
#    rarely, so averaged over many appends the cost per append stays O(1).
# 3. b = a: same object, two names, no new list created.
#    b = a.copy(): new outer list object, separate from a.
# 4. .copy() only duplicates the OUTER list. Nested items (like inner lists)
#    are still the SAME shared objects. Mutating a nested item through one
#    copy shows up in the other too.
# 5. Mutating: changes what's INSIDE the object, same object, same id().
#    Rebinding: points the NAME at a totally different object, id() changes.
# 6. HASHING -- dict/set compute a hash of the value to know where to look,
#    instead of scanning.
# 7. list: shopping cart. tuple: fixed (x,y) coordinate.
#    dict: employee_id -> employee info. set: username existence check.
#    deque: task queue, add/remove from both ends.
# 8. "Requirement is to preserve insertion order and allow duplicates, which a
#    set can't do. Chose list because order matters here. Trade-off is O(n)
#    membership checks instead of O(1), but that's fine since lookups aren't
#    frequent/this isn't huge data. Would switch to set if that changed."
# 9. Dict keys (and set items) must be hashable, which requires being
#    immutable. A list can change after being added, so its hash would become
#    unreliable -- Python disallows it. A tuple can't change, so it's safe to
#    hash and use as a key.
# 10. append(x) is O(1) because it just writes to a free slot at the end,
#     nothing else moves. insert(0, x) is O(n) because every existing item has
#     to shift one position right to make room at the front.