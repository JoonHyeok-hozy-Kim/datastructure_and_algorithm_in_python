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