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

# class ArrayQueue:
#     DEFAULT_CAPACITY = 10
#
#     def __init__(self):
#         self._data = deque()
#         for i in range(ArrayQueue.DEFAULT_CAPACITY):
#             self._data.append(None)
#         self._size = 0
#         self._front = -1
#
#     def __len__(self):
#         return self._size
#
#     def __str__(self):
#         text_list = ['[']
#         if self._size > 0:
#             for i in range(self._size):
#                 text_list.append(str(self._data[(self._front + i) % len(self._data)]))
#                 text_list.append(', ')
#             text_list.pop()
#         text_list.append(']')
#         return ''.join(text_list)
#
#     def is_empty(self):
#         return self._size == 0
#
#     def first(self):
#         if self.is_empty():
#             raise Empty
#         return self._data[self._front]
#
#     def dequeue(self):
#         if self.is_empty():
#             raise Empty
#         if self._size < len(self._data)//4:
#             self._resize(len(self._data)//2)
#         result = self._data[self._front]
#         self._data[self._front] = None
#         self._size -= 1
#         self._front += 1
#         return result
#
#     def enqueue(self, val):
#         if self._size == len(self._data):
#             self._resize(2 * len(self._data))
#         self._data[(self._front + self._size) % len(self._data)] = val
#         self._size += 1
#
#     def _resize(self, cap):
#         temp = [None] * cap
#         for i in range(self._size):
#             temp[i] = self._data[(self._front + i) % len(self._data)]
#         self._data = temp
#         self._front = 0

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


def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j > -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k].split()[0]
        print(tag)
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            elif S.pop() != tag[1:]:
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

def non_recursive_permutation(A):
    from copy import deepcopy
    result_set = []
    S = ArrayStack()
    for i in range(len(A)):
        S.push([A[i]])
    while len(S) > 0:
        temp = S.pop()
        if len(temp) == len(A):
            temp_copy = deepcopy(temp)
            result_set.append(temp_copy)
        for i in A:
            temp_copy = deepcopy(temp)
            if i not in temp:
                temp_copy.append(i)
                S.push(temp_copy)
                # print('{} -> {}'.format(S, result_set))
    return result_set

def non_recursive_subset(A):
    from copy import deepcopy
    S = ArrayStack()
    Q = ArrayQueue()
    Q.enqueue([])
    for i in A:
        while not Q.is_empty():
            S.push(Q.dequeue())
            # print('[Filling S] S {}, Q {}'.format(S, Q))

        while not S.is_empty():
            temp = S.pop()
            temp_copy = deepcopy(temp)
            Q.enqueue(temp)
            temp_copy.append(i)
            Q.enqueue(temp_copy)
            # print('[Filling Q] S {}, Q {}'.format(S, Q))
    return Q


from copy import deepcopy
class PostfixConverter:

    LEFTY_PARENTHESIS = '({['
    RIGHTY_PARENTHESIS = ')}]'
    OPERATORS = '+-*/'

    def __init__(self):
        self._parenthesis_stack = ArrayStack()
        self._temp_expr = [None] * 3
        self._temp_element = None
        self._temp_element_list = []
        self._operator_cnt = 0

    def parse_expression(self, str_expr):
        for c in str_expr:
            # print('TARGET CHAR : {}'.format(c))
            if c == ' ':
                pass

            elif c in PostfixConverter.LEFTY_PARENTHESIS:
                copy_expr = deepcopy(self._temp_expr)
                self._parenthesis_stack.push([c, copy_expr, self._operator_cnt])
                self._temp_expr = [None] * 3
                self._operator_cnt = 0
                # self.debug_temp_expr_num('Open parenthesis')

            elif c in PostfixConverter.RIGHTY_PARENTHESIS:
                parenthesis_pop = self._parenthesis_stack.pop()
                if PostfixConverter.LEFTY_PARENTHESIS.index(parenthesis_pop[0]) != PostfixConverter.RIGHTY_PARENTHESIS.index(c):
                    raise ValueError('Parenthesis mismatch.')

                if self._temp_element is None:
                    self._temp_element = ''.join(self._temp_element_list)
                after_close_expr = self.merge_expression_num(self._temp_expr, self._temp_element)

                self._temp_element = self.clear_expression(after_close_expr)
                self._temp_element_list = []
                self._temp_expr = parenthesis_pop[1]
                self._operator_cnt = parenthesis_pop[2]

                # self.debug_temp_expr_num('Close parenthesis')

            elif c.isnumeric():
                self._temp_element_list.append(c)

            elif c in PostfixConverter.OPERATORS:
                if self._temp_element_list is None:
                    raise ValueError('[parse_expression] operator : temp_num is None : {}'.format(self._temp_expr))

                if self._operator_cnt > 0:
                    # self.debug_temp_expr_num('IF in operation')
                    self._temp_element = ''.join(self._temp_element_list)
                    self._temp_element_list = self.merge_expression_num(self._temp_expr, self._temp_element)
                    self._temp_element = ' '.join(self._temp_element_list)

                self._operator_cnt += 1
                if self._temp_element is None:
                    self._temp_element = ''.join(self._temp_element_list)

                element = deepcopy(self._temp_element)
                self._temp_expr[0] = element
                self._temp_expr[2] = c

                self._temp_element = None
                self._temp_element_list = []
                # self.debug_temp_expr_num('operation_end')

        if len(self._temp_element_list) > 0:
            self._temp_element = ''.join(self._temp_element_list)
        final_expression = self.merge_expression_num(self._temp_expr, self._temp_element)

        if self._operator_cnt > 0:
            raise ValueError('Operator not cleared.')

        return self.clear_expression(final_expression)


    def merge_expression_num(self, expr, element):
        none_cnt =0
        for i in expr:
            if i is None:
                none_cnt += 1
        if none_cnt > 2 or expr[2] is None:
            raise ValueError('[merge_expression_num] expr not qualified : {}'.format(expr))

        copy_expr = deepcopy(expr)
        if copy_expr[0] is None:
            copy_expr[0] = element
        elif copy_expr[1] is None:
            copy_expr[1] = element
        else:
            raise ValueError('[merge_expression_num] temp_num not added to temp_expr')

        self._operator_cnt -= 1
        return copy_expr

    def clear_expression(self, expr):
        for i in expr:
            if i is None:
                raise ValueError('[clear_expr] Expression not qualified : {}'.format(expr))

        result = ' '.join(expr)
        return result

    def debug_temp_expr_num(self, debug_point=None):
        if debug_point is None:
            debug_point = ''
        print('[DEBUG {}] temp_expr : {} / _temp_element : {}'.format(debug_point, self._temp_expr, self._temp_element))

from DataStructures.queue import ArrayQueue
class QueueStack:

    def __init__(self):
        self._queue = ArrayQueue()

    def __len__(self):
        return len(self._queue)

    def push(self, val):
        self._queue.enqueue(val)

    def pop(self):
        for i in range(len(self)-1):
            e = self._queue.dequeue()
            self._queue.enqueue(e)
        return self._queue.dequeue()

    def top(self):
        for i in range(len(self)):
            e = self._queue.dequeue()
            self._queue.enqueue(e)
        return e

from DataStructures.stack import ArrayStack
class StackQueue:
    def __init__(self):
        self._enqueue_stack = ArrayStack()
        self._dequeue_stack = ArrayStack()

    def __len__(self):
        return len(self._enqueue_stack) + len(self._dequeue_stack)

    def enqueue(self, val):
        self._enqueue_stack.push(val)

    def dequeue(self):
        if len(self) == 0:
            raise IndexError
        if len(self._dequeue_stack) == 0:
            self.migration()
        return self._dequeue_stack.pop()

    def migration(self):
        if len(self._dequeue_stack) == 0 and len(self._enqueue_stack) > 0:
            for i in range(len(self._enqueue_stack)):
                self._dequeue_stack.push(self._enqueue_stack.pop())
        else:
            raise ValueError('Migration inapplicable.')

from DataStructures.stack import ArrayStack
class StackDeque:

    def __init__(self):
        self._front_stack = ArrayStack()
        self._back_stack = ArrayStack()

    def __len__(self):
        return len(self._front_stack) + len(self._back_stack)

    def back_to_front(self):
        if len(self._front_stack) > 0:
            raise ValueError('Front is NOT empty.')
        for i in range(len(self._back_stack)):
            self._front_stack.push(self._back_stack.pop())

    def front_to_back(self):
        if len(self._back_stack) > 0:
            raise ValueError('Back is NOT empty.')
        for i in range(len(self._front_stack)):
            self._back_stack.push(self._front_stack.pop())

    def add_first(self, val):
        self._front_stack.push(val)

    def add_last(self, val):
        self._back_stack.push(val)

    def delete_first(self):
        if len(self) == 0:
            raise IndexError('Deque is empty.')
        if len(self._front_stack) == 0:
            self.back_to_front()
        return self._front_stack.pop()

    def delete_last(self):
        if len(self) == 0:
            raise IndexError('Deque is empty.')
        if len(self._back_stack) == 0:
            self.front_to_back()
        return self._back_stack.pop()

    def __str__(self):
        reverser_stack = ArrayStack()
        if len(self._back_stack) > 0:
            for i in range(len(self._back_stack)):
                reverser_stack.push(self._back_stack.pop())
        text_list = ['[']
        len_front = len(self._front_stack)
        if len_front + len(reverser_stack) > 0:
            if len_front > 0:
                for i in range(len_front):
                    text_list.append(str(self._front_stack.pop()))
                    text_list.append(', ')
                for i in range(len_front):
                    self._front_stack.push(text_list[(i+1)*(-2)])
            if len(reverser_stack) > 0:
                for i in range(len(reverser_stack)):
                    e = reverser_stack.pop()
                    text_list.append(str(e))
                    text_list.append(', ')
                    self._back_stack.push(e)
            text_list.pop()
        text_list.append(']')
        return ''.join(text_list)

from DataStructures.queue import ArrayQueue
def StackScanner(S, val):
    Q = ArrayQueue()
    scan_cnt = 0
    found_flag = False
    while len(S) > 0:
        scan_cnt += 1
        popped = S.pop()
        Q.enqueue(popped)
        if val == popped:
            found_flag = True
            break
    for i in range(scan_cnt):
        S.push(Q.dequeue())
    for i in range(scan_cnt):
        Q.enqueue(S.pop())
    for i in range(scan_cnt):
        S.push(Q.dequeue())
    return found_flag







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
    # a = ArrayStack()
    # b = ArrayStack()
    # c = ArrayStack()
    # for i in range(5):
    #     a.push(i)
    # print(a)
    # a.transfer(b)
    # b.transfer(c)
    # c.transfer(a)
    # print(a)

    # C-6.19
    # a = '<table border="3" cellpadding="5"></table>'
    # print(is_matched_html(a))

    # C-6.20
    # a = [i for i in range(3)]
    # # print(len(non_recursive_permutation(a)))
    # # print(non_recursive_permutation(a))
    # print(non_recursive_subset(a))

    # C-6.22
    # expr_list = []
    # expr_list.append('((5+2)*(8-3))/4')
    # expr_list.append('(12+13)-4')
    # expr_list.append('9*(12+13)')
    # expr_list.append('1+2*3')
    # p = PostfixConverter()
    # for expr in expr_list:
    #     print(p.parse_expression(expr))

    # C-6.23
    # def mixer(R, S, T):
    #     print('[Before] R : {}, S : {}, T : {}'.format(R, S, T))
    #     len_s = len(S)
    #     len_t = len(T)
    #     for i in range(len_s):
    #         R.push(S.pop())
    #     for i in range(len_t):
    #         R.push(T.pop())
    #     for i in range(len_s+len_t):
    #         S.push(R.pop())
    #     print('[After] R : {}, S : {}, T : {}'.format(R, S, T))
    #
    # R = ArrayStack()
    # S = ArrayStack()
    # T = ArrayStack()
    # r = [1, 2, 3]
    # s = [4, 5]
    # t = [6, 7, 8, 9]
    #
    # for i in r:
    #     R.push(i)
    # for i in s:
    #     S.push(i)
    # for i in t:
    #     T.push(i)
    #
    # mixer(R, S, T)

    # C-6.24
    # s = QueueStack()
    # for i in range(3):
    #     s.push(i)
    # for i in range(2):
    #     print(s.top())
    # for i in range(3):
    #     print(s.pop())

    # C-6.25
    # sd = StackDeque()
    # print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    # for i in range(5):
    #     sd.add_first(i)
    # print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    # print(sd.delete_first())
    # print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    # print(sd.delete_last())
    # print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    # for i in range(3):
    #     sd.add_first((i+1)*10)
    # print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    # for i in range(2):
    #     sd.add_last((i+1)*(-1))
    # print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    # for i in range(6):
    #     sd.delete_last()
    # print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    # for i in range(2):
    #     sd.delete_first()
    #     print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))

    # C-6.25
    # sq = StackQueue()
    # for i in range(5):
    #     sq.enqueue(i)
    # for i in range(5):
    #     print(sq.dequeue())

    # C-6.27
    # S = ArrayStack()
    # for i in range(10):
    #     S.push(i)
    # print(S)
    # print(StackScanner(S, 3), S)
    # print(StackScanner(S, 9), S)
    # print(StackScanner(S, -1), S)

    # C-6.28
    Q = ArrayQueue(5)
    for i in range(6):
        Q.enqueue(i)
        print(Q)

