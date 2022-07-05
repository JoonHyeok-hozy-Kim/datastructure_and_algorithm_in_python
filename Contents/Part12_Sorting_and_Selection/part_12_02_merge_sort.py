



if __name__ == '__main__':

    # from SortingAlgorithms.merge_sort import merge_sort_array
    # from random import randint
    # n = 10
    # S = [randint(0, 100) for i in range(n)]
    # print(S)
    # merge_sort_array(S)
    # print(S)

    from DataStructures.queue import LinkedQueue
    from SortingAlgorithms.merge_sort import merge_sort_queue
    from random import randint
    n = 10
    S = LinkedQueue()
    for i in range(n):
        S.enqueue(randint(0, 100))
    merge_sort_queue(S)
    while not S.is_empty():
        print(S.dequeue())


