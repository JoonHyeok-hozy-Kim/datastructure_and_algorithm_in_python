<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part06_Stacks_Queues_and_Deques/part06_stacks_queues_and_deques.md">Part 6. Stacks, Queues, and Deques</a>
</p>

### R-6.1 R-6.1 What values are returned during the following series of stack operations, if executed upon an initially empty stack? push(5), push(3), pop(), push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(), pop(), push(4), pop(), pop().
```python
S = ArrayStack()
S.push(5)
S.push(3)
S.pop()
S.push(2)
S.push(8)
S.pop()
S.pop()
S.push(9)
S.push(1)
S.pop()
S.push(7)
S.push(6)
S.pop()
S.pop()
S.push(4)
S.pop()
S.pop()
print(S)
```

### R-6.2 Suppose an initially empty stack S has executed a total of 25 push operations, 12 top operations, and 10 pop operations, 3 of which raised Empty errors that were caught and ignored. What is the current size of S?
* Sol) 25-(10-3) = 18

### R-6.3 Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that the element that starts at the top of S is the first to be inserted onto T, and the element at the bottom of S ends up at the top of T.
```python
def transfer(self, other):
    if type(self) != type(other):
        raise TypeError
    for i in range(len(self)):
        other.push(self.pop())
```

### R-6.4 Give a recursive method for removing all the elements from a stack.
```python
def recursive_truncate(self):
    if len(self) == 0:
        return
    self.pop()
    return self.recursive_truncate()
```

### R-6.5 Implement a function that reverses a list of elements by pushing them onto a stack in one order, and writing them back to the list in reversed order.
```python
def stack_reverse(A):
    S = ArrayStack()
    result = []
    for i in A:
        S.push(i)
    for i in range(len(S)):
        result.append(S.pop())
    return result
```

### R-6.6 Give a precise and complete definition of the concept of matching for grouping symbols in an arithmetic expression. Your definition may be recursive.
```python
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
```

### R-6.7 What values are returned during the following sequence of queue operations, if executed on an initially empty queue?
* enqueue(5), enqueue(3), dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9), enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(), enqueue(4), dequeue(), dequeue().
```python
q = ArrayQueue()
q.enqueue(5)
q.enqueue(3)
q.dequeue()
q.enqueue(2)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.enqueue(9)
q.enqueue(1)
q.dequeue()
q.enqueue(7)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.enqueue(4)
q.dequeue()
q.dequeue()
print(q)
```

### R-6.8 Suppose an initially empty queue Q has executed a total of 32 enqueue operations, 10 first operations, and 15 dequeue operations, 5 of which raised Empty errors that were caught and ignored. What is the current size of Q?
* Sol.) 32-(15-5) = 22

### R-6.9 Had the queue of the previous problem been an instance of ArrayQueue that used an initial array of capacity 30, and had its size never been greater than 30, what would be the final value of the front instance variable?
* Sol.) self._front = 10

### R-6.10 Consider what happens if the loop in the ArrayQueue. resize method at lines 53–55 of Code Fragment 6.7 had been implemented as:
```python
for k in range(self. size):
    self. data[k] = old[k]
```
### Give a clear explanation of what could go wrong.
* Sol.) Existing elements in the previous self._data may remain and distort the data.

### R-6.11 Give a simple adapter that implements our queue ADT while using a collections.deque instance for storage.
```python
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
```

### R-6.12 What values are returned during the following sequence of deque ADT operations, on initially empty deque? 
* add first(4), add last(8), add last(9), add first(5), back( ), delete first( ), delete last( ), add last(7), first( ), last( ), add last(6), delete first( ), delete first( ).
```python
d = ArrayDeque()
d.add_first(4)
d.add_last(8)
d.add_last(9)
d.add_first(5)
# d.back() # ???
d.delete_first()
d.delete_last()
d.add_last(7)
d.first()
d.last()
d.add_last(6)
d.delete_first()
d.delete_first()
print(d)
```

### R-6.13 Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8), in this order. Suppose further that you have an initially empty queue Q. Give a code fragment that uses only D and Q (and no other variables) and results in D storing the elements in the order (1,2,3,5,4,6,7,8).
```python
d = ArrayDeque()
q = ArrayQueue()
for i in range(8):
    d.add_last(i+1)
print('D {} - Q {}'.format(d, q))
for i in range(4):
    q.enqueue(d.delete_first())
print('D {} - Q {}'.format(d, q))
for i in range(3):
    d.add_last(q.dequeue())
print('D {} - Q {}'.format(d, q))
q.enqueue(d.delete_first())
print('D {} - Q {}'.format(d, q))
d.add_first(q.dequeue())
print('D {} - Q {}'.format(d, q))
for i in range(4):
    q.enqueue(d.delete_first())
print('D {} - Q {}'.format(d, q))
for i in range(5):
    d.add_last(q.dequeue())
print('D {} - Q {}'.format(d, q))
```

### R-6.14 Repeat the previous problem using the deque D and an initially empty stack S.
```python
d = ArrayDeque()
s = ArrayStack()
for i in range(8):
    d.add_last(i+1)
print('D {} - S {}'.format(d, s))
for i in range(4):
    s.push(d.delete_first())
print('D {} - S {}'.format(d, s))
d.add_last(s.pop())
s.push(d.delete_first())
s.push(d.delete_last())
print('D {} - S {}'.format(d, s))
for i in range(5):
    d.add_first(s.pop())
print('D {} - S {}'.format(d, s))
```

### C-6.15 Suppose Alice has picked three distinct integers and placed them into a stack S in random order. Write a short, straight-line piece of pseudo-code (with no loops or recursion) that uses only one comparison and only one variable x, yet that results in variable x storing the largest of Alice’s three integers with probability 2/3. Argue why your method is correct.
```python
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
    a = [i for i in range(3)]
    permutaion_set = permutation(a)
    right_count = 0
    for i in permutaion_set:
        x = probably_largest(i)
        if x == max(a):
            right_count += 1
    print('Probability : {}/{}'.format(right_count, len(permutaion_set)))
```

### C-6.16 Modify the ArrayStack implementation so that the stack’s capacity is limited to maxlen elements, where maxlen is an optional parameter to the constructor (that defaults to None). If push is called when the stack is at full capacity, throw a Full exception (defined similarly to Empty).
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/stack.py">Modified ArrayStack</a>
</p>

```python
if __name__ == '__main__':
    s = ArrayStack(3)
    for i in range(4):
        s.push(i)
```

### C-6.17 In the previous exercise, we assume that the underlying list is initially empty. Redo that exercise, this time preallocating an underlying list with length equal to the stack’s maximum capacity.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/stack.py">Modified ArrayStack</a>
</p>

### C-6.18 Show how to use the transfer function, described in Exercise R-6.3, and two temporary stacks, to replace the contents of a given stack S with those same elements, but in reversed order.
```python
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
```

### C-6.19 In Code Fragment 6.5 we assume that opening tags in HTML have form \<name>, as with \<li>. More generally, HTML allows optional attributes to be expressed as part of an opening tag. The general form used is \<name attribute1="value1" attribute2="value2">; for example, a table can be given a border and additional padding by using an opening tag of \<table border="3" cellpadding="5">. Modify Code Fragment 6.5 so that it can properly match tags, even when an opening tag may include one or more such attributes.
```python
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
```

### C-6.20 Describe a nonrecursive algorithm for enumerating all permutations of the numbers {1,2,...,n} using an explicit stack.
```python
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

if __name__ == '__main__':
    a = [i for i in range(5)]
    print(len(non_recursive_permutation(a)))
    print(non_recursive_permutation(a))
```

### C-6.21 Show how to use a stack S and a queue Q to generate all possible subsets of an n-element set T nonrecursively.
```python
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
```

### C-6.22 Postfix notation is an unambiguous way of writing an arithmetic expression without parentheses. It is defined so that if “(exp1)op(exp2)” is a normal, fully parenthesized expression whose operation is op, the postfix version of this is “pexp1 pexp2 op”, where pexp1 is the postfix version of exp1 and pexp2 is the postfix version of exp2. The postfix version of a single number or variable is just that number or variable. For example, the postfix version of “((5+2) ∗ (8−3))/4” is “5 2 + 8 3 − ∗ 4 /”. Describe a nonrecursive way of evaluating an expression in postfix notation.
```python
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

if __name__ == '__main__':
    expr_list = []
    expr_list.append('((5+2)*(8-3))/4')
    expr_list.append('(12+13)-4')
    expr_list.append('9*(12+13)')
    expr_list.append('1+2*3')
    p = PostfixConverter()
    for expr in expr_list:
        print(p.parse_expression(expr))
```

### C-6.23 Suppose you have three nonempty stacks R, S, and T. Describe a sequence of operations that results in S storing all elements originally in T below all of S’s original elements, with both sets of those elements in their original order. The final configuration for R should be the same as its original configuration. For example, if R = [1,2,3], S = [4,5], and T = [6,7,8,9], the final configuration should have R = [1,2,3] and S = [6,7,8,9,4,5].
```python
def mixer(R, S, T):
    print('[Before] R : {}, S : {}, T : {}'.format(R, S, T))
    len_s = len(S)
    len_t = len(T)
    for i in range(len_s):
        R.push(S.pop())
    for i in range(len_t):
        R.push(T.pop())
    for i in range(len_s+len_t):
        S.push(R.pop())
    print('[After] R : {}, S : {}, T : {}'.format(R, S, T))

R = ArrayStack()
S = ArrayStack()
T = ArrayStack()
r = [1, 2, 3]
s = [4, 5]
t = [6, 7, 8, 9]

for i in r:
    R.push(i)
for i in s:
    S.push(i)
for i in t:
    T.push(i)
    
mixer(R, S, T)
```

### C-6.24 Describe how to implement the stack ADT using a single queue as an instance variable, and only constant additional local memory within the method bodies. What is the running time of the push(), pop(), and top() methods for your design?
* Sol.) 
  * push : O(1)
  * pop : O(n)
  * top : O(n)
```python
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

if __name__ == '__main__':
    s = QueueStack()
    for i in range(3):
        s.push(i)
    for i in range(2):
        print(s.top())
    for i in range(3):
        print(s.pop())
```

### C-6.25 Describe how to implement the queue ADT using two stacks as instance variables, such that all queue operations execute in amortized O(1) time. Give a formal proof of the amortized bound.
```python
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

if __name__ == '__main__':
    sq = StackQueue()
    for i in range(5):
        sq.enqueue(i)
    for i in range(5):
        print(sq.dequeue())
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part06_Stacks_Queues_and_Deques/images/06_04_25.png" style="height: 150px;"></img><br/>
</p>

### C-6.26 Describe how to implement the double-ended queue ADT using two stacks as instance variables. What are the running times of the methods?
```python
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

if __name__ == '__main__':
    sd = StackDeque()
    print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    for i in range(5):
        sd.add_first(i)
    print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    print(sd.delete_first())
    print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    print(sd.delete_last())
    print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    for i in range(3):
        sd.add_first((i+1)*10)
    print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    for i in range(2):
        sd.add_last((i+1)*(-1))
    print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    for i in range(6):
        sd.delete_last()
    print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
    for i in range(2):
        sd.delete_first()
        print('{} | {}-{}'.format(sd, sd._front_stack, sd._back_stack))
```

### C-6.27 Suppose you have a stack S containing n elements and a queue Q that is initially empty. Describe how you can use Q to scan S to see if it contains a certain element x, with the additional constraint that your algorithm must return the elements back to S in their original order. You may only use S, Q, and a constant number of other variables.
```python
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
    S = ArrayStack()
    for i in range(10):
        S.push(i)
    print(S)
    print(StackScanner(S, 3), S)
    print(StackScanner(S, 9), S)
    print(StackScanner(S, -1), S)
```

### C-6.28 Modify the ArrayQueue implementation so that the queue’s capacity is limited to maxlen elements, where maxlen is an optional parameter to the constructor (that defaults to None). If enqueue is called when the queue is at full capacity, throw a Full exception (defined similarly to Empty).
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/queue.py">Modified Queue</a>
</p>

```python
Q = ArrayQueue(5)
for i in range(6):
    Q.enqueue(i)
    print(Q)
```



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part06_Stacks_Queues_and_Deques/part06_stacks_queues_and_deques.md">Part 6. Stacks, Queues, and Deques</a>
</p>