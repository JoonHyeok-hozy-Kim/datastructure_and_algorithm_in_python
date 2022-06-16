from DataStructures.maps import MapBase

class SortedTableMap(MapBase):

    def _find_index(self, k, low, high):
        """
        Return index of the leftmost item with key greater than or equal to k

        Return high+1 if no such item qualifies.
        i.e.) j will be returned such that
            all items of slice table[low:j] have key < k
            all items of slice table[j:high+1] have key >= k
        """
        if high < low:
            return high+1
        else:
            mid = (low + high)//2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid-1)
            else:
                return self._find_index(k, mid+1, high)

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self)-1)
        if j == len(self) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self)-1)
        if j < len(self) and self._table[j] == k:
            self._table[j]._value = v
        else:
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self)-1)
        if j > len(self)-1 or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table[j].pop(j)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self) == 0:
            return None
        return (self._table[0]._key, self._table[0]._value)

    def find_max(self):
        if len(self) == 0:
            return None
        return (self._table[len(self)-1]._key, self._table[len(self)-1]._value)

    def find_ge(self, k):
        j = self._find_index(k, 0, len(self)-1)
        if j < len(self):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self)-1)
        if j == 0:
            return None
        return (self._table[j-1]._key, self._table[j-1]._value)

    def find_gt(self, k):
        j = self._find_index(k, 0, len(self) - 1)
        if j < len(self) and self._table[j]._key == k:
            j += 1
        if j < len(self):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_le(self, k):
        j = self._find_index(k, 0, len(self)-1)
        if j < len(self) and self._table[j]._key == k:
            return (self._table[j]._key, self._table[j]._value)
        elif j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None

    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self)-1)
        while j < len(self) and (self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1