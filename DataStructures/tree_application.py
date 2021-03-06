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

    def evaluate(self, dictionary=None):
        return self._evaluate_recur(self.root(), dictionary)

    def _evaluate_recur(self, p, dictionary=None):
        if self.is_leaf(p):
            if isinstance(p.element(), ExpressionTree):
                result = p.element().root().element()
            else:
                result = p.element()
            if result.isnumeric():
                return float(result)
            elif dictionary is not None:
                return dictionary[result]
            error_message = 'Unproper element in the expression : {}'.format(result)
            raise ValueError(error_message)
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p), dictionary)
            right_val = self._evaluate_recur(self.right(p), dictionary)
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

    def postfix_notation(self, p=None, text_list=None):
        if p is None:
            p = self.root()
            text_list = []
        text_list.insert(0, p.element())
        if self.right(p) is not None:
            self.postfix_notation(self.right(p), text_list)
        if self.left(p) is not None:
            self.postfix_notation(self.left(p), text_list)
        return ' '.join(text_list)


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


# Parenthesize Tree Algorithm.
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


# Searching Lowest Common Ancestor(LCA)
from copy import deepcopy
def lowest_common_ancestor(T, position_list):
    """
    Method that searches the Lowest Common Ancestor(LCA)
    :param T: Target tree
    :param position_list: list of positions belong to T. Multiple positions more than three are allowed.
    :return: Position of the LCA
    """
    path_list = _tour_tree_for_lca(T, position_list, T.root(), [], [])
    min_len = len(path_list[0])
    for path in path_list:
        if min_len > len(path):
            min_len = len(path)
    ancestor = None

    for i in range(min_len):
        common_flag = True
        temp = path_list[0][i]
        for path in path_list:
            if temp != path[i]:
                common_flag = False
                break
        if common_flag:
            ancestor = temp
        else:
            break

    return ancestor

def _tour_tree_for_lca(T, position_list, p, path, result_list):
    """
    Hidden touring method for LCA searching.
    """
    if len(position_list) == 0:
        return result_list
    path.append(p)
    for i in range(len(position_list)):
        if position_list[i] == p:
            path_copy = []
            for position in path:
                path_copy.append(position)
            result_list.append(path_copy)
            position_list.pop(i)
        break
    if len(position_list) == 0:
        return result_list
    for c in T.children(p):
        _tour_tree_for_lca(T, position_list, c, path, result_list)
    path.pop()
    return result_list


# Diameter Calculation
from DataStructures.tree import BinaryEulerTour
class Diameter(BinaryEulerTour):
    """
    Inherit _tour mechanism from BinaryEuler Tour.
    Put Tree instance when declaring an instance of Diameter class.
    Run calculate() method to get diameter and the related nodes.
    """
    def __init__(self, tree):
        super().__init__(tree)

    def calculate(self):
        result = self.execute()
        print('{} - {} : {}'.format(result['node1']['position'].element(),
                                    result['node2']['position'].element(),
                                    result['diameter']))
        return result

    def _hook_postvisit(self, p, d, path, results):
        """

        :param p: position
        :param d: deptn
        :param path: not used.
        :param results: _hook_postvisit result of left and right child are saved in the list.
        :return: _partial_diameter() result.
        """
        parent = {
            'position': p,
            'depth': d,
        }
        if self.tree().is_leaf(p):
            return self._partial_diameter(parent, parent, None)
        else:
            return self._comparison(parent, results[0], results[1])

    def _comparison(self, parent, left_diameter, right_diameter):
        """

        :param parent: current node.
        :param left_diameter: _partial_diameter() from left descendants.
        :param right_diameter: _partial_diameter() from right descendants.
        :return: maximum _partial_diameter() result.
        """
        nominees = []
        if left_diameter is not None and right_diameter is not None:
            nominees.append(left_diameter)
            nominees.append(right_diameter)
            nominees.append(self._partial_diameter(parent, left_diameter['node1'], right_diameter['node1']))
            if right_diameter['node2'] is not None:
                nominees.append(self._partial_diameter(parent, left_diameter['node1'], right_diameter['node2']))
            if left_diameter['node2'] is not None:
                nominees.append(self._partial_diameter(parent, left_diameter['node2'], right_diameter['node1']))
                if right_diameter['node2'] is not None:
                    nominees.append(self._partial_diameter(parent, left_diameter['node2'], right_diameter['node2']))
        elif left_diameter is None:
            nominees.append(right_diameter)
            nominees.append(self._partial_diameter(parent, right_diameter['node1'], parent))
            if right_diameter['node2'] is not None:
                nominees.append(self._partial_diameter(parent, right_diameter['node2'], parent))
        else:
            nominees.append(left_diameter)
            nominees.append(self._partial_diameter(parent, left_diameter['node1'], parent))
            if left_diameter['node2'] is not None:
                nominees.append(self._partial_diameter(parent, left_diameter['node2'], parent))
        cursor = nominees[0]
        for nominee in nominees:
            if cursor['diameter'] < nominee['diameter']:
                cursor = nominee
        return cursor

    def _partial_diameter(self, parent, node1, node2):
        """

        :param parent: parent node.
        :param node1: one of the left descendants or the parent node itself if parent is leaf.
        :param node2: one of the right descendants or None if parent is leaf.
        :return: Dictionary with diameter, node1, node2
        """
        if node2 is None:
            diameter = 0
        else:
            diameter = node1['depth'] + node2['depth'] - 2 * parent['depth']
        return {
            'diameter': diameter,
            'node1': node1,
            'node2': node2
        }


# Heap Implementation with LinkedBinaryTree starts.
from DataStructures.tree import LinkedBinaryTree
class LinkedHeapBinaryTree(LinkedBinaryTree):

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

        def __str__(self):
            return '({}, {})'.format(self._key, self._value)

    def __init__(self):
        super().__init__()
        self._last_position = None
        self._max_height = 1

    def last(self):
        return self._last_position

    def _swap(self, p, q):
        if self._last_position == p:
            self._last_position = q
        elif self._last_position == q:
            self._last_position = p
        super()._swap(p, q)

    def _upheap(self, p):
        while p != self.root():
            parent = self.parent(p)
            if p.element() < parent.element():
                self._swap(p, parent)

    def _downheap(self, p):
        if len(self) == 0:
            return
        while not self.is_leaf(p):
            if self.left(p) is not None:
                small_child = self.left(p)
                if self.right(p) is not None:
                    right = self.right(p)
                    if right.element() < small_child.element():
                        small_child = right
                # print('[DOWN] {} - {}'.format(p.element(), small_child.element()))
                if p.element() > small_child.element():
                    self._swap(p, small_child)
                else:
                    return

    def add(self, key, value):
        new_item = self._Item(key, value)
        if self._last_position is None:
            self._last_position = self._add_root(new_item)
        elif self._size == pow(2, self._max_height)-1:
            self._last_position = self._add_drill_left(self.root(), new_item)
            self._max_height += 1
        else:
            self._last_position = self._add_next_last_position(self._last_position, new_item)
        self._upheap(self._last_position)

    def _add_drill_left(self, p, new_item):
        while not self.is_leaf(p):
            p = self.left(p)
        return self._add_left(p, new_item)

    def _add_next_last_position(self, p, new_item):
        parent = self.parent(p)
        if p == self.left(parent):
            if self.is_leaf(p):
                return self._add_right(parent, new_item)
            else:
                right_sibling = self.right(parent)
                return self._add_drill_left(right_sibling, new_item)
        else:
            return self._add_next_last_position(parent, new_item)

    def remove_min(self):
        root_copy = self.root()
        # print('[RM] root : {}'.format(self.root().element()))
        # print('[RM] last : {}'.format(self.last().element()))
        self._swap(self.root(), self.last())
        self._last_position = self._after_remove_last_position(root_copy)
        deleted = self._delete(root_copy)
        self._downheap(self.root())
        return deleted

    def _after_remove_last_position(self, current_last):
        if current_last == self.root():
            return None
        if self._size == pow(2, self._max_height-1):
            self._max_height -= 1
            return self._after_remove_drill_right(self.root())
        parent = self.parent(current_last)
        if current_last == self.right(parent):
            if self.is_leaf(current_last):
                return self.left(parent)
            else:
                left_sibling = self.left(parent)
                return self._after_remove_drill_right(left_sibling)
        else:
            return self._after_remove_last_position(parent)

    def _after_remove_drill_right(self, p):
        while not self.is_leaf(p):
            if self.right(p) is not None:
                p = self.right(p)
            else:
                break
        return p
# Heap Implementation with LinkedBinaryTree ends.


from tree import BinaryTree
class LinkedBinaryTreeSentinel(BinaryTree):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) == type(other) and self._node == other._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._parent == p._node:
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_position(self, node):
        if node == self._sentinel or node is None:
            return None
        return self.Position(self, node)

    def __init__(self):
        self._size = 0
        self._sentinel = self._Node(None, None, None, None)

        # Class members for the explicit iteration logic
        self._preorder_iter = None
        self._preorder_iter_stop = False
        self._preorder_iter_cnt = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._sentinel._left)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    ''' Implemented in BinaryTree class by R-8.10 '''
    ''' Method overriding due to sentinel '''
    def num_children(self, p):
        result = 0
        if self.left(p) is not None:
            result += 1
        if self.right(p) is not None:
            result += 1
        return result

    def _add_root(self, e):
        if self.root() is not None:
            raise ValueError('Root already exists.')
        root = self._Node(e, self._sentinel, self._sentinel, self._sentinel)
        self._sentinel._left = root
        self._size += 1
        return self._make_position(root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left != self._sentinel:
            raise ValueError('Left already exists.')
        node._left = self._Node(e, node, self._sentinel, self._sentinel)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right != self._sentinel:
            raise ValueError('Right already exists.')
        node._right = self._Node(e, node, self._sentinel, self._sentinel)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        self._make_position(node)
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children.')
        child = node._left if node._left != self._sentinel else node._right
        if child != self._sentinel:
            child._parent = node._parent
        if p == self.root():
            self._sentinel._left = child
            child._parent = self._sentinel
        else:
            parent = node._parent
            if node == parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be a leaf.')
        if not (type(self) == type(t1) == type(t2) or (t1 is None and type(self) == type(t2)) or (t2 is None and type(self) == type(t1))):
            raise TypeError('Tree types must match.')
        if t1 is not None:
            self._size += len(t1)
        if t2 is not None:
            self._size += len(t2)
        # print('Attach {} <- {}, {}'.format(node._element, t1._root._element, t2._root._element))
        if t1 is not None and not t1.is_empty():
            for p in t1.postorder():
                p_node = t1._validate(p)
                if p_node._parent == t1._sentinel:
                    p_node._parent = node
                if p_node._left == t1._sentinel:
                    p_node._left = self._sentinel
                if p_node._right == t1._sentinel:
                    p_node._right = self._sentinel
            node._left = t1.root()._node
            t1._size = 0
            self._make_position(node._left)

        if t2 is not None and not t2.is_empty():
            for p in t2.postorder():
                p_node = t2._validate(p)
                if p_node._parent == t2._sentinel:
                    p_node._parent = node
                if p_node._left == t2._sentinel:
                    p_node._left = self._sentinel
                if p_node._right == t2._sentinel:
                    p_node._right = self._sentinel
            node._right = t2.root()._node
            t2._size = 0
            self._make_position(node._right)

    # Choose traversal type
    def positions(self):
        return self.preorder()
        # return self.postorder()
        # return self.breadthfirst()
        # return self.inorder()

    # [C-8.51] Explicit preorder iteration Logic starts.
    def __next__(self):
        if self._preorder_iter_cnt == self._size-1:
            raise StopIteration
        if self._preorder_iter is None:
            self._preorder_iter = self.root()
        else:
            self._next_preorder(self.root())
        self._preorder_iter_stop = False
        return self._preorder_iter

    def _next_preorder(self, p):
        if self._preorder_iter_stop:
            self._preorder_iter = p
            self._preorder_iter_cnt += 1
            return True
        if p == self._preorder_iter:
            self._preorder_iter_stop = True
        if not self.is_leaf(p):
            for c in self.children(p):
                if self._next_preorder(c):
                    return True

    def __iter__(self):
        return self
    # [C-8.51] Explicit preorder iteration Logic ends.

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self, p=None):
        from collections import deque
        dq = deque()
        if p is None:
            p = self.root()
        dq.append(p)
        while len(dq) > 0:
            popped = dq.popleft()
            yield popped
            dq.extend(self.children(popped))

    def level_numbering(self, p):
        idx = 0
        for position in self.breadthfirst():
            if position == p:
                return idx
            idx +=1

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for left_descendent in self._subtree_inorder(self.left(p)):
                yield left_descendent
        yield p
        if self.right(p) is not None:
            for right_descendent in self._subtree_inorder(self.right(p)):
                yield right_descendent

    def fill_tree(self, n):
        from DataStructures.queue import LinkedQueue
        idx = 0
        Q = LinkedQueue()
        Q.enqueue(self._add_root(idx))
        while idx < n-1:
            idx += 1
            dequeued = Q.dequeue()
            Q.enqueue(self._add_left(dequeued, idx))
            if idx >= n-1:
                break
            idx += 1
            Q.enqueue(self._add_right(dequeued, idx))

    def fill_tree_height(self, height):
        if not self.is_empty():
            raise ValueError('Tree is not empty.')
        self.fill_tree(pow(2, height)-1)

    # C-8.38
    def _delete_subtree(self, p):
        self._validate(p)
        for descendant in self._subtree_postorder(p):
            self._delete(descendant)

    # C-8.39
    def _swap(self, p, q):
        p_node = self._validate(p)
        q_node = self._validate(q)

        p_parent_node = self._sentinel if p == self.root() else self._validate(self.parent(p))
        p_left_flag = False
        if p_parent_node._left == p_node:
            p_left_flag = True
        p_l_child_node = self._sentinel
        p_r_child_node = self._sentinel
        if self.left(p) is not None:
            p_l_child_node = self._validate(self.left(p))
        if self.right(p) is not None:
            p_r_child_node = self._validate(self.right(p))

        q_parent_node = self._sentinel if q == self.root() else self._validate(self.parent(q))
        q_left_flag = False
        if q_parent_node._left == q_node:
            q_left_flag = True
        q_l_child_node = self._sentinel
        q_r_child_node = self._sentinel
        if self.left(q) is not None:
            q_l_child_node = self._validate(self.left(q))
        if self.right(q) is not None:
            q_r_child_node = self._validate(self.right(q))

        # Case 1. p is Parent, q is child
        if self.parent(q) == p:
            q_node._parent = p_parent_node
            p_node._parent = q_node
            if p_left_flag:
                p_parent_node._left = q_node
            else:
                p_parent_node._right = q_node

            if p_l_child_node == q_node:
                q_node._left = p_node
                q_node._right = p_r_child_node
                p_r_child_node._parent = q_node
            elif p_r_child_node == q_node:
                q_node._left = p_l_child_node
                q_node._right = p_node
                p_l_child_node._parent = q_node
            else:
                raise ValueError('q is not a child of p')
            p_node._left = q_l_child_node
            p_node._right = q_r_child_node
            q_l_child_node._parent = p_node
            q_r_child_node._parent = p_node

        # Case 2. q is Parent, p is child
        elif self.parent(p) == q:
            p_node._parent = q_parent_node
            q_node._parent = p_node
            if q_left_flag:
                q_parent_node._left = p_node
            else:
                q_parent_node._right = p_node

            if q_l_child_node == p_node:
                p_node._left = q_node
                p_node._right = q_r_child_node
                q_r_child_node._parent = p_node
            elif q_r_child_node == p_node:
                p_node._left = q_l_child_node
                p_node._right = q_node
                q_l_child_node._parent = p_node
            else:
                raise ValueError('p is not a child of q')
            q_node._left = p_l_child_node
            q_node._right = p_r_child_node
            p_l_child_node._parent = q_node
            p_r_child_node._parent = q_node

        # Case 3. Other relations
        else:
            # Parent Shift
            if p_left_flag:
                p_parent_node._left = q_node
            else:
                p_parent_node._right = q_node
            q_node._parent = p_parent_node

            if q_left_flag:
                q_parent_node._left = p_node
            else:
                q_parent_node._right = p_node
            p_node._parent = q_parent_node

            # Left Child Shift
            p_node._left = q_l_child_node
            q_node._left = p_l_child_node
            p_l_child_node._parent = q_node
            q_l_child_node._parent = p_node

            # Right Child Shift
            p_node._right = q_r_child_node
            q_node._right = p_r_child_node
            p_r_child_node._parent = q_node
            q_r_child_node._parent = p_node

        return [self._make_position(p_node), self._make_position(q_node)]

    # Binary string idea from C-9.34 starts
    def last(self):
        from math import log2
        if len(self) == 1:
            return self.root()
        n = len(self)
        max_height = int(log2(n)) + 1
        leaf_cnt = n - pow(2, max_height-1) + 1
        path = self._binary_exp(leaf_cnt-1, max_height-1)
        return self._decode_binary_string_path(path)

    def _binary_exp(self, n, digit):
        result_list = []
        if n == 0:
            result_list.append(str(0))
        else:
            while n > 0:
                result_list.append(str(n % 2))
                n //= 2
        for i in range(digit - len(result_list)):
            result_list.append('0')
        return ''.join(reversed(result_list))

    def _decode_binary_string_path(self, s):
        p = self.root()
        for i in s:
            if i == '0':
                if self.left(p) is None:
                    return None
                p = self.left(p)
            else:
                if self.right(p) is None:
                    return None
                p = self.right(p)
        return p
    # Binary string idea from C-9.34 ends

    def split_subtree(self, p):
        target_node = p._node
        parent_node = self._validate(self.parent(p))
        new_subtree = type(self)()
        new_subtree._size = self._modify_sentinel(p, self._sentinel, new_subtree._sentinel)

        if parent_node._left == target_node:
            parent_node._left = self._sentinel
        else:
            parent_node._right = self._sentinel

        return new_subtree

    def _modify_sentinel(self, p, old_sentinel, new_sentinel, init=True):
        size = 0
        if p._node._left == old_sentinel:
            p._node._left = new_sentinel
            if p._node._right == old_sentinel:
                p._node._right = new_sentinel
                return 1
        elif p._node._right == old_sentinel:
            p._node._right = new_sentinel
        if self.left(p) is not None:
            size += self._modify_sentinel(self.left(p), old_sentinel, new_sentinel, False)
        if self.right(p) is not None:
            size += self._modify_sentinel(self.right(p), old_sentinel, new_sentinel, False)
        if init:
            p._node._parent = new_sentinel
            new_sentinel._left = p._node
        return size + 1