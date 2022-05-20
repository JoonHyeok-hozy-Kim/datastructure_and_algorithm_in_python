<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 7. Linked Lists

#### Props.) Disadvantages of Dynamic Arrays
1. The length of a dynamic array might be longer than the actual number of elements that it stores.
2. Amortized bounds for operations may be unacceptable in real-time systems.
3. Insertions and deletions at interior positions of an array are expensive.  
* Solution) Linked List

#### Tech.) Node
* Each node maintains 
  1. a reference to its element 
  2. one or more references to neighboring nodes in order to collectively represent the linear order of the sequence.

## 7.1. Implementing a Stack with a Singly Linked List
#### Concepts)
* head : the first node
  * Each list contains the address of the first node.
* tail : the last node
  * reference to the next node is None
  * Not strictly required to be stored in the list but desired to avoid the inefficiency of traversing.
* traversing : searching through the nodes in a list
  * also called as
    1. link hopping
    2. pointer hopping

### 7.1. Linked Stacks
```python
class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('The stack is empty.')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('The stack is empty.')
        popped = self._head._element
        self._head = self._head._next
        self._size -= 1
        return popped
```
* Runtime Analysis
  * Every operations have O(1) running times.

### 7.1.2. Implementing a Queue with Singly Linked List
```python
class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty():
            raise Empty('The queue is empty.')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('The queue is empty.')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

    def enqueue(self, e):
        if self.is_empty():
            self._head = self._Node(e, None)
            self._tail = self._head
        else:
            new_node = self._Node(e, None)
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1
```



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/part07_08_exercises.md">Excercises</a>    
</p>
