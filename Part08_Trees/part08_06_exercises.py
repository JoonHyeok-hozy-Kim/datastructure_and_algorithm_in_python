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


class LevelNumberCalculator(EulerTour):

    def f(self, p):
        return self._tour(self.tree().root(), p)

    def _tour(self, current_p, target_p, level_num=None):
        if level_num is None:
            level_num = 0
        if current_p == target_p:
            return level_num
        if self.tree().left(current_p) is not None:
            left_val = self._tour(self.tree().left(current_p), target_p, 2*level_num+1)
            if left_val is not None:
                return left_val
        if self.tree().right(current_p) is not None:
            right_val = self._tour(self.tree().right(current_p), target_p, 2*level_num+2)
            if right_val is not None:
                return right_val

class ArrayTree:

    class Position:
        def __init__(self, container, element):
            self._container = container
            self._element = element

        def element(self):
            return self._element

    def _make_position(self, element):
        return self.Position(self, element)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p.element() is None:
            raise ValueError('p is no longer valid.')
        return p.element()

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def root(self):
        if self.is_empty():
            raise ValueError('Tree is Empty.')
        return self._data[0]

    def parent(self, p):
        idx = self._data.index(p)
        if i % 2 == 0:
            return self._data[(idx-2)//2]
        else:
            return self._data[(idx-1)//2]

    def left(self, p):
        idx = self._data.index(p)
        if len(self) < 2*idx+1:
            return None
        else:
            return self._data[2*idx+1]

    def right(self, p):
        idx = self._data.index(p)
        if len(self) < 2*idx+2:
            return None
        else:
            return self._data[2*idx+2]

    def is_leaf(self, p):
        idx = self._data.index(p)
        return self._data[2*idx+1] is None and self._data[2*idx+2] is None

    def is_root(self, p):
        return self._data.index(p) == 0

    def f(self, p):
        return self._data.index(p)

    def g(self, p):
        return self._data.index(p) + 1

from DataStructures.tree import MutableLinkedBinaryTree
from DataStructures.queue import LinkedQueue
from copy import deepcopy
def tree_generator(element_list):
    result_list = []
    q = LinkedQueue()
    num_elements = len(element_list)
    initial_tree = MutableLinkedBinaryTree()
    initial_tree.add_root(element_list.pop(0))
    q.enqueue(initial_tree)

    while len(element_list) > 0:
        popped = element_list.pop(0)
        current_len = len(q)
        for i in range(current_len):
            dequeued = q.dequeue()
            tree_builder = TreeBuilderTour(dequeued)
            tree_list = tree_builder.execute(popped)
            for tree in tree_list:
                q.enqueue(tree)

    while not q.is_empty():
        dequeued = q.dequeue()
        if len(dequeued) == num_elements:
            result_list.append(dequeued)

    return result_list

class TreeBuilderTour(EulerTour):
    def execute(self, e):
        result_list = []
        self._tour(self.tree().root(), e, result_list)
        return result_list

    def _tour(self, p, e, result_list):
        self._hook_previsit(p, e, result_list)
        if self.tree().left(p) is not None:
            self._tour(self.tree().left(p), e, result_list)
        if self.tree().right(p) is not None:
            self._tour(self.tree().right(p), e, result_list)

    def _hook_previsit(self, p, e, result_list):
        if self.tree().right(p) is None:
            # Add left if left and right are None
            if self.tree().left(p) is None:
                new_left = self.tree()._add_left(p, e)
                tree_copy = deepcopy(self.tree())
                result_list.append(tree_copy)
                self.tree()._delete(new_left)

            # Add right if right is None
            new_right = self.tree()._add_right(p, e)
            tree_copy = deepcopy(self.tree())
            result_list.append(tree_copy)
            self.tree()._delete(new_right)

def preorder_inorder_comparison(T, pre_target, in_target, p=None, pre_result=None, in_result=None):
    if p is None:
        p = T.root()
        pre_result = []
        in_result = []
    pre_result.append(p.element())
    if T.left(p) is not None:
        preorder_inorder_comparison(T, pre_target, in_target, T.left(p), pre_result, in_result)
    in_result.append(p.element())
    if T.right(p) is not None:
        preorder_inorder_comparison(T, pre_target, in_target, T.right(p), pre_result, in_result)

    if pre_target == ''.join(pre_result):
        if in_target == ''.join(in_result):
            return T



if __name__ == '__main__':
    a = LinkedBinaryTree()
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

    # from DataStructures.tree import MutableLinkedBinaryTree
    # a = MutableLinkedBinaryTree()
    # a.add_root(1)
    # print(a)
    # left = a.add_left(a.root(), 2)
    # print(a)
    # right = a.add_right(a.root(), 3)
    # print(a)
    # a.add_right(left, 4)
    # print(a)
    # a.add_left(right, 5)
    # print(a)

    # from DataStructures.tree import MutableLinkedBinaryTree
    # a = MutableLinkedBinaryTree()
    # for i in range(7):
    #     if i == 0:
    #         node = a.add_root(i)
    #     else:
    #         node = a.add_right(node, i)
    # b = LevelNumberCalculator(a)
    # print(b.tree())
    # b_root = b.tree().root()
    # print(b.f(b_root))
    # b_root_right = b.tree().right(b_root)
    # print(b.f(b_root_right))

    str_list = list('EXAMFUN')
    tree_list = tree_generator(str_list)
    for tree in tree_list:
        result = preorder_inorder_comparison(tree, 'EXAMFUN', 'MAFXUEN')
        if result is not None:
            print(tree)












