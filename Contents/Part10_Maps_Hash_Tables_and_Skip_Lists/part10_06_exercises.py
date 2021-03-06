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


def vehicle_id_hash_function(S):
    FORMAT = '9X9XX99X9XX999999'
    text_num = []
    if len(S) != len(FORMAT):
        raise ValueError('Invalid id : Length')
    for i in range(len(FORMAT)):
        if FORMAT[i].isnumeric() != S[i].isnumeric():
            raise ValueError('Invalid id : Format')
        if S[i].isnumeric():
            text_num.append(str(S[i]))
        else:
            text_num.append(str(ord(S[i])))
    return int(''.join(text_num))

from random import randint
def random_id_generator(n=None):
    FORMAT = '9X9XX99X9XX999999'
    result_list = []
    if n is None:
        n = 1

    for i in range(n):
        temp_list = []
        for char in FORMAT:
            if char.isnumeric():
                temp_list.append(str(randint(0,9)))
            else:
                temp_list.append(chr(65+randint(0, 25)))
        result_list.append(''.join(temp_list))
    return result_list


def generate_all_id(idx=0, current_num=0, temp_list=[], result_list=[]):
    FORMAT = '9X9XX99X9XX999999'
    if len(temp_list) == len(FORMAT):
        new_id = ''.join(temp_list)
        print(new_id)
        result_list.append(new_id)
        return result_list

    if FORMAT[idx].isnumeric():
        if current_num > 9:
            return result_list
        else:
            temp_list.append(str(current_num))
            generate_all_id(idx+1, 0, temp_list, result_list)
            temp_list.pop()
            return generate_all_id(idx, current_num+1, temp_list, result_list)
    else:
        if current_num > 25:
            return result_list
        else:
            temp_list.append(chr(current_num+65))
            generate_all_id(idx+1, 0, temp_list, result_list)
            temp_list.pop()
            return generate_all_id(idx, current_num+1, temp_list, result_list)

from DataStructures.hash_tables import ChainHashMap
def hashed_id_tester(A):
    result_map = ChainHashMap()
    # result_map = {(A[0], vehicle_id_hash_function(A[0]))}
    for idx in range(len(A)):
        new_hash_id = vehicle_id_hash_function(A[idx])
        if A[idx] in result_map:
            if new_hash_id != result_map[A[idx]]:
                return (False, (A[idx], new_hash_id, result_map[A[idx]]))
        else:
            result_map[A[idx]] = new_hash_id
    return (True, result_map)


from DataStructures.hash_tables import HashMapBase
class CollisionHashMap(HashMapBase):
    def _hash_function(self, k):
        return (3*k+5)%11

class CollisionProbeHashMap(CollisionHashMap):
    _AVAIL = object()       # sentinel marks locations of previous deletions

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is CollisionProbeHashMap._AVAIL

    def _find_key(self, j, k):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j+1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_key(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_key(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_key(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = CollisionProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key


class CollisionQuadraticProbeHashMap(CollisionProbeHashMap):
    def _find_key(self, j, k):
        firstAvail = None
        idx = 0
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            idx += 1
            j = (j+pow(idx, 2)) % len(self._table)


class CollisionDoubleHashMap(CollisionProbeHashMap):

    def _double_hash(self, j, k, i):
        q = 7  # Set arbitrarily
        double_hash_formula = (q - (k % q)) * i
        return (j + double_hash_formula) % len(self._table)

    def _find_key(self, j, k):
        firstAvail = None
        idx = 0
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            idx += 1
            j = self._double_hash(j, k, idx)


from DataStructures.hash_tables import HashMapBase
class CollisionHashMapNew(HashMapBase):
    def _hash_function(self, k):
        return (3*k) % 17


class CollisionChainHashMapNew(CollisionHashMapNew):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

from random import randint
def coin_flip():
    cnt = -1
    coin = 0
    while coin == 0:
        cnt += 1
        coin = randint(0, 1)
    return cnt

def sieve_algorithm(M):
    l = [True for i in range(2*M)]
    l[0] = False
    i = 2
    while True:
        if pow(i, 2) > 2*M:
            return l
        j = 2
        while i*j <= 2*M:
            l[i*j-1] = False
            j += 1
        i += 1

from random import randint
from time import time
def load_factor_tester(data_type_set, sample_size):
    load_factor_set = [(i+1)/10 for i in range(9)]
    print('[load_factor_set] : {}'.format(load_factor_set))
    num = randint(0, 3)
    random_key_set = [num]
    for i in range(sample_size-1):
        num += randint(1, 3)
        random_key_set.append(num)
    print('[random_key_set] : {}'.format(random_key_set))
    print('----------- Report -----------')

    for data_type in data_type_set:
        print('Data Type : {}'.format(str(data_type)))

        for load_factor in load_factor_set:
            print('\t[load_factor : {}]'.format(str(load_factor)))
            object = data_type(load_factor=load_factor)

            # __setitem_ test
            t1 = time()
            for key in random_key_set:
                object[key] = key
            t2 = time()
            print('\t\t- set  : {}'.format(t2-t1))

            # __iter__ test
            t1 = time()
            for key in random_key_set:
                # print(key, object[key])
                object[key]
            t2 = time()
            print('\t\t- iter : {}'.format(t2-t1))

            # __delitem test
            t1 = time()
            for key in random_key_set:
                del object[key]
            t2 = time()
            print('\t\t- del : {}'.format(t2-t1))
        print()


class OptimizedChainHashMap(CollisionHashMap):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        if type(bucket) == self._Item:
            return bucket._value
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = self._Item(k, v)
            self._n += 1
        else:
            if type(self._table[j]) == self._Item:
                if self._table[j]._key == k:
                    self._table[j]._value = v
                else:
                    item = self._table[j]
                    self._table[j] = UnsortedTableMap()
                    self._table[j][item._key] = item._value
                    self._table[j][k] = v
                    self._n += 1
            else:
                old_size = len(self._table)
                self._table[j][k] = v
                if old_size < len(self._table):
                    self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        if type(bucket) == self._Item:
            self._table[j] = None
        else:
            if len(bucket) == 2:
                for key in bucket:
                    if key != k:
                        new_item = self._Item(key, bucket[key])
                        break
                self._table[j] = new_item
            else:
                del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                if type(bucket) == self._Item:
                    yield bucket._key
                else:
                    for key in bucket:
                        yield key

    def _bucket_setdefault(self, j, k, d):
        if self._table[j] is not None:
            return self._table[j].setdefault(k, d)
        else:
            self._bucket_setitem(j, k, d)
            return d


class CustomProbeHashMap(CollisionHashMap):
    _AVAIL = object()       # sentinel marks locations of previous deletions

    def __init__(self, linear_unit=1):
        super().__init__()
        if linear_unit >= len(self._table):
            raise ValueError('Linear unit cannot be larger than the capacity.')
        self._linear_unit = linear_unit

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j+self._linear_unit) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        print('j : {}, s : {}, k :{}'.format(j, s, k))
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

    def _bucket_setdefault(self, j, k, d):
        found, s = self._find_slot(j, k)
        if found:
            return self._table[s]._value
        else:
            self._table[s] = self._Item(k, d)
            return d

from DataStructures.sorted_maps import SortedTableMap
from DataStructures.maps import MultiMap
class SortedMultiMap(MultiMap):

    def __init__(self):
        self._map = SortedTableMap()
        self._n = 0

    def __iter__(self):
        for k, secondary in self._map.items():
            for v in secondary:
                yield (k, v)

    def add(self, k, v):
        container = self._map.setdefault(k, [])
        container.append(v)
        self._n += 1

    def pop(self, k):
        secondary = self._map[k]
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]
        self._n -= 1
        return (k, v)

    def find(self, k):
        """ Return arbitrary (k, v) pair with given key (or raise KeyError)"""
        secondary = self._map[k]
        return (k, secondary[0])

    def find_all(self, k):
        """ Generate iteration of all (k, v) pairs with given key """
        secondary = self._map[k]
        for v in secondary:
            yield (k, v)

def double_binary_search(S, T, k):
    s_idx = 0
    t_idx = 0
    while k > 0:
        if S._table[s_idx]._key > T._table[t_idx]._key:
            result = (S, S._table[s_idx]._key)
            t_idx += 1
        else:
            result = (T, T._table[t_idx]._key)
            s_idx += 1
        k -= 1
        print(result)
    return result

def n_by_n_one_counter(A):
    cnt = 0
    for array in A:
        low = 0
        high = len(array)-1
        while True:
            mid = (low + high) // 2
            # print('{} // low : {}, mid : {}, high : {}'.format(array, low, mid, high))
            if array[low] == array[high] == 0:
                # print('ADD 0')
                break
            if array[low] == array[high] == 1:
                # print('ADD {} '.format(high - low + 1))
                cnt += high - low + 1
                break
            if array[mid] == 0:
                if array[mid+1] == 1:
                    cnt += len(array) - (mid + 1)
                    # print('ADD {} '.format(len(array) - (mid + 1)))
                    break
                else:
                    low = mid
            elif array[mid] == 1:
                if array[mid-1] == 0:
                    cnt += len(array) - mid
                    # print('ADD {} '.format(len(array) - mid))
                    break
                else:
                    high = mid
    return cnt

from DataStructures.maps import UnsortedTableMap
class UnsortedListTableMap(UnsortedTableMap):

    def __setitem__(self, k, v):
        walk = self._table.first()
        while walk is not None:
            if walk.element()._key == k:
                new_list = []
                for e in walk.element()._value:
                    new_list.append(e)
                new_list.append(v)
                walk.element()._value = new_list
                return
            walk = self._table.after(walk)
        if isinstance(v, list):
            self._table.add_last(self._Item(k, v))
        else:
            self._table.add_last(self._Item(k, [v]))

    def items(self):
        result = []
        walk = self._table.first()
        while walk is not None:
            result.append((walk.element()._key, walk.element()._value))
            walk = self._table.after(walk)
        return result

from DataStructures.hash_tables import ChainHashMap
class InvertedTextHashMap(ChainHashMap):

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedListTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


def invert_text(T):
    raw_word_list = T.split(' ')
    s = InvertedTextHashMap()
    for i in range(len(raw_word_list)):
        s[raw_word_list[i].lower()] = i
    return s

def polynomial_hash_code(S, a):
    sum = 0
    indeterminate = 1
    m = pow(10, 9) + 7
    for c in S:
        sum += ord(c) * indeterminate
        # print('{} {} {}'.format(ord(c), indeterminate, sum))
        indeterminate *= a
    return sum % m

def phone_number_genertor(digit=10, i=0, temp_list=[], result_list=[], max_num=None):
    if max_num is not None:
        if len(result_list) >= max_num:
            return result_list
    if digit == i:
        num = ''.join(temp_list)
        result_list.append(num)
        return result_list
    for j in range(10):
        temp_list.append(str(j))
        phone_number_genertor(digit, i+1, temp_list, result_list, max_num)
        temp_list.pop()
    return result_list


from DataStructures.hash_tables import ProbeHashMap
class OrderDict(ProbeHashMap):
    class _Item(ProbeHashMap._Item):
        __slots__ = '_key', '_value', '_next_key', '_prev_key'

        def __init__(self, key, value, next_key=None, prev_key=None):
            super().__init__(key, value)
            self._next_key = next_key
            self._prev_key = prev_key

        def next(self):
            return self._next

    def __init__(self, linear_unit=1):
        super().__init__(linear_unit=linear_unit)
        self._first_key = None
        self._last_key = None

    def get_slot(self, k):
        found, s = self._find_slot(self._hash_function(k), k)
        if not found:
            raise ValueError('In get_slot, slot not found')
        return s

    def _bucket_setitem(self, j, k, v):
        # print('In _bucket_setitem, j {}, k {}, v {}'.format(j, k, v))
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v, self._last_key, None)
            if self._first_key is None:
                self._first_key = k
            if self._last_key is not None:
                last_found, last_slot = self._find_slot(self._hash_function(self._last_key), self._last_key)
                if last_found:
                    last_item = self._table[self.get_slot(self._last_key)]
                    last_item._next_key = k
            self._last_key = k
            self._n += 1
        else:
            curr = self._table[s]
            prev_slot = self.get_slot(curr._prev_key)
            next_slot = self.get_slot(curr._next_key)
            if self._first_key == k:
                self._first_key = curr._next_key
            elif self._last_key != k:
                self._table[prev_slot]._next_key = curr._next_key
                self._table[next_slot]._prev_key = curr._prev_key
            curr._prev_key = self._last_key
            last_item = self._table[self.get_slot(self._last_key)]
            last_item._next_key = k
            self._last_key = k
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        k = self._first_key
        while True:
            found, s = self._find_slot(self._hash_function(k), k)
            yield self._table[s]._key
            if self._last_key == k:
                break
            k = self._table[s]._next_key

    def items(self):
        k = self._first_key
        result = []
        while True:
            s = self.get_slot(k)
            result.append(self._table[s])
            if self._last_key == k:
                break
            k = self._table[s]._next_key
        return result

    def _resize(self, c):
        old = self.items()
        self._table = c * [None]
        self._n = 0
        for item in old:
            self[item._key] = item._value


from DataStructures.sets import HozyMutableSet
from copy import deepcopy
class SpellChecker:

    def __init__(self):
        self._W = HozyMutableSet()

    def set_words(self, A):
        for word in A:
            self._W.add(word)
        return self._W

    def check(self, s):
        if s in self._W:
            return [s]
        else:
            result = []
            for word in self._W:
                check = self._swap_adjacent_characters(word, s)
                if check is not None:
                    result.append(word)
                    continue
                check = self._insert_character_in_between(word, s)
                if check is not None:
                    result.append(word)
                    continue
                check = self._delete_single_character(word, s)
                if check is not None:
                    result.append(word)
                    continue
                check = self._replace_character(word, s)
                if check is not None:
                    result.append(word)
            return result

    def _swap_adjacent_characters(self, w, s):
        w_list = list(w)
        for i in range(len(w_list)-1):
            w_copy = deepcopy(w_list)
            w_copy.insert(i+1, w_copy.pop(i))
            if ''.join(w_copy) == s:
                return w

    def _insert_character_in_between(self, w, s):
        w_list = list(w)
        for i in range(len(w_list)-1):
            for j in range(26):
                w_list.insert(i+1, chr(j+97))
                if ''.join(w_list) == s:
                    return w
                w_list.pop(i+1)

    def _delete_single_character(self, w, s):
        w_list = list(w)
        for i in range(len(w_list)):
            popped = w_list.pop(i)
            if ''.join(w_list) == s:
                return w
            w_list.insert(i, popped)

    def _replace_character(self, w, s):
        w_list = list(w)
        for i in range(len(w_list)):
            popped = w_list.pop(i)
            for j in range(26):
                w_list.insert(i, chr(j+97))
                if ''.join(w_list) == s:
                    return w
                w_list.pop(i)
            w_list.insert(i, popped)

if __name__ == '__main__':
    pass
    # a = UnsortedTableMap()
    # for i in range(5):
    #     a[chr(i+65)] = i
    # print(a['B'])
    # del a['C']
    # print(items(a))

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

    # from DataStructures.hash_tables import ChainHashMap
    # from DataStructures.linked_list import PositionalList
    # l = PositionalList()
    # for i in range(5):
    #     l.add_last(i)
    #
    # # Insert elements of l into a with positions as keys
    # a = ChainHashMap()
    # walk = l.first()
    # while walk is not None:
    #     a[walk] = walk.element()
    #     walk = l.after(walk)
    #
    # # Insert elements of l into b with positions as keys
    # b = ChainHashMap()
    # walk = l.first()
    # while walk is not None:
    #     b[walk] = walk.element()
    #     walk = l.after(walk)
    #
    # print('a == b : {}'.format(a == b))
    #
    # # Make another Positional list with identical values
    # m = PositionalList()
    # for i in range(5):
    #     m.add_last(i)
    #
    # # Insert elements of m into c with positions as keys
    # c = ChainHashMap()
    # walk = m.first()
    # while walk is not None:
    #     c[walk] = walk.element()
    #     walk = m.after(walk)
    #
    # print('a == c : {}'.format(a == c))
    #
    # # Change l
    # l.add_last(99)
    #
    # # Insert elements of l' into d with positions as keys
    # d = ChainHashMap()
    # walk = l.first()
    # while walk is not None:
    #     d[walk] = walk.element()
    #     walk = l.after(walk)
    #
    # print('a == d : {}'.format(a == c))

    # id = '9X9XX99X9XX999999'
    # hashed_id = vehicle_id_hash_function(id)
    # print(hashed_id)
    # sample_size = 10
    # for i in range(sample_size):
    #     id = random_id_generator()
    #     hashed_id = vehicle_id_hash_function(id)
    #     print('id : {}, hashed : {}'.format(id, hashed_id))

    # a = random_id_generator(20)
    # # a = generate_all_id()
    # test = hashed_id_tester(a)
    # print(test[0])

    # l = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    # separate_chained = []
    # for i in l:
    #     hash_code = (3*i+5)%11
    #     insert_flag = False
    #     for bucket in separate_chained:
    #         if bucket[0] == hash_code:
    #             bucket[1].append(i)
    #             insert_flag = True
    #             break
    #     if not insert_flag:
    #         separate_chained.append((hash_code, [i]))
    # for bucket in separate_chained:
    #     print(bucket)

    # l = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    # p = CollisionProbeHashMap()
    # for i in l:
    #     p[i] = i
    # text_list = ['---------------------Linear Probing----------------------\n']
    # for item in p._table:
    #     if item is None:
    #         text_list.append('-')
    #     else:
    #         text_list.append('(h : {}, k : {}, v : {})'.format( (3*item._key+5)%11, item._key, item._value))
    # print(' '.join(text_list))

    # p = CollisionQuadraticProbeHashMap()
    # for i in l:
    #     p[i] = i
    # text_list = ['---------------------Quadratic Probing----------------------\n']
    # for item in p._table:
    #     if item is None:
    #         text_list.append('-')
    #     else:
    #         text_list.append('(h : {}, k : {}, v : {})'.format( (3*item._key+5)%11, item._key, item._value))
    # print(' '.join(text_list))

    # p = CollisionDoubleHashMap()
    # for i in l:
    #     p[i] = i
    # text_list = ['---------------------Quadratic Probing----------------------\n']
    # for item in p._table:
    #     if item is None:
    #         text_list.append('-')
    #     else:
    #         text_list.append('(h : {}, k : {}, v : {})'.format( (3*item._key+5)%11, item._key, item._value))
    # print(' '.join(text_list))

    # r = CollisionChainHashMapNew(cap=17, load_factor=0.2)
    # l = [54, 28, 41, 18, 10, 36, 25, 38, 12, 90]
    # for i in l:
    #     r[i] = i
    # text_list = []
    # for container in r._table:
    #     if container is None:
    #         text_list.append('-')
    #     else:
    #         for item in container._table:
    #             text_list.append('({}, {})'.format(item._key, item._value))
    #     text_list.append('\n')
    # print(''.join(text_list))

    # from DataStructures.sets import HozyMutableSet
    # h = HozyMutableSet()
    # for i in range(5):
    #     h.add(i)
    # k = HozyMutableSet()
    # for i in range(1,9):
    #     k.add(i)
    # print(h)
    # h |= k
    # print(h)

    # from DataStructures.maps import UnsortedTableMap
    # a = UnsortedTableMap()
    # for i in range(5):
    #     a[i] = i
    # print('SET DEFAULT')
    # for i in range(7):
    #     a.setdefault(i, 'a')
    #
    # for k in a:
    #     print(a[k])

    # from DataStructures.hash_tables import ProbeHashMap
    # a = ProbeHashMap()
    # for i in range(5):
    #     a[i] = chr(i+65)
    #
    # for i in range(7):
    #     a.setdefault(i, 'a')
    #
    # for i in a:
    #     print(i, a[i])

    # from DataStructures.hash_tables import ChainHashMap
    # a = ChainHashMap()
    # for i in range(5):
    #     a[i] = chr(i+65)
    #
    # for i in range(7):
    #     print(a.setdefault(i, 'a'))
    #
    # for i in a:
    #     print(i, a[i])

    # a = sieve_algorithm(50)
    # idx = 1
    # for i in a:
    #     if i:
    #         print(idx)
    #     idx += 1

    # from DataStructures.hash_tables import *
    # data_types = [ChainHashMap, ProbeHashMap]
    # load_factor_tester(data_types, 1000)

    # c = ChainHashMap()
    # # for i in range(23):
    # #     c[i] = i
    # # for i in range(2):
    # #     c[i] = chr(i+65)
    # # print(c._table)
    # # for i in range(23):
    # #     print(i, c[i])
    # # for i in range(23):
    # #     del c[i]
    # #     print(c._table)
    # for i in range(3):
    #     c[i] = i
    # for i in range(5):
    #     print('default', i, c.setdefault(i, 'A'))
    # for i in c:
    #     print(i, c[i])

    # a = sieve_algorithm(100)
    # idx = 1
    # target_primes = []
    # for i in a:
    #     if i:
    #         if idx%4 == 3:
    #             target_primes.append(idx)
    #     idx += 1
    # print(target_primes)
    #
    # print(-1%7)

    # from DataStructures.hash_tables import ProbeHashMap, MapBase
    # a = CustomProbeHashMap(3)
    # for i in range(200):
    #     a[i] = i
    # for i in range(200):
    #     print(a[i])

    # a = SortedMultiMap()
    # for i in range(5):
    #     for j in range(5):
    #         a.add(i, j)
    # for v in a.find_all(3):
    #     print(v)

    # from DataStructures.sorted_maps import SortedTableMap
    # s = SortedTableMap()
    # for i in range(5):
    #     s[2*i+1] = i
    # t = SortedTableMap()
    # for i in range(5):
    #     t[2*i] = i
    # double_binary_search(s, t, 5)

    # matrix = []
    # row_num = 5
    # col_num = 10
    # for i in range(row_num):
    #     array = []
    #     rand = randint(0, col_num)
    #     for j in range(rand):
    #         array.append(0)
    #     for k in range(col_num-rand):
    #         array.append(1)
    #     matrix.append(array)
    # for array in matrix:
    #     print(array)
    #
    # cnt = n_by_n_one_counter(matrix)
    # print(cnt)

    # from DataStructures.skip_lists import HozySkipList, PositionalNextBelowList
    #
    # a = HozySkipList()
    #
    # for i in range(32):
    #     j = randint(0, 100)
    #     a.skip_insert(j, j)
    #     print(a)

    # from DataStructures.sets import HozyMutableSet
    # a = HozyMutableSet()
    # b = HozyMutableSet()
    # for i in range(10):
    #     a.add(i)
    # for i in range(10):
    #     b.add(i+5)
    # c = a&b
    # print(c)

    # l = 'erform a comparative analysis that studies the collision rates for various hash codes for character strings, such as various polynomial hash codes for different values of the parameter a. Use a hash table to determine collisions, but only count collisions where different strings map to the same hash code (not if they map to the same location in this hash table). Test these hash codes on text files found on the Internet. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae aliquet lorem. Aliquam sed enim neque. Maecenas imperdiet lorem est, eget efficitur lorem suscipit sed. Praesent blandit ut quam a tempor. Curabitur faucibus, ipsum eget laoreet facilisis, augue ipsum blandit ligula, in ullamcorper est quam sed elit. Proin sit amet sapien nisi. Fusce interdum suscipit erat dapibus laoreet. Sed sodales elit nec nibh faucibus, et bibendum magna dictum. Curabitur non libero libero. Vivamus ullamcorper arcu sed bibendum fringilla. Aliquam erat volutpat. Pellentesque suscipit eu nisi tempus convallis. Sed imperdiet sapien id aliquet imperdiet. Ut non est quis sem scelerisque dictum vitae ac erat. Suspendisse at justo magna. Nulla facilisi. Etiam efficitur ut nulla in molestie. Curabitur convallis erat vitae varius eleifend. Sed placerat lorem nunc, ac cursus magna semper at. Vestibulum sit amet dui sit amet risus malesuada facilisis eu eu lectus. Morbi ornare quis arcu et congue. Phasellus sed suscipit dolor. Aenean euismod finibus velit et dignissim. Maecenas accumsan risus et mi feugiat ullamcorper. Morbi eu vehicula enim. Sed nec ipsum imperdiet nibh pharetra rhoncus. Morbi mauris dui, sollicitudin at fringilla nec, finibus ac lorem. Fusce bibendum, quam eget bibendum egestas, mi nisi varius diam, a sodales enim metus in dolor. Proin nibh nibh, fermentum quis viverra consequat, maximus at velit. Aliquam fringilla, purus vitae fermentum commodo, felis urna consequat tortor, eu sodales ex sapien vel eros. Praesent suscipit tincidunt arcu, eget egestas nibh ultricies non. Cras suscipit posuere turpis, at bibendum ligula varius quis. Donec in ipsum non erat elementum iaculis. Integer tincidunt mollis sem ac egestas. Quisque ac dui id est ultricies egestas. Phasellus et purus arcu. Maecenas eleifend consectetur massa, eu faucibus felis faucibus ac. Sed at metus tempor, vestibulum urna in, mattis arcu. Curabitur porta fermentum purus, quis elementum quam dapibus nec. Nullam mattis, ex at bibendum accumsan, leo nulla eleifend neque, ac imperdiet nunc tellus sit amet velit. Duis tristique sapien id diam gravida iaculis. In maximus mattis enim nec auctor. Integer interdum, neque et hendrerit iaculis, ex nisl varius mauris, dictum vehicula velit lacus et sapien. Ut at aliquam magna. Maecenas in sapien in risus fermentum auctor. Etiam finibus eget erat a feugiat. Cras nec tempor felis, sit amet lacinia arcu. Vestibulum augue sem, mollis sed mollis vitae, commodo eu sapien. Fusce cursus pulvinar pulvinar. Phasellus pulvinar felis at erat lobortis porta. Suspendisse pulvinar ex nunc, vitae ornare turpis pellentesque ut. Integer feugiat felis non sodales euismod. Vivamus facilisis iaculis dui a dignissim. Phasellus semper aliquam enim at ultrices. Aliquam erat volutpat. Pellentesque mattis dui eu leo pulvinar, ut scelerisque mi mattis.'
    # invert_text = invert_text(l)
    # for i in range(40):
    #     cnt = 0
    #     set = []
    #     for key in invert_text:
    #         hash_code = polynomial_hash_code(key, i+2)
    #         if hash_code in set:
    #             cnt += 1
    #         else:
    #             set.append(hash_code)
    #     print('indeterminate : {}, crash : {}'.format(i+2, cnt))

    # ps = phone_number_genertor(digit=10, max_num=10000)
    #
    # for i in range(2, 40, 3):
    #     cnt = 0
    #     set = []
    #     for phone_num in ps:
    #         hash_code = polynomial_hash_code(phone_num, i+2)
    #         if hash_code in set:
    #             cnt += 1
    #         else:
    #             set.append(hash_code)
    #     print('indeterminate : {}, crash : {}'.format(i+2, cnt))

    # # o = ProbeHashMap()
    # o = OrderDict()
    # for i in range(100):
    #     o[i] = chr(91+i)
    # for key in o:
    #     print(key, o[key])

    a = SpellChecker()
    words = ['cat', 'pat', 'mate', 'lat', 'cap', 'pal', 'gate', 'ate']
    print(a.set_words(words))
    check = a.check('amte')
    print(check)