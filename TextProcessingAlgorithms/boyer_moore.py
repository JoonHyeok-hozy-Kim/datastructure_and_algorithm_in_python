

def find_boyer_moore(T, P):
    """ Return the lowest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)    # min(k, j+1) : The minimum of
                                    #               (1) k   : m - 1 - (the number of matches in the previous search)
                                    #               (2) j+1 : (the index of the last position that T[i] is contained in P) + 1

            k = m-1                 # Initialize k

    return -1


def rfind_boyer_moore(T, P):
    """ Return the highest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i+m-1
            i -= 1
            k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)    # min(k, j+1) : The minimum of
                                    #               (1) k   : m - 1 - (the number of matches in the previous search)
                                    #               (2) j+1 : (the index of the last position that T[i] is contained in P) + 1

            k = m-1                 # Initialize k

    return -1


def count_boyer_moore(T, P):
    """ Return the maximum number of nonoverlapping occurrences of a P within T """
    n, m = len(T), len(P)
    cnt = 0
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while 0 <= i < n:
        # print('T[{}] : {}, P[{}] : {}'.format(i, T[i], k, P[k]))
        if T[i] == P[k]:
            if k == 0:
                # print('T[{}:{}] : {}'.format(i, i+m, T[i:i+m]))
                cnt += 1
                k = m-1
                i += m*2-1
                continue
            i -= 1
            k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m-1

    return cnt
