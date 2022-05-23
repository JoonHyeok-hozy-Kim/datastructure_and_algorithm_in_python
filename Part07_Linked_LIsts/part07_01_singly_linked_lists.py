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
    for i in range(5):
        cq.enqueue(i)
    for i in range(5):
        print(cq.dequeue())