def sum(S, idx=None):
    if idx is None:
        idx = len(S)-1
    if idx == 0:
        return S[0]
    else:
        return sum(S, idx-1) + S[idx]

def reverse(S, start=None, stop=None):
    if start is None and stop is None:
        start, stop = 0, len(S)-1
    if start < stop:
        S[start], S[stop] = S[stop], S[start]
        return reverse(S, start+1, stop-1)
    return S


def power(a, n):
    if n == 0:
        return 1
    else:
        return power(a, n-1) * a


def faster_power(a, n):
    if n == 0:
        return 1
    else:
        partial = faster_power(a, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= a
        return result


if __name__ == '__main__':
    sample_size = 10
    S = [i for i in range(sample_size)]

    # print(S)
    # print(reverse(S))

    from time import time
    import sys
    sys.setrecursionlimit(100000000)
    t1 = time()
    print(power(3, 999))
    t2 = time()
    print(faster_power(3, 999))
    t3 = time()
    print('{} vs {}'.format(round(t2-t1, 6),
                            round(t3-t2, 6)))