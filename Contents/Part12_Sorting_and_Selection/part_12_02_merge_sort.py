



if __name__ == '__main__':

    from SortingAlgorithms.merge_sort import merge_sort
    from random import randint
    n = 10
    S = [randint(0, 100) for i in range(n)]
    print(S)
    merge_sort(S)
    print(S)