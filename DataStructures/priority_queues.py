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

# Heap Sort Family starts.
def heap_sort(A):
    n = len(A)
    heap_start = n-1
    for i in range(n):
        popped = A.pop(0)
        A.append(popped)
        # print('BEFORE UP : {}'.format(A))
        _heap_sort_upheap(A, heap_start, n-1)
        heap_start -= 1
    heap_len = n
    for i in range(n):
        # print('BEFORE REMOVE : {}'.format(A))
        max_idx = _heap_sort_remove_max(A, 0, heap_len)
        _heap_sort_swap(A, max_idx, heap_len-1)
        # print('REMOVED and SWAPPED : {}'.format(A))
        heap_len -= 1

def _heap_sort_parent(start, j):
    return (j-start-1)//2+start

def _heap_sort_left(n, start, heap_len, j):
    idx = (j-start)*2+1+start
    if n-1 < idx or idx > start+heap_len-1:
        return None
    return idx

def _heap_sort_right(n, start, heap_len, j):
    idx = (j-start)*2+2+start
    if n-1 < idx or idx > start+heap_len-1:
        return None
    return idx

def _heap_sort_swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def _heap_sort_upheap(A, start, j):
    if start < j:
        parent = _heap_sort_parent(start, j)
        # print('[UP] {} - {}'.format(A[parent], A[j]))
        if A[parent] < A[j]:
            _heap_sort_swap(A, parent, j)
            # print('[UP] swapped : {}'.format(A))
            _heap_sort_upheap(A, start, parent)

def _heap_sort_downheap(A, start, heap_len, j):
    left = _heap_sort_left(len(A), start, heap_len, j)
    if left is not None:
        big_child = left
        right = _heap_sort_right(len(A), start, heap_len, j)
        if right is not None:
            if A[right] > A[left]:
                big_child = right
        # print('[DOWN] {} - {}'.format(A[j], A[big_child]))
        if A[j] < A[big_child]:
            _heap_sort_swap(A, j, big_child)
            # print('[DOWN] swapped : {}'.format(A))
            _heap_sort_downheap(A, start, heap_len, big_child)

def _heap_sort_remove_max(A, start, heap_len):
    last = start + heap_len -1
    _heap_sort_swap(A, start, last)
    _heap_sort_downheap(A, start, heap_len-1, start)
    return last
# Heap Sort Family ends.


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


from DataStructures.tree import BinaryLayout
class LocationAwareUnsortedPriorityQueue:
    class Location:
        __slots__ = '_key', '_value', '_index', '_parent', '_left', '_right'

        def __init__(self, key, index, parent=None, left=None, right=None):
            self._key = key
            self._index = index
            self._parent = parent
            self._left = left
            self._right = right

        def __str__(self):
            return '[key : {}, idx : {}]'.format(self._key, self._index)

        def index(self):
            return self._index

    class UnsortedBinaryLayout(BinaryLayout):
        def __init__(self, tree):
            super().__init__(tree)

        def _hook_invisit(self, p, d, path):
            x_increase = len(str(self.tree().value(p)))
            self.x_max_increase(x_increase)
            self.y_max_increase(d + 1)
            for i in range(x_increase):
                self._graphic[d + 1][self._x_max - i] = str(self.tree().value(p))[x_increase - 1 - i]
            return None

    def __init__(self):
        self._data = []
        self._size = 0
        self._root = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def parent(self, loc):
        return loc._parent

    def left(self, loc):
        return loc._left

    def right(self, loc):
        return loc._right

    def root(self):
        return self._root

    def num_children(self, loc):
        n = 0
        if self.left(loc) is not None:
            n += 1
        if self.right(loc) is not None:
            n += 1
        return n

    def children(self, loc):
        if self.left(loc) is not None:
            yield self.left(loc)
        if self.right(loc) is not None:
            yield self.right(loc)

    def is_leaf(self, loc):
        return self.num_children(loc) == 0

    def __str__(self):
        B = self.UnsortedBinaryLayout(self)
        return B.execute()

    def key(self, loc):
        return loc._key

    def index(self, loc):
        return loc._index

    def value(self, loc):
        return self._data[loc._index]

    def _add_left(self, parent_loc, child_loc):
        left = self.left(parent_loc)
        if left is not None:
            raise ValueError('Left is not None.')
        parent_loc._left = child_loc
        child_loc._parent = parent_loc
        return child_loc

    def _add_right(self, parent_loc, child_loc):
        right = self.right(parent_loc)
        if right is not None:
            raise ValueError('Left is not None.')
        parent_loc._right = child_loc
        child_loc._parent = parent_loc
        return child_loc

    def _swap(self, l, m):
        l_p = l._parent
        l_l = l._left
        l_r = l._right
        m_p = m._parent
        m_l = m._left
        m_r = m._right

        if self.parent(l) == m:
            # Parent Shift
            l._parent = m_p
            if m_p is not None:
                if m_p._left == m:
                    m_p._left = l
                else:
                    m_p._right = l
            m._parent = l

            # Child Shift
            if m_l == l:
                l._left = m
                l._right = m_r
                if m_r is not None:
                    m_r._parent = l
            else:
                l._left = m_l
                if m_l is not None:
                    m_l._parent = l
                l._right = m
            m._left = l_l
            if l_l is not None:
                l_l._parent = m
            m._right = l_r
            if l_r is not None:
                l_r._parent = m

        elif self.parent(m) == l:
            # Parent Shift
            m._parent = l_p
            if l_p is not None:
                if l_p._left == l:
                    l_p._left = m
                else:
                    l_p._right = m
            l._parent = m

            # Child Shift
            if l_l == m:
                m._left = l
                m._right = l_r
                if l_r is not None:
                    l_r._parent = m
            else:
                m._left = l_l
                if l_l is not None:
                    l_l._parent = m
                m._right = l
            l._left = m_l
            if m_l is not None:
                m_l._parent = l
            l._right = m_r
            if m_r is not None:
                m_r._parent = l

        else:
            # Parent Shift
            l._parent = m_p
            if m_p is not None:
                if m_p._left == m:
                    m_p._left = l
                else:
                    m_p._right = l
            m._parent = l_p
            if l_p is not None:
                if l_p._left == l:
                    l_p._left = m
                else:
                    l_p._right = m

            # Child Shift
            l._left = m_l
            if m_l is not None:
                m_l._parent = l
            l._right = m_r
            if m_r is not None:
                m_r._parent = l
            m._left = l_l
            if l_l is not None:
                l_l._parent = m
            m._right = l_r
            if l_r is not None:
                l_r._parent = m

        if self.root() == l:
            self._root = m
        elif self.root() == m:
            self._root = l

    def delete(self, loc):
        if self.num_children(loc) == 2:
            raise ValueError('Location has 2 children.')
        parent = self.parent(loc)
        child = self.left(loc)
        if child is None:
            child = self.right(loc)

        if parent is not None:
            if parent._left == loc:
                parent._left = child
            else:
                parent._right = child
        if child is not None:
            child._parent = parent

        self._size -= 1
        return self._data.pop(self.index(loc))

    def _binary_exp(self, n, digit):
        text_list = []
        while n > 0:
            text_list.append(str(n%2))
            n //= 2
        if len(text_list) < digit:
            for i in range(digit-len(text_list)):
                text_list.append('0')
        return ''.join(reversed(text_list))

    def last(self):
        from math import log2
        loc = self.root()
        if len(self) == 1:
            return loc
        height = int(log2(len(self))) + 1
        leaf_idx = len(self) - pow(2, height-1)
        binary = self._binary_exp(leaf_idx, height-1)
        for chr in binary:
            if chr == '0':
                loc = self.left(loc)
            else:
                loc = self.right(loc)
        return loc

    def add(self, key, value):
        new_loc = self.Location(key, len(self))
        self._data.append(value)
        if len(self) == 0:
            self._root = new_loc
            self._size += 1
        else:
            new_loc = self._add_next_position(self.last(), new_loc)
            self._size += 1
            new_loc = self._upheap(new_loc)
        return new_loc

    def _add_next_position(self, last, loc):
        from math import log2
        if self._size == pow(2, int(log2(self._size))+1) - 1:
            target = self._drill_down_left(self.root())
            return self._add_left(target, loc)
        else:
            parent = self.parent(last)
            if last == self.left(parent):
                if self.is_leaf(last):
                    return self._add_right(parent, loc)
                else:
                    target = self._drill_down_left(self.right(parent))
                    return self._add_left(target, loc)
            else:
                return self._add_next_position(parent, loc)

    def _drill_down_left(self, loc):
        while not self.is_leaf(loc):
            loc = self.left(loc)
        return loc

    def _upheap(self, loc):
        parent = self.parent(loc)
        if parent is not None:
            if self.key(parent) > self.key(loc):
                self._swap(parent, loc)
                self._upheap(loc)
        return loc

    def _downheap(self, loc):
        if self.left(loc) is not None:
            small_child = self.left(loc)
            right = self.right(loc)
            if right is not None:
                if self.key(right) < self.key(small_child):
                    small_child = right
            self._swap(loc, small_child)
            self._downheap(loc)
        return loc

    def remove_min(self):
        self._swap(self.root(), self.last())
        popped = self.delete(self.last())
        self._downheap(self.root())
        return popped