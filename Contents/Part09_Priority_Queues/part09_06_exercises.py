from DataStructures.priority_queues import *
def heap_sort_naive(A):
    n = len(A)
    H = HeapPriorityQueue()
    for i in range(n):
        popped = A.pop(0)
        H.add(popped, popped)
    for i in range(n):
        A.append(H.remove_min()[0])
    return A

def preorder(H, j=0, text_list=[]):
    text_list.append(str(H._data[j]._key))
    if H._has_left(j):
        preorder(H, H._left(j), text_list)
    if H._has_right(j):
        preorder(H, H._right(j), text_list)
    return ' - '.join(text_list)

def postorder(H, j=0, text_list=[]):
    if H._has_left(j):
        postorder(H, H._left(j), text_list)
    if H._has_right(j):
        postorder(H, H._right(j), text_list)
    text_list.append(str(H._data[j]._key))
    return ' - '.join(text_list)

def inorder(H, j=0, text_list=[]):
    if H._has_left(j):
        inorder(H, H._left(j), text_list)
    text_list.append(str(H._data[j]._key))
    if H._has_right(j):
        inorder(H, H._right(j), text_list)
    return ' - '.join(text_list)

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

from DataStructures.priority_queues import HeapPriorityQueue
class HeapStack:
    def __init__(self):
        self._heap = HeapPriorityQueue()

    def push(self, e):
        self._heap.add(len(self._heap), e)

    def pop(self):
        return self._heap._data.pop()._value

from DataStructures.priority_queues import HeapPriorityQueue
class HeapQueue:
    def __init__(self):
        self._heap = HeapPriorityQueue()

    def enqueue(self, e):
        self._heap.add(len(self._heap), e)

    def dequeue(self):
        return self._heap.remove_min()[1]

from DataStructures.priority_queues import PriorityQueueBase
class ListSortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        item = self._Item(key, value)
        idx = None
        for i in range(len(self)):
            if item < self._data[i]:
                idx = i
                break
        if idx is None:
            self._data.append(item)
        else:
            self._data.insert(idx, item)


    def min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data.pop(0)
        return (item._key, item._value)


from DataStructures.tree import LinkedBinaryTree
class LinkedHeapBinaryTree(LinkedBinaryTree):

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def __str__(self):
            return '({}, {})'.format(self._key, self._value)

    def __init__(self):
        super().__init__()
        self._last_position = None
        self._max_height = 1

    def last(self):
        return self._last_position

    def _swap(self, p, q):
        if self._last_position == p:
            self._last_position = q
        elif self._last_position == q:
            self._last_position = p
        super()._swap(p, q)

    def _upheap(self, p):
        while p != self.root():
            parent = self.parent(p)
            if p.element() < parent.element():
                self._swap(p, parent)

    def _downheap(self, p):
        if len(self) == 0:
            return
        while not self.is_leaf(p):
            if self.left(p) is not None:
                small_child = self.left(p)
                if self.right(p) is not None:
                    right = self.right(p)
                    if right.element() < small_child.element():
                        small_child = right
                # print('[DOWN] {} - {}'.format(p.element(), small_child.element()))
                if p.element() > small_child.element():
                    self._swap(p, small_child)
                else:
                    return

    def add(self, key, value):
        new_item = self._Item(key, value)
        if self._last_position is None:
            self._last_position = self._add_root(new_item)
        elif self._size == pow(2, self._max_height)-1:
            self._last_position = self._add_drill_left(self.root(), new_item)
            self._max_height += 1
        else:
            self._last_position = self._add_next_last_position(self._last_position, new_item)
        self._upheap(self._last_position)

    def _add_drill_left(self, p, new_item):
        while not self.is_leaf(p):
            p = self.left(p)
        return self._add_left(p, new_item)

    def _add_next_last_position(self, p, new_item):
        parent = self.parent(p)
        if p == self.left(parent):
            if self.is_leaf(p):
                return self._add_right(parent, new_item)
            else:
                right_sibling = self.right(parent)
                return self._add_drill_left(right_sibling, new_item)
        else:
            return self._add_next_last_position(parent, new_item)

    def remove_min(self):
        root_copy = self.root()
        # print('[RM] root : {}'.format(self.root().element()))
        # print('[RM] last : {}'.format(self.last().element()))
        self._swap(self.root(), self.last())
        self._last_position = self._after_remove_last_position(root_copy)
        deleted = self._delete(root_copy)
        self._downheap(self.root())
        return deleted

    def _after_remove_last_position(self, current_last):
        if current_last == self.root():
            return None
        if self._size == pow(2, self._max_height-1):
            self._max_height -= 1
            return self._after_remove_drill_right(self.root())
        parent = self.parent(current_last)
        if current_last == self.right(parent):
            if self.is_leaf(current_last):
                return self.left(parent)
            else:
                left_sibling = self.left(parent)
                return self._after_remove_drill_right(left_sibling)
        else:
            return self._after_remove_last_position(parent)

    def _after_remove_drill_right(self, p):
        while not self.is_leaf(p):
            if self.right(p) is not None:
                p = self.right(p)
            else:
                break
        return p

from math import log2
def last_node_from_binary_string(T):
    n = len(T)
    if n == 1:
        return T.root()
    max_height = int(log2(n)) + 1
    leaf_cnt = n - pow(2, max_height-1) + 1
    path = _binary_exp(leaf_cnt-1, max_height-1)
    return _decode_binary_string_path(T, path)

def _binary_exp(n, digit):
    result_list = []
    if n == 0:
        result_list.append(str(0))
    else:
        while n > 0:
            result_list.append(str(n%2))
            n //= 2
    for i in range(digit - len(result_list)):
        result_list.append('0')
    return ''.join(reversed(result_list))

def _encode_binary_string_path(T, p, path_list=[]):
    if T.root() == p:
        return ''.join(reversed(path_list))
    parent = T.parent(p)
    if T.left(parent) == p:
        path_list.append('0')
    else:
        path_list.append('1')
    return _encode_binary_string_path(T, parent, path_list)

def _decode_binary_string_path(T, s):
    p = T.root()
    for i in s:
        if i == '0':
            if T.left(p) is None:
                return None
            p = T.left(p)
        else:
            if T.right(p) is None:
                return None
            p = T.right(p)
    return p

def all_entries_less_than(H, key, idx=0, result_list=[]):
    print('cnt')
    if H._data[idx]._key <= key:
        result_list.append(H._data[idx])
        if H._has_left(idx):
            all_entries_less_than(H, key, H._left(idx), result_list)
        if H._has_right(idx):
            all_entries_less_than(H, key, H._right(idx), result_list)
    return result_list

from math import log2
def frequent_flyers(L):
    result_list = []
    n = len(L)
    H = HeapPriorityQueue(L)
    print(H)
    top_cnt = int(log2(n))
    for i in range(top_cnt):
        result_list.append(H.remove_min())
    return result_list

def k_largest_elements(L, k):
    result_list = []
    result_list.append(L[0])
    if k > 1:
        H = HeapPriorityQueue()
        for i in range(len(L)-1):
            if L[i+1] > result_list[0]:
                temp = result_list.pop()
                result_list.append(L[i+1])
            else:
                temp = L[i+1]
            if len(H) < k-1:
                H.add(temp, temp)
            else:
                H.heappushpop(temp, temp)
        while not H.is_empty():
            result_list.append(H.remove_min()[0])
    return result_list

def pq_sort_key(C):
    n = len(C)
    P = HeapPriorityQueue()
    for i in range(n):
        element = C.delete(C.first())
        P.add(element._key, element._value)

def selection_sort_in_place(A):
    A.append(A.pop(0))
    for i in range(len(A)-1):
        temp = A.pop(0)
        idx = len(A)-1
        for j in range(i+1):
            if temp < A[len(A)-2-j]:
                idx = len(A)-2-j
        A.insert(idx, temp)
    return A

def insertion_sort_in_place(A):
    for i in range(len(A)):
        idx = 0
        for j in range(len(A)-i):
            if A[j] < A[idx]:
                idx = j
        A.append(A.pop(idx))
    return A


def heap_sort_min(A):
    n = len(A)
    heap_start = 0
    heap_len = 1
    for i in range(n):
        popped = A.pop(n-1)
        A.insert(0, popped)
        # print('BEFORE UP : {}'.format(A))
        _heap_sort_downheap_min(A, heap_len, 0)
        heap_len += 1
    heap_len -= 1
    for i in range(n):
        current_min_idx = _heap_sort_remove_min(A, heap_len)
        A.append(A.pop(current_min_idx))
        heap_len -= 1
    print(A)
    return A

def _heap_sort_parent_min(j):
    return (j-1)//2

def _heap_sort_left_min(n, heap_len, j):
    idx = j*2+1
    if n-1 < idx or idx > heap_len-1:
        return None
    return idx

def _heap_sort_right_min(n, heap_len, j):
    idx = j*2+2
    if n-1 < idx or idx > heap_len-1:
        return None
    return idx

def _heap_sort_swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def _heap_sort_upheap_min(A, j):
    if j > 0:
        parent = _heap_sort_parent_min(j)
        # print('[UP] {} - {}'.format(A[parent], A[j]))
        if A[parent] > A[j]:
            _heap_sort_swap(A, parent, j)
            # print('[UP] swapped : {}'.format(A))
            _heap_sort_upheap_min(A, parent)

def _heap_sort_downheap_min(A, heap_len, j):
    left = _heap_sort_left_min(len(A), heap_len, j)
    if left is not None:
        small_child = left
        right = _heap_sort_right_min(len(A), heap_len, j)
        if right is not None:
            if A[right] < A[left]:
                small_child = right
        # print('[DOWN] {} - {}'.format(A[j], A[big_child]))
        if A[j] > A[small_child]:
            _heap_sort_swap(A, j, small_child)
            # print('[DOWN] swapped : {}'.format(A))
            _heap_sort_downheap_min(A, heap_len, small_child)

def _heap_sort_remove_min(A, heap_len):
    last = heap_len -1
    _heap_sort_swap(A, 0, last)
    _heap_sort_downheap_min(A, heap_len-1, 0)
    return last


from DataStructures.priority_queues import HeapPriorityQueue, MaxPriorityQueue
class StockTrading:
    def __init__(self):
        self._buy = MaxPriorityQueue()
        self._sell = HeapPriorityQueue()
        self._successful_transactions = []

    def visualize_queues(self):
        print('BUY')
        print(self._buy)
        print('SELL')
        print(self._sell)
        print('SUCCESS')
        print(self._successful_transactions)
        print('-------------------------------')

    def buy(self, price, quantity):
        while (not self._sell.is_empty()) and quantity > 0:
            min_sell = self._sell.min()
            if min_sell[0] <= price:
                popped = self._sell.remove_min()
                if popped[1] == quantity:
                    self._successful_transactions.append(('SELL', popped[0], popped[1]))
                    self._successful_transactions.append(('BUY', price, quantity))
                    quantity -= popped[1]
                else:
                    self._successful_transactions.append(('SELL', popped[0], min(popped[1], quantity)))
                    self._successful_transactions.append(('BUY', price, min(popped[1], quantity)))

                    if popped[1] > quantity:
                        self._sell.add(popped[0], popped[1] - quantity)
                        quantity = 0
                    else:
                        quantity -= popped[1]
            else:
                break
        if quantity > 0:
            self._buy.add(price, quantity)


    def sell(self, price, quantity):
        while (not self._buy.is_empty()) and quantity > 0:
            max_buy = self._buy.max()
            if max_buy[0] >= price:
                popped = self._buy.remove_max()
                if popped[1] == quantity:
                    self._successful_transactions.append(('BUY', popped[0], popped[1]))
                    self._successful_transactions.append(('SELL', price, quantity))
                    quantity -= popped[1]
                else:
                    self._successful_transactions.append(('BUY', popped[0], min(popped[1], quantity)))
                    self._successful_transactions.append(('SELL', price, min(popped[1], quantity)))

                    if popped[1] > quantity:
                        self._buy.add(popped[0], popped[1] - quantity)
                        quantity = 0
                    else:
                        quantity -= popped[1]
            else:
                break
        if quantity > 0:
            self._sell.add(price, quantity)


from DataStructures.queue import LinkedQueue
from DataStructures.tree import MutableLinkedBinaryTree
def priority_search_tree_builder(S):
    Q = LinkedQueue()
    for i in S:
        new_tree = MutableLinkedBinaryTree()
        new_tree.add_root(i)
        Q.enqueue(new_tree)
    while True:
        left = Q.dequeue()
        print('left')
        print(left)
        if not Q.is_empty():
            right = Q.dequeue()
            print('right')
            print(right)
            new_tree = MutableLinkedBinaryTree()
            if left.root().element()[1] > right.root().element()[1]:
                root = new_tree.add_root(left.root().element())
            else:
                root = new_tree.add_root(right.root().element())
            new_tree.add_left(root, left)
            new_tree.add_right(root, right)
            Q.enqueue(new_tree)
        else:
            break
    return left


from DataStructures.queue import LinkedQueue
class CPUSchedulingJobs:

    class _CPU:
        __slots__ = '_process'

        def __init__(self):
            self._process = None

        def get_time_slice(self, time_slice=None):
            self._process = [time_slice[0], time_slice[1], time_slice[2], 0]

        def operate(self):
            if self._process is None:
                print("no new job this slice")
                return
            self._process[3] = 1
            if self._process[3] == 1:
                print("add job {} with length {} and priority {}".format(self._process[0], self._process[1], self._process[2]))
            processed = self._process
            self._process = None
            return processed

    class _Memory:
        __slots__ = '_to_do_job_queue', '_finished_job_list', '_priority_min', '_priority_max'

        def __init__(self):
            self._to_do_job_queue = HeapPriorityQueue()
            self._finished_job_list = []
            self._priority_min = -20
            self._priority_max = 19

        def add_job_to_memory(self, job):
            if not (self._priority_min <= job._priority <= self._priority_max):
                raise ValueError('Priority out of available band.')
            return self._to_do_job_queue.add(job._priority, job)

        def get_to_do_jobs(self):
            while not self._to_do_job_queue.is_empty():
                job = self._to_do_job_queue.remove_min()[1]
                for i in range(job._length):
                    yield (job._name, job._length, job._priority)

        def get_finished_jobs(self, job):
            from datetime import datetime
            finished_job = {'job': job, 'finished_time': datetime.now()}
            self._finished_job_list.append(finished_job)
            return finished_job

        def show_finished_jobs(self):
            for job in self._finished_job_list:
                print('{} [{}]'.format(job['job'], job['finished_time']))

    class _Job:
        __slots__ = '_name', '_length', '_priority'

        def __init__(self, name, length, priority=None):
            self._name = name
            self._length = length
            self._priority = priority

        def __str__(self):
            return "job {} with length {} and priority {}".format(self._name, self._length, self._priority)

    def __init__(self):
        self._cpu = self._CPU()
        self._memory = self._Memory()

    def add_job(self, name, length, priority):
        new_job = self._Job(name, length, priority)
        return self._memory.add_job_to_memory(new_job)

    def run(self):
        current_job = None
        job_time_slice_cnt = 0
        for process in self._memory.get_to_do_jobs():
            if (current_job is None) or not (current_job[0], current_job[1], current_job[2] == process[0], process[1], process[2]):
                current_job = process
                job_time_slice_cnt = 0

            self._cpu.get_time_slice(process)
            processed = self._cpu.operate()
            job_time_slice_cnt += processed[3]

            if job_time_slice_cnt == current_job[1]:
                self._memory.get_finished_jobs(current_job)
                current_job = None
        self._memory.show_finished_jobs()


from DataStructures.tree import BinaryLayout
class UnsortedPriorityQueue:
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




if __name__ == '__main__':
    from random import randint
    size = 5
    l = [randint(0, 100) for i in range(size)]
    k = [i for i in range(size, -1, -1)]
    # print(k)

    # from DataStructures.priority_queues import HeapPriorityQueue
    # a = HeapPriorityQueue()
    # for i in range(15):
    #     a.add(i, i)
    # print(preorder(a))
    # print(postorder(a))
    # print(inorder(a))

    # a.add(1, 1)
    # l_idx = 3
    # r_idx = 33
    # h_idx = 0
    # while h_idx < 4:
    #     for i in range(pow(2, h_idx)):
    #         a.add(l_idx, l_idx)
    #         l_idx += 2
    #     for i in range(pow(2, h_idx)):
    #         a.add(r_idx, r_idx)
    #         r_idx += 2
    #         if r_idx >59:
    #             break
    #     h_idx += 1
    # print(a)
    # a.add(32, 32)
    # print(a)

    # x = [randint(0, 100) for i in range(10)]
    # print(x)
    # heap_sort(x)
    # print(x)

    # from random import randint
    # hs = HeapStack()
    # for i in range(5):
    #     e = randint(0, 100)
    #     print('Push {}'.format(e))
    #     hs.push(e)
    # for i in range(5):
    #     print(hs.pop())

    # from random import randint
    # hq = HeapQueue()
    # for i in range(5):
    #     e = randint(0, 100)
    #     print('Enqueue {}'.format(e))
    #     hq.enqueue(e)
    # for i in range(5):
    #     print(hq.dequeue())

    # x = ListSortedPriorityQueue()
    # print(l)
    # for i in l:
    #     x.add(i, i)
    # while not x.is_empty():
    #     print(x.remove_min())

    # from math import log2
    # print(round(log2(9)))
    # a = LinkedHeapBinaryTree()
    # for i in range(7):
    #     print(a.add(i+1, i+1).element())
    #     print(a)

    # a = LinkedHeapBinaryTree()
    # for i in range(14,-1,-1):
    #     a.add(i+1, i+1)
    # print(a)
    # for i in range(15):
    #     print('REMOVED_MIN : {}'.format(a.remove_min()))
    #     print(a)
    # print('root : {}'.format(a.root()))
    # print('last : {}'.format(a.last()))

    # for i in range(15):
    #     a = LinkedBinaryTree()
    #     a.fill_tree(i+1)
    #     print(a)
    #     b = last_node_from_binary_string(a)
    #     print(b.element())

    # s = StockTrading()
    # s.buy(100, 5)
    # s.visualize_queues()
    # s.sell(120, 3)
    # s.visualize_queues()
    # s.buy(130, 4)
    # s.visualize_queues()
    # s.sell(90, 7)
    # s.visualize_queues()

    # from copy import deepcopy
    # from time import time
    # l_naive = deepcopy(l)
    # t1 = time()
    # heap_sort_naive(l_naive)
    # t2 = time()
    # heap_sort(l)
    # t3 = time()
    # print('[naive   ] {}'.format(t2-t1))
    # print('[in-place] {}'.format(t3-t2))

    # from DataStructures.linked_list import FavoriteListMTF
    # f = FavoriteListMTF()
    # for i in range(10):
    #     f.access(i)
    # for i in range(100):
    #     f.access(randint(0, 9))
    # t = f.top(5)
    # for i in t:
    #     print('val : {}, cnt : {}'.format(i.element()._value, i.element()._count))

    # l = [(i, randint(0, 100))  for i in range(size)]
    # priority_search_tree_builder(l)

    # j = CPUSchedulingJobs()
    # l = [randint(-20, 19) for i in range(-20, 20)]
    # for i in range(len(l)):
    #     j.add_job('Job_' + str(l[i]) + chr(65+randint(0, 25)),
    #               randint(1, 100),
    #               l[i])
    # j.run()

    u = UnsortedPriorityQueue()
    u.add(0, 'A')
    u.add(2, 'B')
    u.add(3, 'C')
    u.add(-1, 'E')
    u.add(-2, 'F')
    u.add(-3, 'G')
    u.add(-4, 'H')
    print(u)
    print(u.remove_min())
    print(u)