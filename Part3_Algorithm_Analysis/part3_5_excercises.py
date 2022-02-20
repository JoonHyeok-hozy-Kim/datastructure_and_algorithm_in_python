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


if __name__ == '__main__':
    from random import randint as ri
    sample_size = 11
    A = [ri(1, 100) for i in range(sample_size)]

    print(c_3_36(A))