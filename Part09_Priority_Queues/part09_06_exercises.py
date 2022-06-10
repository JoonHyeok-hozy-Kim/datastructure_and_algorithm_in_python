from DataStructures.priority_queues import HeapPriorityQueue
def heap_sort(A):
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


if __name__ == '__main__':
    from random import randint
    size = 16
    l = [randint(0, 100) for i in range(size)]
    k = [i for i in range(size, -1, -1)]
    print(k)

    from DataStructures.priority_queues import HeapPriorityQueue
    a = HeapPriorityQueue()
    # for i in range(15):
    #     a.add(i, i)
    # print(preorder(a))
    # print(postorder(a))
    # print(inorder(a))

    b = heap_sort(k)
    print(b)





