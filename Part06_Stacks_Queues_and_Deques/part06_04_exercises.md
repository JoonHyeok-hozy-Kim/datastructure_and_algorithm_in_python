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

### 

<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part06_Stacks_Queues_and_Deques/part06_stacks_queues_and_deques.md">Part 6. Stacks, Queues, and Deques</a>
</p>