from DataStructures.tree import *


if __name__ == '__main__':

    a = ArrayBasedTree()
    root = a._add_root(0)
    left = a._add_left(root, 1)
    right = a._add_right(root, 2)
    print(a)
    print('Swap : {} <> {}'.format(root.element(), right.element()))
    a.swap(root, right)
    print(a)
    print('Delete : {}'.format(a._delete(left)))
    print(a)
    right = a.right(a.root())
    for i in range(4):
        right = a._add_right(right, i+4)
    print(a)

