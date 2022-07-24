def prefix_suffix_compare(X):
    prefix = []
    walk = len(X)-1
    while walk > 0:
        temp_text = []
        for i in range(len(X)-walk):
            if X[i] != X[walk+i]:
                break
            else:
                temp_text.append(X[i])
            if i == len(X)-walk-1:
                prefix.append(''.join(temp_text))
        walk -= 1
    return prefix

def efficient_matrix_product_order(d):
    n = len(d)-1
    N = []
    for i in range(n):
        temp = [[0,''] for i in range(n)]
        N.append(temp)

    for b in range(n):
        for i in range(n-b):
            j = i+b
            if i != j:
                min_val = None
                for k in range(i, j):
                    if min_val is None:
                        min_val = N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1]
                        temp_path = [N[i][k][1], N[k+1][j][1], '({}, {}, {})'.format(i, k + 1, j + 1)]
                    else:
                        if N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1] < min_val:
                            min_val = N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1]
                            temp_path = [N[i][k][1], N[k+1][j][1], '({}, {}, {})'.format(i, k + 1, j + 1)]

                N[i][j][0] = min_val
                N[i][j][1] = ''.join(temp_path)
    return N


def LCS(X, Y):
    n, m = len(X), len(Y)
    L = [[0] * (m+1) for k in range(n+1)]
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j+1][k+1] = 1 + L[j][k]
            else:
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L


def LCS_solution(X, Y):
    solution = []
    j, k = len(X), len(Y)
    L = LCS(X, Y)
    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))

def LCS_solution_ver2(X, Y):
    solution = []
    j, k = len(X), len(Y)
    L = LCS(X, Y)
    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] > L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))

def LCS_solution_ver3(X, Y):
    solution = []
    j, k = len(X), len(Y)
    L = LCS(X, Y)
    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] <= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))

from TextProcessingAlgorithms.knuth_morris_pratt import _compute_kmp_fail
def longest_prefix_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return None
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    cnt = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                k += 1
                cnt = max(cnt, k)
                break
            # print('k : {}, cnt : {}, P[k] : {}'.format(k, cnt, P[k]))
            j += 1
            k += 1
            cnt = max(cnt, k)
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1

    return P[:cnt]


from TextProcessingAlgorithms.knuth_morris_pratt import _compute_kmp_fail
def circular_substring_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return None
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n+m:
        if T[j%n] == P[k]:
            print('{}'.format(P[k]))
            if k == m-1:
                print(j)
                return T[j-m+1:j+1] if j < n else T[j-m+1:] + T[0:j%n+1]
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return None


def find_boyer_moore_x_kmp(T, P):
    """ Return the lowest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    if m == 0:
        return -1
    fail = _compute_kmp_fail_backward(P)

    i = m-1
    k = m-1
    check_start = -1
    while i < n:
        if T[i] == P[k]:
            check_start = i if check_start < i else check_start
            if k == 0:
                return i
            i -= 1
            k -= 1
        elif k < m-1:
            k = fail[k+1]
        else:
            if check_start > 0:
                i = check_start + 1
                check_start = -1
            else:
                i += 1

    return -1


def _compute_kmp_fail_backward(P):
    m = len(P)
    fail = [m-1] * m
    k = m-1
    j = m-2
    while j >= 0:
        if P[j] == P[k]:
            fail[j] = k-1
            j -= 1
            k -= 1
        elif k < m-1:
            k = fail[k+1]
        else:
            j -= 1
    return fail




def efficient_matrix_product_order_text(d):
    n = len(d)-1
    N = []
    for i in range(n):
        temp = [[0,[]] for i in range(n)]
        N.append(temp)

    for b in range(n):
        for i in range(n-b):
            j = i+b
            if i != j:
                min_val = None
                for k in range(i, j):
                    if min_val is None:
                        min_val = N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1]
                        temp_path = []
                        temp_path.extend(N[i][k][1])
                        temp_path.extend(N[k+1][j][1])
                        temp_path.append([i, k+1, j+1])
                    else:
                        if N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1] < min_val:
                            min_val = N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1]
                            temp_path = []
                            temp_path.extend(N[i][k][1])
                            temp_path.extend(N[k+1][j][1])
                            temp_path.append([i, k+1, j+1])

                N[i][j][0] = min_val
                N[i][j][1] = temp_path

    array_format = N[0][-1][1]
    for arr in array_format:
        print(arr)

    return N[0][-1][1]

if __name__ == '__main__':
    pass
    # # x = "aaabbaaa"
    # # print(prefix_suffix_compare(x))
    # #
    # # y = "cgtacgttcgtacg"
    # # print(prefix_suffix_compare(y))
    #
    # # p = "the quick brown fox jumped over a lazy cat"
    # # last = {}
    # # for i in range(len(p)):
    # #     last[p[i]] = i
    # # for c in last:
    # #     print('{} : {}'.format(c, last[c]))
    #
    # # from TextProcessingAlgorithms.knuth_morris_pratt import _compute_kmp_fail
    # # p = "cgtacgttcgtac"
    # # a = _compute_kmp_fail(p)
    # # print(a)
    #
    # d = [10, 5, 2, 20, 12,4, 60]
    # N = efficient_matrix_product_order(d)
    # for row in N:
    #     for e in row:
    #         print('{}'.format(e), end=' ')
    #     print()

    # x = "GTTCCTAATA"
    # y = "CAGATAATTGAG"
    # print(LCS_solution(x,y))
    # print(LCS_solution_ver2(x,y))

    # x = "skullandbones"
    # y = "lullabybabies"
    # print(LCS_solution(x, y))
    # print(LCS_solution_ver2(x, y))

    # from TextProcessingAlgorithms.huffman import huffman_with_frequency_array
    # a = "dogs do not spot hot pots or cats"
    # result = huffman_with_frequency_array(a)
    # for e in result['frequency_array']:
    #     print('{} : {}'.format(e, result['frequency_array'][e]))
    # print(result['tree'])

    # from TextProcessingAlgorithms.boyer_moore import rfind_boyer_moore
    # t = "aaaabceeeee"
    # p = "abc"
    # print(rfind_boyer_moore(t, p))
    #
    # from TextProcessingAlgorithms.knuth_morris_pratt import rfind_kmp
    # print(rfind_kmp(t, p))

    # t = "abababaabaaaabacc"
    # p = "ab"
    #
    # from TextProcessingAlgorithms.brute_force import count_brute
    # print(count_brute(t, p))
    #
    # from TextProcessingAlgorithms.boyer_moore import count_boyer_moore
    # print(count_boyer_moore(t, p))
    #
    # from TextProcessingAlgorithms.knuth_morris_pratt import count_kmp
    # print(count_kmp(t, p))

    # t = "asdfasfqwertysfdasdqwertyufa"
    # p = "qwertyu"
    # print(longest_prefix_kmp(t, p))

    # t = "abcdefasdfasfdawexxxx"
    # p = "exxxxabc"
    # print(circular_substring_kmp(t, p))


    # from TextProcessingAlgorithms.boyer_moore import find_boyer_moore, _compute_kmp_fail_backward
    # from TextProcessingAlgorithms.knuth_morris_pratt import find_kmp, _compute_kmp_fail
    # from time import time
    #
    # a = "amalgamation"
    # print(_compute_kmp_fail(a))


    d = [10, 5, 2, 20, 12,4, 60]
    N = efficient_matrix_product_order_text(d)
