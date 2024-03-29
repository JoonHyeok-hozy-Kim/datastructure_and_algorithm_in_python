from DataStructures.linked_list import *

def second_to_last(A):
    if len(A) < 2:
        raise ValueError('Length is less than two.')
    walk = A._head
    while walk._next._next is not None:
        walk = walk._next
    return walk._element

from DataStructures.queue import LinkedQueue
def concatenate(first_node, second_node):
    new_queue = LinkedQueue()
    new_queue._head = first_node
    new_queue._size += 1
    walk = first_node
    while walk._next is not None:
        walk = walk._next
        new_queue._size += 1
    walk._next = second_node
    new_queue._size += 1
    while walk._next is not None:
        walk = walk._next
        new_queue._size += 1
    new_queue._tail = walk
    return new_queue

def singly_linked_list_count(L, node=None, count=None):
    if node is None:
        node = L._head
        count = 1
    if node._next is None:
        return count
    else:
        return singly_linked_list_count(L, node._next, count+1)

def singly_swap(L, node_x, node_y):
    walk = L._head
    cnt = 0
    prev_x = None
    prev_y = None
    while walk._next is not None and cnt < 2:
        # print('walk : {}'.format(walk._element))
        if walk is L._head:
            if walk is node_x or walk is node_y:
                cnt += 1
        elif walk._next == node_x:
            cnt += 1
            prev_x = walk
        elif walk._next == node_y:
            cnt += 1
            prev_y = walk

        walk = walk._next

    if prev_x is None:
        L._head = node_y
    else:
        prev_x._next = node_y
    if prev_y is None:
        L._head = node_x
    else:
        prev_y._next = node_x

    temp = node_x._next
    node_x._next = node_y._next
    node_y._next = temp

def doubly_swap(node_x, node_y):
    temp_prev = node_x._prev
    temp_next = node_x._next
    # Adjacent Nodes
    node_x._prev._next = node_y
    node_x._next._prev = node_y
    node_y._prev._next = node_x
    node_y._next._prev = node_x

    # Target Nodes
    node_x._prev = node_y._prev
    node_x._next = node_y._next
    node_y._prev = temp_prev
    node_y._next = temp_next

def middle_finder(L):
    front = L._header
    back = L._trailer
    while True:
        front = front._next
        back = back._prev
        if front is back:
            break
        elif front._next is back:
            break
    return front._element

def concatenate_doubly(L, M):
    L._size += M._size
    # Link Middle
    L._trailer._prev._next = M._header._next
    M._header._next._prev = L._trailer._prev
    L._trailer = M._trailer

def max(L):
    walk = L._header._next
    result = walk._element
    while walk._next is not None:
        if result < walk._element:
            result = walk._element
        walk = walk._next
    return result

def add_last(L, e):
    if L.is_empty:
        L.add_first(e)
    else:
        last = L.last()
        L.add_after(last, e)

def add_before(L, p, e):
    if p == L.first():
        L.add_first(e)
    else:
        walk = L.first()
        while walk._next is not None:
            if walk._next == p:
                L.add_after(walk, e)
                return


class PositionalListNoSentinel:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
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

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position Type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        # if p._node._next is None:
        #     raise ValueError('p is no longer valid.')
        return p._node

    def _make_poistion(self, node):
        return self.Position(self, node)

    def __init__(self):
        self._cursor = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        iter_cursor = self.first()
        while True:
            yield iter_cursor.element()
            if len(self) > 1:
                iter_cursor = self.after(iter_cursor)
            if iter_cursor == self.first():
                break


    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        return self._make_poistion(self._cursor)

    def last(self):
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            return self.first()
        return self._make_poistion(self._cursor._prev)

    def before(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._prev)

    def after(self, p):
        target_node = self._validate(p)
        return self._make_poistion(target_node._next)

    def _insert_between(self, e, prev_node=None, next_node=None):
        new_node = self._Node(e, prev_node, next_node)
        if self.is_empty():
            self._cursor = new_node
        elif len(self) == 1:
            self._cursor._prev = self._cursor._next = new_node
            new_node._prev = new_node._next = self._cursor
        else:
            prev_node._next = new_node
            next_node._prev = new_node

        self._size += 1
        return new_node

    def _delete_node(self, node):
        if self.is_empty():
            raise Empty
        if len(self) == 1:
            self._cursor = None
        else:
            if node == self._cursor:
                self._cursor = node._next
            if len(self) == 2:
                self._cursor._prev = self._cursor._next = None
            else:
                node._prev._next = node._next
                node._next._prev = node._prev
        self._size -= 1
        return node._element

    def add_first(self, e):
        if self.is_empty():
            return self._insert_between(e)
        return self.add_before(self.first(), e)

    def add_last(self, e):
        if self.is_empty():
            return self._insert_between(e)
        return self.add_after(self.last(), e)


    def add_before(self, p, e):
        target_node = self._validate(p)
        new_node = self._insert_between(e, target_node._prev, target_node)
        if target_node == self._cursor:
            self._cursor = new_node
        return self._make_poistion(new_node)

    def add_after(self, p, e):
        target_node = self._validate(p)
        new_node = self._insert_between(e, target_node, target_node._next)
        return self._make_poistion(new_node)

    def delete(self, p):
        target_node = self._validate(p)
        return self._delete_node(target_node)

def sum_pair(N, V):
    diff_list = PositionalList()
    for i in N:
        temp = V-i
        if temp <= N.last().element():
            diff_list.add_first(temp)
    N_cursor = N.first()
    diff_cursor = diff_list.first()
    while N.after(N_cursor) is not None and diff_list.after(diff_cursor) is not None:
        if N_cursor.element() == diff_cursor.element():
            return [N_cursor.element(), V-N_cursor.element()]
        elif N_cursor.element() > diff_cursor.element():
            diff_cursor = diff_list.after(diff_cursor)
        else:
            N_cursor = N.after(N_cursor)
    return None


def bubble_sort(L):
    cnt = len(L)
    swap_cnt = 0
    move_cnt = 0
    while cnt > 0:
        cursor = L.first()
        walk = L.after(cursor)
        while walk is not None:
            if cursor.element() > walk.element():
                print('Swap[{}] {} <> {} : {}'.format(swap_cnt+1,
                                                      cursor.element(),
                                                      walk.element(),
                                                      L))
                L.swap(cursor, walk)
                walk = L.after(cursor)
                swap_cnt += 1
            else:
                cursor = L.after(cursor)
                walk = L.after(cursor)
                move_cnt += 1
        cnt -= 1

    return 'swap : {}, move : {}, total : {}'.format(swap_cnt,
                                                     move_cnt,
                                                     swap_cnt+move_cnt)

def natural_join(L, M):
    from copy import deepcopy
    L_cursor = L.first()
    result = []
    while L_cursor is not None:
        M_cursor = M.first()
        while M_cursor is not None:
            if L_cursor.element()[-1] == M_cursor.element()[0]:
                print('Matched {} - {}'.format(L_cursor.element(),
                                               M_cursor.element()))
                temp = deepcopy(L_cursor.element())
                temp.append(M_cursor.element()[-1])
                result.append(temp)
            M_cursor = M.after(M_cursor)
        L_cursor = L.after(L_cursor)
    return result

from DataStructures.queue import LinkedQueue as new_linked_queue
class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class ScoreBoard:

    def __init__(self, capacity=10):
        self._capacity = capacity
        self._board = new_linked_queue()
        self._n = 0

    def __str__(self):
        str_list = ['---------------']
        walk = self._board._header._next
        while walk is not None:
            str_list.append(str(walk._element))
            walk = walk._next
        str_list.append('---------------')
        return '\n'.join(str_list)

    def add(self, entry):
        if self._board.is_empty():
            self._board.enqueue(entry)
            return

        score = entry.get_score()
        walk = self._board._header
        rotate_cnt = min(self._capacity-1, len(self._board))
        not_inserted = True

        for i in range(rotate_cnt):
            if score > walk._next._element.get_score() and not_inserted:
                self._board.enqueue(entry)
                not_inserted = False
            self._board.enqueue(self._board.dequeue())

        while self._capacity < len(self._board):
            self._board.dequeue()

from DataStructures.linked_list import PositionalList
class CardShuffle:

    def __init__(self):
        self._card_deck = PositionalList()

    def create_card_deck(self, symbols=None, numbers=None):
        self._card_deck = PositionalList()
        if symbols is None:
            symbols = ['♠', '♣', '♡', '◇']
        if numbers is None:
            numbers = ['A']
            for i in range(9):
                numbers.append(str(i+2))
            numbers.append('K')
            numbers.append('Q')
            numbers.append('J')

        for symbol in symbols:
            for number in numbers:
                self._card_deck.add_last(symbol+number)

    def shuffle(self):
        l1_walk = self._card_deck.first()
        l2_walk = self._card_deck.first()
        for i in range(len(self._card_deck)//2):
            l2_walk = self._card_deck.after(l2_walk)
        print('[In shuffle] mid : {}'.format(l2_walk.element()))
        while self._card_deck.after(l2_walk) is not None:
            temp_l1 = self._card_deck.after(l1_walk)
            temp_l2 = self._card_deck.after(l2_walk)
            self._card_deck.add_after(l1_walk, self._card_deck.delete(l2_walk))
            l1_walk = temp_l1
            l2_walk = temp_l2
        return self._card_deck


class TextEditor:
    def __init__(self):
        self._data = PositionalList()
        self._cursor = None

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def left(self):
        if self.is_empty():
            raise Empty
        if self._cursor != self._data.first():
            self._cursor = self._data.before(self._cursor)
        return self._cursor

    def right(self):
        if self.is_empty():
            raise Empty
        if self._cursor != self._data.last():
            self._cursor = self._data.after(self._cursor)
        return self._cursor

    def insert(self, c):
        if self.is_empty():
            self._data.add_last(c)
            self._cursor = self._data.first()
        else:
            self._cursor = self._data.add_after(self._cursor, c)
        return self._cursor

    def delete(self):
        if self._cursor != self._data.last():
            self._data.delete(self._data.after(self._cursor))
            return

    def __str__(self):
        if self.is_empty():
            return ''
        text_list = []
        walk = self._data.first()
        while walk is not None:
            text_list.append(str(walk.element()))
            walk = self._data.after(walk)
        return ''.join(text_list)

class SparseArray:
    class Entry:
        __slots__ = '_index', '_value'

        def __init__(self, index, value):
            self._index = index
            self._value = value

        def index(self):
            return self._index

        def value(self):
            return self._value

        def __str__(self):
            return 'A[{}]={}'.format(self._index, self._value)

    def __init__(self):
        self._data = PositionalList()
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def add_last(self, v):
        if self.is_empty():
            self._data.add_last(self.Entry(0, v))
        else:
            self._data.add_last(self.Entry(len(self), v))
        self._size += 1
        return self._data.last()

    def make_none(self, index):
        if index > len(self)-1:
            raise IndexError
        walk = self._data.first()
        while walk is not None:
            if walk.element().index() == index:
                return self._data.delete(walk)
            walk = self._data.after(walk)


    def __getitem__(self, item):
        if len(self)-1 < item:
            raise IndexError
        walk = self._data.first()
        while walk is not None:
            if walk.element().index() == item:
                return walk.element().value()
            walk = self._data.after(walk)
        return None

    def __setitem__(self, key, value):
        if key > len(self)-1:
            raise IndexError
        if key == len(self)-1:
            if self._data.last().element().index() == key:
                self._data.last().element()._value = value
                return self._data.last()
            else:
                return self._data.add_after(self._data.last(), self.Entry(key, value))

        walk = self._data.first()
        while self._data.after(walk) is not None:
            if walk.element().index() == key:
                walk.element()._value = value
                return walk
            if self._data.after(walk).element().index() > key:
                return self._data.add_after(walk, self.Entry(key, value))
            walk = self._data.after(walk)

    def __str__(self):
        text_list = ['[']
        idx = 0
        walk = self._data.first()
        while idx <= len(self)-1:
            if walk is None:
                text_list.append('None')
            else:
                if idx == walk.element().index():
                    text_list.append(walk.element().value())
                    walk = self._data.after(walk)
                else:
                    text_list.append('None')
            text_list.append(',')
            idx += 1
        text_list.pop()
        text_list.append(']')
        return ''.join(text_list)


from DataStructures.stack import ArrayStack
class ArrayBasedPositionalArray:
    class Item:
        def __init__(self, index, element):
            self._index = index
            self._element = element

        def element(self):
            return self._element

        def __str__(self):
            return '([{}] {})'.format(self._index, self._element)

    def _validate(self, p):
        if not isinstance(p, self.Item):
            raise ValueError('Not a proper Item instance.')
        return p._index

    def __init__(self):
        self._data = []
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        text_list = []
        for i in range(len(self)):
            text_list.append(str(self._data[i]))
        return ','.join(text_list)

    def is_empty(self):
        return self._size == 0

    def empty_validation(self):
        if self.is_empty():
            raise Empty

    def first(self):
        self.empty_validation()
        return self._data[0]

    def last(self):
        self.empty_validation()
        return self._data[-1]

    def before(self, p):
        target_index = self._validate(p)
        if target_index == 0:
            raise IndexError
        return self._data[target_index-1]

    def after(self, p):
        target_index = self._validate(p)
        if target_index == self._size-1:
            raise IndexError
        return self._data[target_index+1]

    def add_first(self, e):
        if self.is_empty():
            self._data.append(self.Item(0, e))
            self._size += 1
        else:
            self.add_before(self.first(), e)
        return

    def add_last(self, e):
        self._data.append(self.Item(len(self), e))
        self._size += 1

    def add_before(self, p, e):
        target_index = self._validate(p)
        temp_stack = ArrayStack()
        for i in range(len(self)-target_index):
            temp_stack.push(self._data.pop())
        self._data.append(self.Item(target_index, e))
        while not temp_stack.is_empty():
            temp_item = temp_stack.pop()
            temp_item._index += 1
            self._data.append(temp_item)
        self._size += 1
        return

    def add_after(self, p, e):
        target_index = self._validate(p)
        temp_stack = ArrayStack()
        for i in range(len(self)-target_index-1):
            temp_stack.push(self._data.pop())
        self._data.append(self.Item(target_index+1, e))
        while not temp_stack.is_empty():
            temp_item = temp_stack.pop()
            temp_item._index += 1
            self._data.append(temp_item)
        self._size += 1
        return

    def delete(self, p):
        self.empty_validation()
        target_index = self._validate(p)
        temp_stack = ArrayStack()
        for i in range(len(self)-target_index-1):
            temp_stack.push(self._data.pop())
        result = self._data.pop()
        while not temp_stack.is_empty():
            temp_item = temp_stack.pop()
            temp_item._index -= 1
            self._data.append(temp_item)
        self._size -= 1
        return result.element()


from DataStructures.linked_list import PositionalList
from random import randint
class CardHand:
    def __init__(self):
        self._suits = ['♠', '♣', '♡', '◇']
        self._ranks = ['A', 'K', 'Q', 'J']
        for i in range(9):
            self._ranks.append(str(10-i))
        self._card_list = self.reset_card_list()
        self._hand = []
        for i in range(len(self._suits)):
            new_list = PositionalList()
            self._hand.append(new_list)
        self._hand_cnt = 0
        self._iter_cursor = self._hand[0]._header
        self._iter_cnt = 0

    def _reset_iterator(self):
        self._iter_cursor = self._hand[0]._header
        self._iter_cnt = 0

    def reset_card_list(self):
        card_list = PositionalList()
        for s in self._suits:
            for r in self._ranks:
                card_list.add_last(s+r)
        return card_list

    def _get_from_card_list(self, r, s):
        r = str(r)
        if s in self._suits:
            walk = self._card_list.first()
            while walk is not None:
                if walk.element()[1:] == r and walk.element()[0] == s:
                    card = self._card_list.delete(walk)
                    return card
                walk = self._card_list.after(walk)
        raise ValueError('Card {}{} not in _card_list'.format(s, r))

    def _add_card_to_hand(self, card):
        if card is None:
            raise ValueError('Received None for card.')
        self._hand[self._suits.index(card[0])].add_last(card)
        self._hand_cnt += 1
        print('Add card {}'.format(card))

    def add_card(self, r, s):
        card = self._get_from_card_list(r, s)
        self._add_card_to_hand(card)

    def _get_random_card_from_card_list(self, s=None):
        if s is None:
            random_new_idx = randint(0, len(self._card_list) - 1)
            walk = self._card_list.first()
            for i in range(random_new_idx):
                walk = self._card_list.after(walk)
        else:
            in_hand_cnt = len(self._hand[self._suits.index(s)])
            random_new_idx = randint(0, len(self._ranks)-in_hand_cnt-1)
            walk = self._card_list.first()
            while walk is not None:
                if walk.element()[0] == s:
                    if random_new_idx == 0:
                        break
                    else:
                        random_new_idx -= 1
                walk = self._card_list.after(walk)

        return self._card_list.delete(walk)


    def play(self, s):
        suit_idx = self._suits.index(s)
        loop_cnt = 0

        # delete card
        if len(self._hand[suit_idx]) == 0:
            random_idx = randint(0, self._hand_cnt-1)
            for card in self:
                if loop_cnt == random_idx:
                    # Delete card from hand
                    print('In play, delete card : {}'.format(card))
                    target_finger = self._hand[self._suits.index(card[0])]
                    target_finger.delete(target_finger.find(card))
                    self._hand_cnt -= 1

                    # Add Random Card to _hand
                    new_card = self._get_random_card_from_card_list()
                    self._add_card_to_hand(new_card)

                    # Add deleted card to _card_list
                    self._card_list.add_last(card)

                    self._reset_iterator()
                    break
                else:
                    loop_cnt += 1
        else:
            target_hand = self._hand[self._suits.index(s)]
            random_idx = randint(0, len(target_hand)-1)
            walk = target_hand.first()
            for i in range(random_idx):
                walk = target_hand.after(walk)
            old_card = target_hand.delete(walk)
            print('In play, delete card : {}'.format(old_card))

            new_card = self._get_random_card_from_card_list(s)
            self._add_card_to_hand(new_card)

            self._card_list.add_last(old_card)

        # get card
        return

    def __next__(self):
        self._iter_cursor = self._iter_cursor._next
        if self._iter_cursor == self._hand[self._iter_cnt]._trailer:
            if self._iter_cnt == len(self._hand)-1:
                self._iter_cursor = self._hand[0]._header
                self._iter_cnt = 0
                raise StopIteration()
            else:
                self._iter_cnt += 1
                while len(self._hand[self._iter_cnt]) == 0:
                    self._iter_cnt += 1
                self._iter_cursor = self._hand[self._iter_cnt]._header._next

        return self._iter_cursor._element

    def __iter__(self):
        return self

    def all_of_suits(self, s):
        finger = self._hand[self._suits.index(s)]
        walk = finger.first()
        while walk is not None:
            yield walk.element()
            walk = finger.after(walk)

    def show_hand(self):
        text_list = []
        for i in self:
            text_list.append(i)
        result = ','.join(text_list)
        print(result)
        return result


if __name__ == '__main__':
    None
    from DataStructures.queue import LinkedQueue as new_linked_queue
    from DataStructures.linked_list import PositionalList
    import sys
    # 7.1

    # lq = LinkedQueue()
    # for i in range(5):
    #     lq.enqueue(i)
    # # for i in range(5):
    # #     print(lq.dequeue())
    # print(second_to_last(lq))

    # 7.2
    # a = LinkedQueue()
    # b = LinkedQueue()
    # for i in range(3):
    #     a.enqueue(i)
    # for i in range(4):
    #     b.enqueue((i+1)*(-1))
    # c = concatenate(a._head, b._head)
    # for i in range(7):
    #     print(c.dequeue())

    # 7.3
    # a = LinkedQueue()
    # for i in range(11):
    #     a.enqueue(i)
    # # print(singly_linked_list_count(a))
    # node_x = a._head
    # for i in range(4):
    #     node_x = node_x._next
    # node_y = a._head
    # for i in range(7):
    #     node_y = node_y._next
    # print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    # singly_swap(a, node_x, node_y)
    # for i in range(11):
    #     print(a.dequeue())

    # a = LinkedQueue()
    # for i in range(10):
    #     a.enqueue(i)
    # node_x = a._head
    # for i in range(3):
    #     node_x = node_x._next
    # node_y = a._head
    # for i in range(7):
    #     node_y = node_y._next
    # print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    # singly_swap(a, node_x, node_y)
    # for i in range(10):
    #     print(a.dequeue())

    # Test for Doubly
    # b = LinkedDeque()
    # for i in range(10):
    #     b.insert_last(i)
    # node_x = b._header
    # for i in range(3):
    #     node_x = node_x._next
    # node_y = b._trailer
    # for i in range(4):
    #     node_y = node_y._prev
    # print('node_x : {}, node_y : {}'.format(node_x._element, node_y._element))
    # doubly_swap(node_x, node_y)
    # for i in range(10):
    #     print(b.delete_first())


    # b = LinkedDeque()
    # for i in range(9):
    #     b.insert_last(i)
    # print(middle_finder(b))
    # for i in range(len(b)):
    #     print(b.delete_first())

    # a = LinkedDeque()
    # for i in range(5):
    #     a.insert_last(i+1)
    # b = LinkedDeque()
    # for i in range(5):
    #     b.insert_last((i+1)*(-1))
    # concatenate_doubly(a, b)
    # # for i in range(10):
    # #     print(a.delete_first())
    #
    # print(max(a))

    # a = PositionalList()
    # for i in range(5):
    #     # a.add_last(randint(0, 100))
    #     a.add_last(i)
    # print(a)
    # # print(max(a))
    # # print(a.max())
    # # print(a.find(0), a.find(0).element())
    # # print(a.find(10))
    # #
    # # print(a.recursive_find(0), a.recursive_find(0).element())
    # # print(a.recursive_find(10))
    #
    # # for i in a.__reversed__():
    # #     print(i)
    # for i in range(5):
    #     a.move_to_front(a.last())
    #     print(a)

    # fl = FavoriteListMTF()
    # fl.access('a')
    # fl.access('b')
    # fl.access('c')
    # fl.access('d')
    # fl.access('e')
    # fl.access('f')
    # fl.access('a')
    # fl.access('b')
    # fl.access('c')
    # fl.access('d')
    # fl.access('e')
    # for i in fl.top(6):
    #     print(i)

    # fl = FavoriteListMTF()
    # sample_size = 5
    # for i in range(sample_size):
    #     fl.access(i)
    # text_list = ['Original :']
    # for i in fl.top(sample_size):
    #     text_list.append(str(i))
    # print(' '.join(text_list))
    # for i in range(sample_size):
    #     fl.access(sample_size-i-1)
    # text_list = ['Reversed :']
    # for i in fl.top(sample_size):
    #     text_list.append(str(i))
    # print(' '.join(text_list))

    # f = FavoriteList()
    # for i in range(5):
    #     f.access(i)
    # first = f._data.first()
    # for i in range(4):
    #     print(first.element()._count)
    #     first = f._data.after(first)
    # f.reset_counts()
    # first = f._data.first()
    # for i in range(4):
    #     print(first.element()._count)
    #     first = f._data.after(first)

    # a = new_linked_stack()
    # for i in range(5):
    #     a.push(i)
    # print(a.top())
    # for i in range(6):
    #     print(a.pop())

    # a = new_linked_queue()
    # for i in range(5):
    #     a.enqueue(i+1)
    # for i in range(5):
    #     print(a.dequeue())
    # print('=========================')
    # for i in range(5):
    #     a.enqueue(i+1)
    # # reversed(a)
    # a.nonrecursive_reverse()
    # for i in range(5):
    #     print(a.dequeue())

    # lls = new_leaky_linked_stack(5)
    # for i in range(7):
    #     lls.push(i)
    # for i in range(5):
    #     print(lls.pop())
    # print(lls.pop())

    # fl = ForwardList()
    # for i in range(5):
    #     fl.add_first((i+1)*(-1))
    #     # print(fl.first().element())
    # for i in range(5):
    #     fl.add_last(i)
    #     # print(fl.last().element())
    # fl.add_after(fl.last(), 999)
    # print(fl.last().element())
    # fl.add_before(fl.first(), 6666)
    # print(fl.first().element())
    # fl.add_before(fl.after(fl.first()), -777)
    # print(fl.after(fl.first()).element())
    # print(fl.delete(fl.first()))
    # print(fl.first().element())
    # print(fl.last().element())
    # print(fl.delete(fl.last()))
    # print(fl.last().element())

    # a = CircularlyLinkedList()
    # a.append(-1)
    # print(a.cursor().element())
    # for i in range(5):
    #     a.append(i)
    #     print(a.cursor().element())
    # a.delete()
    # print(a.cursor().element())
    # a.rotate()
    # print(a.cursor().element())
    # a.rotate()
    # print(a.cursor().element())

    # from DataStructures.linked_list import _DoublyLinkedBase
    # a = _DoublyLinkedBase()
    # cursor = a._header
    # for i in range(5):
    #     a._insert_between(i, cursor, a._trailer)
    #     cursor = cursor._next
    # cursor = a._header._next
    # for i in range(len(a)):
    #     print(cursor._element)
    #     cursor = cursor._next
    # a.reverse()
    # cursor = a._header._next
    # for i in range(len(a)):
    #     print(cursor._element)
    #     cursor = cursor._next

    # a = PositionalList()
    # for i in range(5):
    #     a.add_last(i)
    # print(a)
    # a.swap(a.first(), a.last())
    # print(a)
    # # a.swap(a.first(), a.after(a.first()))
    # a.swap(a.after(a.first()), a.first())
    # print(a)
    #
    # for i in a:
    #     print(i)
    # a = PositionalListNoSentinel()
    # for i in range(5):
    #     # a.add_first(i)
    #     a.add_last(i)
    # print('----------------------')
    # for i in a:
    #     print(i)
    # for i in range(5):
    #     print('----------------------')
    #     print('Delete {}'.format(a.delete(a.last())))
    #     for i in a:
    #         print(i)

    # 7.37
    # recursive_limit = 10000000
    # old = sys.getrecursionlimit()
    # sys.setrecursionlimit(recursive_limit)
    # a = PositionalList()
    # for i in range(7000):
    #     a.add_last(i)
    # print(a)
    # print(sum_pair(a, 12000))

    # 7.38
    # a = PositionalList()
    # for i in range(10):
    #     a.add_last(randint(0, 100))
    # print(a)
    # print(bubble_sort(a))
    # print(a)

    # a = PositionalQueue()
    # for i in range(5):
    #     a.enqueue(i)
    #     print(a)
    # for i in range(5):
    #     # print(a.dequeue(), a)
    #     print(a.delete(a.last()), a)

    # a = FavoriteListMTF()
    # for i in range(5):
    #     for j in range(5):
    #         a.access(i)
    # for i in range(3):
    #     a.access(i)
    # for i in range(10):
    #     a.access(i)
    # # for i in a.top(5):
    # #     print(i)
    #
    # a.purge(7)
    # for i in a.top(3):
    #     print(i)

    # l = PositionalList()
    # m = PositionalList()
    # l.add_last(['a', 'd'])
    # l.add_last(['b', 'e'])
    # l.add_last(['c', 'f'])
    # m.add_last(['d', 'x'])
    # m.add_last(['d', 'y'])
    # m.add_last(['f', 'z'])
    # m.add_last(['g', 'w'])
    # m.add_last(['g', 'o'])
    # print('{} JOIN {}'.format(l, m))
    # print(natural_join(l, m))

    # s = ScoreBoard()
    # for i in range(12):
    #     s.add(GameEntry(chr(i+65), i))
    #     print(s)

    # c = CardShuffle()
    # c.create_card_deck()
    # print(c._card_deck)
    # for i in range(10):
    #     c.shuffle()
    #     print(c._card_deck)

    # t = TextEditor()
    # for i in range(5):
    #     t.insert(chr(i+65))
    # print(t)
    # t.left()
    # t.left()
    # t.left()
    # t.left()
    # t.insert(4)
    # print(t)
    # t.right()
    # t.right()
    # t.insert(6)
    # print(t)
    # for i in range(3):
    #     t.left()
    # for i in range(8):
    #     t.delete()
    #     print(t)

    # s = SparseArray()
    # for i in range(10):
    #     s.add_last(chr(i+65))
    # print(s)
    # for i in range(5):
    #     s.make_none(i+3)
    # print(s)
    # s[0] = 'X'
    # print(s)
    # s[5] = 'Y'
    # print(s)
    # s[len(s)-1] = '가'
    # print(s)
    # s.make_none(len(s)-1)
    # print(s)
    # s[len(s)-1] = 'ㅎ'
    # print(s)

    # a = ArrayBasedPositionalArray()
    # for i in range(3):
    #     a.add_first(i)
    #     print(a)
    # for i in range(3):
    #     a.add_before(a.after(a.first()), chr(ord('가')+i))
    #     print(a)
    # for i in range(3):
    #     a.add_last(chr(i+65))
    #     print(a)
    # for i in range(3):
    #     a.add_after(a.before(a.last()), chr(ord('나')+i))
    #     print(a)
    # for i in range(5):
    #     a.delete(a.last())
    #     print(a)
    # for i in range(8):
    #     a.delete(a.first())
    #     print(a)

    # '♠', '♣', '♡', '◇'
    c = CardHand()
    c.add_card('A', '◇')
    # c.add_card('K', '♡')
    c.add_card('3', '♠')
    c.add_card('5', '♣')
    c.add_card('10', '◇')
    c.add_card('J', '♠')
    c.add_card('K', '♠')
    c.show_hand()
    c.play('♡')
    c.show_hand()
    c.play('♠')
    c.show_hand()

