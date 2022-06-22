from collections import MutableSet
from DataStructures.linked_list import PositionalList

class HozyMutableSet(MutableSet):

    def __init__(self):
        self._table = PositionalList()

    def __contains__(self, e):
        for v in self._table:
            if v == e:
                return True
        return False

    def __iter__(self):
        for e in self._table:
            yield e

    def __len__(self):
        return len(self._table)

    def add(self, e):
        self._table.add_last(e)

    def discard(self, e):
        walk = self._table.first()
        while walk is not None:
            if walk.element() == e:
                self._table.delete(walk)
                return
            walk = self._table.after(walk)

    def __str__(self):
        text_list = ['{']
        for e in self._table:
            text_list.append(str(e))
            text_list.append(', ')
        text_list.pop()
        text_list.append('}')
        return ''.join(text_list)

    def __lt__(self, other):
        if len(self) >= len(other):
            return False
        for e in self:
            if e not in other:
                return False
        return True

    def __or__(self, other):
        result = type(self)()
        for e in self:
            result.add(e)
        for e in other:
            result.add(e)
        return result

    def __ior__(self, other):
        for e in other:
            self.add(e)
        return self

    def pop(self):
        if len(self) == 0:
            raise KeyError
        v = None
        for e in self:
            if e is not None:
                v = e
        self.discard(v)
        return v

    def isdisjoint(self, other):
        if len(self) < len(other):
            for e in self:
                if e in other:
                    return False
        else:
            for e in other:
                if e in self:
                    return False
        return True

    def __xor__(self, other):
        result = type(self)()
        for e in self:
            if e not in other:
                result.add(e)
        for e in other:
            if e not in self:
                result.add(e)
        return result