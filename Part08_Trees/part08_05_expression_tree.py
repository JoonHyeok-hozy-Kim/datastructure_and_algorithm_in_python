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

if __name__ == '__main__':
    exp = '((1+3)*(2-7))'
    exp_tree = build_expression_trees(exp)
    print(exp_tree.evaluate())