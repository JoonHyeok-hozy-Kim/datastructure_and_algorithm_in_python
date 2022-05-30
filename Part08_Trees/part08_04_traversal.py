from DataStructures.tree import LinkedBinaryTree

if __name__ == '__main__':
    a = LinkedBinaryTree()
    a._add_root(1)
    a._add_left(a.root(), 2)
    a._add_right(a.root(), 3)
    a._add_left(a.left(a.root()), 4)
    a._add_right(a.left(a.root()), 5)
    a._add_left(a.right(a.root()), 6)
    a._add_right(a.right(a.root()), 7)

    for i in a.positions():
        print(i.element())
