from DataStructures.stack import ArrayStack

if __name__ == '__main__':
    # R-6.1
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