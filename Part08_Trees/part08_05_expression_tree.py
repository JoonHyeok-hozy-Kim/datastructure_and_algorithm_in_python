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
    for t in tokens:
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


from DataStructures.queue import LinkedQueue
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


if __name__ == '__main__':
    # exp = '((1+3)*(2-7))'
    # exp_tree = build_expression_trees(exp)
    # print(exp_tree.evaluate())

    num = [1, 5, 6, 7]
    a = ExpressionGenerator(num)
    # a.display_all()
    a.find_value(21)