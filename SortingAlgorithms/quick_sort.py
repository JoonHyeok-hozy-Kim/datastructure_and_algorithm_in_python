from DataStructures.queue import LinkedQueue


def quick_sort(S):
    n = len(S)
    if n < 2:
        return
    p = S.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif S.first() == p:
            E.enqueue(S.dequeue())
        else:
            G.enqueue(S.dequeue())

    quick_sort(L)
    quick_sort(G)

    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


from random import randint
def inplace_quick_sort(S, a=0, b=None):
    if b is None:
        b = len(S)-1
    if a >= b: return

    # Random pivot selection
    p = randint(a, b)
    S[p], S[b] = S[b], S[p]

    pivot = S[b]
    left = a
    right = b-1
    # print('[Initial] pivot : {}, {}'.format(pivot, S))
    while left <= right:
        # print(' -> left : {}'.format(S[left]), end='')
        while left <= right and S[left] < pivot:
            left += 1
        #     print(' -> {}'.format(S[left]), end='')
        # print('\n -> right : {}'.format(S[right]), end='')
        while left <= right and pivot < S[right]:
            right -= 1
            # print(' -> {}'.format(S[right]), end='')

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
            # print('\n[After swap 1] {}'.format(S))
            # print(' left : {}, right : {}'.format(S[left], S[right]))

    S[left], S[b] = S[b], S[left]
    # print('\n[After swap 2] {}'.format(S))

    # if a < left-1:
    #     print('\n[Recursion 1] {} ~ {}'.format(S[a], S[left-1]))
    # else:
    #     print('[Recursion 1] RETURN')
    inplace_quick_sort(S, a, left-1)
    # if left+1 < b:
    #     print('\n[Recursion 2] {} ~ {}'.format(S[left+1], S[b]))
    # else:
    #     print('[Recursion 2] RETURN')
    inplace_quick_sort(S, left+1, b)


def quick_sort_sequences_by_key_k(seq_set, k):
    # Length Validation
    for seq in seq_set:
        if len(seq)-1 < k:
            raise KeyError('seq element length error.')

    if len(seq_set) == 1:
        return seq_set

    pivot_val = seq_set[0][k]
    L, E, G = [], [], []
    while len(seq_set) > 0:
        popped = seq_set.pop()
        if popped[k] < pivot_val:
            L.append(popped)
        elif popped[k] == pivot_val:
            E.append(popped)
        else:
            G.append(popped)

    L = quick_sort_sequences_by_key_k(L, k) if len(L) > 1 else L
    G = quick_sort_sequences_by_key_k(G, k) if len(G) > 1 else G

    seq_set.extend(L)
    seq_set.extend(E)
    seq_set.extend(G)
    return seq_set