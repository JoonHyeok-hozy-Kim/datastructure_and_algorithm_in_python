from DataStructures.binary_search_trees import TreeMap


class AVLBalanceTreeMap(TreeMap):
    """ AVL Tree with Balance Factor Instead of Height """

    class _Node(TreeMap._Node):
        __slots__ = '_balance'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance = 0

    def height(self, p):
        if p is None:
            return 0
        if self.is_leaf(p):
            return 1
        return 1 + max(self.height(self.left(p)), self.height(self.right(p)))

    def _recompute_height(self, p):
        node = self._validate(p)
        node._height = 1 + max(node.left_height(), node.right_height())

    def _recompute_balance(self, p):
        node = self._validate(p)
        node._balance = self.height(self.left(p)) - self.height(self.right(p))

    def _is_balanced(self, p):
        node = self._validate(p)
        return abs(node._balance) <= 1

    def _tall_child(self, p, favor_left=False):
        node = self._validate(p)
        if node._balance > 0:
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            self._recompute_balance(p)
            if not self._is_balanced(p):
                p = self._restructure(self._tall_grandchild(p))
            p = self.parent(p)

    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)


class TreeMapBeforeAfter(TreeMap):
    """ TreeMap with _prev and _next : O(1) running time for before(p) and after(p) """

    class _Node(TreeMap._Node):
        __slots__ = '_prev', '_next'

        def __init__(self, element, parent=None, left=None, right=None, prev=None, next=None):
            super().__init__(element, parent, left, right)
            self._prev = prev
            self._next = next

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def _subtree_search(self, p, k):
        greatest_min = None
        smallest_max = None
        while p is not None:
            if k == p.key():
                return (p, greatest_min, smallest_max)
            elif k < p.key():
                if smallest_max is None or smallest_max._element._key > p.key():
                    smallest_max = p._node

                if self.left(p) is not None:
                    p = self.left(p)
                else:
                    return (p, greatest_min, smallest_max)
            else:
                if greatest_min is None or greatest_min._element._key < p.key():
                    greatest_min = p._node

                if self.right(p) is not None:
                    p = self.right(p)
                else:
                    return (p, greatest_min, smallest_max)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError('Key Error : ', repr(k))
        else:
            p, prev, next = self._subtree_search(self.root(), k)
            node = self._validate(p)
            node._prev = prev
            node._next = next

            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error : ', repr(k))
            return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p, prev, next = self._subtree_search(self.root(), k)
            if k == p.key():
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)

                leaf._node._prev = prev
                if prev is not None:
                    prev._next = leaf._node
                leaf._node._next = next
                if next is not None:
                    next._prev = leaf._node
        self._rebalance_insert(leaf)

    def __delitem__(self, k):
        if not self.is_empty():
            p, prev, next = self._subtree_search(self.root(), k)
            if p.key() == k:
                if prev is not None:
                    prev._next = p._node._next
                if next is not None:
                    next._prev = p._node._prev
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError('Key Error : ', repr(k))


class AVLBalanceTreeMapBeforeAfter(TreeMapBeforeAfter):
    """ AVLTree inheriting TreeMapBeforeAfter """

    class _Node(TreeMapBeforeAfter._Node):
        __slots__ = '_balance'

        def __init__(self, element, parent=None, left=None, right=None, prev=None, next=None):
            super().__init__(element, parent, left, right, prev, next)
            self._balance = 0

    def height(self, p):
        if p is None:
            return 0
        if self.is_leaf(p):
            return 1
        return 1 + max(self.height(self.left(p)), self.height(self.right(p)))

    def _recompute_height(self, p):
        node = self._validate(p)
        node._height = 1 + max(node.left_height(), node.right_height())

    def _recompute_balance(self, p):
        node = self._validate(p)
        node._balance = self.height(self.left(p)) - self.height(self.right(p))

    def _is_balanced(self, p):
        node = self._validate(p)
        return abs(node._balance) <= 1

    def _tall_child(self, p, favor_left=False):
        node = self._validate(p)
        if node._balance > 0:
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            self._recompute_balance(p)
            if not self._is_balanced(p):
                p = self._restructure(self._tall_grandchild(p))
            p = self.parent(p)

    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)