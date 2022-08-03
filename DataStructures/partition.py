

class TreePartition:

    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            self._container = container     # Reference to the Partition instance
            self._element = e
            self._size = 1
            self._parent = self             # Convention for a group leader

        def element(self):
            return self._element

    def make_group(self, e):
        return self.Position(self, e)

    def find(self, p):
        """ Find the group containing p and return the position of the group leader"""
        if p._parent is not p:
            p._parent = self.find(p._parent)    # Overwrite parent after recursion
        return p._parent

    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size

