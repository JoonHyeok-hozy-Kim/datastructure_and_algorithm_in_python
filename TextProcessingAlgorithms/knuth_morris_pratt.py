

def find_kmp(T, P):
    """ Return the lowest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j-m+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1


def _compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail


def rfind_kmp(T, P):
    """ Return the highest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1


def count_kmp(T, P):
    """ Return the maximum number of nonoverlapping occurrences of a P within T """
    n, m = len(T), len(P)
    cnt = 0
    if m == 0:
        return 0
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        # print('T[{}] : {}, P[{}] : {}'.format(j, T[j], k, P[k]))
        if T[j] == P[k]:
            if k == m-1:
                # print('T[{}:{}] : {}'.format(j-m+1, j+1, T[j-m+1:j+1]))
                cnt += 1
                j += m-2
                k = 0
                continue
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return cnt