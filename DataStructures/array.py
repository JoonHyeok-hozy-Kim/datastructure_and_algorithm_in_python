import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def __str__(self):
        str_list = ['[']
        if self._n > 0:
            for i in range(self._n):
                str_list.append(str(self._A[i]))
                if i < self._n-1:
                    str_list.append(',')
        str_list.append(']')
        return ''.join(str_list)

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        result = self._A[self._n-1]
        self._A[self._n-1] = None
        self._n -= 1
        if self._n == self._capacity//2:
            self._resize(int(self._capacity//2))
        return result

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)( )

    # 5.4
    def insert(self, k, value):
        if k > self._n+1:
            raise IndexError('Cannot insert at {}-th index. Max is {}.'.format(k, self._n+1))
        if k == self._n+1:
            self.append(value)
        else:
            if self._n == self._capacity:
                self._resize(2 * self._capacity)
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i-1]
            self._A[k] = value
            self._n += 1

    # 5.4
    def remove(self, k):
        if k > self._n-1:
            raise IndexError('Cannot remove {}-th item. Max is {}.'.format(k, self._n-1))
        result = self._A[k]
        for i in range(k, self._n-1):
            self._A[i] = self._A[i+1]
        self._A[self._n-1] = None
        self._n -= 1
        if self._n == self._capacity//2:
            self._resize(int(self._capacity//2))
        return result