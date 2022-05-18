from DataStructures.stack import ArrayStack
from DataStructures.queue import ArrayQueue
from DataStructures.deque import ArrayDeque

def stack_reverse(A):
    S = ArrayStack()
    result = []
    for i in A:
        S.push(i)
    for i in range(len(S)):
        result.append(S.pop())
    return result

def recursive_match(expr, stack=None):
    lefty = '({['
    righty = ')}]'
    print('{} - {}'.format(expr, stack))
    if stack is None:
        stack = ArrayStack()
    if len(expr) == 0:
        return True

    if expr[0] in righty:
        if stack.is_empty() or righty.index(expr[0]) != lefty.index(stack.pop()):
            return False
        else:
            return recursive_match(expr[1:], stack)
    else:
        if expr[0] in lefty:
            stack.push(expr[0])
        return recursive_match(expr[1:], stack)


from collections import deque
from DataStructures.stack import Empty

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = deque()
        for i in range(ArrayQueue.DEFAULT_CAPACITY):
            self._data.append(None)
        self._size = 0
        self._front = -1

    def __len__(self):
        return self._size

    def __str__(self):
        text_list = ['[']
        if self._size > 0:
            for i in range(self._size):
                text_list.append(str(self._data[(self._front + i) % len(self._data)]))
                text_list.append(', ')
            text_list.pop()
        text_list.append(']')
        return ''.join(text_list)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        result = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front += 1
        return result

    def enqueue(self, val):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._front + self._size) % len(self._data)] = val
        self._size += 1

    def _resize(self, cap):
        temp = [None] * cap
        for i in range(self._size):
            temp[i] = self._data[(self._front + i) % len(self._data)]
        self._data = temp
        self._front = 0

def probably_largest(S):
    x = S.pop()
    if x < S[-1]:
        x = S.pop()
    return x

def permutation(A, num= None, result_set=None, temp_set=None):
    from copy import deepcopy
    if num is None:
        num = len(A)
    if result_set is None:
        result_set = []
    if temp_set is None:
        temp_set = []
    for i in range(len(A)):
        popped = A.pop(i)
        temp_set.append(popped)
        if num == 1:
            temp_copy = deepcopy(temp_set)
            result_set.append(temp_copy)
            # print(result_set)
        else:
            permutation(A, num-1, result_set, temp_set)
        re_popped = temp_set.pop(-1)
        A.insert(i, re_popped)
    return result_set



if __name__ == '__main__':
    1
    # R-6.1
    # S = ArrayStack()
    # S.push(5)
    # S.push(3)
    # S.pop()
    # S.push(2)
    # S.push(8)
    # S.pop()
    # S.pop()
    # S.push(9)
    # S.push(1)
    # S.pop()
    # S.push(7)
    # S.push(6)
    # S.pop()
    # S.pop()
    # S.push(4)
    # S.pop()
    # S.pop()
    # print(S)

    # R-6.3
    # S = ArrayStack()
    # T = ArrayStack()
    # for i in range(3):
    #     S.push(i+1)
    #     T.push((i+1)*(-1))
    # print(S, T)
    # S.transfer(T)
    # print(S, T)
    #
    # # R-6.4
    # T.recursive_truncate()
    # print(T)

    # R-6.5
    # a = [i for i in range(10)]
    # print(a)
    # print(stack_reverse(a))

    # R-6.6
    # a = '(5+3*{12+1})+1-3]'
    # print(recursive_match(a))

    # R-6.7
    # q = ArrayQueue()
    # q.enqueue(5)
    # q.enqueue(3)
    # q.dequeue()
    # q.enqueue(2)
    # q.enqueue(8)
    # q.dequeue()
    # q.dequeue()
    # q.enqueue(9)
    # q.enqueue(1)
    # q.dequeue()
    # q.enqueue(7)
    # q.enqueue(6)
    # q.dequeue()
    # q.dequeue()
    # q.enqueue(4)
    # q.dequeue()
    # q.dequeue()
    # print(q)

    # a = ArrayQueue()
    # for i in range(3):
    #     a.enqueue(i)
    #     print(a)
    # for i in range(3):
    #     a.dequeue()
    #     print(a)

    # R-6.12
    # d = ArrayDeque()
    # d.add_first(4)
    # d.add_last(8)
    # d.add_last(9)
    # d.add_first(5)
    # # d.back()
    # d.delete_first()
    # d.delete_last()
    # d.add_last(7)
    # d.first()
    # d.last()
    # d.add_last(6)
    # d.delete_first()
    # d.delete_first()
    # print(d)

    # R-6.13
    # d = ArrayDeque()
    # q = ArrayQueue()
    # for i in range(8):
    #     d.add_last(i+1)
    # print('D {} - Q {}'.format(d, q))
    # for i in range(4):
    #     q.enqueue(d.delete_first())
    # print('D {} - Q {}'.format(d, q))
    # for i in range(3):
    #     d.add_last(q.dequeue())
    # print('D {} - Q {}'.format(d, q))
    # q.enqueue(d.delete_first())
    # print('D {} - Q {}'.format(d, q))
    # d.add_first(q.dequeue())
    # print('D {} - Q {}'.format(d, q))
    # for i in range(4):
    #     q.enqueue(d.delete_first())
    # print('D {} - Q {}'.format(d, q))
    # for i in range(5):
    #     d.add_last(q.dequeue())
    # print('D {} - Q {}'.format(d, q))

    # R-6.14
    # d = ArrayDeque()
    # s = ArrayStack()
    # for i in range(8):
    #     d.add_last(i+1)
    # print('D {} - S {}'.format(d, s))
    # for i in range(4):
    #     s.push(d.delete_first())
    # print('D {} - S {}'.format(d, s))
    # d.add_last(s.pop())
    # s.push(d.delete_first())
    # s.push(d.delete_last())
    # print('D {} - S {}'.format(d, s))
    # for i in range(5):
    #     d.add_first(s.pop())
    # print('D {} - S {}'.format(d, s))

    # C-6.15
    # a = [i for i in range(3)]
    # permutaion_set = permutation(a)
    # right_count = 0
    # for i in permutaion_set:
    #     x = probably_largest(i)
    #     if x == max(a):
    #         right_count += 1
    # print('Probability : {}/{}'.format(right_count, len(permutaion_set)))

    # C-6.16, C-6.17
    # s = ArrayStack(3)
    # for i in range(3):
    #     s.push(i)
    #     print(s)
    # for i in range(4):
    #     s.pop()
    #     print(s)

    # C-6.18
    a = ArrayStack()
    b = ArrayStack()
    c = ArrayStack()
    for i in range(5):
        a.push(i)
    print(a)
    a.transfer(b)
    b.transfer(c)
    c.transfer(a)
    print(a)