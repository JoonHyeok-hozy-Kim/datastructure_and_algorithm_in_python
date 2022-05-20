from DataStructures.stack import Empty
from copy import deepcopy

class ArrayDeque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = -1

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
            return Empty
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            return Empty
        return self._data[(self._front + self._size -1) % len(self._data)]

    def _resize(self, cap):
        temp = [None] * cap
        for i in range(self._size):
            temp[i] = self._data[(self._front + i) % len(self._data)]
        self._data = temp
        self._front = 0

    def add_first(self, val):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        if self._front == -1:
            new_front = 0
        elif self._front == 0:
            new_front = len(self._data)-1
        else:
            new_front = self._front-1
        self._data[new_front] = val
        self._front = new_front
        self._size += 1

    def add_last(self, val):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._front + self._size) % len(self._data)] = val
        self._size += 1

    def delete_first(self):
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        result = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        return result

    def delete_last(self):
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        last_idx = (self._front + self._size -1) % len(self._data)
        result = self._data[last_idx]
        self._data[last_idx] = None
        self._size -= 1
        return result

    # Imitating collections.deque
    def __getitem__(self, key):
        result = None
        if len(self) == 0:
            raise Empty
        if key >= len(self) or key < len(self) * (-1):
            raise IndexError
        if key < 0:
            key += len(self)
        for i in range(len(self)):
            temp = self.delete_first()
            if i == key:
                result = deepcopy(temp)
            self.add_last(temp)
        return result

    def __setitem__(self, key, value):
        if len(self) == 0:
            raise Empty
        if key >= len(self) or key < len(self) * (-1):
            raise IndexError
        if key < 0:
            key += len(self)
        self.rotate(key)
        self.delete_first()
        self.add_last(value)
        self.rotate(len(self)-key-1)

    def clear(self):
        for i in range(len(self)):
            self._data[(self._front + i) % len(self._data)] = None
        self._front = -1
        self._size = 0


    def rotate(self, k=None):
        if k is None:
            k = 1
        for i in range(k):
            temp = deepcopy(self._data[self._front])
            self._data[(self._front + self._size) % len(self._data)] = temp
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)

    def remove(self, element):
        removed_flag = False
        for i in range(len(self)):
            if not removed_flag and self.first() == element:
                self.delete_first()
                removed_flag = True
                continue
            self.rotate()

    def count(self, element):
        result = 0
        for i in range(len(self)):
            if self.first() == element:
                result += 1
            self.rotate()
        return result
