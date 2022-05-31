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
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

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
        self._root = self._Node(e)
        self._size += 1
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left already exists.')
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right already exists.')
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children.')
        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent
        if node == self._root:
            self._root = child
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
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    # Choose traversal type
    def positions(self):
        # return self.preorder()
        # return self.postorder()
        # return self.breadfast()
        return self.inorder()

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

    def breadfast(self, p=None):
        from DataStructures.queue import LinkedQueue
        if p is None:
            p = self.root()
        q = LinkedQueue()
        q.enqueue(p)
        while not q.is_empty():
            dequeued = q.dequeue()
            yield dequeued
            for c in self.children(dequeued):
                q.enqueue(c)

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
        answer = self._hook_postvisit(p, d, result)
        return answer

    def _hook_invisit(self, p, d, path):
        pass


class BinaryLayout(BinaryEulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1