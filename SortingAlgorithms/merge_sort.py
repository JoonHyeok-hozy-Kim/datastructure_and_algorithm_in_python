

# Array Based Merge-Sort starts
import math


def _merge_array(S1, S2, S):
    """ Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1


def merge_sort_array(S):

    n = len(S)
    if n < 2:
        return

    # Divide
    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]

    # Conquer (with recursion)
    merge_sort_array(S1)
    merge_sort_array(S2)

    # Combine results
    _merge_array(S1, S2, S)
# Array Based Merge-Sort ends


# LinkedQueue Based Merge-Sort starts
def _merge_queue(S1, S2, S):
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():
        S.enqueue(S1.dequeue())
    while not S2.is_empty():
        S.enqueue(S2.dequeue())


from DataStructures.queue import LinkedQueue
def merge_sort_queue(S):
    n = len(S)
    if n < 2:
        return
    S1 = LinkedQueue()
    S2 = LinkedQueue()

    while len(S1) < n//2:
        S1.enqueue(S.dequeue())
    while not S.is_empty():
        S2.enqueue(S.dequeue())

    merge_sort_queue(S1)
    merge_sort_queue(S2)

    _merge_queue(S1, S2, S)
# LinkedQueue Based Merge-Sort ends


# Bottom-Up Merge-Sort starts
def _merge_bottom_up(src, result, start, inc):
    end1 = start + inc
    end2 = min(start + 2*inc, len(src))
    x, y, z = start, start+inc, start
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1
        else:
            result[z] = src[y]
            y += 1
        z += 1
    if x < end1:
        result[z:end2] = src[x:end1]
    elif y < end2:
        result[z:end2] = src[y:end2]

def merge_sort_bottom_up(S):
    n = len(S)
    logn = math.ceil(math.log2(n))
    src, dest = S, [None] * n
    for i in (2**k for k in range(logn)):
        for j in range(0, n, 2*i):
            _merge_bottom_up(src, dest, j, i)
        src, dest = dest, src
    if S is not src:
        S[0:n] = src[0:n]
# Bottom-Up Merge-Sort ends