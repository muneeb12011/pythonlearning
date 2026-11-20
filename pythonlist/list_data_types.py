# lists notes - muneeb
# run this file and read the output, dont just read the code

# ---------- why do we even need a list ----------

# first i thought just make variables
s1 = "ali"
s2 = "sara"
s3 = "usman"
# ok but what if 500 students?? no way im making 500 variables

students = ["ali", "sara", "usman"]
print(students)
print(len(students))   # 3

students.append("hina")   # grows while program runs
print(students)

for s in students:
    print("hello", s)

# what data belongs in a listt 
# many things, order matters, can change later

temps = [31.5, 33.0, 29.8, 35.2]
todo = ["buy milk", "study python", "call mom"]
marks = [88, 92, 75, 60]

# list inside list (like excel rows)
table = [["ali", 88], ["sara", 92]]
print(table[1][0])   # sara  <- first [1] picks row, second [0] picks item in row

# mixed types also work but usually dont do it
mixed = [1, "hi", 3.5, True]
print(mixed)

# ---------- where used in real programs ----------

# 1. collecting stuff in a loop (most common thing)
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)

# 2. data from api / database comes as list of dicts
users = [{"name": "ali", "age": 20}, {"name": "sara", "age": 22}]
for u in users:
    print(u["name"], u["age"])

# 3. undo button (stack) - last in first out
history = []
history.append("typed a")
history.append("typed b")
print(history.pop())   # typed b  -> undo last

# 4. waiting line (queue) - first in first out
line = ["ali", "sara", "usman"]
first = line.pop(0)
print(first, line)

# 5. sorting
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

# 6. split a sentence into words
words = "python is easy".split()
print(words)

# ---------- when list is GOOD ----------

race = ["sara", "ali", "usman"]
print("winner", race[0])       # order matters

rolls = [4, 2, 4, 6, 4]
print(rolls.count(4))          # duplicates are ok, gives 3

cart = ["laptop", "mouse"]
cart.append("keyboard")
cart.remove("mouse")
cart[0] = "gaming laptop"      # can edit
print(cart)
print(cart[-1])                # last item, negative index

# ---------- when list is BAD ----------

# 1. labeled data -> dict
person = ["ali", 20, "lahore"]      # bad, what is person[1]? age? i forget
person = {"name": "ali", "age": 20, "city": "lahore"}
print(person["age"])                # much better

# 2. should never change -> tuple
loc = (31.52, 74.35)
# loc[0] = 5    # error, tuple is locked, thats the point

# 3. checking "is x in here" on huge data -> set (way faster)
big_list = list(range(1000000))
big_set = set(big_list)
print(999999 in big_list)   # slow, checks one by one
print(999999 in big_set)    # fast

# 4. want unique only -> set
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(set(emails))

# 5. list as dict key - NOT allowed
# d = {[1, 2]: "x"}   # TypeError unhashable (list is mutable)
d = {(1, 2): "x"}     # tuple is fine
print(d)

# 6. pop(0) again and again on big list is slow, everything shifts
# later use collections.deque for that

# ---------- remember ----------
# order + change + duplicates ok = list
# order + never change           = tuple
# name -> value                  = dict
# unique / fast lookup           = set