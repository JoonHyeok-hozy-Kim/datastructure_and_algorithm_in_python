def sorted_union(A, B):
    result = [None] * (len(A)+len(B))
    i = j = 0
    eq_cnt = 0
    while i+j < len(A)+len(B):
        if i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result[i+j-eq_cnt] = A[i]
                if A[i] == B[j]:
                    result.pop()
                    j += 1
                    eq_cnt += 1
                i += 1
            else:
                result[i+j-eq_cnt] = B[j]
                j += 1
        elif j == len(B):
            result[i+j-eq_cnt] = A[i]
            i += 1
        else:
            result[i+j-eq_cnt] = B[j]
            j += 1
        # print('i: {}, j: {}, {}'.format(i, j, result))

    return result


def in_place_sort_zero_one(S):
    start = 0
    end = len(S)-1
    while (start < end):
        while S[start] == 0 and start < len(S)-1:
            start += 1
        while S[end] == 1 and end > 0:
            end -= 1
        if start < end:
            S[start] = 0
            S[end] = 1
            start += 1
            end -= 1
    return S

def is_sorted(S):
    temp_max = None
    for i in S:
        temp_max = i if temp_max is None else max(temp_max, i)
        if temp_max != i:
            return False
    return True

from DataStructures.priority_queues import HeapPriorityQueue
def duplicate_remover_with_heap(S):
    H = HeapPriorityQueue()
    temp_max = None
    cnt = 0
    for i in range(len(S)):
        e = S[i]
        S[i] = None
        H.add(e, e)
    while not H.is_empty():
        if temp_max is None:
            temp_max = H.remove_min()[0]
            S[cnt] = temp_max
            cnt += 1
        else:
            temp = H.remove_min()[0]
            if temp > temp_max:
                S[cnt] = temp
                temp_max = temp
                cnt += 1
    for i in range(len(S)-cnt):
        S.pop()
    return S


from DataStructures.queue import LinkedQueue
def bottom_up_merge_sort(S):
    Q = LinkedQueue()
    if len(S) == 1:
        Q.enqueue(S[0])
    else:
        mid = len(S)//2
        Q1 = bottom_up_merge_sort(S[:mid])
        Q2 = bottom_up_merge_sort(S[mid:])
        while not (Q1.is_empty() and Q2.is_empty()):
            if Q2.is_empty():
                while not Q1.is_empty():
                    Q.enqueue(Q1.dequeue())
            elif Q1.is_empty():
                while not Q2.is_empty():
                    Q.enqueue(Q2.dequeue())
            elif Q1.first() < Q2.first():
                Q.enqueue(Q1.dequeue())
            else:
                Q.enqueue(Q2.dequeue())
    return Q


if __name__ == '__main__':
    from random import randint
    pass
    # a = [1,2,3,4,5,6]
    # b = [3,6,9,12]
    # # print(sorted_union(a, b))
    #
    # from random import randint
    # from SortingAlgorithms.quick_sort import inplace_quick_sort
    # c = [1,2,2,3,2]
    # c = [1,2]
    # print(c)
    # inplace_quick_sort(c)
    # print(c)


    # from SortingAlgorithms.linear_time_sort import bucket_sort
    # from random import randint
    # b = [randint(0, 99) for i in range(10)]
    # print(b)
    # bucket_sort(b)
    # print(b)


    # a = [(randint(1, 7), randint(1, 7)) for i in range(20)]
    # a = [(4, 3), (2, 1), (5, 5), (4, 4), (2, 5), (1, 0), (4, 5), (2, 2), (1, 2), (2, 2)]
    # print(a)

    # from SortingAlgorithms.linear_time_sort import _bucket_sort_for_radix, radix_sort
    # # _bucket_sort_for_radix(a, 1)
    # # print(a)
    # # _bucket_sort_for_radix(a, 0)
    # # print(a)
    # # radix_sort(a, 2)
    # # print(a)
    #
    # c = []
    # from copy import deepcopy
    # for i in range(5):
    #     d = [5-i, None, None]
    #     for j in range(5):
    #         d_1 = deepcopy(d)
    #         d_1[1] = 5-j
    #         for k in range(5):
    #             d_2 = deepcopy(d_1)
    #             d_2[2] = 5-k
    #             c.append(d_2)
    #
    # print(c)
    # radix_sort(c, 3)
    # print(c)

    # a = [randint(0, 1) for i in range(10)]
    # # a = [0 for i in range(10)]
    # # a = [1 for i in range(10)]
    # print(a)
    # print(is_sorted(a))
    # in_place_sort_zero_one(a)
    # print(a)
    # print(is_sorted(a))

    # b = [1,3, 3, 2, 2, 1, 7, 5, 4]
    # duplicate_remover_with_heap(b)
    # print(b)

    # from DataStructures.linked_list import PositionalList
    # a = PositionalList()
    # b = PositionalList()
    # b.add_last(-0.5)
    # b.add_last(-1)
    # for i in range(5):
    #     a.add_last(2*i)
    #     b.add_last(2*i+1)
    #     b.add_last(2*i+1.5)
    # a.merge(b)
    # print(a)
    # print(b)

    # from DataStructures.linked_list import PositionalList
    # from copy import deepcopy
    # a = [28, 95, 18, 51, 51, 52, 79, 81, 87, 59]
    #
    #
    #
    # b = PositionalList()
    # for i in a:
    #     b.add_last(i)
    # print(b)
    # b.sort()
    # print(b)
    #
    # # from SortingAlgorithms.quick_sort import inplace_quick_sort
    # # print(a)
    # # inplace_quick_sort(a)
    # # print(a)


    # a = [randint(0,100) for i in range(10)]
    # print(a)
    # q = bottom_up_merge_sort(a)
    # while not q.is_empty():
    #     print(q.dequeue(), end=', ')

    from SortingAlgorithms.quick_sort import inplace_quick_sort
    a = [randint(0, 100) for i in range(10)]
    print(a)
    inplace_quick_sort(a)
    print(a)