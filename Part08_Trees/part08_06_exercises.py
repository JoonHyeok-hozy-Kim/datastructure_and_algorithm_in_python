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


from Part08_Trees.part08_05_expression_tree import ExpressionTree
from DataStructures.queue import LinkedQueue
from copy import deepcopy
def repeated_set(S, result_length):
    result_set = []
    temp_queue = LinkedQueue()
    temp_queue.enqueue([])
    while not temp_queue.is_empty():
        dequeued = temp_queue.dequeue()
        if len(dequeued) == result_length:
            result_set.append(dequeued)
        else:
            for i in S:
                temp = deepcopy(dequeued)
                temp.append(i)
                temp_queue.enqueue(temp)
    return result_set


def permutation(S, num=None, result_list=None, temp_list=None):
    if num is None:
        num = len(S)
    if result_list is None and temp_list is None:
        result_list, temp_list = [], []
    for i in range(len(S)):
        popped = S.pop(i)
        temp_list.append(popped)
        if num == 1:
            temp_copy = deepcopy(temp_list)
            result_list.append(temp_copy)
        else:
            permutation(S, num-1, result_list, temp_list)
        re_popped = temp_list.pop()
        S.insert(i, re_popped)
    return result_list

def make_operator_tree(operator_list, result_list=None, root_tree=None, temp_tree=None, p=None):
    if result_list is None:
        result_list = []
        root_tree = ExpressionTree(operator_list.pop())
        temp_tree = root_tree
        p = temp_tree.root()
    if len(operator_list) == 0:
        root_tree_copy = deepcopy(root_tree)
        result_list.append(root_tree_copy)
        return result_list
    popped = operator_list.pop()
    # add leftward
    left = temp_tree._add_left(p, popped)
    operator_list_copy = deepcopy(operator_list)
    make_operator_tree(operator_list_copy, result_list, root_tree, temp_tree, left)
    temp_tree._delete(left)

    # add rightward
    right = temp_tree._add_right(p, popped)
    operator_list_copy = deepcopy(operator_list)
    make_operator_tree(operator_list_copy, result_list, root_tree, temp_tree, right)
    temp_tree._delete(right)
    return result_list

def add_numbers(T, num_list, root_tree=None, p=None, num_list_copy=None):
    if root_tree is None:
        root_tree = deepcopy(T)
        p = root_tree.root()
        num_list_copy = deepcopy(num_list)
    if len(num_list) == 0:
        return root_tree
    if root_tree.left(p) is not None:
        add_numbers(T, num_list_copy, root_tree, root_tree.left(p), num_list_copy)
    else:
        num_tree = ExpressionTree(str(num_list_copy.pop()))
        root_tree._add_left(p, num_tree)
    if root_tree.right(p) is not None:
        add_numbers(T, num_list_copy, root_tree, root_tree.right(p), num_list_copy)
    else:
        num_tree = ExpressionTree(str(num_list_copy.pop()))
        root_tree._add_right(p, num_tree)
    return root_tree





if __name__ == '__main__':
    # a = LinkedBinaryTree()
    # recursive_add_left(a, 5)

    # lbt = LinkedBinaryTree()
    # lbt.fill_tree(5)
    # print(num_left_leaves(lbt))
    # print(lbt.num_children(lbt.root()))


    num_list = [1, 5, 6, 7]
    operator_set = '+-*/'
    perm_num_list = permutation(num_list)
    repeated_op_set = repeated_set(operator_set, 3)

    cnt = 0
    for op_set in repeated_op_set:
        op_tree_list = make_operator_tree(op_set)
        for op_tree in op_tree_list:
            for num_list in perm_num_list:
                expression = add_numbers(op_tree, num_list)
                value = expression.evaluate()
                cnt += 1
                if value == 21:
                    print('{} = {}'.format(expression, value))
    print(cnt)





