from DataStructures.tree import LinkedBinaryTree
from DataStructures.maps import MapBase

class TreeMap(LinkedBinaryTree, MapBase):

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    def _subtree_search(self, p, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        if self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        if self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        if self.left(p) is not None:
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        if self.right(p) is not None:
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        if self.is_empty():
            return None
        p = self._subtree_search(self.root(), k)
        self._rebalance_access(p)
        return p

    def find_min(self):
        if self.is_empty():
            return None
        p = self.first()
        return (p.key(), p.value())

    def find_ge(self, k):
        """
        Return (key,value) pair with least key greater than or equal to k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        p = self.find_position(k)
        if p.key() < k:
            p = self.after(p)
        return (p.key(), p.value())

    def find_range(self, start, stop):
        """
        Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)

            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError('Key Error : ', repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error : ', repr(k))
            return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
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
        self._rebalance_insert(leaf)

    def __iter__(self):
        if not self.is_empty():
            walk = self.first()
            while walk is not None:
                yield walk.key()
                walk = self.after(walk)

    def delete(self, p):
        """ Remove item in the given position p """
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                parent = self.parent(p)
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError('Key Error : ', repr(k))

    def _rebalance_insert(self, p):
        """ Will be implemented by subclass """
        pass

    def _rebalance_delete(self, p):
        """ Will be implemented by subclass """
        pass

    def _rebalance_access(self, p):
        """ Will be implemented by subclass """
        pass

    def _relink(self, parent, child, make_left_child):
        """ Relink parent node with child node (we allow child to be None). """
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)

        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)

    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.left(y)) == (y == self.left(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x


class AVLTreeMap(TreeMap):

    class _Node(TreeMap._Node):
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

    def _recompute_height(self, p):
        node = self._validate(p)
        node._height = 1 + max(node.left_height(), node.right_height())

    def _is_balanced(self, p):
        node = self._validate(p)
        return abs(node.left_height() - node.right_height()) <= 1

    def _tall_child(self, p, favor_left=False):
        node = self._validate(p)
        if node.left_height() + (1 if favor_left else 0) > node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_node = self._validate(p)
            old_height = old_node._height
            if not self._is_balanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            new_node = self._validate(p)
            if new_node._height == old_height:
                p = None
            else:
                p = self.parent(p)

    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)


class SplayTreeMap(TreeMap):

    def _splay(self, p):
        while p != self.root():
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

    def _rebalance_insert(self, p):
        self._splay(p)

    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)


from DataStructures.tree import Tree
class MultiwaySearchTreeBase(Tree, MapBase):
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
