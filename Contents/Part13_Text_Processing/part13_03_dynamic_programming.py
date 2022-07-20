def matrix_chain(d):
    """
    :param d: a list of n+1 numbers such that size of kth matrix is d[k]-by-d[k+1].
    :return: n-by-n table such that N[i][j] represents the minimum number of multiplications needed to compute the product of Ai through Aj inclusive.
    """
    n = len(d)-1
    N = [[0]*n for i in range(n)]

    for b in range(n):
        for i in range(n-b):
            j = i+b
            if i != j:
                N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i, j))
    return N


def print_matrix(N):
    for row in N:
        for e in row:
            print(e, end=' ')
        print()


if __name__ == '__main__':

    # d = [3, 5, 6, 2, 20, 30, 50]
    # m = matrix_chain(d)
    # print_matrix(m)


    from TextProcessingAlgorithms.longest_common_sequence import LCS
    X = "GTTCCTAATA"
    Y = "CGATAATTGAGA"

    L = LCS(X, Y)
    for row in L:
        for e in row:
            print("{}".format(e), end=" ")
        print()


