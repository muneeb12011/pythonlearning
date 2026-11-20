from collections import deque

d = deque([10, 20, 30])
d.append(40)        # add to back, fast
d.appendleft(5)      # add to front, fast (a list would be slow here)
d.pop()               # remove from back, fast
d.popleft()           # remove from front, fast
print(d)