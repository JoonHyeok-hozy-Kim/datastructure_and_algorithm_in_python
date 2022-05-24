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
