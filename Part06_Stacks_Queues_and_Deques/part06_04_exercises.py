from DataStructures.stack import ArrayStack

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



if __name__ == '__main__':
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
    a = '(5+3*{12+1})+1-3]'
    print(recursive_match(a))