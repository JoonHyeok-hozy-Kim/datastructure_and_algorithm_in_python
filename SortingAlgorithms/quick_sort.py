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


def inplace_quick_sort(S, a, b):

    if a >= b: return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1