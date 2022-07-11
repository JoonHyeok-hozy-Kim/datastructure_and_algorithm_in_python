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




if __name__ == '__main__':
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


    from SortingAlgorithms.linear_time_sort import bucket_sort
    from random import randint
    # b = [randint(0, 99) for i in range(10)]
    # print(b)
    # bucket_sort(b)
    # print(b)


    # a = [(randint(1, 7), randint(1, 7)) for i in range(20)]
    # a = [(4, 3), (2, 1), (5, 5), (4, 4), (2, 5), (1, 0), (4, 5), (2, 2), (1, 2), (2, 2)]
    # print(a)

    from SortingAlgorithms.linear_time_sort import _bucket_sort_for_radix, radix_sort
    # _bucket_sort_for_radix(a, 1)
    # print(a)
    # _bucket_sort_for_radix(a, 0)
    # print(a)
    # radix_sort(a, 2)
    # print(a)

    c = []
    from copy import deepcopy
    for i in range(5):
        d = [5-i, None, None]
        for j in range(5):
            d_1 = deepcopy(d)
            d_1[1] = 5-j
            for k in range(5):
                d_2 = deepcopy(d_1)
                d_2[2] = 5-k
                c.append(d_2)

    print(c)
    radix_sort(c, 3)
    print(c)