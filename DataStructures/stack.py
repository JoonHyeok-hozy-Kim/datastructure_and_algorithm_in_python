class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass

class Full(Exception):
    """ Error pushing more elements than maxlen if maxlen exists """
    pass

class ArrayStack:
    """ LIFO Stack implementation using Python's List class as an underlying storage """

    def __init__(self, maxlen=None):
        self._data = []
        # Added by C-6.17
        if maxlen:
            self._data = [None] * maxlen

        self._maxlen = maxlen # Added by C-6.16
        self._top = -1

    def __len__(self):
        return self._top + 1

    def __str__(self):
        text_list = ['[']
        if len(self) > 0:
            for i in range(len(self)):
                text_list.append(str(self._data[i]))
                text_list.append(', ')
            text_list.pop()
        text_list.append(']')
        return ''.join(text_list)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        # Added by C-6.16
        if self._maxlen:
            if len(self) == self._maxlen:
                text = 'Stack is full with the capacity of {}'.format(self._maxlen)
                raise Full(text)
            else:
                self._data[self._top] = val
        else:
            self._data.append(val)
        self._top += 1


    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[self._top]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        popped = self._data[self._top]
        if self._maxlen:
            self._data[self._top] = None
        else:
            self._data.pop()
        self._top -= 1
        return popped

    def transfer(self, other):
        if type(self) != type(other):
            raise TypeError
        for i in range(len(self)):
            # print('TRANSFER {} -> {}'.format(self, other))
            other.push(self.pop())

    def recursive_truncate(self):
        if len(self) == 0:
            return
        self.pop()
        return self.recursive_truncate()