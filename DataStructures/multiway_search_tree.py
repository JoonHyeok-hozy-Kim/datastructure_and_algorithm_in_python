from DataStructures.tree import LinkedTree
from DataStructures.maps import MapBase

class TwoFourTreeMap(LinkedTree, MapBase):

    class _Node(LinkedTree._Node):

        def __init__(self, e, parent=None, children=None):
            self._element = []
            self._parent = parent
            if children is None:
                children = []
            self._children = children

        def __len__(self):
            return len(self._element)

        def is_empty(self):
            return len(self) == 0

        def _add_item(self, k, v):
            if 0 <= len(self) <= 2:
                if self.is_empty():
                    self._element.append(MapBase._Item(k, v))
                    self._children.append(None)
                    self._children.append(None)
                else:
                    idx = 0
                    while idx < len(self):
                        if k > self._element[idx]._key:
                            idx += 1
                        else:
                            break
                    self._element.insert(idx, MapBase._Item(k, v))
                    self._children.insert(idx, None)

