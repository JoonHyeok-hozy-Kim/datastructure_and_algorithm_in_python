<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/part07_00_linked_lists.md">Part 7. Linked Lists</a>
</p>

### R-7.1 Give an algorithm for finding the second-to-last node in a singly linked list in which the last node is indicated by a next reference of None.
```python
def second_to_last(A):
    if len(A) < 2:
        raise ValueError('Length is less than two.')
    walk = A._head
    while walk._next._next is not None:
        walk = walk._next
    return walk._element
```

### R-7.2 Describe a good algorithm for concatenating two singly linked lists L and M, given only references to the first node of each list, into a single list L that contains all the nodes of L followed by all the nodes of M. 
```python
from DataStructures.linked_list import LinkedQueue
def concatenate(first_node, second_node):
    new_queue = LinkedQueue()
    new_queue._head = first_node
    new_queue._size += 1
    walk = first_node
    while walk._next is not None:
        walk = walk._next
        new_queue._size += 1
    walk._next = second_node
    new_queue._size += 1
    while walk._next is not None:
        walk = walk._next
        new_queue._size += 1
    new_queue._tail = walk
    return new_queue
```

### R-7.3 Describe a recursive algorithm that counts the number of nodes in a singly linked list.
```python
def singly_linked_list_count(L, node=None, count=None):
    if node is None:
        node = L._head
        count = 1
    if node._next is None:
        return count
    else:
        return singly_linked_list_count(L, node._next, count+1)
```

### R-7.4 Describe in detail how to swap two nodes x and y (and not just their contents) in a singly linked list L given references only to x and y. Repeat this exercise for the case when L is a doubly linked list. Which algorithm takes more time?
* Sol.) Singly Linked List takes more time since it requires a traversal to the element x.
```python
def singly_swap(L, node_x, node_y):
    walk = L._head
    cnt = 0
    prev_x = None
    prev_y = None
    while walk._next is not None and cnt < 2:
        # print('walk : {}'.format(walk._element))
        if walk is L._head:
            if walk is node_x or walk is node_y:
                cnt += 1
        elif walk._next == node_x:
            cnt += 1
            prev_x = walk
        elif walk._next == node_y:
            cnt += 1
            prev_y = walk
        walk = walk._next

    if prev_x is None:
        L._head = node_y
    else:
        prev_x._next = node_y
    if prev_y is None:
        L._head = node_x
    else:
        prev_y._next = node_x

    temp = node_x._next
    node_x._next = node_y._next
    node_y._next = temp

def doubly_swap(node_x, node_y):
    temp_prev = node_x._prev
    temp_next = node_x._next
    # Adjacent Nodes 
    node_x._prev._next = node_y
    node_x._next._prev = node_y
    node_y._prev._next = node_x
    node_y._next._prev = node_x
    
    # Target Nodes
    node_x._prev = node_y._prev
    node_x._next = node_y._next
    node_y._prev = temp_prev
    node_y._next = temp_next


if __name__ == '__main__':
    # Test for a Singly Linked List
    a = LinkedQueue()
    for i in range(10):
        a.enqueue(i)
    node_x = a._head
    for i in range(3):
        node_x = node_x._next
    node_y = a._head
    for i in range(7):
        node_y = node_y._next
    print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    singly_swap(a, node_x, node_y)
    for i in range(10):
        print(a.dequeue())

    # Test for Doubly
    b = LinkedDeque()
    for i in range(10):
        b.insert_last(i)
    node_x = b._header
    for i in range(3):
        node_x = node_x._next
    node_y = b._trailer
    for i in range(4):
        node_y = node_y._prev
    print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    doubly_swap(node_x, node_y)
    for i in range(10):
        print(b.delete_first())
```

### R-7.5 Implement a function that counts the number of nodes in a circularly linked list.
* Sol.) Parameter _size already exists.

### R-7.6 Suppose that x and y are references to nodes of circularly linked lists, although not necessarily the same list. Describe a fast algorithm for telling if x and y belong to the same list.
* Sol.) Check whether y exists while rotating the list that x is contained.

### R-7.7 Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty queue. Implement such a method for the LinkedQueue class of Section 7.1.2 without the creation of any new nodes.
```python
def rotate(self):
    if self.is_empty():
        raise Empty('The queue is empty.')
    else:
        self._tail = self._tail._next
```

### R-7.8 Describe a nonrecursive method for finding, by link hopping, the middle node of a doubly linked list with header and trailer sentinels. In the case of an even number of nodes, report the node slightly left of center as the “middle.” (Note: This method must only use link hopping; it cannot use a counter.) What is the running time of this method? 
* Sol.) Running Time : 
```python
def middle_finder(L):
    front = L._header
    back = L._trailer
    while True:
        front = front._next
        back = back._prev
        if front is back:
            break
        elif front._next is back:
            break
    return front._element
```

### R-7.9 Give a fast algorithm for concatenating two doubly linked lists L and M, with header and trailer sentinel nodes, into a single list L'.
```python
def concatenate_doubly(L, M):
    L._size += M._size
    # Link Middle
    L._trailer._prev._next = M._header._next
    M._header._next._prev = L._trailer._prev
    L._trailer = M._trailer
    
if __name__ == '__main__':
    a = LinkedDeque()
    for i in range(5):
        a.insert_last(i+1)
    b = LinkedDeque()
    for i in range(5):
        b.insert_last((i+1)*(-1))
    concatenate_doubly(a, b)
    for i in range(10):
        print(a.delete_first())
```

### R-7.10 There seems to be some redundancy in the repertoire of the positional list ADT, as the operation L.add first(e) could be enacted by the alternative L.add before(L.first( ), e). Likewise, L.add last(e) might be performed as L.add after(L.last( ), e). Explain why the methods add first and add last are necessary.
* Sol.) Maintaining redundant methods can prevent the potential traversal. 
  * Suppose insert_last() and delete_last() are the only available methods.
  * And repeated insert or delete at the position before the target elements is required.
  * Then one-node traversal to the element previous to the targe is needed any time insertion or deletion takes place.
  * On the other hand, by securing insert_before() and delete_before() method, that traversal may not be needed.

### R-7.11 Implement a function, with calling syntax max(L), that returns the maximum element from a PositionalList instance L containing comparable elements.
```python
def max(L):
    walk = L._header._next
    result = walk._element
    while walk._next is not None:
        if result < walk._element:
            result = walk._element
        walk = walk._next
    return result
```

### R-7.12 Redo the previously problem with max as a method of the PositionalList class, so that calling syntax L.max( ) is supported.
```python
def max(self):
    walk = self.first()
    result = walk.element()
    while self.after(walk) is not None:
        if result < self.after(walk).element():
            result = self.after(walk).element()
        walk = self.after(walk)
    return result
```

### R-7.13 Update the PositionalList class to support an additional method find(e), which returns the position of the (first occurrence of) element e in the list (or None if not found).
```python
def find(self, e):
    walk = self.first()
    while self.after(walk) is not None:
        if walk.element() == e:
            return walk
        walk = self.after(walk)
    return None
```

### R-7.14 Repeat the previous process using recursion. Your method should not contain any loops. How much space does your method use in addition to the space used for L?
* Sol.) Assuming that the element _e_ is located at the k-th position, it requires 3k additional memories.
  * why?) Each recursion returns one node which contains 3 memory spaces for the element, the reference to the prev, and the one for the next.
```python
def recursive_find(self, e, node=None):
    if node is None:
        node = self.first()
    if node.element() == e:
        return node
    elif node == self.last():
        return None
    else:
        return self.recursive_find(e, self.after(node))
```

### R-7.15 Provide support for a reversed method of the PositionalList class that is similar to the given iter , but that iterates the elements in reversed order.
```python
def __reversed__(self):
    cursor = self.last()
    while cursor is not None:
        yield cursor.element()
        cursor = self.before(cursor)
```

### R-7.16 Describe an implementation of the PositionalList methods add last and add before realized by using only methods in the set {is empty, first, last, prev, next, add after, and add first}.
```python
def add_last(L, e):
    if L.is_empty:
        L.add_first(e)
    else:
        last = L.last()
        L.add_after(last, e)

def add_before(L, p, e):
    if p == L.first():
        L.add_first(e)
    else:
        walk = L.first()
        while walk._next is not None:
            if walk._next == p:
                L.add_after(walk, e)
                return
```

### R-7.17 In the FavoritesListMTF class, we rely on public methods of the positional list ADT to move an element of a list at position p to become the first element of the list, while keeping the relative order of the remaining elements unchanged. Internally, that combination of operations causes one node to be removed and a new node to be inserted. Augment the PositionalList class to support a new method, move to front(p), that accomplishes this goal more directly, by relinking the existing node. 
```python
def move_to_front(self, p):
    target_node = self._validate(p)
    prev_node = self._validate(self.before(p))
    if self.last() == p:
        next_node = self._trailer
    else:
        next_node = self._validate(self.after(p))
    prev_node._next = next_node
    next_node._prev = prev_node

    old_first_node = self._validate(self.first())
    self._header._next = target_node
    old_first_node._prev = target_node

    target_node._prev = self._header
    target_node._next = old_first_node
```

### R-7.18 Given the set of element {a,b,c,d,e, f } stored in a list, show the final state of the list, assuming we use the move-to-front heuristic and access the elements according to the following sequence: (a,b,c,d,e,f,a,c,f,b,d,e).
```python
if __name__ == '__main__':
    fl = FavoriteListMTF()
    fl.access('a')
    fl.access('b')
    fl.access('c')
    fl.access('d')
    fl.access('e')
    fl.access('f')
    fl.access('a')
    fl.access('b')
    fl.access('c')
    fl.access('d')
    fl.access('e')
    for i in fl.top(6):
        print(i)
```

### R-7.19 Suppose that we have made kn total accesses to the elements in a list L of n elements, for some integer k ≥ 1. What are the minimum and maximum number of elements that have been accessed fewer than k times? 
* Sol.) Max : (n-1), Min : 0

### R-7.20 Let L be a list of n items maintained according to the move-to-front heuristic. Describe a series of O(n) accesses that will reverse L.
```python
fl = FavoriteListMTF()
sample_size = 5
for i in range(sample_size):
    fl.access(i)
text_list = ['Original :']
for i in fl.top(sample_size):
    text_list.append(str(i))
print(' '.join(text_list))
for i in range(sample_size-1):
    fl.access(sample_size-i-2)
text_list = ['Reversed :']
for i in fl.top(sample_size):
    text_list.append(str(i))
print(' '.join(text_list))
```

### R-7.21 Suppose we have an n-element list L maintained according to the move-to-front heuristic. Describe a sequence of n^2 accesses that is guaranteed to take Ω(n^3) time to perform on L.
```python
    fl = FavoriteListMTF()
    sample_size = 5
    for i in range(sample_size):
        fl.access(i)
    for i in range(sample_size):
        fl.access(sample_size-i-1)
```

### R-7.22 Implement a clear( ) method for the FavoritesList class that returns the list to empty.
```python
def clear(self):
    self._data = PositionalList()
```

### R-7.23 Implement a reset counts( ) method for the FavoritesList class that resets all elements’ access counts to zero (while leaving the order of the list unchanged).
```python
def reset_counts(self):
    walk = self._data.first()
    while self._data.after(walk) is not None:
        walk.element()._count = 0
        walk = self._data.after(walk)
```

### C-7.24 Give a complete implementation of the stack ADT using a singly linked list that includes a header sentinel.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/stack.py">LinkedStack</a>
</p>

```python
class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        new_node = self._Node(e, None)
        if not self.is_empty():
            new_node._next = self._header._next
        self._header._next = new_node
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('The stack is Empty')
        top_node = self._header._next
        return top_node._element

    def pop(self):
        if self.is_empty():
            raise Empty('The stack is Empty')
        original_top = self._header._next
        self._header._next = original_top._next
        self._size -= 1
        return original_top._element
```

### C-7.25 Give a complete implementation of the queue ADT using a singly linked list that includes a header sentinel.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/queue.py">LinkedQueue</a>
</p>

```python
class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('The queue is empty.')
        first_node = self._header._next
        return first_node._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('The queue is empty.')
        first_node = self._header._next
        self._header._next = first_node._next
        self._size -= 1
        return first_node._element

    def enqueue(self, e):
        walk = self._header
        while walk._next is not None:
            walk = walk._next
        walk._next = self._Node(e, None)
        self._size += 1
```

### C-7.26 Implement a method, concatenate(Q2) for the LinkedQueue class that takes all elements of LinkedQueue Q2 and appends them to the end of the original queue. The operation should run in O(1) time and should result in Q2 being an empty queue.
* Sol.) As long as a queue has a singly linked form, the inefficiency that comes from traversing elements is inevitable.
  * Let k the size of Q1 and n the size of Q2.
  * Consider that concatenation can be implemented by the linkage between Q1's last and Q2's first element.
  * However, under the singly linked condition, we have to make a choice : whether each element possesses the reference to the item next to or previous to it.
    * In case of the former, searching for the last item needs traversing while the latter requires it for searching the first one.
  * Thus, at least one queue, Q1 or Q2, needs to be traversed at least one time.
  * Since the problem requires O(1) running time for Q2, regarding the number of elements in Q1 as a constant, we may achieve our goal.
```python
def concatenate(self, other):
    if type(self) != type(other):
        raise TypeError
    last_node = self._header
    while last_node._next is not None:
        last_node = last_node._next
    last_node._next = other._header._next
    other._header._next = None
    self._size += other._size
    other._size = 0
```

### C-7.27 Give a recursive implementation of a singly linked list class, such that an instance of a nonempty list stores its first element and a reference to a list of remaining elements.
* Sol.) Recursive traversing logic created for the Singly LinkedQueue.
```python
def recursively_traverse(self, e, node=None):
    if node is None:
        node = self._header
    if node._element == e:
        return node
    elif node._next is None:
        return None
    else:
        return self.recursively_traverse(e, node._next)
```

### C-7.28 Describe a fast recursive algorithm for reversing a singly linked list.
* Sol.) Recursive reverse algorithm for Singly Linked Queue as follows
```python
def __reversed__(self, current_node=None, prev_node=None):
    if self.is_empty():
        raise Empty('The queue is empty.')
    if current_node is None:
        current_node = self._header._next

    original_next_node = current_node._next

    if prev_node is None:
        current_node._next = None
    else:
        current_node._next = prev_node

    if original_next_node is None:
        self._header._next = current_node
        return
    else:
        return self.__reversed__(original_next_node, current_node)
```

### C-7.29 Describe in detail an algorithm for reversing a singly linked list L using only a constant amount of additional space and not using any recursion.
* Sol.) Using two memory spaces for variables, prev and original_next, the non-recursive reverse algorithm goes as follows.
```python
def nonrecursive_reverse(self):
    if self.is_empty():
        raise Empty
    if len(self) == 1:
        return
    walk = self._header._next
    prev = None
    while walk._next is not None:
        original_next = walk._next
        walk._next = prev
        prev = walk
        walk = original_next
    walk._next = prev
    self._header._next = walk
```

### C-7.30 Exercise P-6.35 describes a LeakyStack abstraction. Implement that ADT using a singly linked list for storage.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/stack.py">LeakyLinkedStack</a>
</p>

```python
class LeakyLinkedStack(LinkedStack):
    def push(self, e):
        if self._size == self._maxlen:
            self.leak()
        super().push(e)

    def leak(self):
        walk = self._header
        while walk._next._next is not None:
            walk = walk._next
        walk._next = None
        self._size -= 1
```

### C-7.31 Design a forward list ADT that abstracts the operations on a singly linked list, much as the positional list ADT abstracts the use of a doubly linked list. Implement a ForwardList class that supports such an ADT.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/linked_list.py">ForwardList</a>
</p>

```python
class ForwardList:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

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

    def __init__(self):
        self._header = self._Node(None, None)
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position Type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        # if p._node._next is None:
        #     raise ValueError('p is no longer valid.')
        return p._node

    def _make_poistion(self, node):
        if node == self._header:
            return None
        else:
            return self.Position(self, node)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        return self._make_poistion(self._header._next)

    def last(self):
        if self.is_empty():
            raise Empty
        walk = self.first()
        while walk._node._next is not None:
            walk = self.after(walk)
        return walk

    def before(self, p):
        target_node = self._validate(p)
        if self._header._next == target_node:
            return None
        walk = self.first()
        while self.after(walk) is not None:
            if self.after(walk) == p:
                return walk
            walk = self.after(walk)
        return None

    def after(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_after(self, e, prev_node):
        new_node = self._Node(e, prev_node._next)
        prev_node._next = new_node
        self._size += 1
        return self._make_poistion(new_node)

    def add_first(self, e):
        return self._insert_after(e, self._header)

    def add_last(self, e):
        if self.is_empty():
            return self.add_first(e)
        last_position = self.last()
        return self._insert_after(e, last_position._node)

    def add_before(self, p, e):
        if p == self.first():
            return self.add_first(e)
        return self.add_after(self.before(p), e)

    def add_after(self, p, e):
        target_node = self._validate(p)
        return self._insert_after(e, target_node)

    def delete(self, p):
        target_node = self._validate(p)
        if p == self.first():
            prev_node = self._header
        else:
            prev_node = self._validate(self.before(p))
        prev_node._next = target_node._next
        self._size -= 1
        return target_node._element
```

### C-7.32 Design a circular positional list ADT that abstracts a circularly linked list in the same way that the positional list ADT abstracts a doubly linked list, with a notion of a designated “cursor” position within the list.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/linked_list.py">CircularlyLinkedList</a>
</p>

```python
class CircularlyLinkedList:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

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
        if node == self._header:
            return None
        else:
            return self.Position(self, node)

    def cursor(self):
        if self.is_empty():
            raise Empty
        return self._make_poistion(self._header._prev)

    def before(self, p):
        target_node = self._validate(p)
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            return p
        return self._make_poistion(target_node._prev)

    def after(self, p):
        target_node = self._validate(p)
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            return p
        return self._make_poistion(target_node._next)

    def append(self, e):
        new_node = self._Node(e, None, None)
        if self.is_empty():
            prev_node = next_node = self._header
            self._header._next = new_node
        else:
            cursor_node = self._validate(self.cursor())
            prev_node = cursor_node
            next_node = cursor_node._next
            cursor_node._next = new_node
        new_node._prev = prev_node
        new_node._next = next_node
        self._header._prev = new_node
        self._size += 1
        return self._make_poistion(new_node)

    def delete(self):
        if self.is_empty():
            raise Empty
        target_node = self._validate(self.cursor())
        if len(self) == 1:
            self._header._prev = None
            self._header._next = None
        else:            
            target_node._next._prev = target_node._prev
            target_node._prev._next = target_node._next
        self._size -= 1
        return target_node._element

    def rotate(self):
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            return self.cursor()
        old_cursor_node = self._validate(self.cursor())
        after_header = self._header._next
        new_cursor_node = old_cursor_node._prev

        after_header._prev = old_cursor_node
        old_cursor_node._next = after_header
        old_cursor_node._prev = self._header
        self._header._next = old_cursor_node
        self._header._prev = new_cursor_node
        new_cursor_node._next = self._header

        return self._make_poistion(new_cursor_node)
```

### C-7.33 Modify the DoublyLinkedBase class to include a reverse method that reverses the order of the list, yet without creating or destroying any nodes.
```python
def reverse(self):
    if self.is_empty():
        raise Empty
    walk = self._header
    while True:
        temp_next = walk._next
        walk._next = walk._prev
        walk._prev = temp_next
        if walk == self._trailer:
            break
        else:
            walk = temp_next
    temp_trailer = self._trailer
    self._trailer = self._header
    self._header = temp_trailer
```

### C-7.34 Modify the PositionalList class to support a method swap(p, q)that causes the underlying nodes referenced by positions p and q to be exchanged for each other. Relink the existing nodes; do not create any new nodes.
```python
def swap(self, p, q):
    node_p = self._validate(p)
    node_q = self._validate(q)
    adjacent_flag = False
    if node_p._next == node_q:
        adjacent_flag = True
    elif node_p._prev == node_q:
        self.swap(q, p)
        return

    # prev, next allocation
    p_prev = node_p._prev
    p_next = node_p._next  # if adjacent, node_q
    q_prev = node_q._prev  # if adjacent, node_p
    q_next = node_q._next

    # outer linkage
    p_prev._next = node_q
    node_q._prev = p_prev
    q_next._prev = node_p
    node_p._next = q_next

    # inner linkage
    if adjacent_flag:
        node_p._prev = node_q
        node_q._next = node_p
    else:
        p_next._prev = node_q
        q_prev._next = node_p
        node_p._prev = q_prev
        node_q._next = p_next

    return
```

### C-7.35 To implement the iter method of the PositionalList class, we relied on the convenience of Python’s generator syntax and the yield statement. Give an alternative implementation of iter by designing a nested iterator class. (See Section 2.3.4 for discussion of iterators.)
```python
def __init__(self):
    super().__init__()
    self._iter_cursor = self._header
    
def __next__(self):
    self._iter_cursor = self._iter_cursor._next
    if self._iter_cursor != self._trailer:
        return self._iter_cursor._element
    else:
        raise StopIteration()

def __iter__(self):
    return self
```

### C-7.36 Give a complete implementation of the positional list ADT using a doubly linked list that does not include any sentinel nodes.
```python
class PositionalListNoSentinel:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

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
        # if p._node._next is None:
        #     raise ValueError('p is no longer valid.')
        return p._node

    def _make_poistion(self, node):
        return self.Position(self, node)

    def __init__(self):
        self._cursor = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        iter_cursor = self.first()
        while True:
            yield iter_cursor.element()
            if len(self) > 1:
                iter_cursor = self.after(iter_cursor)
            if iter_cursor == self.first():
                break


    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        return self._make_poistion(self._cursor)

    def last(self):
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            return self.first()
        return self._make_poistion(self._cursor._prev)

    def before(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._prev)

    def after(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._next)

    def _insert_between(self, e, prev_node=None, next_node=None):
        new_node = self._Node(e, prev_node, next_node)
        if self.is_empty():
            self._cursor = new_node
        elif len(self) == 1:
            self._cursor._prev = self._cursor._next = new_node
            new_node._prev = new_node._next = self._cursor
        else:
            prev_node._next = new_node
            next_node._prev = new_node

        self._size += 1
        return new_node

    def _delete_node(self, node):
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            self._cursor = None
        else:
            if node == self._cursor:
                self._cursor = node._next
            if len(self) == 2:
                self._cursor._prev = self._cursor._next = None
            else:
                node._prev._next = node._next
                node._next._prev = node._prev
        self._size -= 1
        return node._element

    def add_first(self, e):
        if self.is_empty():
            return self._insert_between(e)
        return self.add_before(self.first(), e)

    def add_last(self, e):
        if self.is_empty():
            return self._insert_between(e)
        return self.add_after(self.last(), e)


    def add_before(self, p, e):
        target_node = self._validate(p)
        new_node = self._insert_between(e, target_node._prev, target_node)
        if target_node == self._cursor:
            self._cursor = new_node
        return self._make_poistion(new_node)

    def add_after(self, p, e):
        target_node = self._validate(p)
        new_node = self._insert_between(e, target_node, target_node._next)
        return self._make_poistion(new_node)

    def delete(self, p):
        target_node = self._validate(p)
        return self._delete_node(target_node)
```

### C-7.37 Implement a function that accepts a PositionalList L of n integers sorted in nondecreasing order, and another value V, and determines in O(n) time if there are two elements of L that sum precisely to V. The function should return a pair of positions of such elements, if found, or None otherwise. 
```python
from DataStructures.linked_list import PositionalList
def sum_pair(N, V):
    diff_list = PositionalList()
    for i in N:
        temp = V-i
        if temp <= N.last().element():
            diff_list.add_first(temp)
    N_cursor = N.first()
    diff_cursor = diff_list.first()
    while N.after(N_cursor) is not None and diff_list.after(diff_cursor) is not None:
        if N_cursor.element() == diff_cursor.element():
            return [N_cursor.element(), V-N_cursor.element()]
        elif N_cursor.element() > diff_cursor.element():
            diff_cursor = diff_list.after(diff_cursor)
        else:
            N_cursor = N.after(N_cursor)
    return None

if __name__ == '__main__':
    import sys
    recursive_limit = 10000000
    old = sys.getrecursionlimit()
    sys.setrecursionlimit(recursive_limit)
    
    a = PositionalList()
    for i in range(7000):
        a.add_last(i)
    print(a)
    print(sum_pair(a, 12000))
```

### C-7.38 There is a simple, but inefficient, algorithm, called bubble-sort, for sorting a list L of n comparable elements. This algorithm scans the list n−1 times, where, in each scan, the algorithm compares the current element with the next one and swaps them if they are out of order. Implement a bubble sort function that takes a positional list L as a parameter. What is the running time of this algorithm, assuming the positional list is implemented with a doubly linked list? 
* Sol.) O(n^2) running time.
```python
def bubble_sort(L):
    cnt = len(L)
    swap_cnt = 0
    move_cnt = 0
    while cnt > 0:
        cursor = L.first()
        walk = L.after(cursor)
        while walk is not None:
            if cursor.element() > walk.element():
                print('Swap[{}] {} <> {} : {}'.format(swap_cnt+1,
                                                      cursor.element(),
                                                      walk.element(),
                                                      L))
                L.swap(cursor, walk)
                walk = L.after(cursor)
                swap_cnt += 1
            else:
                cursor = L.after(cursor)
                walk = L.after(cursor)
                move_cnt += 1
        cnt -= 1

    return 'swap : {}, move : {}, total : {}'.format(swap_cnt,
                                                     move_cnt,
                                                     swap_cnt+move_cnt)

if __name__ == '__main__':
    from DataStructures.linked_list import PositionalList
    from random import randint
    a = PositionalList()
    for i in range(10):
        a.add_last(randint(0, 100))
    print(a)
    print(bubble_sort(a))
    print(a)
```

### C-7.39 To better model a FIFO queue in which entries may be deleted before reaching the front, design a PositionalQueue class that supports the complete queue ADT, yet with enqueue returning a position instance and support for a new method, delete(p), that removes the element associated with position p from the queue. You may use the adapter design pattern (Section 6.1.2), using a PositionalList as your storage.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/queue.py">PositionalQueue</a>
</p>

```python
if __name__ == '__main__':
    from DataStructures.queue import PositionalQueue
    a = PositionalQueue()
    for i in range(5):
        a.enqueue(i)
        print(a)
    for i in range(5):
        # print(a.dequeue(), a)
        print(a.delete(a.last()), a)
```

### C-7.40 Describe an efficient method for maintaining a favorites list L, with move-to-front heuristic, such that elements that have not been accessed in the most recent n accesses are automatically purged from the list.
```python
def purge(self, n):
    if len(self) < n:
        raise ValueError('Cannot purge more than {} elements.'.format(len(self)))
    walk = self._data.first()
    for i in range(n-1):
        walk = self._data.after(walk)
    while self._data.after(walk) is not None:
        self._data.delete(self._data.after(walk))
```

### C-7.41 Exercise C-5.29 introduces the notion of a natural join of two databases. Describe and analyze an efficient algorithm for computing the natural join of a linked list A of n pairs and a linked list B of m pairs.
```python
from DataStructures.linked_list import PositionalList
def natural_join(L, M):
    from copy import deepcopy
    L_cursor = L.first()
    result = []
    while L_cursor is not None:
        M_cursor = M.first()
        while M_cursor is not None:
            if L_cursor.element()[-1] == M_cursor.element()[0]:
                print('Matched {} - {}'.format(L_cursor.element(),
                                               M_cursor.element()))
                temp = deepcopy(L_cursor.element())
                temp.append(M_cursor.element()[-1])
                result.append(temp)
            M_cursor = M.after(M_cursor)
        L_cursor = L.after(L_cursor)
    return result

if __name__ == '__main__':
    l = PositionalList()
    m = PositionalList()
    l.add_last(['a', 'd'])
    l.add_last(['b', 'e'])
    l.add_last(['c', 'f'])
    m.add_last(['d', 'x'])
    m.add_last(['d', 'y'])
    m.add_last(['f', 'z'])
    m.add_last(['g', 'w'])
    m.add_last(['g', 'o'])
    print('{} JOIN {}'.format(l, m))
    print(natural_join(l, m))
```

### C-7.42 Write a Scoreboard class that maintains the top 10 scores for a game application using a singly linked list, rather than the array that was used in Section 5.5.1.
```python
from DataStructures.queue import LinkedQueue as new_linked_queue
class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class ScoreBoard:

    def __init__(self, capacity=10):
        self._capacity = capacity
        self._board = new_linked_queue()
        self._n = 0

    def __str__(self):
        str_list = ['---------------']
        walk = self._board._header._next
        while walk is not None:
            str_list.append(str(walk._element))
            walk = walk._next
        str_list.append('---------------')
        return '\n'.join(str_list)

    def add(self, entry):
        if self._board.is_empty():
            self._board.enqueue(entry)
            return

        score = entry.get_score()
        walk = self._board._header
        rotate_cnt = min(self._capacity-1, len(self._board))
        not_inserted = True

        for i in range(rotate_cnt):
            if score > walk._next._element.get_score() and not_inserted:
                self._board.enqueue(entry)
                not_inserted = False
            self._board.enqueue(self._board.dequeue())

        while self._capacity < len(self._board):
            self._board.dequeue()

if __name__ == '__main__':
    s = ScoreBoard()
    for i in range(12):
        s.add(GameEntry(chr(i+65), i))
        print(s)
```

### C-7.43 Describe a method for performing a card shuffle of a list of 2n elements, by converting it into two lists. A card shuffle is a permutation where a list L is cut into two lists, L1 and L2, where L1 is the first half of L and L2 is the second half of L, and then these two lists are merged into one by taking the first element in L1, then the first element in L2, followed by the second element in L1, the second element in L2, and so on. 
```python
from DataStructures.linked_list import PositionalList
class CardShuffle:

    def __init__(self):
        self._card_deck = PositionalList()

    def create_card_deck(self, symbols=None, numbers=None):
        self._card_deck = PositionalList()
        if symbols is None:
            symbols = ['♠', '♣', '♡', '◇']
        if numbers is None:
            numbers = ['A']
            for i in range(9):
                numbers.append(str(i+2))
            numbers.append('K')
            numbers.append('Q')
            numbers.append('J')

        for symbol in symbols:
            for number in numbers:
                self._card_deck.add_last(symbol+number)

    def shuffle(self):
        l1_walk = self._card_deck.first()
        l2_walk = self._card_deck.first()
        for i in range(len(self._card_deck)//2):
            l2_walk = self._card_deck.after(l2_walk)
        print('[In shuffle] mid : {}'.format(l2_walk.element()))
        while self._card_deck.after(l2_walk) is not None:
            temp_l1 = self._card_deck.after(l1_walk)
            temp_l2 = self._card_deck.after(l2_walk)
            self._card_deck.add_after(l1_walk, self._card_deck.delete(l2_walk))
            l1_walk = temp_l1
            l2_walk = temp_l2
        return self._card_deck

if __name__ == '__main__':
    c = CardShuffle()
    c.create_card_deck()
    print(c._card_deck)
    for i in range(10):
        c.shuffle()
        print(c._card_deck)
```

### P-7.44 Write a simple text editor that stores and displays a string of characters using the positional list ADT, together with a cursor object that highlights a position in this string. A simple interface is to print the string and then to use a second line of output to underline the position of the cursor. Your editor should support the following operations:
* left: Move cursor left one character (do nothing if at beginning).
* right: Move cursor right one character (do nothing if at end).
* insert c: Insert the character c just after the cursor.
* delete: Delete the character just after the cursor (do nothing at end).
```python
class TextEditor:
    def __init__(self):
        self._data = PositionalList()
        self._cursor = None

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def left(self):
        if self.is_empty():
            raise Empty
        if self._cursor != self._data.first():
            self._cursor = self._data.before(self._cursor)
        return self._cursor

    def right(self):
        if self.is_empty():
            raise Empty
        if self._cursor != self._data.last():
            self._cursor = self._data.after(self._cursor)
        return self._cursor

    def insert(self, c):
        if self.is_empty():
            self._data.add_last(c)
            self._cursor = self._data.first()
        else:
            self._cursor = self._data.add_after(self._cursor, c)
        return self._cursor

    def delete(self):
        if self._cursor != self._data.last():
            self._data.delete(self._data.after(self._cursor))
            return

    def __str__(self):
        if self.is_empty():
            return ''
        text_list = []
        walk = self._data.first()
        while walk is not None:
            text_list.append(str(walk.element()))
            walk = self._data.after(walk)
        return ''.join(text_list)
```

### P-7.45 An array A is sparse if most of its entries are empty (i.e., None). A list L can be used to implement such an array efficiently. In particular, for each nonempty cell A\[i], we can store an entry (i,e) in L, where e is the element stored at A\[i]. This approach allows us to represent A using O(m) storage, where m is the number of nonempty entries in A. Provide such a SparseArray class that minimally supports methods \_\_getitem\_\_(j) and \_\_setitem\_\_(j, e) to provide standard indexing operations. Analyze the efficiency of these methods.
```python
class SparseArray:
    class Entry:
        __slots__ = '_index', '_value'

        def __init__(self, index, value):
            self._index = index
            self._value = value

        def index(self):
            return self._index

        def value(self):
            return self._value

        def __str__(self):
            return 'A[{}]={}'.format(self._index, self._value)

    def __init__(self):
        self._data = PositionalList()
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def add_last(self, v):
        if self.is_empty():
            self._data.add_last(self.Entry(0, v))
        else:
            self._data.add_last(self.Entry(len(self), v))
        self._size += 1
        return self._data.last()

    def make_none(self, index):
        if index > len(self)-1:
            raise IndexError
        walk = self._data.first()
        while walk is not None:
            if walk.element().index() == index:
                return self._data.delete(walk)
            walk = self._data.after(walk)


    def __getitem__(self, item):
        if len(self)-1 < item:
            raise IndexError
        walk = self._data.first()
        while walk is not None:
            if walk.element().index() == item:
                return walk.element().value()
            walk = self._data.after(walk)
        return None

    def __setitem__(self, key, value):
        if key > len(self)-1:
            raise IndexError
        if key == len(self)-1:
            if self._data.last().element().index() == key:
                self._data.last().element()._value = value
                return self._data.last()
            else:
                return self._data.add_after(self._data.last(), self.Entry(key, value))

        walk = self._data.first()
        while self._data.after(walk) is not None:
            if walk.element().index() == key:
                walk.element()._value = value
                return walk
            if self._data.after(walk).element().index() > key:
                return self._data.add_after(walk, self.Entry(key, value))
            walk = self._data.after(walk)

    def __str__(self):
        text_list = ['[']
        idx = 0
        walk = self._data.first()
        while idx <= len(self)-1:
            if walk is None:
                text_list.append('None')
            else:
                if idx == walk.element().index():
                    text_list.append(walk.element().value())
                    walk = self._data.after(walk)
                else:
                    text_list.append('None')
            text_list.append(',')
            idx += 1
        text_list.pop()
        text_list.append(']')
        return ''.join(text_list)

if __name__ == '__main__':
    s = SparseArray()
    for i in range(10):
        s.add_last(chr(i+65))
    print(s)
    for i in range(5):
        s.make_none(i+3)
    print(s)
    s[0] = 'X'
    print(s)
    s[5] = 'Y'
    print(s)
    s[len(s)-1] = '가'
    print(s)
    s.make_none(len(s)-1)
    print(s)
    s[len(s)-1] = 'ㅎ'
    print(s)
```

### P-7.46 Although we have used a doubly linked list to implement the positional list ADT, it is possible to support the ADT with an array-based implementation. The key is to use the composition pattern and store a sequence of position items, where each item stores an element as well as that element’s current index in the array. Whenever an element’s place in the array is changed, the recorded index in the position must be updated to match. Given a complete class providing such an array-based implementation of the positional list ADT. What is the efficiency of the various operations? 
* Analysis 1) Array-Based positional list is inefficient if add or delete takes place in the middle of the list.
  * Suppose add or delete is needed at the k-th index of a list with the length n.
  * Then, elements from (k+1)-th to (n-1)-th must undergo following two operations.
    1. Changing the index value of each Item : decrease by 1 when deleting and increase by 1 when adding.
    2. Shifting Item's position in self._data : leftward when deleting and rightward when adding.
* Analysis 2) However, this ADT is efficient when searching an element by index. 
  * why?) The index of the element is synchronized with the index of Item instance in self._data.
  * One can directly call k-th element in the positional list.
    * In the Linked version, it was inefficient on the point that every search required traversals.
```python
from DataStructures.stack import ArrayStack
class ArrayBasedPositionalArray:
    class Item:
        def __init__(self, index, element):
            self._index = index
            self._element = element

        def element(self):
            return self._element

        def __str__(self):
            return '([{}] {})'.format(self._index, self._element)

    def _validate(self, p):
        if not isinstance(p, self.Item):
            raise ValueError('Not a proper Item instance.')
        return p._index

    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        text_list = []
        for i in range(len(self)):
            text_list.append(str(self._data[i]))
        return ','.join(text_list)

    def is_empty(self):
        return self._size == 0

    def empty_validation(self):
        if self.is_empty():
            raise Empty

    def first(self):
        self.empty_validation()
        return self._data[0]

    def last(self):
        self.empty_validation()
        return self._data[-1]

    def before(self, p):
        target_index = self._validate(p)
        if target_index == 0:
            raise IndexError
        return self._data[target_index-1]

    def after(self, p):
        target_index = self._validate(p)
        if target_index == self._size-1:
            raise IndexError
        return self._data[target_index+1]

    def add_first(self, e):
        if self.is_empty():
            self._data.append(self.Item(0, e))
            self._size += 1
        else:
            self.add_before(self.first(), e)
        return

    def add_last(self, e):
        self._data.append(self.Item(len(self), e))
        self._size += 1

    def add_before(self, p, e):
        target_index = self._validate(p)
        temp_stack = ArrayStack()
        for i in range(len(self)-target_index):
            temp_stack.push(self._data.pop())
        self._data.append(self.Item(target_index, e))
        while not temp_stack.is_empty():
            temp_item = temp_stack.pop()
            temp_item._index += 1
            self._data.append(temp_item)
        self._size += 1
        return

    def add_after(self, p, e):
        target_index = self._validate(p)
        temp_stack = ArrayStack()
        for i in range(len(self)-target_index-1):
            temp_stack.push(self._data.pop())
        self._data.append(self.Item(target_index+1, e))
        while not temp_stack.is_empty():
            temp_item = temp_stack.pop()
            temp_item._index += 1
            self._data.append(temp_item)
        self._size += 1
        return

    def delete(self, p):
        self.empty_validation()
        target_index = self._validate(p)
        temp_stack = ArrayStack()
        for i in range(len(self)-target_index-1):
            temp_stack.push(self._data.pop())
        result = self._data.pop()
        while not temp_stack.is_empty():
            temp_item = temp_stack.pop()
            temp_item._index -= 1
            self._data.append(temp_item)
        self._size -= 1
        return result.element()

if __name__ == '__main__':
    a = ArrayBasedPositionalArray()
    for i in range(3):
        a.add_first(i)
        print(a)
    for i in range(3):
        a.add_before(a.after(a.first()), chr(ord('가')+i))
        print(a)
    for i in range(3):
        a.add_last(chr(i+65))
        print(a)
    for i in range(3):
        a.add_after(a.before(a.last()), chr(ord('나')+i))
        print(a)
    for i in range(5):
        a.delete(a.last())
        print(a)
    for i in range(8):
        a.delete(a.first())
        print(a)
```




<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/part07_00_linked_lists.md">Part 7. Linked Lists</a>
</p>