<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_00_priority_queues.md">Part 9. Priority Queues</a>
</p>

### R-9.1 How long would it take to remove the ┌log(n)┑ smallest elements from a heap that contains n entries, using the remove min operation?
* Sol.) n/2

### R-9.2 Suppose you label each position p of a binary tree T with a key equal to its preorder rank. Under what circumstances is T a heap?
* Sol.) The binary tree should be in a complete shape or at least has the minimum height.

### R-9.3 What does each remove min call return within the following sequence of priority queue ADT methods: 
* add(5,A)
* add(4,B)
* add(7,F)
* add(1,D),
* remove_min( )
* add(3,J)
* add(6,L)
* remove_min( )
* remove_min( )
* add(8,G)
* remove_min( )
* add(2,H)
* remove_min( )
* remove_min( )  
```python
from DataStructures.priority_queues import HeapPriorityQueue
a = HeapPriorityQueue()
a.add(5, 'A')
a.add(4, 'B')
a.add(7, 'F')
a.add(1, 'D')
print(a.remove_min())
a.add(3, 'J')
a.add(6, 'L')
print(a.remove_min())
print(a.remove_min())
a.add(8, 'G')
print(a.remove_min())
a.add(2, 'H')
print(a.remove_min())
print(a.remove_min())
```

### R-9.4 An airport is developing a computer simulation of air-traffic control that handles events such as landings and takeoffs. Each event has a time stamp that denotes the time when the event will occur. The simulation program needs to efficiently perform the following two fundamental operations:
* Insert an event with a given time stamp (that is, add a future event).
* Extract the event with smallest time stamp (that is, determine the next event to process).
#### Which data structure should be used for the above operations? Why?
* Sol.)
  * If time stamp is given in the strictly increasing order, queue is idealistic.
  * If time stamp is given in the strictly decreasing order, stack is idealistic.
  * If time stamp is given in random order
    * and the number of the flight is 
      * small, then LinkedList
        * If the size of the list is small, traversal that maybe performed for inserting a flight in the middle of the class may not cost that much.
      * large, PriorityQueue
        * If the size of the list is huge, instead of traversal that takes O(n) time, priority queue with O(log(n)) time maybe more efficient.

### R-9.5 The min method for the UnsortedPriorityQueue class executes in O(n) time, as analyzed in Table 9.2. Give a simple modification to the class so that min runs in O(1) time. Explain any necessary modifications to other methods of the class.
* Sol.) If addition sorts data like SortedPriorityQueue, min method may run in O(1) time.

### R-9.6 Can you adapt your solution to the previous problem to make remove min run in O(1) time for the UnsortedPriorityQueue class? Explain your answer.
* Sol.) If _data is sorted, remove_min is simply popping the very first element. Thus, remove_min() will also run in O(1) running time.

### R-9.7 Illustrate the execution of the selection-sort algorithm on the following input sequence: (22,15,36,44,10,3,9,13,29,25).
* Sol.)
  1. Elements simply added at the last position of self._data.
  2. Loop runs 10 times searching for the minimum element and add it to self._data.
  3. Return self._data

### R-9.8 Illustrate the execution of the insertion-sort algorithm on the input sequence of the previous problem.
* Sol.)
  1. For each addition of the element, loop runs searching for the proper position.
  2. Return self._data

### R-9.9 Give an example of a worst-case sequence with n elements for insertion-sort, and show that insertion-sort runs in Ω(n2) time on such a sequence.
* Sol.) If an input sequence is sorted in decreasing order, it may run in Ω(n2) time.

### R-9.10 At which positions of a heap might the third smallest key be stored?
* Sol.) At the left or right child position of the root. 
  * i.e.) self._data[1] or self._data[2]

### R-9.11 At which positions of a heap might the largest key be stored?
* Sol.) One of the leaf positions of the tree. 
  * i.e.) Between self._data[2^(h-1)] and self.[2^(h)-2] where h is the height of the tree.

### R-9.12 Consider a situation in which a user has numeric keys and wishes to have a priority queue that is maximum-oriented. How could a standard (min-oriented) priority queue be used for such a purpose?
* Sol.) Consider a logic that all the upheap and downheap's key comparison works in opposite direction.
```python
class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self, contents=(), max_oriented=False):
        self._data = [self._Item(k, v) for k, v in contents]
        self._max_oriented = max_oriented  # Added for the max-oriented case
        if len(self) > 0:
            self._heapify()

    def __len__(self):
        return len(self._data)

    def _heapify(self):
        start = self._parent(len(self)-1)
        for i in range(start, -1, -1):
            self._downheap(start)

    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j+1

    def _right(self, j):
        return 2*j+2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        # max-oriented case starts.
        if self._max_oriented:
            if j > 0 and self._data[parent] < self._data[j]:
                self._swap(j, parent)
                self._upheap(parent)
        # max-oriented case ends.
        else:
            if j > 0 and self._data[parent] > self._data[j]:
                self._swap(j, parent)
                self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    if not self._max_oriented:
                        small_child = right
                # max-oriented case starts.
                else:
                    if self._max_oriented:
                        small_child = right
                # max-oriented case ends.
            # max-oriented case starts.
            if self._max_oriented:
                if self._data[j] < self._data[small_child]:
                    self._swap(j, small_child)
                    self._downheap(small_child)
            # max-oriented case ends.
            else:
                if self._data[j] > self._data[small_child]:
                    self._swap(j, small_child)
                    self._downheap(small_child)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data)-1)

    def min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        self._swap(0, len(self)-1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
```

### R-9.13 Illustrate the execution of the in-place heap-sort algorithm on the following input sequence: (2,5,16,4,10,23,39,18,26,15)
```python
from DataStructures.priority_queues import HeapPriorityQueue
def heap_sort(A):
    n = len(A)
    H = HeapPriorityQueue()
    for i in range(n):
        popped = A.pop(0)
        H.add(popped, popped)
    for i in range(n):
        A.append(H.remove_min()[0])
    return A
if __name__ == '__main__':
    m = [2,5,16,4,10,23,39,18,26,15]
    print(m)
    print(heap_sort(m))
```

### R-9.14 Let T be a complete binary tree such that position p stores an element with key f(p), where f(p) is the level number of p (see Section 8.3.2). Is tree T a heap? Why or why not?
* Sol.) No. 
  * Complete binary tree does share similar data structure with heap.
  * However, binary tree itself does not support main operations such as upheap and downheap, which allow sustainable level numbering after numerous data updates in the middle of the tree.

### R-9.15 Explain why the description of down-heap bubbling does not consider the case in which position p has a right child but not a left child.
* Sol.) Array-Based Structure of the heap secures minimum height and left-first add_child system.
  * We use index as an indicator for the virtual parent-child relation between elements.
  * Thus, minimum height and left-first add_child system continues even after numerous additions and removals of the elements.

### R-9.16 Is there a heap H storing seven entries with distinct keys such that a preorder traversal of H yields the entries of H in increasing or decreasing order by key? How about an inorder traversal? How about a postorder traversal? If so, give an example; if not, say why.
* Sol.) No such traversals enables increasing or decreasing order of keys.
  * This is because the heap is conformed in level-numbering rule, which is breadth-first order of elements.

### R-9.17 Let H be a heap storing 15 entries using the array-based representation of a complete binary tree. What is the sequence of indices of the array that are visited in a preorder traversal of H? What about an inorder traversal of H? What about a postorder traversal of H?
```python
def preorder(H, j=0, text_list=[]):
    text_list.append(str(H._data[j]._key))
    if H._has_left(j):
        preorder(H, H._left(j), text_list)
    if H._has_right(j):
        preorder(H, H._right(j), text_list)
    return ' - '.join(text_list)

def postorder(H, j=0, text_list=[]):
    if H._has_left(j):
        postorder(H, H._left(j), text_list)
    if H._has_right(j):
        postorder(H, H._right(j), text_list)
    text_list.append(str(H._data[j]._key))
    return ' - '.join(text_list)

def inorder(H, j=0, text_list=[]):
    if H._has_left(j):
        inorder(H, H._left(j), text_list)
    text_list.append(str(H._data[j]._key))
    if H._has_right(j):
        inorder(H, H._right(j), text_list)
    return ' - '.join(text_list)

if __name__ == '__main__':
    from DataStructures.priority_queues import HeapPriorityQueue
    a = HeapPriorityQueue()
    for i in range(15):
        a.add(i, i)

    print(preorder(a))
    print(postorder(a))
    print(inorder(a))
```

### R-9.18 Show that the sum
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/images/09_06_18.png" style="height: 100px;"></img><br/>
</p>

#### which appears in the analysis of heap-sort, is Ω(nlogn).
* Sol.) Worst case : Input collection C is in decreasing order.
  * Recall that ┌log(i)┐ is equal to the height of i-th position.
    * Since C is in decreasing order, every time i-th element is added to the heap, ┌log(i)┐ upheap operation is performed.
    * Therefore, the given summation appears.
  * One can check this by counting the number of upheap operations for each addition.

### R-9.19 Bill claims that a preorder traversal of a heap will list its keys in non-decreasing order. Draw an example of a heap that proves him wrong.
* Sol.) Check <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_06_exercises.md#r-917-let-h-be-a-heap-storing-15-entries-using-the-array-based-representation-of-a-complete-binary-tree-what-is-the-sequence-of-indices-of-the-array-that-are-visited-in-a-preorder-traversal-of-h-what-about-an-inorder-traversal-of-h-what-about-a-postorder-traversal-of-h">R-9.17</a>

### R-9.20 Hillary claims that a postorder traversal of a heap will list its keys in non-increasing order. Draw an example of a heap that proves her wrong.
* Sol.) Check <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_06_exercises.md#r-917-let-h-be-a-heap-storing-15-entries-using-the-array-based-representation-of-a-complete-binary-tree-what-is-the-sequence-of-indices-of-the-array-that-are-visited-in-a-preorder-traversal-of-h-what-about-an-inorder-traversal-of-h-what-about-a-postorder-traversal-of-h">R-9.17</a>

### R-9.21 Show all the steps of the algorithm for removing the entry (16,X) from the heap of Figure 9.1, assuming the entry had been identified with a locator.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/images/09_06_21_figure_9_1.png" style="height: 300px;"></img><br/>
</p>

* Sol.) 
  1. Swap (16, X) and (13, W)
  2. Pop (16, X)
  3. Start upheap from (13, W)
     1. Swap (13, W) and (15, K) -> Finished.

### R-9.22 Show all the steps of the algorithm for replacing key of entry (5,A) with 18 in the heap of Figure 9.1, assuming the entry had been identified with a locator.
* Sol.)
  1. Replace key and the result is (18, A)
  2. Start downheap from (18, A)
     1. Swap (18, A) and (9, F)
     2. Swap (18, A) and (12, H) -> Finished.

### R-9.23 Draw an example of a heap whose keys are all the odd numbers from 1 to 59 (with no repeats), such that the insertion of an entry with key 32 would cause up-heap bubbling to proceed all the way up to a child of the root (replacing that child’s key with 32).
```python
from DataStructures.priority_queues import HeapPriorityQueue
a = HeapPriorityQueue()
a.add(1, 1)
l_idx = 3
r_idx = 33
h_idx = 0
while h_idx < 4:
    for i in range(pow(2, h_idx)):
        a.add(l_idx, l_idx)
        l_idx += 2
    for i in range(pow(2, h_idx)):
        a.add(r_idx, r_idx)
        r_idx += 2
        if r_idx >59:
            break
    h_idx += 1
print(a)
a.add(32, 32)
print(a)
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/images/09_06_23.png" style="height: 150px;"></img><br/>
</p>

### R-9.24 Describe a sequence of n insertions in a heap that requires Ω(nlogn) time to process.
* Sol.) If the key of elements in the sequence are in decreasing order, insertion to the heap will take Ω(nlogn) time.

### R-9.25 Complete Figure 9.9 by showing all the steps of the in-place heap-sort algorithm. Show both the array and the associated heap at the end of each step.
```python
def heap_sort(A):
    n = len(A)
    heap_start = n-1
    for i in range(n):
        popped = A.pop(0)
        A.append(popped)
        # print('BEFORE UP : {}'.format(A))
        _heap_sort_upheap(A, heap_start, n-1)
        heap_start -= 1
    heap_len = n
    for i in range(n):
        # print('BEFORE REMOVE : {}'.format(A))
        max_idx = _heap_sort_remove_max(A, 0, heap_len)
        _heap_sort_swap(A, max_idx, heap_len-1)
        # print('REMOVED and SWAPPED : {}'.format(A))
        heap_len -= 1

def _heap_sort_parent(start, j):
    return (j-start-1)//2+start

def _heap_sort_left(n, start, heap_len, j):
    idx = (j-start)*2+1+start
    if n-1 < idx or idx > start+heap_len-1:
        return None
    return idx

def _heap_sort_right(n, start, heap_len, j):
    idx = (j-start)*2+2+start
    if n-1 < idx or idx > start+heap_len-1:
        return None
    return idx

def _heap_sort_swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def _heap_sort_upheap(A, start, j):
    if start < j:
        parent = _heap_sort_parent(start, j)
        # print('[UP] {} - {}'.format(A[parent], A[j]))
        if A[parent] < A[j]:
            _heap_sort_swap(A, parent, j)
            # print('[UP] swapped : {}'.format(A))
            _heap_sort_upheap(A, start, parent)

def _heap_sort_downheap(A, start, heap_len, j):
    left = _heap_sort_left(len(A), start, heap_len, j)
    if left is not None:
        big_child = left
        right = _heap_sort_right(len(A), start, heap_len, j)
        if right is not None:
            if A[right] > A[left]:
                big_child = right
        # print('[DOWN] {} - {}'.format(A[j], A[big_child]))
        if A[j] < A[big_child]:
            _heap_sort_swap(A, j, big_child)
            # print('[DOWN] swapped : {}'.format(A))
            _heap_sort_downheap(A, start, heap_len, big_child)

def _heap_sort_remove_max(A, start, heap_len):
    last = start + heap_len -1
    _heap_sort_swap(A, start, last)
    _heap_sort_downheap(A, start, heap_len-1, start)
    return last

if __name__ == '__main__':
    from random import randint
    x = [randint(0, 100) for i in range(10)]
    print(x)
    heap_sort(x)
    print(x)
```

### C-9.26 Show how to implement the stack ADT using only a priority queue and one additional integer instance variable.
```python
from DataStructures.priority_queues import HeapPriorityQueue
class HeapStack:
    def __init__(self):
        self._heap = HeapPriorityQueue()

    def push(self, e):
        self._heap.add(len(self._heap), e)

    def pop(self):
        return self._heap._data.pop()._value

if __name__ == '__main__':
    from random import randint
    hs = HeapStack()
    for i in range(5):
        e = randint(0, 100)
        print('Push {}'.format(e))
        hs.push(e)
    for i in range(5):
        print(hs.pop())
```

### C-9.27 Show how to implement the FIFO queue ADT using only a priority queue and one additional integer instance variable.
```python
from DataStructures.priority_queues import HeapPriorityQueue
class HeapQueue:
    def __init__(self):
        self._heap = HeapPriorityQueue()

    def enqueue(self, e):
        self._heap.add(len(self._heap), e)

    def dequeue(self):
        return self._heap.remove_min()[1]

if __name__ == '__main__':
    from random import randint
    hq = HeapQueue()
    for i in range(5):
        e = randint(0, 100)
        print('Enqueue {}'.format(e))
        hq.enqueue(e)
    for i in range(5):
        print(hq.dequeue())
```

### C-9.28 Professor Idle suggests the following solution to the previous problem. Whenever an item is inserted into the queue, it is assigned a key that is equal to the current size of the queue. Does such a strategy result in FIFO semantics? Prove that it is so or provide a counterexample.
* Sol.) Check C-9.27 solution.

### C-9.29 Reimplement the SortedPriorityQueue using a Python list. Make sure to maintain remove min’s O(1) performance.
```python
from DataStructures.priority_queues import PriorityQueueBase
class ListSortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        item = self._Item(key, value)
        idx = None
        for i in range(len(self)):
            if item < self._data[i]:
                idx = i
                break
        if idx is None:
            self._data.append(item)
        else:
            self._data.insert(idx, item)

    def min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data.pop(0)
        return (item._key, item._value)

if __name__ == '__main__':
    from random import randint
    size = 16
    l = [randint(0, 100) for i in range(size)]
    x = ListSortedPriorityQueue()
    print(l)
    for i in l:
        x.add(i, i)
    while not x.is_empty():
        print(x.remove_min())
```

### C-9.30 Give a nonrecursive implementation of the upheap method for the class HeapPriorityQueue.
```python
def _upheap(self, j):
    parent = self._parent(j)
    while self._data[parent] > self._data[j]:
        self._swap(parent, j)
        j = parent
        parent = self._parent(j)
```

### C-9.31 Give a nonrecursive implementation of the downheap method for the class HeapPriorityQueue.
```python
def _downheap(self, j):
    while True:
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[j] > self._data[small_child]:
                self._swap(j, small_child)
                j = small_child
            else:
                break
```

### C-9.32 Assume that we are using a linked representation of a complete binary tree T, and an extra reference to the last node of that tree. Show how to update the reference to the last node after operations add or remove_min in O(logn) time, where n is the current number of nodes of T. Be sure and handle all possible cases, as illustrated in Figure 9.12.
```python
from DataStructures.tree import LinkedBinaryTree
class LinkedHeapBinaryTree(LinkedBinaryTree):

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def __str__(self):
            return '({}, {})'.format(self._key, self._value)

    def __init__(self):
        super().__init__()
        self._last_position = None
        self._max_height = 1

    def last(self):
        return self._last_position

    def _swap(self, p, q):
        if self._last_position == p:
            self._last_position = q
        elif self._last_position == q:
            self._last_position = p
        super()._swap(p, q)

    def _upheap(self, p):
        while p != self.root():
            parent = self.parent(p)
            if p.element() < parent.element():
                self._swap(p, parent)

    def _downheap(self, p):
        if len(self) == 0:
            return
        while not self.is_leaf(p):
            if self.left(p) is not None:
                small_child = self.left(p)
                if self.right(p) is not None:
                    right = self.right(p)
                    if right.element() < small_child.element():
                        small_child = right
                # print('[DOWN] {} - {}'.format(p.element(), small_child.element()))
                if p.element() > small_child.element():
                    self._swap(p, small_child)
                else:
                    return

    def add(self, key, value):
        new_item = self._Item(key, value)
        if self._last_position is None:
            self._last_position = self._add_root(new_item)
        elif self._size == pow(2, self._max_height)-1:
            self._last_position = self._add_drill_left(self.root(), new_item)
            self._max_height += 1
        else:
            self._last_position = self._add_next_last_position(self._last_position, new_item)
        self._upheap(self._last_position)

    def _add_drill_left(self, p, new_item):
        while not self.is_leaf(p):
            p = self.left(p)
        return self._add_left(p, new_item)

    def _add_next_last_position(self, p, new_item):
        parent = self.parent(p)
        if p == self.left(parent):
            if self.is_leaf(p):
                return self._add_right(parent, new_item)
            else:
                right_sibling = self.right(parent)
                return self._add_drill_left(right_sibling, new_item)
        else:
            return self._add_next_last_position(parent, new_item)

    def remove_min(self):
        root_copy = self.root()
        # print('[RM] root : {}'.format(self.root().element()))
        # print('[RM] last : {}'.format(self.last().element()))
        self._swap(self.root(), self.last())
        self._last_position = self._after_remove_last_position(root_copy)
        deleted = self._delete(root_copy)
        self._downheap(self.root())
        return deleted

    def _after_remove_last_position(self, current_last):
        if current_last == self.root():
            return None
        if self._size == pow(2, self._max_height-1):
            self._max_height -= 1
            return self._after_remove_drill_right(self.root())
        parent = self.parent(current_last)
        if current_last == self.right(parent):
            if self.is_leaf(current_last):
                return self.left(parent)
            else:
                left_sibling = self.left(parent)
                return self._after_remove_drill_right(left_sibling)
        else:
            return self._after_remove_last_position(parent)

    def _after_remove_drill_right(self, p):
        while not self.is_leaf(p):
            if self.right(p) is not None:
                p = self.right(p)
            else:
                break
        return p


if __name__ == '__main__':
    a = LinkedHeapBinaryTree()
    for i in range(14,-1,-1):
        a.add(i+1, i+1)
    print(a)
    for i in range(15):
        print('REMOVED_MIN : {}'.format(a.remove_min()))
        print(a)
    print('root : {}'.format(a.root()))
    print('last : {}'.format(a.last()))
```

### C-9.33 When using a linked-tree representation for a heap, an alternative method for finding the last node during an insertion in a heap T is to store, in the last node and each leaf node of T, a reference to the leaf node immediately to its right (wrapping to the first node in the next lower level for the rightmost leaf node). Show how to maintain such references in O(1) time per operation of the priority queue ADT assuming that T is implemented with a linked structure.
* Sol.) One might be able to achieve O(1) running time of getting next right position by doing O(log(n)) operation in-advance in the previous addition.

### 




<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_00_priority_queues.md">Part 9. Priority Queues</a>
</p>