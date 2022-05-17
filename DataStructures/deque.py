from DataStructures.stack import Empty

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
