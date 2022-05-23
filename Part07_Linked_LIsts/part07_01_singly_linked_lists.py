from DataStructures.linked_list import LinkedStack, LinkedQueue, CircularQueue

if __name__ == '__main__':
    # s = LinkedStack()
    # for i in range(5):
    #     s.push(i)
    # for i in range(5):
    #     print(s.pop())

    # q = LinkedQueue()
    # for i in range(5):
    #     q.enqueue(i)
    # for i in range(5):
    #     print(q.dequeue())
    #     print(q.first())

    cq = CircularQueue()
    # cq.enqueue(1)
    # print(cq.first())
    # print(cq.dequeue())
    # # print(cq.first())
    # cq.enqueue(3)
    # print(cq.first())
    # print(cq.dequeue())

    for i in range(1):
        cq.enqueue(i)
    for i in range(10):
        # print(cq.dequeue())
        print(cq.first())
        cq.rotate()