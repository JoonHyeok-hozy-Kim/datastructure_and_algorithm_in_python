from copy import deepcopy

class Empty(Exception):
    pass

class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('The stack is empty.')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('The stack is empty.')
        popped = self._head._element
        self._head = self._head._next
        self._size -= 1
        return popped


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty():
            raise Empty('The queue is empty.')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('The queue is empty.')
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

    def enqueue(self, e):
        if self.is_empty():
            self._head = self._Node(e, None)
            self._tail = self._head
        else:
            new_node = self._Node(e, None)
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1


class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            result = self._tail._element
            self._tail = None
        else:
            old_head = self._tail._next
            self._tail._next = old_head._next
            result = old_head._element
        self._size -= 1
        return result

    def enqueue(self, val):
        new_node = self._Node(val, None)
        if self.is_empty():
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def rotate(self):
        if self.is_empty():
            raise Empty('The queue is empty.')
        # elif len(self) == 1:
        #     pass
        else:
            self._tail = self._tail._next


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

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

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
