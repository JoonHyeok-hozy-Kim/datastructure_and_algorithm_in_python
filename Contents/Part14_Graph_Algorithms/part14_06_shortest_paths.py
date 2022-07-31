



if __name__ == '__main__':

    from DataStructures.priority_queues import LocationAwareUnsortedPriorityQueue
    from random import randint
    pq = LocationAwareUnsortedPriorityQueue()
    for i in range(5):
        n = randint(1, 100)
        pq.add(n, n)
        print("{} added.".format(n))
        print("min : {}".format(pq.min()))