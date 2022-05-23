from DataStructures.linked_list import PositionalList

class FavoriteList:
    class Item:
        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p is not self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and cnt > walk.element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk)

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def access(self, e):
        p = self._find_position(e)
        if p is None:
            self._data.add_last(self.Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal Value for k')
        walk = self._data.first()
        for i in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)
