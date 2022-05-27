from copy import deepcopy

class Empty(Exception):
    pass

class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None  # This truncation may help Python's garbage collection
        return element

    def reverse(self):
        if self.is_empty():
            raise Empty
        walk = self._header
        while True:
            temp_next = walk._next
            walk._next = walk._prev
            walk._prev = temp_next
            if walk == self._trailer:
                break
            else:
                walk = temp_next
        temp_trailer = self._trailer
        self._trailer = self._header
        self._header = temp_trailer



class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty
        deleted = self._delete_node(self._header._next)
        return deleted

    def delete_last(self):
        if self.is_empty():
            raise Empty
        deleted = self._delete_node(self._trailer._prev)
        return deleted


class PositionalList(_DoublyLinkedBase):

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) == type(self) and other._node ==  self._node

        def __ne__(self, other):
            return not (self == other)

    def __init__(self):
        super().__init__()
        self._iter_cursor = self._header

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position Type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._next is None:
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_poistion(self, node):
        if node == self._header or node == self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_poistion(self._header._next)

    def last(self):
        return self._make_poistion(self._trailer._prev)

    def before(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._prev)

    def after(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._next)

    # [C-7.35] Formal Iteration Definition
    def __next__(self):
        self._iter_cursor = self._iter_cursor._next
        if self._iter_cursor != self._trailer:
            return self._iter_cursor._element
        else:
            raise StopIteration()

    def __iter__(self):
        return self

    # # Python's Iteration Generator Syntax
    # def __iter__(self):
    #     cursor = self.first()
    #     while cursor is not None:
    #         yield cursor.element()
    #         cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_poistion(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        target_node = self._validate(p)
        return self._insert_between(e, target_node._prev, target_node)

    def add_after(self, p, e):
        target_node = self._validate(p)
        return self._insert_between(e, target_node, target_node._next)

    def delete(self, p):
        target_node = self._validate(p)
        return self._delete_node(target_node)

    def replace(self, p, e):
        target_node = self._validate(p)
        old_value = target_node._element
        target_node._element = e
        return old_value

    def __str__(self):
        if self.is_empty():
            return '[]'
        else:
            return self._create_str_text()

    def _create_str_text(self, text_list=None, cursor=None):
        if text_list is None and cursor is None:
            text_list = ['[']
            cursor = self.first()
        if cursor is self.after(self.last()):
            text_list.pop()
            text_list.append(']')
            return ''.join(text_list)
        else:
            text_list.append(str(cursor.element()))
            text_list.append(', ')
            return self._create_str_text(text_list, self.after(cursor))

    def insertion_sort(self):
        if self.is_empty():
            return
        target = self.after(self.first())
        while target is not None:
            cursor = self.first()
            # print('[Phase1] target : {}'.format(target.element()))
            while cursor != target:
                # print('[Phase2] cursor : {}'.format(cursor.element()))
                if cursor.element() > target.element():
                    temp_target = self.before(target)
                    deleted = self.delete(target)
                    # print('[Shifted] {} <> {}'.format(cursor.element(),
                    #                                   deleted))
                    self.add_before(cursor, deleted)
                    target = temp_target
                    break
                else:
                    cursor = self.after(cursor)
            target = self.after(target)

    def max(self):
        walk = self.first()
        result = walk.element()
        while self.after(walk) is not None:
            if result < self.after(walk).element():
                result = self.after(walk).element()
            walk = self.after(walk)
        return result

    def find(self, e):
        walk = self.first()
        while self.after(walk) is not None:
            if walk.element() == e:
                return walk
            walk = self.after(walk)
        return None

    def recursive_find(self, e, node=None):
        if node is None:
            node = self.first()
        if node.element() == e:
            return node
        elif node == self.last():
            return None
        else:
            return self.recursive_find(e, self.after(node))

    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    def move_to_front(self, p):
        target_node = self._validate(p)
        prev_node = self._validate(self.before(p))
        if self.last() == p:
            next_node = self._trailer
        else:
            next_node = self._validate(self.after(p))
        prev_node._next = next_node
        next_node._prev = prev_node

        old_first_node = self._validate(self.first())
        self._header._next = target_node
        old_first_node._prev = target_node

        target_node._prev = self._header
        target_node._next = old_first_node

    # C-7.34
    def swap(self, p, q):
        node_p = self._validate(p)
        node_q = self._validate(q)
        adjacent_flag = False
        if node_p._next == node_q:
            adjacent_flag = True
        elif node_p._prev == node_q:
            self.swap(q, p)
            return

        # prev, next allocation
        p_prev = node_p._prev
        p_next = node_p._next  # if adjacent, node_q
        q_prev = node_q._prev  # if adjacent, node_p
        q_next = node_q._next

        # outer linkage
        p_prev._next = node_q
        node_q._prev = p_prev
        q_next._prev = node_p
        node_p._next = q_next

        # inner linkage
        if adjacent_flag:
            node_p._prev = node_q
            node_q._next = node_p
        else:
            p_next._prev = node_q
            q_prev._next = node_p
            node_p._prev = q_prev
            node_q._next = p_next

        return



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
        if p != self._data.first():
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
            p = self._data.add_last(self.Item(e))
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

    def clear(self):
        self._data = PositionalList()

    def reset_counts(self):
        walk = self._data.first()
        while self._data.after(walk) is not None:
            walk.element()._count = 0
            walk = self._data.after(walk)


class FavoriteListMTF(FavoriteList):
    def _move_up(self, p):
        if p is not self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        temp = PositionalList()
        for i in self._data:
            temp.add_last(i)

        for i in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value
            temp.delete(highPos)

    def purge(self, n):
        if len(self) < n:
            raise ValueError('Cannot purge more than {} elements.'.format(len(self)))
        walk = self._data.first()
        for i in range(n-1):
            walk = self._data.after(walk)
        while self._data.after(walk) is not None:
            self._data.delete(self._data.after(walk))

class ForwardList:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) == type(self) and other._node ==  self._node

        def __ne__(self, other):
            return not (self == other)

    def __init__(self):
        self._header = self._Node(None, None)
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position Type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        # if p._node._next is None:
        #     raise ValueError('p is no longer valid.')
        return p._node

    def _make_poistion(self, node):
        if node == self._header:
            return None
        else:
            return self.Position(self, node)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        return self._make_poistion(self._header._next)

    def last(self):
        if self.is_empty():
            raise Empty
        walk = self.first()
        while walk._node._next is not None:
            walk = self.after(walk)
        return walk

    def before(self, p):
        target_node = self._validate(p)
        if self._header._next == target_node:
            return None
        walk = self.first()
        while self.after(walk) is not None:
            if self.after(walk) == p:
                return walk
            walk = self.after(walk)
        return None

    def after(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_after(self, e, prev_node):
        new_node = self._Node(e, prev_node._next)
        prev_node._next = new_node
        self._size += 1
        return self._make_poistion(new_node)

    def add_first(self, e):
        return self._insert_after(e, self._header)

    def add_last(self, e):
        if self.is_empty():
            return self.add_first(e)
        last_position = self.last()
        return self._insert_after(e, last_position._node)

    def add_before(self, p, e):
        if p == self.first():
            return self.add_first(e)
        return self.add_after(self.before(p), e)

    def add_after(self, p, e):
        target_node = self._validate(p)
        return self._insert_after(e, target_node)

    def delete(self, p):
        target_node = self._validate(p)
        if p == self.first():
            prev_node = self._header
        else:
            prev_node = self._validate(self.before(p))
        prev_node._next = target_node._next
        self._size -= 1
        return target_node._element


class CircularlyLinkedList:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) == type(self) and other._node ==  self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position Type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._next is None:
            raise ValueError('p is no longer valid.')
        return p._node

    def _make_poistion(self, node):
        if node == self._header:
            return None
        else:
            return self.Position(self, node)

    def cursor(self):
        if self.is_empty():
            raise Empty
        return self._make_poistion(self._header._prev)

    def before(self, p):
        target_node = self._validate(p)
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            return p
        return self._make_poistion(target_node._prev)

    def after(self, p):
        target_node = self._validate(p)
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            return p
        return self._make_poistion(target_node._next)

    def append(self, e):
        new_node = self._Node(e, None, None)
        if self.is_empty():
            prev_node = next_node = self._header
            self._header._next = new_node
        else:
            cursor_node = self._validate(self.cursor())
            prev_node = cursor_node
            next_node = cursor_node._next
            cursor_node._next = new_node
        new_node._prev = prev_node
        new_node._next = next_node
        self._header._prev = new_node
        self._size += 1
        return self._make_poistion(new_node)

    def delete(self):
        if self.is_empty():
            raise Empty
        target_node = self._validate(self.cursor())
        if len(self) == 1:
            self._header._prev = None
            self._header._next = None
        else:
            target_node._next._prev = target_node._prev
            target_node._prev._next = target_node._next
        self._size -= 1
        return target_node._element

    def rotate(self):
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            return self.cursor()
        old_cursor_node = self._validate(self.cursor())
        after_header = self._header._next
        new_cursor_node = old_cursor_node._prev

        after_header._prev = old_cursor_node
        old_cursor_node._next = after_header
        old_cursor_node._prev = self._header
        self._header._next = old_cursor_node
        self._header._prev = new_cursor_node
        new_cursor_node._next = self._header

        return self._make_poistion(new_cursor_node)