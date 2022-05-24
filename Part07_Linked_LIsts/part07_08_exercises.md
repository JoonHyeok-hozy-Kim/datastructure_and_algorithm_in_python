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




<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part07_Linked_LIsts/part07_00_linked_lists.md">Part 7. Linked Lists</a>
</p>