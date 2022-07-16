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


def in_place_equal_considered(S):
    n = len(S)
    if n == 1:
        return S
    p = n-1
    while True:
        k = p
        while k > 0 and S[k-1] > S[p] and S[k-1] <= S[k]:
            k -= 1
        j = k
        if j > 0:
            while j > 0 and S[j-1] == S[p]:
                j -= 1
        i = j
        if i > 0:
            while i > 0 and S[i-1] < S[p] and S[i-1] <= S[i]:
                i -= 1

        # print('{} [i:{}, j:{}, k:{}]'.format(S, i, j, k))

        if i == 0:
            temp = S[p]
            l = n-1
            while l > k:
                S[l] = S[l-1]
                l -= 1
            S[k] = temp
            return

        else:
            temp = S[i-1]
            l = i-1
            while l < j-1:
                S[l] = S[l+1]
                l += 1
            S[j-1] = S[p]
            S[p] = temp


from SortingAlgorithms.quick_sort import inplace_quick_sort
def election_winner(S):
    race = [[S[0], 0], [None, None]]
    inplace_quick_sort(S)
    for i in S:
        if i == race[0][0]:
            race[0][1] += 1
        else:
            if race[1][0] is None:
                race[1][0] = i
                race[1][1] = 1
            elif race[1][0] == i:
                race[1][1] += 1

                if race[0][1] < race[1][1]:
                    race[0][0] = race[1][0]
                    race[0][1] = race[1][1]
                    race[1][0] = None
                    race[1][1] = None
            else:
                race[1][0] = i
                race[1][1] = 1

    return race[0][0] if (race[1][1] is None or race[0][1] > race[1][1]) else None


def candidate_known_election_winner(S, k):
    candidates = [[None, None] for i in range(k)]
    for e in S:
        for i in range(k):
            if candidates[i][0] is None:
                candidates[i][0] = e
                candidates[i][1] = 0
                break
            elif candidates[i][0] == e:
                candidates[i][1] += 1
                if candidates[i][1] > candidates[0][1]:
                    candidates[0], candidates[i] = candidates[i], candidates[0]
    # print(candidates)
    return candidates[0][0]


def k_less_than_n_election_winner(S):
    candidates = []
    leader = None
    for e in S:
        if len(candidates) < e:
            for i in range(len(candidates), e):
                candidates.append([i, 1])
        else:
            candidates[e-1][1] += 1
    print(candidates)
    for c in range(len(candidates)):
        if leader is None:
            leader = c
        else:
            if candidates[c][1] > candidates[leader][1]:
                leader = c
    return leader+1


from SortingAlgorithms.quick_sort import inplace_quick_sort
def sequence_elements_comparison(S, T):
    inplace_quick_sort(S)
    inplace_quick_sort(T)
    s_i = 0
    t_i = 0
    while s_i < len(S) and t_i < len(T):
        target = T[t_i]

        if S[s_i] == T[t_i]:
            while s_i < len(S) and S[s_i] == target:
                s_i += 1
        else:
            return False
        while t_i < len(T) and T[t_i] == target:
            t_i += 1

    return True if s_i == len(S) and t_i == len(T) else False


def squared_range_sorting(S):
    n = len(S)
    buckets = [[] for i in range(n)]
    for e in S:
        root = int(pow(e, .5))
        # print('e : {}, root : {}'.format(e, root))
        idx = 0
        if len(buckets[root]) == 0:
            buckets[root].append(e)
        else:
            for i in buckets[root]:
                if i < e:
                    idx += 1
                else:
                    break
            buckets[root].insert(idx, e)
        # print(buckets)
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result


def sort_sequences(seq_set, N):
    buckets = [[i, []] for i in range(N)]
    for j in range(len(seq_set)):
        for k in range(len(seq_set[j])):
            val = seq_set[j][k]
            buckets[val][1].append(j)
        seq_set[j] = []

    for bucket in buckets:
        for j in bucket[1]:
            seq_set[j].append(bucket[0])
    return seq_set


def repeated_element_finder(S):
    if len(S) == 1:
        return None
    return _merge_sort_application(S)[1]

def _merge_sort_application(S):
    if len(S) == 1:
        return S, None

    mid = len(S)//2
    # print('S[:mid] : {}\nS[mid:] : {}'.format(S[:mid], S[mid:]))
    S1, r1 = _merge_sort_application(S[:mid])
    S2, r2 = _merge_sort_application(S[mid:])

    # print('r1 : {}, S1 : {}\nr2 : {}, S2 : {}'.format(r1, S1, r2, S2))
    if r1 is not None:
        return S, r1
    elif r2 is not None:
        return S, r2
    else:
        return _merge_sequences(S1, S2)

def _merge_sequences(S1, S2):
    temp = []
    i1 = 0
    i2 = 0
    while i1 < len(S1) and i2 < len(S2):
        v1, v2 = S1[i1], S2[i2]
        if v1 == v2:
            return temp, v1
        elif v1 < v2:
            temp.append(v1)
            i1 += 1
        else:
            temp.append(v2)
            i2 += 1

    if i1 < len(S1):
        temp.extend(S1[i1:])
    if i2 < len(S2):
        temp.extend(S2[i2:])

    return temp, None


from SortingAlgorithms.quick_sort import quick_sort_sequences_by_key_k
def inversion_counter(S):
    result = 0
    new_S = [[S[i], i] for i in range(len(S))]
    quick_sort_sequences_by_key_k(new_S, 0)
    for i in range(len(new_S)):
        if new_S[i][1] < i:
            result += i - new_S[i][1]
    return result

def get_inversion_pairs(S):
    inversion_partners = []
    pair_result = []
    new_S = [[S[i], i] for i in range(len(S))]
    quick_sort_sequences_by_key_k(new_S, 0)
    for i in range(len(new_S)):
        if new_S[i][1] > i:
            inversion_partners.append([new_S[i][0], new_S[i][1]-i])
    for i in range(len(new_S)):
        if new_S[i][1] < i:
            for partner in inversion_partners:
                if partner[1] > 0 and partner[0] < new_S[i][0]:
                    pair_result.append([new_S[i][0], partner[0]])
                    partner[1] -= 1
    return pair_result







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

    # from SortingAlgorithms.quick_sort import inplace_quick_sort
    # a = [randint(0, 100) for i in range(10)]
    # print(a)
    # inplace_quick_sort(a)
    # print(a)


    # from random import randint
    # a = [randint(1,7) for i in range(10)]
    # print(a)
    # in_place_equal_considered(a)
    # print(a)

    # from random import randint
    # a = [randint(0,5) for i in range(1000)]
    # print(a)
    # w = election_winner(a)
    # print(w)

    # from random import randint
    # a = [randint(1,5) for i in range(1000)]
    # print(a)
    # w = candidate_known_election_winner(a, 4)
    # print(w)

    # from random import randint
    # a = [randint(1,5) for i in range(10)]
    # print(a)
    # w = k_less_than_n_election_winner(a)
    # print(w)

    # s = [5,1,2,3,4,4,4,4,4,8]
    # t = [1,1,2,3,4,5,1,2,3]
    # print(sequence_elements_comparison(s, t))

    # from random import randint
    # n = 10
    # a = [randint(0, n*n-1) for i in range(n)]
    # print(a)
    # s_a = squared_range_sorting(a)
    # print(s_a)

    # from random import randint
    # N = 10
    # k = 5
    # seq_set = [[randint(0, N-1) for i in range(randint(1, N-1))] for j in range(k)]
    # print(seq_set)
    # sort_sequences(seq_set, N)
    # print(seq_set)

    # from random import randint
    # n = 100
    # a = [randint(0, n) for i in range(n//10)]
    # print(a)
    # print(repeated_element_finder(a))

    # n = 100
    # a = [randint(0, n) for i in range(n//10)]
    # print(a)
    # print(inversion_counter(a))


    n = 100
    a = [randint(0, n) for i in range(n//10)]
    a_p = get_inversion_pairs(a)
    print(a_p)
