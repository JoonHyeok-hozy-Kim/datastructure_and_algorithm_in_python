from DataStructures.queue import ArrayQueue
from DataStructures.deque import ArrayDeque

d = ArrayDeque()
print(d)
for i in range(30):
    d.add_first(i)
for i in range(20):
    d.delete_first()
for i in range(20):
    d.add_first(i)
for i in range(30):
    d.delete_last()
    print(d)