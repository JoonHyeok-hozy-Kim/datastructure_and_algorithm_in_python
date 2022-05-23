from DataStructures.linked_list import LinkedStack, LinkedQueue, CircularQueue
from DataStructures.linked_list import _DoublyLinkedBase, LinkedDeque

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

    # for i in range(1):
    #     cq.enqueue(i)
    # for i in range(10):
    #     # print(cq.dequeue())
    #     print(cq.first())
    #     cq.rotate()

    # a = _DoublyLinkedBase()
    # a._insert_between(0, a._header, a._trailer)
    # # print(a._header._next._element)
    # # print(a._trailer._prev._element)
    #
    # a._insert_between(1, a._header, a._header._next)
    # # print(a._header._next._element)
    # # print(a._trailer._prev._prev._element)
    # # print(a._trailer._prev._element)
    #
    # a._insert_between(2, a._trailer._prev, a._trailer)
    # # print(a._header._next._next._next._element)
    # # print(a._trailer._prev._element)
    #
    # print(a._delete_node(a._header._next))
    # print(a._header._next._element)
    # print(a._header._next._next._element)
    # print(a._trailer._prev._prev._element)
    # print(a._trailer._prev._element)

    ld = LinkedDeque()
    for i in range(5):
        # ld.insert_first(i)
        ld.insert_last(i)
    for i in range(5):
        print(ld.delete_first())
        # print(ld.delete_last())