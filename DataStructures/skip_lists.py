from math import inf
from random import randint
from DataStructures.linked_list import PositionalList

class PositionalNextBelowList:

    class _Node:
        __slots__ = '_item', '_next', '_below'

        def __init__(self, item, next, below):
            self._item = item
            self._next = next
            self._below = below

        def item(self):
            return self._item

        def set_below(self, node):
            self._below = node

    def __init__(self, container):
        self._container = container
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        cursor = self._header._next
        while cursor != self._trailer:
            yield cursor._item
            cursor = cursor._next

    def __str__(self):
        if self.is_empty():
            return '[]'
        else:
            return self._create_str_text()

    def _create_str_text(self, text_list=None, cursor=None):
        if text_list is None and cursor is None:
            text_list = ['[']
            cursor = self.first_node()
        if cursor == self._trailer:
            text_list.pop()
            text_list.append(']')
            return ''.join(text_list)
        else:
            text_list.append(str(cursor.item()))
            text_list.append(', ')
            return self._create_str_text(text_list, self.next_node(cursor))

    def is_empty(self):
        return self._size == 0

    def first_node(self):
        return self._header._next

    def last_node(self):
        walk = self._header
        while walk._next != self._trailer:
            walk = walk._next
        return walk

    def prev_node(self, p):
        raise NotImplementedError('Must be implemented by iteration.')

    def next_node(self, node):
        return node._next

    def below_node(self, node):
        return node._below

    def add_node_after(self, predecessor, item):
        newest = self._Node(item, predecessor._next, None)
        predecessor._next = newest
        self._size += 1
        return newest

    def add_node_first(self, item):
        return self.add_node_after(self._header, item)

    def add_node_last(self, item):
        raise NotImplementedError('Must be implemented by iteration.')

    def add_node_before(self, successor, item):
        raise NotImplementedError('Must be implemented by iteration.')

    def delete_node_after(self, predecessor):
        item = predecessor._next._item
        predecessor._next._item = predecessor._next._below = None  # Truncate for the garbage collection
        predecessor._next = predecessor._next._next                # Link with next node.
        self._size -= 1
        return item


class HozySkipList:
    _POS_INF = inf
    _NEG_INF = inf * (-1)

    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def lt(self, other):
            return self._key < other._key

        def __str__(self):
            return '({}, {})'.format(self._key, self._value)

    def __init__(self):
        self._levels = PositionalList()
        self._height = 0
        self._make_new_level()

    def __str__(self):
        text_list = []
        lv_cnt = 1
        for level in self._levels:
            text_list.append('[LV {}] '.format(lv_cnt))
            for item in level:
                text_list.append(str(item))
                text_list.append(' ')
            text_list.append('\n')
            lv_cnt += 1
        return ''.join(text_list)

    def start_node(self):
        top_level = self._levels.first().element()
        return top_level.first_node()

    def next_node(self, node):
        return node._next

    def prev_node(self, node):
        raise NotImplementedError('Must be implemented by iteration.')

    def below_node(self, node):
        return node._below

    def _make_new_level(self):
        new_level = PositionalNextBelowList(self)
        start_item = self._Item(self._NEG_INF, self._height)
        end_item = self._Item(self._POS_INF, self._height)

        end_node = new_level.add_node_first(end_item)
        start_node = new_level.add_node_first(start_item)

        if len(self._levels) > 0:
            top_level = self._levels.first().element()
            start_node._below = top_level.first_node()
            end_node._below = top_level.last_node()

        self._height += 1
        return self._levels.add_first(new_level)

    def skip_search(self, k):
        walk = self.start_node()
        # print(walk.item())
        while self.below_node(walk) is not None:
            walk = self.below_node(walk)
            # print('↓ : {}'.format(walk.item()))
            while self.next_node(walk).item()._key <= k:
                walk = self.next_node(walk)
                # print('→ : {}'.format(walk.item()))
        return walk

    def skip_insert(self, k, v):
        h = self._random_height()

        # Add New Line
        new_level_cnt = h - self._height
        if new_level_cnt > 0:
            for i in range(new_level_cnt + 1):
                self._make_new_level()

        # Add top level for initial insert.
        if len(self._levels) == 1:
            self._make_new_level()

        p = self._levels.first()
        walk_node = None
        above_node = None
        for i in range(self._height - h - 1):
            p = self._levels.after(p)
        while self._levels.after(p) is not None:
            # Go down the level
            p = self._levels.after(p)
            level = p.element()

            # Set walk node.
            walk_node = self.below_node(walk_node) if walk_node is not None else level.first_node()

            # Shift node forward until key is le to k.
            while self.next_node(walk_node).item()._key <= k:
                walk_node = self.next_node(walk_node)

            # Add new item after the walk node.
            new_node = level.add_node_after(walk_node, self._Item(k, v))

            # Link above node if exists.
            if above_node is not None:
                above_node._below = new_node
            above_node = new_node

    def _random_height(self):
        cnt = 1
        while randint(0, 1) == 0:
            cnt += 1
        return cnt

    def skip_delete(self, k):
        p = self._levels.first()
        walk_node = self.start_node()
        # print(walk_node.item())
        while self._levels.after(p) is not None:
            p = self._levels.after(p)
            level = p.element()
            walk_node = self.below_node(walk_node)
            # print('↓', walk_node.item())
            while self.next_node(walk_node).item()._key < k:
                walk_node = self.next_node(walk_node)
                # print('→', walk_node.item())
            if self.next_node(walk_node).item()._key == k:
                level.delete_node_after(walk_node)