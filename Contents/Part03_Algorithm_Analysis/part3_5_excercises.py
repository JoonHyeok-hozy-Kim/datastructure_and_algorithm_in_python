def c_3_35(A):
    n = len(A)
    sorted_A = sorted(A)
    print(sorted_A)
    for i in range(n-2):
        if sorted_A[i] == sorted_A[i+1]:
            if sorted_A[i+1] == sorted_A[i+2]:
                return False
    return True


def c_3_36(A):
    n = len(A)
    if n <= 10:
        return A
    else:
        sorted_A = sorted(A)
        return sorted_A[-11:-1]


def c_3_41(A):
    n = len(A)
    min, max = A[0], A[0]
    comparison_count = 0
    max_candidates = []
    min_candidates = []
    for i in range(n//2):
        comparison_count += 1
        if A[i*2] >= A[i*2-1]:
            comparison_count += 1
            if A[i*2] > max:
                max = A[i*2]
            comparison_count += 1
            if A[i*2-1] < min:
                min = A[i*2-1]
        else:
            comparison_count += 1
            if A[i*2-1] > max:
                max = A[i*2-1]
            comparison_count += 1
            if A[i*2] < min:
                min = A[i*2]

    return [min, max, comparison_count]


def c_3_45(S):
    n = len(S)
    sum = n*(n+1)/2
    for i in S:
        sum -= i
    return int(sum)


def Fibonacci(n):
    if n < 1:
        return None
    elif n == 1:
        return [1, 1]
    elif n == 2:
        return [2, 1]
    else:
        return [Fibonacci(n-1)[0] + Fibonacci(n-2)[0], Fibonacci(n-1)[1] + Fibonacci(n-2)[1] + 1]


def c_3_54(S):
    n = len(S)
    sorted_S = sorted(S)
    target = [S[0], 1]
    temp = [None] * 2
    for i in range(n-1):
        if sorted_S[i+1] == target[0]:
            target[1] += 1
        else:
            if temp[0] == sorted_S[i+1]:
                temp[1] += 1
                if temp[1] > target[1]:
                    target = temp
            else:
                temp = [sorted_S[i+1], 1]

    return target[0]

if __name__ == '__main__':
    from random import randint, uniform, shuffle
    sample_size = 10
    test_case = 1000
    test_result = []
    # for i in range(test_case):
    #     A = [round(randint(0, 10000000)) for i in range(sample_size)]
    #     print(c_3_41(A))

    # S = [i for i in range(sample_size)]
    # S.pop(randint(0,sample_size))
    # print('{} : {}'.format(S, c_3_45(S)))

    S = [randint(0, sample_size*4) for i in range(sample_size)]
    print(c_3_54(S))