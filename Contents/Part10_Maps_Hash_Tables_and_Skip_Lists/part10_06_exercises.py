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

    a = random_id_generator(20)
    # a = generate_all_id()
    test = hashed_id_tester(a)
    print(test[0])