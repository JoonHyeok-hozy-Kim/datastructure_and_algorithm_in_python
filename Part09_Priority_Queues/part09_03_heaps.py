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
    a = [(i, chr(randint(0, 25)+65)) for i in range(size)]
    key_set = shuffle(a)
    print('key set : {}'.format(key_set))
    for k, v in key_set:
        h.add(k, v)
    while not h.is_empty():
        print(h.remove_min())

    print('key set : {}'.format(key_set))
    b = HeapPriorityQueue(key_set)
    while not b.is_empty():
        print(b.remove_min())