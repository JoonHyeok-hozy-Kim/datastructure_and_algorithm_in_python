def sorted_union(A, B):
    result = [None] * (len(A)+len(B))
    i = j = 0
    eq_cnt = 0
    while i+j < len(A)+len(B):
        if i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result[i+j-eq_cnt] = A[i]
                if A[i] == B[j]:
                    result.pop()
                    j += 1
                    eq_cnt += 1
                i += 1
            else:
                result[i+j-eq_cnt] = B[j]
                j += 1
        elif j == len(B):
            result[i+j-eq_cnt] = A[i]
            i += 1
        else:
            result[i+j-eq_cnt] = B[j]
            j += 1
        # print('i: {}, j: {}, {}'.format(i, j, result))

    return result


if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    b = [3,6,9,12]
    print(sorted_union(a, b))