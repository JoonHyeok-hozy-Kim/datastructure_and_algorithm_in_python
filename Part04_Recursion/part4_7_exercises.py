# R-4.1
def max_sequence(S, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(S)-1
    if start == end:
        return S[start]
    elif start == end-1:
        return max(S[start], S[end])
    else:
        mid = (start+end)//2
        return max(max_sequence(S, start, mid),
                   max_sequence(S, mid+1, end))


def harmonic_number(n):
    if n == 1:
        return 1
    else:
        return harmonic_number(n-1) + 1/n


def string_converter(number):
    if number < 1000:
        return str(int(number))
    else:
        return string_converter(number/1000) + ',' + str(int(number%1000))


def min_max(S, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(S)-1

    if start == end:
        return (S[start], S[end])
    elif start == end-1:
        if S[start] > S[end]:
            return (S[start], S[end])
        else:
            return (S[end], S[start])
    else:
        mid = (start+end)//2
        part_one = min_max(S, start, mid)
        part_two = min_max(S, mid+1, end)
        maximum = part_one[0] if part_one[0] > part_two[0] else part_two[0]
        minimum = part_one[1] if part_one[1] < part_two[1] else part_two[1]
        return (maximum, minimum)


def log_base_two_int(n):
    if n == 1:
        return 0
    else:
        return log_base_two_int(n//2) + 1


def element_uniqueness(S, start=None, target=None):
    if start is None and target is None:
        start = 0
        target = start
    if start == len(S):
        return True
    else:
        if target == len(S):
            return element_uniqueness(S, start+1, start+1)
        else:
            if S[start] == S[target] and start != target:
                return False
            return element_uniqueness(S, start, target+1)


def recursive_product(m, n):
    if m == 0 or n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return recursive_product(m, n-1) + m



if __name__ == '__main__':
    import random
    sample_size = 10
    S = [i for i in range(sample_size)]
    random_S = [random.randint(1,100) for i in range(sample_size)]

    # print('{} : {}'.format(max_sequence(random_S), random_S))

    # for i in range(1, 10):
    #     print(harmonic_number(i))

    # print(string_converter(12345678))

    # print('{} : {}'.format(min_max(random_S),
    #                        random_S))

    # for i in range(65):
    #     print(log_base_two_int(i+1))

    # S.append(6)
    # print(element_uniqueness(S))

    print(recursive_product(10, 6))