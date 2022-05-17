class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass

class ArrayStack:
    """ LIFO Stack implementation using Python's List class as an underlying storage """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

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