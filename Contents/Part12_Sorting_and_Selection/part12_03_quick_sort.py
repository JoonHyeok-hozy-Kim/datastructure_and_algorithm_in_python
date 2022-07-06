

if __name__ == '__main__':
    from DataStructures.queue import LinkedQueue
    from SortingAlgorithms.quick_sort import quick_sort
    from random import randint
    a = LinkedQueue()
    for i in range(10):
        a.enqueue(randint(0, 1000))
    quick_sort(a)
    while not a.is_empty():
        print(a.dequeue())
