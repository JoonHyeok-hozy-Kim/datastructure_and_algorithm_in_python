class Tree:
    class Position:

        def element(self):
            raise NotImplementedError('Must be implemented by subclass.')

        def __eq__(self, other):
            raise NotImplementedError('Must be implemented by subclass.')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError('Must be implemented by subclass.')

    def parent(self, p):
        raise NotImplementedError('Must be implemented by subclass.')

    def num_children(self, p):
        raise NotImplementedError('Must be implemented by subclass.')

    def children(self, p):
        raise NotImplementedError('Must be implemented by subclass.')

    def __len__(self):
        raise NotImplementedError('Must be implemented by subclass.')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return self.depth(self.parent(p)) + 1

    def height(self, p=None):
        if p is None:
            p = self.root()
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))


class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    ''' R-8.10 '''
    def num_children(self, p):
        result = 0
        for c in self.children(p):
            result += 1
        return result

    def __str__(self):
        layout = BinaryLayout(self)
        layout.execute()
        return layout.str_graphic()

class LinkedBinaryTree(BinaryTree):
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
        if not type(self) == type(t1) == type(t2):
            raise TypeError('Tree types must match.')
        self._size += len(t1) + len(t2)
        # print('Attach {} <- {}, {}'.format(node._element, t1._root._element, t2._root._element))
        if not t1.is_empty():
            for p in t1.postorder():
                p_node = t1._validate(p)
                if p_node._parent == t1._sentinel:
                    p_node._parent = node
                if p_node._left == t1._sentinel:
                    p_node._left = self._sentinel
                if p_node._right == t1._sentinel:
                    p_node._right = self._sentinel
            node._left = t1._root
            t1._size = 0
            self._make_position(node._left)

        if not t2.is_empty():
            for p in t2.postorder():
                p_node = t2._validate(p)
                if p_node._parent == t2._sentinel:
                    p_node._parent = node
                if p_node._left == t2._sentinel:
                    p_node._left = self._sentinel
                if p_node._right == t2._sentinel:
                    p_node._right = self._sentinel
            node._right = t2._root
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

class EulerTour:

    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self.tree()) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """ Perform tour of subtree rooted at Position p.

        :param p: Position of current node being visited.
        :param d: depth of p in the tree
        :param path: list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class BinaryEulerTour(EulerTour):
    def _tour(self, p, d, path):
        result = [None] * 2
        self._hook_previsit(p, d, path)
        if self.tree().left(p) is not None:
            path.append(0)
            result[0] = self._tour(self.tree().left(p), d+1, path)
        self._hook_invisit(p, d, path)
        if self.tree().right(p) is not None:
            path.append(1)
            result[1] = self._tour(self.tree().right(p), d+1, path)
        answer = self._hook_postvisit(p, d, path, result)
        return answer

    def _hook_invisit(self, p, d, path):
        pass

from copy import deepcopy
class BinaryLayout(BinaryEulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0
        self._x_max = 0
        self._y_max = 0
        self._graphic = [[' ']]

    def execute(self):
        super().execute()
        str_graphic = self.str_graphic()
        # print(str_graphic)
        return str_graphic

    def str_graphic(self):
        text_list = []
        for i in self._graphic:
            text_list.append(''.join(i))
            text_list.append('\n')
        result = ''.join(text_list)
        return result

    def _hook_invisit(self, p, d, path):
        x_increase = len(str(p.element()))
        self.x_max_increase(x_increase)
        self.y_max_increase(d+1)
        for i in range(x_increase):
            self._graphic[d+1][self._x_max-i] = str(p.element())[x_increase-1-i]
        return None

    def x_max_increase(self, n):
        for row in self._graphic:
            for i in range(n):
                row.append(' ')
        self._x_max += n

    def y_max_increase(self, n):
        if n < self._y_max:
            return
        new_row = [' '] * (self._x_max + 1)
        for i in range(n - self._y_max):
            new_row_copy = deepcopy(new_row)
            self._graphic.append(new_row_copy)
        self._y_max = n


class MutableLinkedBinaryTree(LinkedBinaryTree):

    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def delete(self, p):
        return self._delete(p)


class ArrayBasedTree:
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
        return self._data.index(p)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for i in self._data:
            yield i

    def __str__(self):
        layout = BinaryLayout(self)
        layout.execute()
        return layout.str_graphic()

    def is_empty(self):
        return len(self) == 0

    def root(self):
        if self.is_empty():
            raise ValueError('Tree is Empty.')
        return self._data[0]

    def parent(self, p):
        idx = self._validate(p)
        if idx % 2 == 0:
            return self._data[(idx - 2) // 2]
        else:
            return self._data[(idx - 1) // 2]

    def left(self, p):
        idx = self._validate(p)
        if len(self) <= 2 * idx + 1:
            return None
        else:
            return self._data[2 * idx + 1]

    def right(self, p):
        idx = self._validate(p)
        if len(self) <= 2 * idx + 2:
            return None
        else:
            return self._data[2 * idx + 2]

    def is_leaf(self, p):
        idx = self._validate(p)
        return self._data[2 * idx + 1] is None and self._data[2 * idx + 2] is None

    def is_root(self, p):
        return self._validate(p) == 0

    def f(self, p):
        return self._validate(p)

    def _add_root(self, e):
        if not self.is_empty():
            raise ValueError('root already exists.')
        p = self._make_position(e)
        self._data.insert(0, p)
        return p

    def _add_left(self, p, e):
        idx = self._validate(p)
        left_idx = 2*idx+1
        if len(self) >= left_idx+1:
            if self._data[left_idx] is not None:
                raise ValueError('left already exists.')
        while len(self) <= left_idx:
            self._data.append(None)
        p = self._make_position(e)
        self._data[left_idx] = p
        return p

    def _add_right(self, p, e):
        idx = self._validate(p)
        right_idx = 2*idx+2
        if len(self) >= right_idx+1:
            if self._data[right_idx] is not None:
                raise ValueError('right already exists.')
        while len(self) <= right_idx:
            self._data.append(None)
        p = self._make_position(e)
        self._data[right_idx] = p
        return p

    def _delete(self, p):
        idx = self._validate(p)
        deleted = self._data[idx]
        self._data[idx] = None
        return deleted.element()

    def swap(self, p, q):
        p_idx = self._validate(p)
        q_idx = self._validate(q)
        temp = self._data[p_idx]
        self._data[p_idx] = self._data[q_idx]
        self._data[q_idx] = temp

class LinkedTree(Tree):

    class _Node:
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, e, parent=None, children=None):
            self._element = e
            self._parent = parent
            if children is None:
                children = []
            self._children = children

        def num_children(self):
            return len(self._children)

        def first_child(self):
            if self.num_children() == 0:
                return None
            else:
                return self._children[0]

        def last_child(self):
            if self.num_children() == 0:
                return None
            else:
                return self._children[-1]

    class Position(Tree.Position):

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
        return self.Position(self, node)

    def __init__(self):
        self._size = 0
        self._root = None

    def __len__(self):
        return self._size

    def __str__(self):
        layout = GeneralTreeLayout(self)
        return layout.execute()

    def is_empty(self):
        return len(self) == 0

    def root(self):
        return self._make_position(self._root)

    def num_children(self, p):
        node = self._validate(p)
        return node.num_children()

    def parent(self, p):
        return self._make_position(self._validate(p)._parent)

    def children(self, p):
        node = self._validate(p)
        if node.num_children() > 0:
            for child_node in node._children:
                yield self._make_position(child_node)

    def first_child(self, p):
        node = self._validate(p)
        return self._make_position(node.first_child())

    def last_child(self, p):
        node = self._validate(p)
        return self._make_position(node.last_child())

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('root already exists.')
        self._root = self._Node(e)
        self._size += 1
        return self._make_position(self._root)

    def _add_child(self, p, e, i=None):
        parent_node = self._validate(p)
        child_node = self._Node(e, parent_node)
        if i is None:
            parent_node._children.append(child_node)
        else:
            parent_node._children.insert(i, child_node)
        self._size += 1
        return self._make_position(child_node)

    def _delete(self, p):
        if not self.is_leaf(p):
            raise ValueError('p is not leaf')
        node = self._validate(p)
        for i in range(len(node._parent._children)):
            if node._parent._children[i] == node:
                popped = node._parent._children.pop(i)
                self._size -= 1
                return popped._element

    def preorder(self):
        return self._preorder_subtree(self.root())

    def _preorder_subtree(self, p):
        yield p
        for other in self.children(p):
            yield other


class GeneralEulerTour(EulerTour):
    def _tour(self, p, d, path):
        num_child = self.tree().num_children(p)
        result = [None] * num_child
        self._hook_previsit(p, d, path)

        if num_child == 0:
            # When no child
            self._hook_invisit(p, d, path)
        else:
            # When have children
            child_idx = 0
            mid = (self.tree().num_children(p)-1)// 2
            for child in self.tree().children(p):
                path.append(child_idx)
                result[child_idx] = self._tour(child, d+1, path)

                if child_idx == mid:
                    self._hook_invisit(p, d, path)

                child_idx += 1

        answer = self._hook_postvisit(p, d, path, result)
        return answer

    def _hook_invisit(self, p, d, path):
        pass


class GeneralTreeLayout(GeneralEulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0
        self._x_max = 0
        self._y_max = 0
        self._graphic = [[' ']]

    def execute(self):
        super().execute()
        str_graphic = self.str_graphic()
        # print(str_graphic)
        return str_graphic

    def str_graphic(self):
        text_list = []
        for i in self._graphic:
            text_list.append(''.join(i))
            text_list.append('\n')
        result = ''.join(text_list)
        return result

    def _hook_invisit(self, p, d, path):
        self.y_max_increase(d+1)

        # Parenthesis Open if first_child
        parent = self.tree().parent(p) if p != self.tree().root() else None
        if parent is not None and p == self.tree().first_child(parent):
            # Open Parenthesis
            self.x_max_increase(1)
            self._graphic[d+1][self._x_max] = '('

        x_increase = len(str(p.element()))
        self.x_max_increase(x_increase)
        for i in range(x_increase):
            self._graphic[d+1][self._x_max-i] = str(p.element())[x_increase-1-i]

        if parent is not None and p == self.tree().last_child(parent):
            # Close Parenthesis
            self.x_max_increase(2)
            self._graphic[d+1][self._x_max-1] = ')'
            self._graphic[d+1][self._x_max] = ' '
        else:
            # Space added
            self.x_max_increase(1)
            self._graphic[d+1][self._x_max] = ' '
        return None


    def x_max_increase(self, n):
        for row in self._graphic:
            for i in range(n):
                row.append(' ')
        self._x_max += n

    def y_max_increase(self, n):
        if n < self._y_max:
            return
        new_row = [' '] * (self._x_max + 1)
        for i in range(n - self._y_max):
            new_row_copy = deepcopy(new_row)
            self._graphic.append(new_row_copy)
        self._y_max = n
