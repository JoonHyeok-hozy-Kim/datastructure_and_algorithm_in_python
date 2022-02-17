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


def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)
    return A


def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for i in range(n):
        total += S[i]
        A[i] = total/(i+1)
    return A


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
    sample_size = 8000
    S = [3*i+1 for i in range(sample_size)]
    time_list = []
    time_counter(time_list)
    time_counter(time_list, 'quadratic1', prefix_average1(S))
    time_counter(time_list, 'quadratic2', prefix_average2(S))
    time_counter(time_list, 'linear1   ', prefix_average3(S))
    time_counter(time_list)
