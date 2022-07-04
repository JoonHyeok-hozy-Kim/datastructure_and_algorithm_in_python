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


from DataStructures.binary_search_trees import SplayTreeMap
from DataStructures.tree import LinkedBinaryTree
class SplayTreeMapTopDown(SplayTreeMap):

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError('Key Error : ', repr(k))
        else:
            p = self._splay_search(self.root(), k)
            if k != p.key():
                raise KeyError('Key Error : ', repr(k))
            return p.value()

    def _splay_search(self, p, k):
        l_subtree = LinkedBinaryTree()
        l_subtree._size = 1
        l_subtree_target = None
        r_subtree = LinkedBinaryTree()
        r_subtree._size = 1
        r_subtree_target = None

        while p is not None:
            # print('p : {}'.format(p.element()))
            p._node._parent = None
            self._root = p._node

            if k == p.key():

                if l_subtree._root is not None:
                    l_subtree_target._right = p._node._left
                    if p._node._left is not None:
                        p._node._left._parent = l_subtree_target
                    l_subtree._root._parent = p._node
                    p._node._left = l_subtree._root

                if r_subtree._root is not None:
                    r_subtree_target._left = p._node._right
                    if p._node._right is not None:
                        p._node._right._parent = r_subtree_target
                    r_subtree._root._parent = p._node
                    p._node._right = r_subtree._root

                # print('l_subtree')
                # print(l_subtree if l_subtree._root is not None else None)
                # print('r_subtree')
                # print(r_subtree if r_subtree._root is not None else None)

                return p

            elif k < p.key() and self.left(p) is not None:
                child = self.left(p)
                zig_flag = True
                move_node = p._node
                if not self.is_leaf(child):
                    if k < child.key() and self.left(child) is not None:
                        # Zig-Zig Case
                        # print('[r_subtree] Zig-Zig')
                        zig_flag = False
                        grand_child = self.left(child)

                        p._node._left._left = None
                        move_node = self._zig_zig_rotate_node(p._node._left)
                        p = grand_child

                if zig_flag:
                    # Zig Case
                    # print('[r_subtree] Zig')
                    p._node._left = None
                    move_node = p._node
                    p = child

                # print('move_node : {}'.format(move_node._element))
                if r_subtree.root() is None:
                    r_subtree._root = move_node
                else:
                    r_subtree_target._left = move_node
                    move_node._parent = r_subtree_target
                r_subtree_target = move_node

                # print('r_subtree')
                # print(r_subtree if r_subtree._root is not None else None)

            elif k > p.key() and self.right(p) is not None:
                child = self.right(p)
                zig_flag = True

                if not self.is_leaf(child):
                    if k > child.key() and self.right(child) is not None:
                        # Zig-Zig Case
                        # print('[l_subtree] Zig-Zig')
                        zig_flag = False
                        grand_child = self.right(child)

                        p._node._right._right = None
                        move_node = self._zig_zig_rotate_node(p._node._right)
                        p = grand_child

                if zig_flag:
                    # Zig Case
                    # print('[l_subtree] Zig')
                    p._node._right = None
                    move_node = p._node
                    p = child

                # print('move_node : {}'.format(move_node._element))
                if l_subtree.root() is None:
                    l_subtree._root = move_node
                else:
                    l_subtree_target._right = move_node
                    move_node._parent = l_subtree_target
                l_subtree_target = move_node

                # print('l_subtree')
                # print(l_subtree if l_subtree._root is not None else None)

            else:
                return p

    def _zig_zig_rotate_node(self, x):
        y = x._parent
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

        return x

from DataStructures.binary_search_trees import SplayTreeMap
class HalfSplayTreeMap(SplayTreeMap):

    def _subtree_search_depth(self, p, k):
        depth = -1
        while p is not None:
            depth += 1
            if k == p.key():
                return (p, depth)
            elif k < p.key():
                if self.left(p) is not None:
                    p = self.left(p)
                else:
                    return (p, depth)
            else:
                if self.right(p) is not None:
                    p = self.right(p)
                else:
                    return (p, depth)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError('Key Error : ', repr(k))
        else:
            p, d = self._subtree_search_depth(self.root(), k)
            self._splay_half(p, d)
            if k != p.key():
                raise KeyError('Key Error : ', repr(k))
            return p.value()

    def _splay_half(self, p, d):
        d //= 2
        while d > 0:
            d -= 2
            parent = self.parent(p)
            grand = self.parent(parent)

            if grand is None:
                # zig case
                self._rotate(p)
            elif ((parent == self.left(grand)) == (p == self.left(parent))):
                # zig-zig case
                self._rotate(parent)
                self._rotate(p)
            else:
                # zig-zag case
                self._rotate(p)
                self._rotate(p)
