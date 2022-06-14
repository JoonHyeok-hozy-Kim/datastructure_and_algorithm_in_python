from DataStructures.tree import *
from DataStructures.priority_queues import *

from random import randint
def shuffle(A, result_list=None):
    if result_list is None:
        result_list = []
    idx = randint(0, len(A)-1)
    result_list.append(A.pop(idx))
    if len(A) > 0:
        shuffle(A, result_list)
    return result_list

def selection_sort(A):
    result_list = []
    P = UnsortedPriorityQueue()
    for i in A:
        P.add(i, i)
    while not P.is_empty():
        result_list.append(P.remove_min()[0])
    return result_list

def insertion_sort(C):
    n = len(C)
    P = SortedPriorityQueue()
    for i in range(n):
        e = C.delete(C.first())
        P.add(e, e)
    while not P.is_empty():
        (k, v) = P.remove_min()
        C.add_last(v)

def pq_sort(A):
    result_list = []
    heap = HeapPriorityQueue(A)
    while not heap.is_empty():
        result_list.append(heap.remove_min())
    return result_list

def heap_sort(C):
    n = len(C)
    H = HeapPriorityQueue()
    for i in range(n):
        e = C.delete(C.first())
        H.add(e, e)
    while not H.is_empty():
        (k, v) = H.remove_min()
        C.add_last(v)

if __name__ == '__main__':

    # a = ArrayBasedTree()
    # root = a._add_root(0)
    # left = a._add_left(root, 1)
    # right = a._add_right(root, 2)
    # print(a)
    # print('Swap : {} <> {}'.format(root.element(), right.element()))
    # a.swap(root, right)
    # print(a)
    # print('Delete : {}'.format(a._delete(left)))
    # print(a)
    # right = a.right(a.root())
    # for i in range(4):
    #     right = a._add_right(right, i+4)
    # print(a)

    from random import randint
    h = HeapPriorityQueue()
    size = 5
    a = [(i, chr(randint(0, 25) + 65)) for i in range(size)]
    key_set = shuffle(a)
    print('key set : {}'.format(key_set))
    sorted = pq_sort(key_set)
    print('sorted : {}'.format(sorted))

    # l = [randint(0,100) for i in range(5)]
    # print('BEFORE : {}'.format(l))
    # print('AFTER : {}'.format(selection_sort(l)))
    # print('AFTER : {}'.format(insertion_sort(l)))


    # sorted = pq_sort(key_set)
    # print('sorted : {}'.format(sorted))

    from time import time
    p = PositionalList()
    q = PositionalList()
    size = 800
    for i in range(size):
        n = randint(0, 100)
        p.add_last(n)
        q.add_last(n)
    print(p)
    t1 = time()
    heap_sort(p)
    t2 = time()
    insertion_sort(q)
    t3 = time()
    print('[H] t : {}, result : {}'.format(t2-t1, p))
    print('[I] t : {}, result : {}'.format(t3-t2, q))