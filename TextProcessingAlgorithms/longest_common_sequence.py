

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


def LCS_solution_wrong(X, Y):
    """
    Wrong Algorithm
    Try the following example compairing with the correct one.
    X = ['G', 'C', 'G', 'A', 'T', 'G', 'T', 'T', 'C', 'A']
    Y = ['C', 'T', 'A', 'T', 'A', 'A', 'G', 'A', 'T', 'G']
    """
    n, m = len(X), len(Y)
    D = []
    i, j = 0, 0
    while i < n and j < m:
        for k in range(j, m):
            if X[i] == Y[k]:
                D.append(X[i])
                j = k+1
                break
        i += 1
    return ''.join(D)