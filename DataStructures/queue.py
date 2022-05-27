class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass

class Full(Exception):
    """ Error pushing more elements than maxlen if maxlen exists """
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self, maxlen=None):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = -1
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def __str__(self):
        text_list = ['[']
        if self._size > 0:
            for i in range(self._size):
                text_list.append(str(self._data[(self._front + i) % len(self._data)]))
                text_list.append(', ')
            text_list.pop()
        text_list.append(']')
        return ''.join(text_list)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        result = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        return result

    def enqueue(self, val):
        if self._maxlen is not None and self._size == self._maxlen:
            raise Full
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._front + self._size) % len(self._data)] = val
        self._size += 1

    def _resize(self, cap):
        temp = [None] * cap
        for i in range(self._size):
            temp[i] = self._data[(self._front + i) % len(self._data)]
        self._data = temp
        self._front = 0

    def rotate(self):
        dequeued = self._data[self._front]
        self._data[self._front] = None
        self._data[(self._front + self._size) % len(self._data)] = dequeued
        self._front += 1
        return dequeued


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
        else:
            self._tail = self._tail._next


# C-7.25
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

    def recursively_traverse(self, e, node=None):
        if node is None:
            node = self._header
        if node._element == e:
            return node
        elif node._next is None:
            return None
        else:
            return self.recursively_traverse(e, node._next)

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


from DataStructures.linked_list import PositionalList
class PositionalQueue:
    def __init__(self):
        self._data = PositionalList()
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._data.first()

    def last(self):
        return self._data.last()

    def after(self, p):
        return self._data.after(p)

    def before(self, p):
        return self._data.before(p)

    def dequeue(self):
        return self._data.delete(self._data.last())

    def enqueue(self, e):
        return self._data.add_last(e)

    def delete(self, p):
        return self._data.delete(p)

    def __str__(self):
        return str(self._data)