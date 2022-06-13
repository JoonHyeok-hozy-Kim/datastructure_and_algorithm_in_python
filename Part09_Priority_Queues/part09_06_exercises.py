from DataStructures.priority_queues import *
def heap_sort_naive(A):
    n = len(A)
    H = HeapPriorityQueue()
    for i in range(n):
        popped = A.pop(0)
        print('[Add] {}'.format(popped))
        H.add(popped, popped)
    for i in range(n):
        A.append(H.remove_min()[0])
        print('[Remove] {}'.format(A[-1]))
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

if __name__ == '__main__':
    from random import randint
    size = 15
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

    l = [16, 21, 42, 19, 65, 80, 90, 57, 30, 36, 24, 66, 17, 31]
    print(l)
    insertion_sort_in_place(l)
    print(l)


