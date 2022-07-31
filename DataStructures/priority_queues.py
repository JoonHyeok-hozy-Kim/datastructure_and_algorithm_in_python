class Empty(Exception):
    pass


class PriorityQueueBase:

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

        def __str__(self):
            return '({}, {})'.format(self._key, self._value)

    def is_empty(self):
        return len(self) == 0

    def key(self):
        return self._key

    def value(self):
        return self._value


from DataStructures.linked_list import PositionalList
class UnsortedPriorityQueue(PriorityQueueBase):

    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        item = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and item < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(item)
        else:
            self._data.add_after(walk, item)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        p = self._data.first()
        item = self._data.delete(p)
        return (item._key, item._value)


class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self, contents=()):
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self) > 0:
            self._heapify()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        from DataStructures.tree import ArrayBasedTree, BinaryLayout
        a = ArrayBasedTree()
        for i in self._data:
            a._data.append(a._make_position(i))
        b = BinaryLayout(a)
        return b.execute()

    def _heapify(self):
        start = self._parent(len(self)-1)
        for i in range(start, -1, -1):
            self._downheap(i)

    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j+1

    def _right(self, j):
        return 2*j+2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[parent] > self._data[j]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[j] > self._data[small_child]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def add(self, key, value):
        new_item = self._Item(key, value)
        self._data.append(new_item)
        self._upheap(len(self._data)-1)
        return new_item

    def min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        self._swap(0, len(self)-1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

    def heappushpop(self, key, value):
        if key < self.min()[0]:
            return (key, value)
        else:
            popped = self._data[0]
            self._data[0] = self._Item(key, value)
            self._downheap(0)
            return (popped._key, popped._value)

    def heapreplace(self, key, value):
        popped = self._data[0]
        self._data[0] = self._Item(key, value)
        self._downheap(0)
        return (popped._key, popped._value)


class AdaptableHeapPriorityQueue(HeapPriorityQueue):

    class Locator(HeapPriorityQueue._Item):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token

    def update(self, loc, new_key, new_val):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] == loc):
            raise ValueError('Invalid Locator')
        loc._key = new_key
        loc._value = new_val
        self._bubble(j)

    def remove(self, loc):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] == loc):
            raise ValueError('Invalid Locator')
        if j == len(self)-1:
            self._data.pop()
        else:
            self._swap(j, len(self)-1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)


class MaxPriorityQueue(HeapPriorityQueue):

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[parent] < self._data[j]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            big_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    big_child = right
            if self._data[j] < self._data[big_child]:
                self._swap(j, big_child)
                self._downheap(big_child)

    def max(self):
        return self.min()

    def remove_max(self):
        return self.remove_min()


class LocationAwareUnsortedPriorityQueue(PriorityQueueBase):

    class Locator(PriorityQueueBase._Item):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def _find_min_idx(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        min_idx = None
        for i in range(len(self)):
            min_idx = i if (min_idx is None or self._data[i] < self._data[min_idx]) else min_idx
        return min_idx

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        return token

    def min(self):
        return self._data[self._find_min_idx()]

    def remove_min(self):
        loc = self._data.remove(self._find_min_idx())
        return (loc._key, loc._value)

    def update(self, loc, new_key, new_val):
        j = loc._index
        self._data[j]._key = new_key
        self._data[j]._value = new_val

    def remove(self, loc):
        j = loc._index
        removed_loc = self._data.remove(j)
        return (removed_loc._key, removed_loc._value)