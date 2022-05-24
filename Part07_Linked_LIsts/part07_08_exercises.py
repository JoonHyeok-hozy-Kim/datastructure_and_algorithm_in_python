from DataStructures.linked_list import *

def second_to_last(A):
    if len(A) < 2:
        raise ValueError('Length is less than two.')
    walk = A._head
    while walk._next._next is not None:
        walk = walk._next
    return walk._element

from DataStructures.linked_list import LinkedQueue
def concatenate(first_node, second_node):
    new_queue = LinkedQueue()
    new_queue._head = first_node
    new_queue._size += 1
    walk = first_node
    while walk._next is not None:
        walk = walk._next
        new_queue._size += 1
    walk._next = second_node
    new_queue._size += 1
    while walk._next is not None:
        walk = walk._next
        new_queue._size += 1
    new_queue._tail = walk
    return new_queue

def singly_linked_list_count(L, node=None, count=None):
    if node is None:
        node = L._head
        count = 1
    if node._next is None:
        return count
    else:
        return singly_linked_list_count(L, node._next, count+1)

def singly_swap(L, node_x, node_y):
    walk = L._head
    cnt = 0
    prev_x = None
    prev_y = None
    while walk._next is not None and cnt < 2:
        # print('walk : {}'.format(walk._element))
        if walk is L._head:
            if walk is node_x or walk is node_y:
                cnt += 1
        elif walk._next == node_x:
            cnt += 1
            prev_x = walk
        elif walk._next == node_y:
            cnt += 1
            prev_y = walk

        walk = walk._next

    if prev_x is None:
        L._head = node_y
    else:
        prev_x._next = node_y
    if prev_y is None:
        L._head = node_x
    else:
        prev_y._next = node_x

    temp = node_x._next
    node_x._next = node_y._next
    node_y._next = temp

def doubly_swap(node_x, node_y):
    temp_prev = node_x._prev
    temp_next = node_x._next
    # Adjacent Nodes
    node_x._prev._next = node_y
    node_x._next._prev = node_y
    node_y._prev._next = node_x
    node_y._next._prev = node_x

    # Target Nodes
    node_x._prev = node_y._prev
    node_x._next = node_y._next
    node_y._prev = temp_prev
    node_y._next = temp_next



if __name__ == '__main__':
    1
    # 7.1

    # lq = LinkedQueue()
    # for i in range(5):
    #     lq.enqueue(i)
    # # for i in range(5):
    # #     print(lq.dequeue())
    # print(second_to_last(lq))

    # 7.2
    # a = LinkedQueue()
    # b = LinkedQueue()
    # for i in range(3):
    #     a.enqueue(i)
    # for i in range(4):
    #     b.enqueue((i+1)*(-1))
    # c = concatenate(a._head, b._head)
    # for i in range(7):
    #     print(c.dequeue())

    # 7.3
    # a = LinkedQueue()
    # for i in range(11):
    #     a.enqueue(i)
    # # print(singly_linked_list_count(a))
    # node_x = a._head
    # for i in range(4):
    #     node_x = node_x._next
    # node_y = a._head
    # for i in range(7):
    #     node_y = node_y._next
    # print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    # singly_swap(a, node_x, node_y)
    # for i in range(11):
    #     print(a.dequeue())

    # a = LinkedQueue()
    # for i in range(10):
    #     a.enqueue(i)
    # node_x = a._head
    # for i in range(3):
    #     node_x = node_x._next
    # node_y = a._head
    # for i in range(7):
    #     node_y = node_y._next
    # print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    # singly_swap(a, node_x, node_y)
    # for i in range(10):
    #     print(a.dequeue())

    # Test for Doubly
    b = LinkedDeque()
    for i in range(10):
        b.insert_last(i)
    node_x = b._header
    for i in range(3):
        node_x = node_x._next
    node_y = b._trailer
    for i in range(4):
        node_y = node_y._prev
    print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    doubly_swap(node_x, node_y)
    for i in range(10):
        print(b.delete_first())