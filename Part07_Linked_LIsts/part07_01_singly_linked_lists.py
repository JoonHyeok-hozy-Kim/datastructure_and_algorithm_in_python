from DataStructures.linked_list import LinkedStack

if __name__ == '__main__':
    s = LinkedStack()
    for i in range(5):
        s.push(i)
    for i in range(5):
        print(s.pop())