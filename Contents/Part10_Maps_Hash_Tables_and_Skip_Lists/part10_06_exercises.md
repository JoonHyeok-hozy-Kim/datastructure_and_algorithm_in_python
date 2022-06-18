<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md">Part 10. Maps, Hash Tables, and Skip Lists</a>
</p>

### R-10.1 Give a concrete implementation of the pop method in the context of the MutableMapping class, relying only on the five primary abstract methods of that class
```python
def pop(M):
    for k in M:
        pop_key = k
    popped = M[k]
    del M[k]
    return popped
```

### R-10.2 Give a concrete implementation of the items( ) method in the context of the MutableMapping class, relying only on the five primary abstract methods of that class. What would its running time be if directly applied to the UnsortedTableMap subclass?
```python
def items(M):
    result = []
    for k in M:
        result.append((k, M[k]))
    return result
```
* Sol.) O(n^2) running time for UnsortedTableMap subclass.
  * why?)
    * For loop in the items() method will run n times.
    * \_\_getitem__ method will run i-times where i is the index that i-th key is located in self._table

### R-10.3 Give a concrete implementation of the items( ) method directly within the UnsortedTableMap class, ensuring that the entire iteration runs in O(n) time.
```python
def items(self):
    result = []
    idx = 0
    for k in self:
        result.append((k, self._table[idx]))
        idx += 1
    return result
```

### R-10.4 What is the worst-case running time for inserting n key-value pairs into an initially empty map M that is implemented with the UnsortedTableMap class?
* Sol.) O(n^2) running time in the worst case
  * why?)
    * for the k-th insertion, \_\_setitem__ method will traverse self._table, which takes O(k-1) time.
    * Thus, the sum of all the n insertions will take n*(n+1)/2 operations.
    * Therefore, O(n^2) running time.

### R-10.5 Reimplement the UnsortedTableMap class from Section 10.1.5, using the PositionalList class from Section 7.4 rather than a Python list.
```python
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
```

### R-10.6 Which of the hash table collision-handling schemes could tolerate a load factor above 1 and which could not?
* Sol.)
  * Seperate Chaning tolerates its load factor to be above 1.
  * Open Addressing's load factor is at most 1.

### R-10.7 Our Position classes for lists and trees support the eq method so that two distinct position instances are considered equivalent if they refer to the same underlying node in a structure. For positions to be allowed as keys in a hash table, there must be a definition for the hash method that is consistent with this notion of equivalence. Provide such a hash method.
* Sol.) Use the id of the position's node as hash value.
```python
from DataStructures.linked_list import _DoublyLinkedBase
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

        def __hash__(self):
            return id(self._node)
```
```python
if __name__ == '__main__':
    from DataStructures.hash_tables import ChainHashMap
    from DataStructures.linked_list import PositionalList
    l = PositionalList()
    for i in range(5):
        l.add_last(i)

    # Insert elements of l into a with positions as keys
    a = ChainHashMap()
    walk = l.first()
    while walk is not None:
        a[walk] = walk.element()
        walk = l.after(walk)

    # Insert elements of l into b with positions as keys
    b = ChainHashMap()
    walk = l.first()
    while walk is not None:
        b[walk] = walk.element()
        walk = l.after(walk)

    print('a == b : {}'.format(a == b))

    # Make another Positional list with identical values
    m = PositionalList()
    for i in range(5):
        m.add_last(i)

    # Insert elements of m into c with positions as keys
    c = ChainHashMap()
    walk = m.first()
    while walk is not None:
        c[walk] = walk.element()
        walk = m.after(walk)

    print('a == c : {}'.format(a == c))

    # Change l
    l.add_last(99)

    # Insert elements of l' into d with positions as keys
    d = ChainHashMap()
    walk = l.first()
    while walk is not None:
        d[walk] = walk.element()
        walk = l.after(walk)

    print('a == d : {}'.format(a == c))
```

### R-10.8 What would be a good hash code for a vehicle identification number that is a string of numbers and letters of the form “9X9XX99X9XX999999,” where a “9” represents a digit and an “X” represents a letter?
* Sol.) Use ord function to make characters in to numbers and concatenate every number in str form. Finally make them int form and return the result.
```python
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
    a = random_id_generator(20)
    # a = generate_all_id()
    test = hashed_id_tester(a)
    print(test[0])
```



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md">Part 10. Maps, Hash Tables, and Skip Lists</a>
</p>