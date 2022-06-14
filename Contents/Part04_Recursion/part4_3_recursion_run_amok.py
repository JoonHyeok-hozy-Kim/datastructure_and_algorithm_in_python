def unique3(S, start, stop):
    if stop - start < 1:
        print('pt1: {} / {}'.format(start, stop))
        return True

    elif not unique3(S, start, stop-1):
        print('pt2: {} / {}-1'.format(start, stop))
        return False

    elif not unique3(S, start+1, stop):
        print('pt3: {}+1 / {}'.format(start, stop))
        return False

    else:
        print('pt4: {} / {}'.format(start, stop))
        return S[start] != S[stop-1]


def bad_fibonacci(n):
    if n <= 1:
        return 1
    else:
        return bad_fibonacci(n-1) + bad_fibonacci(n-2)


def efficient_fibonacci(n):
    if n <= 1:
        return (n, 1)
    else:
        (a, b) = efficient_fibonacci(n-1)
        return (a+b, a)

if __name__ == '__main__':
    sample_size = 10
    S = [i for i in range(sample_size)]
    S[-1] = S[-2]

    # print(S)
    # print(unique3(S, 0, 3))

    for i in range(sample_size):
        print(efficient_fibonacci(i))
