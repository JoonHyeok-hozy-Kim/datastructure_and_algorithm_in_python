from DataStructures.stack import ArrayStack

def stack_reverse(A):
    S = ArrayStack()
    result = []
    for i in A:
        S.push(i)
    for i in range(len(S)):
        result.append(S.pop())
    return result

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
    a = [i for i in range(10)]
    print(a)
    print(stack_reverse(a))