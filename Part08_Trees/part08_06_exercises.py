from DataStructures.tree import *
def recursive_add_left(T, idx, p=None):
    if p is None:
        root = T._add_root(idx)
        return recursive_add_left(T, idx-1, root)
    if idx == 0:
        return
    left = T._add_left(p, idx)
    return recursive_add_left(T, idx-1, left)

def num_left_leaves(T, p=None):
    if p is None:
        p = T.root()
    if T.is_leaf(p):
        parent = T.parent(p)
        if p == T.left(parent):
            return 1
        else:
            return 0
    result = 0
    for c in T.children(p):
        result += num_left_leaves(T, c)
    return result

if __name__ == '__main__':
    # a = LinkedBinaryTree()
    # recursive_add_left(a, 5)

    # lbt = LinkedBinaryTree()
    # lbt.fill_tree(5)
    # print(num_left_leaves(lbt))
    # print(lbt.num_children(lbt.root()))

    # from Part08_Trees.part08_05_expression_tree import ExpressionGenerator
    # num = [1, 5, 6, 7]
    # a = ExpressionGenerator(num)
    # # a.display_all()
    # a.find_value(21)


    # from Part08_Trees.part08_05_expression_tree import ExpressionTree, build_expression_trees
    # from DataStructures.tree import BinaryLayout
    # exp_str = '(((5+2)*(2-1))/((2+9)+((7-2)-1))*8)'
    # a = build_expression_trees(exp_str)
    # b = BinaryLayout(a)
    # print(exp_str, '=', a.evaluate())
    # print(b.execute())

    from DataStructures.tree import MutableLinkedBinaryTree
    a = MutableLinkedBinaryTree()
    a.add_root(1)
    print(a)
    left = a.add_left(a.root(), 2)
    print(a)
    right = a.add_right(a.root(), 3)
    print(a)
    a.add_right(left, 4)
    print(a)
    a.add_left(right, 5)
    print(a)











