from DataStructures.tree import MutableLinkedBinaryTree
from DataStructures.queue import LinkedQueue
from copy import deepcopy

# Custom Tree generator Series
def tree_generator(element_list):
    """
    :param element_list: Possible trees with elements in this list will be created.
    :return: List of possible trees is returned.
    """
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

from DataStructures.tree import EulerTour
class TreeBuilderTour(EulerTour):
    """
        Customized EulerTour for tree_generator() function.
        <How to use>
        (1) Set a tree as a parameter when making an instance of this class.
        (2) Set an element as a parameter when calling execute() method.
            -> List of trees that given element in (2) added to various leaf positions in the tree of (1) will be returned.
    """
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


# Expression Tree Series
from DataStructures.tree import LinkedBinaryTree
class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be a string.')
        self._add_root(token)
        if left is not None:
            if token not in '+-*/':
                raise ValueError('Token must be a valid operator.')
            self._attach(self.root(), left, right)
        # print('----Expression Tree----')
        # for i in self.inorder():
        #     print(i.element())
        # print('-----------------------')

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(')')

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            if isinstance(p.element(), ExpressionTree):
                return float(p.element().root().element())
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            # print('[O] {} {} {}'.format(left_val, op, right_val))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            else:
                if right_val == 0:
                    # print('Zero-division : {} / {}'.format(left_val, right_val))
                    return 0
                return left_val / right_val

def build_expression_trees(tokens):
    S = []
    tokenized = tokenize(tokens)
    for t in tokenized:
        if t in '+-*/':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()

def tokenize(raw):
    result_set = []
    temp_numeric = []
    for c in raw:
        if c.isnumeric():
            temp_numeric.append(c)
        else:
            if len(temp_numeric) > 0:
                result_set.append(''.join(temp_numeric))
                temp_numeric = []
            if c == ' ':
                pass
            else:
                result_set.append(c)
    return result_set


from DataStructures.queue import LinkedQueue
from DataStructures.tree import BinaryLayout
from copy import deepcopy
class ExpressionGenerator:
    def __init__(self, num_list):
        self._num_list = num_list
        self._operator_set = '+-*/'
        self._perm_num_list = self.permutation(self._num_list)
        self._repeated_op_set = self.repeated_set(self._operator_set, len(self._num_list)-1)

    def display_all(self):
        result_set = []
        for op_set in self._repeated_op_set:
            op_tree_list = self.make_operator_tree(op_set)
            for op_tree in op_tree_list:
                for num_list in self._perm_num_list:
                    expression = self.add_numbers(op_tree, num_list)
                    value = expression.evaluate()
                    print('{} = {}'.format(expression, value))
                    result_set.append(expression)

    def find_value(self, value):
        for op_set in self._repeated_op_set:
            op_tree_list = self.make_operator_tree(op_set)
            for op_tree in op_tree_list:
                for num_list in self._perm_num_list:
                    expression = self.add_numbers(op_tree, num_list)
                    expression_value = expression.evaluate()
                    if expression_value == value:
                        print('{} = {}'.format(expression, value))
                        self.display_tree(expression)
                        return expression
        return None


    def make_operator_tree(self, operator_list, result_list=None, root_tree=None, temp_tree=None, p=None):
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
        self.make_operator_tree(operator_list_copy, result_list, root_tree, temp_tree, left)
        temp_tree._delete(left)

        # add rightward
        right = temp_tree._add_right(p, popped)
        operator_list_copy = deepcopy(operator_list)
        self.make_operator_tree(operator_list_copy, result_list, root_tree, temp_tree, right)
        temp_tree._delete(right)
        return result_list

    def add_numbers(self, T, num_list, root_tree=None, p=None, num_list_copy=None):
        if root_tree is None:
            root_tree = deepcopy(T)
            p = root_tree.root()
            num_list_copy = deepcopy(num_list)
        if len(num_list) == 0:
            return root_tree
        if root_tree.left(p) is not None:
            self.add_numbers(T, num_list_copy, root_tree, root_tree.left(p), num_list_copy)
        else:
            num_tree = ExpressionTree(str(num_list_copy.pop()))
            root_tree._add_left(p, num_tree)
        if root_tree.right(p) is not None:
            self.add_numbers(T, num_list_copy, root_tree, root_tree.right(p), num_list_copy)
        else:
            num_tree = ExpressionTree(str(num_list_copy.pop()))
            root_tree._add_right(p, num_tree)
        return root_tree

    def repeated_set(self, S, result_length):
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

    def permutation(self, S, num=None, result_list=None, temp_list=None):
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
                self.permutation(S, num - 1, result_list, temp_list)
            re_popped = temp_list.pop()
            S.insert(i, re_popped)
        return result_list

    def display_tree(self, T):
        layout = BinaryLayout(T)
        layout.execute()


# Parenthesize Tree Algorythm.
def parenthesize(T, p=None):
    if p is None:
        p = T.root()
    text_list = _parenthesize_text(T, p)
    return ''.join(text_list)

def _parenthesize_text(T, p, text_list=None):
    if text_list is None:
        text_list = []
    text_list.append(str(p.element()))
    if T.num_children(p) > 0:
        text_list.append('(')
        for c in T.children(p):
            text_list = _parenthesize_text(T, c, text_list)
            text_list.append(',')
        text_list.pop()
        text_list.append(')')
    return text_list


# Isomorphic Test Series
def isomorphic_test(T1, T2):
    T1_subtrees = generalize_subtrees(T1)
    T2_subtrees = generalize_subtrees(T2)
    if len(T1_subtrees) != len(T2_subtrees):
        return False
    for i in range(len(T1_subtrees)):
        if T1_subtrees[i] != T2_subtrees[i]:
            return False
    return True

def generalize_subtrees(T, p=None, result_list=None):
    if p is None:
        p = T.root()
        result_list = []
    for c in T.children(p):
        generalize_subtrees(T, c, result_list)
    result_list.append(parenthesis_generalize(T, p))
    return result_list

def parenthesis_generalize(T, p, text_list=None):
    if text_list is None:
        text_list = []
    text_list.append('_')
    if T.num_children(p) > 0:
        text_list.append('(')
        if T.left(p) is not None:
            parenthesis_generalize(T, T.left(p), text_list)
        text_list.append(',')
        if T.right(p) is not None:
            parenthesis_generalize(T, T.right(p), text_list)
        text_list.append(')')
    return ''.join(text_list)