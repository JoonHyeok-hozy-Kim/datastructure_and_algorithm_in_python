# Quadratic Solution
def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total/(j+1)
    return A

# Quadratic
def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)
    return A

# Linear
def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for i in range(n):
        total += S[i]
        A[i] = total/(i+1)
    return A


##############################################
# Cubic Loop
def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if b == c:
                        return False
    return True


def unique1(S):
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if i==j:
                return False
    return True

def unique2(S):
    sorted_S = sorted(S)
    for i in range(len(sorted_S)-1):
        if S[i] == S[i+1]:
            return False
    return True


def time_counter(time_list, program_name=None, program_result=None):
    from time import time
    if len(time_list) == 0:
        time_list.append([time(), 'initial', None])
    elif program_result is None:
        for i in range(len(time_list)):
            if i > 0:
                print('{} : {} : {}'.format(time_list[i][1],
                                            round(time_list[i][0]-time_list[i-1][0], 2),
                                            time_list[i][2]))
    else:
        time_list.append([time(), program_name, program_result])


if __name__ == '__main__':
    # # Prefix Average
    # sample_size = 8000
    # S = [3*i+1 for i in range(sample_size)]
    # time_list = []
    # time_counter(time_list)
    # time_counter(time_list, 'quadratic1', prefix_average1(S))
    # time_counter(time_list, 'quadratic2', prefix_average2(S))
    # time_counter(time_list, 'linear1   ', prefix_average3(S))
    # time_counter(time_list)

    # # Three-way
    # import random
    # sample_size = 400
    # sample_set = []
    # for i in range(3):
    #     sample_set.append([random.randint(1, 10000000000) for j in range(sample_size)])
    # time_list = []
    # time_counter(time_list)
    # time_counter(time_list, 'cubic_loop1', disjoint1(sample_set[0], sample_set[1], sample_set[2]))
    # time_counter(time_list, 'cubic_loop2', disjoint2(sample_set[0], sample_set[1], sample_set[2]))
    # time_counter(time_list)

    # Uniqueness
    import random

    sample_size = 4000
    sample_set = [random.randint(1, 10000000000) for j in range(sample_size)]
    time_list = []
    time_counter(time_list)
    time_counter(time_list, 'nested_loop', unique1(sample_set))
    time_counter(time_list, 'sorting    ', unique2(sample_set))
    time_counter(time_list)