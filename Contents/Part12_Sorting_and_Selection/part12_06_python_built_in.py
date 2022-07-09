

if __name__ == '__main__':
    from random import randint
    a = []
    for i in range(10):
        temp = []
        for j in range(randint(1,5)):
            temp.append(chr(randint(65, 80)))
        a.append(''.join(temp))
    print(a)
    print(sorted(a))
    print(sorted(a, key=len))