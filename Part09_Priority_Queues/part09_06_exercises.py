from DataStructures.priority_queues import HeapPriorityQueue
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
        self._last_node = None

    def add(self, key, value):
        item = self._Item(key, value)
        if self._last_node is None:
            self._last_node = self._add_root(item)
        else:
            parent = self.parent(self._last_node)
            if self._last_node == self.left(parent):
                self._last_node = self._add_right(parent, item)
            else:
                pass

    def _next_last_position(self, p, up_cnt):
        parent = self.parent(p)
        if p == self.left(parent):
            if self.right(parent) is None:
                return self._add_right(parent, None)
            else:
                pass
        else:
            pass

    def _go_down_left(self, p, up_cnt):
        pass

if __name__ == '__main__':
    from random import randint
    size = 16
    l = [randint(0, 100) for i in range(size)]
    k = [i for i in range(size, -1, -1)]
    # print(k)

    from DataStructures.priority_queues import HeapPriorityQueue
    a = HeapPriorityQueue()
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

    from math import log2
    print(round(log2(9)))








