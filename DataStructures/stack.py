class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass

class ArrayStack:
    """ LIFO Stack implementation using Python's List class as an underlying storage """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        text_list = ['[']
        if len(self) > 0:
            for i in self._data:
                text_list.append(str(i))
                text_list.append(', ')
            text_list.pop()
        text_list.append(']')
        return ''.join(text_list)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, val):
        self._data.append(val)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()

    def transfer(self, other):
        if type(self) != type(other):
            raise TypeError
        for i in range(len(self)):
            other.push(self.pop())

    def recursive_truncate(self):
        if len(self) == 0:
            return
        self.pop()
        return self.recursive_truncate()