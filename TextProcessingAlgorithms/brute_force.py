

def find_brute(T, P):
    """ Return the lowest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1


def rfind_brute(T, P):
    """ Return the highest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m:
            return i+m-1
    return -1


def count_brute(T, P):
    """ Return the maximum number of nonoverlapping occurrences of a P within T """
    n, m = len(T), len(P)
    cnt = 0
    continue_cnt = 0
    for i in range(n-m+1):
        if continue_cnt > 0:
            # print('Continue i : {}'.format(i))
            continue_cnt -= 1
            continue
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m and i+k < n-1:
            # print('counted at i : {}, i+k : {}, T[i: i+k] : {}'.format(i, i+k, T[i: i+k]))
            cnt += 1
            continue_cnt = m-1
    return cnt
