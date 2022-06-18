from collections import MutableMapping
def pop(M):
    for k in M:
        pop_key = k
    popped = M[k]
    del M[k]
    return popped

def items(M):
    result = []
    for k in M:
        result.append((k, M[k]))
    return result


from DataStructures.maps import MapBase
from DataStructures.linked_list import PositionalList
class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = PositionalList()

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error : {}'.format(repr(k)))

    def __setitem__(self, k, v):
        walk = self._table.first()
        while walk is not None:
            if walk.element()._key == k:
                walk.element()._value = v
                return
            walk = self._table.after(walk)
        self._table.add_last(self._Item(k, v))

    def __delitem__(self, k):
        walk = self._table.first()
        while walk is not None:
            print('IN DEL, walk : {}'.format(str(walk.element())))
            if walk.element()._key == k:
                self._table.delete(walk)
                return
            walk = self._table.after(walk)
        raise KeyError('Key Error : {}'.format(repr(k)))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def items(self):
        result = []
        walk = self._table.first()
        while walk is not None:
            result.append((walk.element()._key, walk.element()._value))
            walk = self._table.after(walk)
        return result


if __name__ == '__main__':
    a = UnsortedTableMap()
    for i in range(5):
        a[chr(i+65)] = i
    print(a['B'])
    del a['C']
    print(items(a))

    # p = PositionalList()
    # for i in range(5):
    #     p.add_last(i)
    # print(p)
    # for i in p:
    #     print(i)
    # k = p.after(p.after(p.first()))
    # p.delete(k)
    # for i in p:
    #     print(i)
