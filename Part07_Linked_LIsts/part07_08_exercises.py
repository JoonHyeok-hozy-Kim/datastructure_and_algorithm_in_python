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

def middle_finder(L):
    front = L._header
    back = L._trailer
    while True:
        front = front._next
        back = back._prev
        if front is back:
            break
        elif front._next is back:
            break
    return front._element

def concatenate_doubly(L, M):
    L._size += M._size
    # Link Middle
    L._trailer._prev._next = M._header._next
    M._header._next._prev = L._trailer._prev
    L._trailer = M._trailer

def max(L):
    walk = L._header._next
    result = walk._element
    while walk._next is not None:
        if result < walk._element:
            result = walk._element
        walk = walk._next
    return result

def add_last(L, e):
    if L.is_empty:
        L.add_first(e)
    else:
        last = L.last()
        L.add_after(last, e)

def add_before(L, p, e):
    if p == L.first():
        L.add_first(e)
    else:
        walk = L.first()
        while walk._next is not None:
            if walk._next == p:
                L.add_after(walk, e)
                return




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
    # b = LinkedDeque()
    # for i in range(10):
    #     b.insert_last(i)
    # node_x = b._header
    # for i in range(3):
    #     node_x = node_x._next
    # node_y = b._trailer
    # for i in range(4):
    #     node_y = node_y._prev
    # print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    # doubly_swap(node_x, node_y)
    # for i in range(10):
    #     print(b.delete_first())


    # b = LinkedDeque()
    # for i in range(9):
    #     b.insert_last(i)
    # print(middle_finder(b))
    # for i in range(len(b)):
    #     print(b.delete_first())

    # a = LinkedDeque()
    # for i in range(5):
    #     a.insert_last(i+1)
    # b = LinkedDeque()
    # for i in range(5):
    #     b.insert_last((i+1)*(-1))
    # concatenate_doubly(a, b)
    # # for i in range(10):
    # #     print(a.delete_first())
    #
    # print(max(a))

    # a = PositionalList()
    from random import randint
    # for i in range(5):
    #     # a.add_last(randint(0, 100))
    #     a.add_last(i)
    # print(a)
    # # print(max(a))
    # # print(a.max())
    # # print(a.find(0), a.find(0).element())
    # # print(a.find(10))
    # #
    # # print(a.recursive_find(0), a.recursive_find(0).element())
    # # print(a.recursive_find(10))
    #
    # # for i in a.__reversed__():
    # #     print(i)
    # for i in range(5):
    #     a.move_to_front(a.last())
    #     print(a)

    # fl = FavoriteListMTF()
    # fl.access('a')
    # fl.access('b')
    # fl.access('c')
    # fl.access('d')
    # fl.access('e')
    # fl.access('f')
    # fl.access('a')
    # fl.access('b')
    # fl.access('c')
    # fl.access('d')
    # fl.access('e')
    # for i in fl.top(6):
    #     print(i)

    # fl = FavoriteListMTF()
    # sample_size = 5
    # for i in range(sample_size):
    #     fl.access(i)
    # text_list = ['Original :']
    # for i in fl.top(sample_size):
    #     text_list.append(str(i))
    # print(' '.join(text_list))
    # for i in range(sample_size):
    #     fl.access(sample_size-i-1)
    # text_list = ['Reversed :']
    # for i in fl.top(sample_size):
    #     text_list.append(str(i))
    # print(' '.join(text_list))

    # f = FavoriteList()
    # for i in range(5):
    #     f.access(i)
    # first = f._data.first()
    # for i in range(4):
    #     print(first.element()._count)
    #     first = f._data.after(first)
    # f.reset_counts()
    # first = f._data.first()
    # for i in range(4):
    #     print(first.element()._count)
    #     first = f._data.after(first)

    from DataStructures.stack import LinkedStack as new_linked_stack
    # a = new_linked_stack()
    # for i in range(5):
    #     a.push(i)
    # print(a.top())
    # for i in range(6):
    #     print(a.pop())

    from DataStructures.queue import LinkedQueue as new_linked_queue
    # a = new_linked_queue()
    # for i in range(5):
    #     a.enqueue(i+1)
    # for i in range(5):
    #     print(a.dequeue())
    # print('=========================')
    # for i in range(5):
    #     a.enqueue(i+1)
    # # reversed(a)
    # a.nonrecursive_reverse()
    # for i in range(5):
    #     print(a.dequeue())

    from DataStructures.stack import LinkedStack as new_linked_stack
    from DataStructures.stack import LeakyLinkedStack as new_leaky_linked_stack
    # lls = new_leaky_linked_stack(5)
    # for i in range(7):
    #     lls.push(i)
    # for i in range(5):
    #     print(lls.pop())
    # print(lls.pop())

    fl = ForwardList()
    for i in range(5):
        fl.add_first((i+1)*(-1))
        # print(fl.first().element())
    for i in range(5):
        fl.add_last(i)
        # print(fl.last().element())
    fl.add_after(fl.last(), 999)
    print(fl.last().element())
    fl.add_before(fl.first(), 6666)
    print(fl.first().element())
    fl.add_before(fl.after(fl.first()), -777)
    print(fl.after(fl.first()).element())
    print(fl.delete(fl.first()))
    print(fl.first().element())
    print(fl.last().element())
    print(fl.delete(fl.last()))
    print(fl.last().element())