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

```python
class PositionalList(_DoublyLinkedBase):

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) == type(self) and other._node ==  self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position Type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._next is None:
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_poistion(self, node):
        if node == self._header or node == self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_poistion(self._header._next)

    def last(self):
        return self._make_poistion(self._trailer._prev)

    def before(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._prev)

    def after(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_poistion(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        target_node = self._validate(p)
        return self._insert_between(e, target_node._prev, target_node)

    def add_after(self, p, e):
        target_node = self._validate(p)
        return self._insert_between(e, target_node, target_node._next)

    def delete(self, p):
        target_node = self._validate(p)
        return self._delete_node(target_node)

    def replace(self, p, e):
        target_node = self._validate(p)
        old_value = target_node._element
        target_node._element = e
        return old_value

    def __str__(self):
        if self.is_empty():
            return '[]'
        else:
            return self._create_str_text()

    def _create_str_text(self, text_list=None, cursor=None):
        if text_list is None and cursor is None:
            text_list = ['[']
            cursor = self.first()
        if cursor is self.after(self.last()):
            text_list.pop()
            text_list.append(']')
            return ''.join(text_list)
        else:
            text_list.append(str(cursor.element()))
            text_list.append(', ')
            return self._create_str_text(text_list, self.after(cursor))
```

## 7.5 Sorting a Positional List
#### Tech.) Insertion Sort Algorithm for the Positional List
```python
def insertion_sort(self):
    if self.is_empty():
        return
    target = self.after(self.first())
    while target is not None:
        cursor = self.first()
        # print('[Phase1] target : {}'.format(target.element()))
        while cursor != target:
            # print('[Phase2] cursor : {}'.format(cursor.element()))
            if cursor.element() > target.element():
                temp_target = self.before(target)
                deleted = self.delete(target)
                # print('[Shifted] {} <> {}'.format(cursor.element(),
                #                                   deleted))
                self.add_before(cursor, deleted)
                target = temp_target
                break
            else:
                cursor = self.after(cursor)
        target = self.after(target)
```

## 7.6 Case Study : Maintaining Access Frequencies

### 7.6.1 Using a Sorted List
* Tech.) Favorite List
  * Make a list such that most frequently accessed item comes to the very top of the list.
  * Each access will move_up the item's position if the count is larger than the one above it in the list.

```python
from DataStructures.linked_list import PositionalList

class FavoriteList:
    class Item:
        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p is not self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and cnt > walk.element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk)

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def access(self, e):
        p = self._find_position(e)
        if p is None:
            self._data.add_last(self.Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal Value for k')
        walk = self._data.first()
        for i in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)
```
* Props)
  * If an element is k-th favorite itme in the list, the access to this item may cost O(k) running time.
  * Worst Case) O(n^3) running time for the access operations.
    * Sol.) <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/part07_00_linked_lists.md#762-using-a-list-with-the-move-to-front-heuristic">Move-to-Front Heuristic</a>

<p align="center">
  <img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/images/07_06_01_worst_scenario.png" style="height: 450px;"></img><br/>
</p>

### 7.6.2 Using a List with the Move-to-Front Heuristic
* Concept) Locality of Reference
  * a scenario such that once an element is accessed it is more likely to be accessed again in the near future
  * Heuristic (AKA rule of thumb) : How to apply this to the FavoriteList
    * Move_up the most recent accessed item.

<p align="center">
  <img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/images/07_06_02_move_to_front_heuristic.png" style="height: 150px;"></img><br/>
</p>

#### Analysis) Trade-Offs with the Move-to-Front Heuristic
* __top(k)__ operation
  * Recall that this heuristic does not keep the sorted list.
  * Thus, __top(k)__ operation will take O(kn) running time.
    * why?) Each __top(k)__ operation may go as follows.
      1. We copy all entries of our favorites list into another list, named temp.
      2. We scan the temp list k times. In each scan, we find the entry with the largest access count, remove this entry from temp, and report it in the results.
    * Then if k is fixed as a constant, __top(k)__ operation takes O(n) running time.
    * However, if k is proportional to n, it takes O(n^2) times.
      * ex.) Top 25%

#### Tech) Implementation of Move-To-Front Heuristics
```python
class FavoriteListMTF(FavoriteList):
    def _move_up(self, p):
        if p is not self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        temp = PositionalList()
        for i in self._data:
            temp.add_last(i)

        for i in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value
            temp.delete(highPos)

if __name__ == '__main__':
    a = FavoriteListMTF()
    for i in range(5):
        a.access(i)
    top = a.top(3)
    for i in a.top(3):
        print(i)
```

## 7.7



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/part07_08_exercises.md">Excercises</a>    
</p>
