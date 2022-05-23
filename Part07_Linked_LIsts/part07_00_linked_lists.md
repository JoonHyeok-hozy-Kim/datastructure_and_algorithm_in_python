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

## 7.2 Circularly Linked Lists
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/images/07_02_01_circularly_linked_list_image.png" style="height: 300px;"></img><br/>
</p>

### 7.2.2. Implementing a Queue with a Circularly Linked List
```python
class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            result = self._tail._element
            self._tail = None
        else:
            old_head = self._tail._next
            self._tail._next = old_head._next
            result = old_head._element
        self._size -= 1
        return result

    def enqueue(self, val):
        new_node = self._Node(val, None)
        if self.is_empty():
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def rotate(self):
        if self.is_empty():
            raise Empty('The queue is empty.')
        # elif len(self) == 1:
        #     pass
        else:
            self._tail = self._tail._next
```

## 7.3 Doubly Linked List
#### Props.) Doubly Linked List
* Each node contains address of its predecessor and successor nodes.
* Symmetric structure compared to the singly-linked-list
  * Thus, more efficient when deleting elements near the tail node.

#### Tech.) Implementing Doubly Linked List
* Use concept Sentinel Nodes, which contain Nones as their elements and keep their positions as the header and the trailer.
  * Every consecutive nodes containing elements will be positioned between the sentinels.
* Use _DoublyLinkedBase class as base class.
  * It contains basic properties that following data structures share. 
    1. Doubly Linked List
    2. Positional List
    
```python
class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty
        deleted = self._delete_node(self._header._next)
        return deleted

    def delete_last(self):
        if self.is_empty():
            raise Empty
        deleted = self._delete_node(self._trailer._prev)
        return deleted
```

## 7.4 Positional List ADT
#### Props.) Positional List ADT
* Allows more advanced operations compared to stacks, queues, deques.
  * Such as insertion and deletion in the middle of the list.
    * If frequent revisions for the elements at arbitrary positions are expected, positional array can be a fine choice.
      * ex.) word processor program
* Numeric indices used in Python's List class is not a efficient material for the Positional Array

#### Tech.) How to describe position
* Use _DoublyLinkedBase class for low level manipulations of nodes.
  * Encapsulate _insert_between and _delete_node methods.
* Create position abstract data type
  * Acts as a marker or token within broader positional list
  * Unaffected by changes in the list
  * Becomes invalid only if an explicit command is issued to delete it.





<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/part07_08_exercises.md">Excercises</a>    
</p>
