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

### R-10.9 Draw the 11-entry hash table that results from using the hash function, h(i)=(3i+5) mod 11, to hash the keys 12, 44, 13, 88, 23, 94, 11, 39, 20, 16, and 5, assuming collisions are handled by chaining.
```python
l = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
separate_chained = []
for i in l:
    hash_code = (3*i+5)%11
    insert_flag = False
    for bucket in separate_chained:
        if bucket[0] == hash_code:
            bucket[1].append(i)
            insert_flag = True
            break
    if not insert_flag:
        separate_chained.append((hash_code, [i]))
for bucket in separate_chained:
    print(bucket)
```

### R-10.10 What is the result of the previous exercise, assuming collisions are handled by linear probing?
```python
from DataStructures.hash_tables import HashMapBase
class CollsionHashMap(HashMapBase):
    def _hash_function(self, k):
        return (3*k+5)%11

class CollisionProbeHashMap(CollsionHashMap):
    _AVAIL = object()       # sentinel marks locations of previous deletions

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is CollisionProbeHashMap._AVAIL

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
            j = (j+1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = CollisionProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

if __name__ == '__main__':
    l = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    p = CollisionProbeHashMap()
    for i in l:
        p[i] = i
    for item in p._table:
        if item is None:
            print('None')
        else:
            print('hash_code : {}, key : {}, value : {}'.format( (3*item._key+5)%11, item._key, item._value))
```

### R-10.11 Show the result of Exercise R-10.9, assuming collisions are handled by quadratic probing, up to the point where the method fails.
* Implementation of Quadratic Probing
```python
from DataStructures.hash_tables import ProbeHashMap
class QuadraticProbeHashMap(ProbeHashMap):
    def _find_slot(self, j, k):
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
```
* Comparison between Linear and Quadratic Probing
```python
class CollisionQuadraticProbeHashMap(CollisionProbeHashMap):
    def _find_slot(self, j, k):
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

if __name__ == '__main__':
    l = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    p = CollisionProbeHashMap()
    for i in l:
        p[i] = i
    text_list = ['---------------------Linear Probing----------------------\n']
    for item in p._table:
        if item is None:
            text_list.append('-')
        else:
            text_list.append('(h : {}, k : {}, v : {})'.format( (3*item._key+5)%11, item._key, item._value))
    print(' '.join(text_list))

    p = CollisionQuadraticProbeHashMap()
    for i in l:
        p[i] = i
    text_list = ['---------------------Quadratic Probing----------------------\n']
    for item in p._table:
        if item is None:
            text_list.append('-')
        else:
            text_list.append('(h : {}, k : {}, v : {})'.format( (3*item._key+5)%11, item._key, item._value))
    print(' '.join(text_list))
```

### R-10.12 What is the result of Exercise R-10.9 when collisions are handled by double hashing using the secondary hash function h'(k) = 7−(k mod 7)?
* Sol.)
```python
class CollisionDoubleHashMap(CollisionProbeHashMap):

    def _double_hash(self, j, k, i):
        q = 7  # Set arbitrarily
        double_hash_formula = (q - (k % q)) * i
        return (j + double_hash_formula) % len(self._table)

    def _find_slot(self, j, k):
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

if __name__ == '__main__':
    l = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    p = CollisionProbeHashMap()
    for i in l:
        p[i] = i
    text_list = ['---------------------Linear Probing----------------------\n']
    for item in p._table:
        if item is None:
            text_list.append('-')
        else:
            text_list.append('(h : {}, k : {}, v : {})'.format( (3*item._key+5)%11, item._key, item._value))
    print(' '.join(text_list))

    p = CollisionDoubleHashMap()
    for i in l:
        p[i] = i
    text_list = ['---------------------Quadratic Probing----------------------\n']
    for item in p._table:
        if item is None:
            text_list.append('-')
        else:
            text_list.append('(h : {}, k : {}, v : {})'.format( (3*item._key+5)%11, item._key, item._value))
    print(' '.join(text_list))
```

### R-10.13 What is the worst-case time for putting n entries in an initially empty hash table, with collisions resolved by chaining? What is the best case?
* Sol.)
  * Worst Case
    * Regarding the amortization of resizing, O(n^2) running time is expected.
      * why?) Consider the case that every entry share the same key.
        * Then i-th insertion may traverse (i-1) element in the target bucket's container.
        * Sum of such insertions may be n(n+1)/2
  * Best Case
    * If every element have distinctive keys, insertion may run in O(n) time.

### R-10.14 Show the result of rehashing the hash table shown in Figure 10.6 into a table of size 19 using the new hash function h(k) = 3k mod 17.
```python
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

if __name__ == '__main__':
    r = CollisionChainHashMapNew(cap=17)
    l = [54, 28, 41, 18, 10, 36, 25, 38, 12, 90]
    for i in l:
        r[i] = i
    text_list = []
    for container in r._table:
        if container is None:
            text_list.append('-')
        else:
            for item in container._table:
                text_list.append('({}, {})'.format(item._key, item._value))
        text_list.append('\n')
    print(''.join(text_list))
```

### R-10.15 Our HashMapBase class maintains a load factor λ ≤ 0.5. Reimplement that class to allow the user to specify the maximum load, and adjust the concrete subclasses accordingly.
* Sol.) Get load_factor as an input parameter for __init__ method.
  * Use reversed number of this load_factor for resizing.
```python
class HashMapBase(MapBase):

    def __init__(self, cap=11, p=109345121, load_factor=0.5):
        # skip
        self._load_factor = load_factor         # user-defined load_factor setting by R-10.15

    # skip
    
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)

        # load_factor customization by R-10.15
        reversed_load_factor = int(pow(self._load_factor, -1)) if int(pow(self._load_factor, -1)) > 1 else 2
        if self._n > len(self._table) * self._load_factor:
            self._resize(reversed_load_factor * len(self._table) - 1)
    
    # skip
```

### R-10.16 Give a pseudo-code description of an insertion into a hash table that uses quadratic probing to resolve collisions, assuming we also use the trick of replacing deleted entries with a special “deactivated entry” object.
* Sol.) Already implemented in <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_06_exercises.md#r-1011-show-the-result-of-exercise-r-109-assuming-collisions-are-handled-by-quadratic-probing-up-to-the-point-where-the-method-fails">R-10.11</a>

### R-10.17 Modify our ProbeHashMap to use quadratic probing.
* Sol.) Already implemented in <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_06_exercises.md#r-1011-show-the-result-of-exercise-r-109-assuming-collisions-are-handled-by-quadratic-probing-up-to-the-point-where-the-method-fails">R-10.11</a>

### R-10.18 Explain why a hash table is not suited to implement a sorted map.
* Sol.)
  * Since hash function only cares the 1 to 1 relation between keys and integers, size comparison of keys is not consistent with the size comparison of hash codes.
  * Thus, the sequence that items are located in the bucket array of hash table is not consistent with the order of size of elements.
  * Recall that increasing order of keys is the key factor that allows indexing of elements.
  * Hash function cannot support such operations.

### R-10.19 Describe how a sorted list implemented as a doubly linked list could be used to implement the sorted map ADT.
* Sol.) If each position in the doubly linked list contains item instance with key and value, it can perfectly perform like a sorted map.

### R-10.20 What is the worst-case asymptotic running time for performing n deletions from a SortedTableMap instance that initially contains 2n entries?
* Sol.)
  * It will take O(log(n)) running time for finding the index of the target item.
  * Considering the fact that SortedMap uses array as its data_table, it will take O(n) time for swapping all the elements after the target item.
  * Therefore, n deletions may take O(n^2 log(2)) running time in the worst case.

### R-10.21 Consider the following variant of the find index method from Code Fragment 10.8, in the context of the SortedTableMap class:
```python
def _find_index(self, k, high, low):
    if high < low:
        return high + 1
    else:
        mid = (low + high) // 2
        if self._table[mid]._key < k:
            return self._find_index(k, mid+1, high)
        else:
            return self._find_index(k, low, mid-1)
```
#### Does this always produce the same result as the original version? Justify your answer.
* Sol.) No.
  * When "self._table[mid]._key == k" is satisfied, _find_index method will not return the index of mid.
  * Thus, in most cases, the method will return wrong indecies.

### R-10.22 What is the expected running time of the methods for maintaining a maxima set if we insert n pairs such that each pair has lower cost and performance than one before it? What is contained in the sorted map at the end of this series of operations? What if each pair had a lower cost and higher performance than the one before it?
* Sol.) ???

### R-10.23 Draw an example skip list S that results from performing the following series of operations on the skip list shown in Figure 10.13: del S[38], S[48] = x , S[24] = y , del S[55]. Record your coin flips, as well.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_04_03_removal.png" style="height: 300px;"></img><br/>
</p>
* Sol.)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_06_23.png" style="height: 150px;"></img><br/>
</p>

```python
from random import randint
def coin_flip():
    cnt = -1
    coin = 0
    while coin == 0:
        cnt += 1
        coin = randint(0, 1)
    return cnt
```

### R-10.24 Give a pseudo-code description of the delitem map operation when using a skip list.
```python
Algorithm SkipDelete(k):
    Input: Key k
    Output: None

    p = start {begin at start position}
    while below(p) != None do
        p = below(p) {drop down}
        while k >= key(next(p)) do
            p = next(p) {scan forward}
        if k == key(p):
            below_p = below(p)
            deleteItem(p)
            p = below_p
    return
```

### R-10.25 Give a concrete implementation of the pop method, in the context of a MutableSet abstract base class, that relies only on the five core set behaviors described in Section 10.5.2.
```python
def pop(self):
    if len(self) == 0:
        raise KeyError
    v = None
    for e in self:
        if e is not None:
            v = e
    self.discard(v)
    return v
```

### R-10.26 Give a concrete implementation of the isdisjoint method in the context of the MutableSet abstract base class, relying only on the five primary abstract methods of that class. Your algorithm should run in O(min(n,m)) where n and m denote the respective cardinalities of the two sets.
```python
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
```

### R-10.27 What abstraction would you use to manage a database of friends’ birthdays in order to support efficient queries such as “find all friends whose birthday is today” and “find the friend who will be the next to celebrate a birthday”?
* Sol.) Sorted map with birthday as key that uses separate chaining for collisions.
  * It supports multiple friends with identical birthdays.
  * \_\_eq__ and \_\_gt__ method will support the given operations.

### C-10.28 On page 406 of Section 10.1.3, we give an implementation of the method setdefault as it might appear in the MutableMapping abstract base class. While that method accomplishes the goal in a general fashion, its efficiency is less than ideal. In particular, when the key is new, there will be a failed search due to the initial use of getitem , and then a subsequent insertion via setitem . For a concrete implementation, such as the UnsortedTableMap, this is twice the work because a complete scan of the table will take place during the failed getitem , and then another complete scan of the table takes place due to the implementation of setitem . A better solution is for the UnsortedTableMap class to override setdefault to provide a direct solution that performs a single search. Give such an implementation of UnsortedTableMap.setdefault.
* Implementation
```python
def setdefault(self, k, d):
    walk = self._table.first()
    while walk is not None:
        if walk.element()._key == k:
            return walk.element()._value
        walk = self._table.after(walk)
    self._table.add_last(self._Item(k, d))
    return d
```
* Test
```python
from DataStructures.maps import UnsortedTableMap
a = UnsortedTableMap()
for i in range(5):
    a[i] = i
print('SET DEFAULT')
for i in range(7):
    a.setdefault(i, 'a')

for k in a:
    print(a[k])
```

### C-10.29 Repeat Exercise C-10.28 for the ProbeHashMap class.
* Implementation
```python
class HashMapBase(MapBase):
    # Skip
    def setdefault(self, k, d):
        j = self._hash_function(k)
        return self._bucket_setdefault(j, k, d)

class ProbeHashMap(HashMapBase):
    # Skip
    def _bucket_setdefault(self, j, k, d):
        found, s = self._find_slot(j, k)
        if found:
            return self._table[s]._value
        else:
            self._table[s] = self._Item(k, d)
            return d
```
* Test
```python
from DataStructures.hash_tables import ProbeHashMap
a = ProbeHashMap()
for i in range(5):
    a[i] = chr(i+65)

for i in range(7):
    a.setdefault(i, 'a')

for i in a:
    print(i, a[i])
```

### C-10.30 Repeat Exercise C-10.28 for the ChainHashMap class.
* Implementation
```python
class ChainHashMap(HashMapBase):
    # Skip
    def _bucket_setdefault(self, j, k, d):
        if self._table[j] is not None:
            return self._table[j].setdefault(k, d)
        else:
            self._bucket_setitem(j, k, d)
            return d
```
* Test
```python
from DataStructures.hash_tables import ChainHashMap
a = ChainHashMap()
for i in range(5):
    a[i] = chr(i+65)

for i in range(7):
    print(a.setdefault(i, 'a'))

for i in a:
    print(i, a[i])
```

### C-10.31 For an ideal compression function, the capacity of the bucket array for a hash table should be a prime number. Therefore, we consider the problem of locating a prime number in a range [M,2M]. Implement a method for finding such a prime by using the __sieve algorithm__. In this algorithm, we allocate a 2M cell Boolean array A, such that cell i is associated with the integer i. We then initialize the array cells to all be “true” and we “mark off” all the cells that are multiples of 2, 3, 5, 7, and so on. This process can stop after it reaches a number larger than √(2M). (Hint: Consider a bootstrapping method for finding the primes up to √(2M).)
```python
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

if __name__ == '__main__':
    a = sieve_algorithm(50)
    idx = 1
    for i in a:
        if i:
            print(idx)
        idx += 1
```

### C-10.32 Perform experiments on our ChainHashMap and ProbeHashMap classes to measure its efficiency using random key sets and varying limits on the load factor (see Exercise R-10.15).
```python
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

if __name__ == '__main__':
    from DataStructures.hash_tables import *
    data_types = [ChainHashMap, ProbeHashMap]
    load_factor_tester(data_types, 1000)
```

### C-10.33 Our implementation of separate chaining in ChainHashMap conserves memory by representing empty buckets in the table as None, rather than as empty instances of a secondary structure. Because many of these buckets will hold a single item, a better optimization is to have those slots of the table directly reference the Item instance, and to reserve use of secondary containers for buckets that have two or more items. Modify our implementation to provide this additional optimization.
```python
class OptimizedChainHashMap(HashMapBase):

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
            if type(self._table[j]) == self._Item:
                if self._table[j]._key == k:
                    return self._table[j]._value
                else:
                    item = self._table[j]
                    self._table[j] = UnsortedTableMap()
                    self._table[j][item._key] = item._value
                    self._table[j][k] = d
                    self._n += 1
            else:
                return self._table[j].setdefault(k, d)
        else:
            self._bucket_setitem(j, k, d)
            return d
```

### C-10.34 Computing a hash code can be expensive, especially for lengthy keys. In our hash table implementations, we compute the hash code when first inserting an item, and recompute each item’s hash code each time we resize our table. Python’s dict class makes an interesting trade-off. The hash code is computed once, when an item is inserted, and the hash code is stored as an extra field of the item composite, so that it need not be recomputed. Reimplement our HashTableBase class to use such an approach.
```python
class HashTableBase(HashMapBase):

    class _Item(MapBase._Item):
        def __init__(self, k, v, h=None):
            super().__init__(k, v)
            self._hash_code = h

    ### Assume that hash_code is inserted into _Item instance in __setitem__ method

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v, h) in old:
            self._table[h] = self._Item(k, v, h)
```

### C-10.35 Describe how to perform a removal from a hash table that uses linear probing to resolve collisions where we do not use a special marker to represent deleted elements. That is, we must rearrange the contents so that it appears that the removed entry was never inserted in the first place
* Sol.) Suppose we make an entry of list that contains the removed hash_codes.
  * Each time _find_slot method runs, if the newly computed hash_code is bigger than k elements in the removed list, deduct k from the result calculated hash_code.
  * It will make hash_code shift k slots so that the removed space will be considered counting space.

### C-10.36 The quadratic probing strategy has a clustering problem related to the way it looks for open slots. Namely, when a collision occurs at bucket h(k), it checks buckets A[(h(k) +i^2) mod N], for i = 1,2,...,N −1.
#### a. Show that i^2 mod N will assume at most (N + 1)/2 distinct values, for N prime, as i ranges from 1 to N − 1. As a part of this justification, note that i^2 mod N = (N−i)^2 mod N for all i.
* Sol.)
  * Firstly, consider that "(N-i)^2 = N^2 - 2iN + i^2 = N(N-2i) + i^2"
  * Thus, (N-i)^2 mod N = i^2 mod N. (A)
  * Let k an integer such that k = N//2.
  * Then, by (A), we may assume that pair of integers {j , N-j} share identical value of i^2 mod N where j = 1, 2, ... k
  * Thus, if N is even then it may have N/2 distinct values of i^2 mod N and (N+1)/2 for odd case.
  * Therefore, i^2 mod N has at most (N+1)/2 distinct values.

#### b. A better strategy is to choose a prime N such that N mod 4 = 3 and then to check the buckets A[(h(k) ± i^2) mod N] as i ranges from 1 to (N − 1)/2, alternating between plus and minus. Show that this alternate version is guaranteed to check every bucket in A.
* Sol.)
  * Recall that i^2 mod N can have at most (N+1)/2 distinct values.
  * By limiting N into a prime number such that N%4 == 3, N is guaranteed to be an odd number.
  * By the property proven in the problem a, there will be (N-1)/2 distinct values of i^2 mod N.
  * The rest can be achieved by reversing the sign like N-i^2 mod N.

### C-10.37 Refactor our ProbeHashMap design so that the sequence of secondary probes for collision resolution can be more easily customized. Demonstrate your new framework by providing separate concrete subclasses for linear probing and quadratic probing.
```python
class ProbeHashMap(HashMapBase):
    _AVAIL = object()       # sentinel marks locations of previous deletions

    def __init__(self, linear_unit=1):
        super().__init__()
        if linear_unit >= len(self._table):
            raise ValueError('Linear unit cannot be larger than the capacity.')
        self._linear_unit = linear_unit

    # skip

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
```

### C-10.38 Design a variation of binary search for performing the multimap operation find all(k) implemented with a sorted search table that includes duplicates, and show that it runs in time O(s+logn), where n is the number of elements in the dictionary and s is the number of items with given key k.
* Implementation : Used SortedTableMap as the _map member in order to take advantage of binary search for keys.
```python
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
```
* Test
```python
a = SortedMultiMap()
for i in range(5):
    for j in range(5):
        a.add(i, j)
for v in a.find_all(3):
    print(v)
```

### C-10.39 Although keys in a map are distinct, the binary search algorithm can be applied in a more general setting in which an array stores possibly duplicative elements in non-decreasing order. Consider the goal of identifying the index of the leftmost element with key greater than or equal to given k. Does the find index method as given in Code Fragment 10.8 guarantee such a result? Does the find index method as given in Exercise R-10.21 guarantee such a result? Justify your answers.
* Sol.) If duplicated values are in a set, O(log(n)) performance of binary search is not guaranteed.
  * Since we are targeting the leftmost element of the duplicated value, if the "mid" value came to be the rightmost element during the binary search, it will incur traversing all the way to the leftmost position.

### C-10.40 Suppose we are given two sorted search tables S and T, each with n entries (with S and T being implemented with arrays). Describe an O(log2 n)-time algorithm for finding the kth smallest key in the union of the keys from S and T (assuming no duplicates).
```python
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

if __name__ == '__main__':
    from DataStructures.sorted_maps import SortedTableMap
    s = SortedTableMap()
    for i in range(5):
        s[2*i+1] = i
    t = SortedTableMap()
    for i in range(5):
        t[2*i] = i
    double_binary_search(s, t, 5)
```

### C-10.41 Give an O(logn)-time solution for the previous problem.
* Sol.)

### C-10.42 Suppose that each row of an n×n array A consists of 1’s and 0’s such that, in any row of A, all the 1’s come before any 0’s in that row. Assuming A is already in memory, describe a method running in O(nlogn) time (not O(n2) time!) for counting the number of 1’s in A.
```python
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

if __name__ == '__main__':
    matrix = []
    row_num = 5
    col_num = 10
    for i in range(row_num):
        array = []
        rand = randint(0, col_num)
        for j in range(rand):
            array.append(0)
        for k in range(col_num-rand):
            array.append(1)
        matrix.append(array)
    for array in matrix:
        print(array)

    cnt = n_by_n_one_counter(matrix)
    print(cnt)
```

### C-10.43 Given a collection C of n cost-performance pairs (c, p), describe an algorithm for finding the maxima pairs of C in O(nlogn) time.
* Sol.) One might achieve O(nlog(n)) running time by using SkipList.
  * Putting c as the key and p as the value of the _Item instance, one can search and replace non-maxima elements in O(log(n)).
  * Thus, the total running time will be O(nlog(n)).

### C-10.44 Show that the methods above(p) and prev(p) are not actually needed to efficiently implement a map using a skip list. That is, we can implement insertions and deletions in a skip list using a strictly top-down, scan-forward approach, without ever using the above or prev methods. (Hint: In the insertion algorithm, first repeatedly flip the coin to determine the level where you should start inserting the new entry.)
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/skip_lists.py#L100">Skip List</a>

### C-10.45 Describe how to modify a skip-list representation so that index-based operations, such as retrieving the item at index j, can be performed in O(logn) expected time.
* Sol.) By making _Items with index as the key and storing data in the SkipList, the search operation of i-th data will take O(log(n)).

### C-10.46 For sets S and T, the syntax SˆT returns a new set that is the symmetric difference, that is, a set of elements that are in precisely one of S or T. This syntax is supported by the special xor method. Provide an implementation of that method in the context of the MutableSet abstract base class, relying only on the five primary abstract methods of that class.
* Implementation
```python
def __xor__(self, other):
    result = type(self)()
    for e in self:
        if e not in other:
            result.add(e)
    for e in other:
        if e not in self:
            result.add(e)
    return result
```
* Test
```python
from DataStructures.sets import HozyMutableSet
a = HozyMutableSet()
b = HozyMutableSet()
for i in range(10):
    a.add(i)
for i in range(10):
    b.add(i+5)
c = a^b
print(c)
```

### C-10.47 In the context of the MutableSet abstract base class, describe a concrete implementation of the and method, which supports the syntax S&T for computing the intersection of two existing sets
* Implementation
```python
def __and__(self, other):
  result = type(self)()
  for e in self:
      if e in other:
          result.add(e)
  return result
```
* Test
```python
from DataStructures.sets import HozyMutableSet
a = HozyMutableSet()
b = HozyMutableSet()
for i in range(10):
    a.add(i)
for i in range(10):
    b.add(i+5)
c = a&b
print(c)
```

### C-10.48 An inverted file is a critical data structure for implementing a search engine or the index of a book. Given a document D, which can be viewed as an unordered, numbered list of words, an inverted file is an ordered list of words, L, such that, for each word w in L, we store the indices of the places in D where w appears. Design an efficient algorithm for constructing L from D.
```python
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
        s[raw_word_list[i]] = i
    return s

if __name__ == '__main__':
    l = 'Lorem Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas gravida congue odio, vel sollicitudin neque sagittis nec. Integer iaculis consectetur ornare. Mauris aliquet ante eu ante aliquet, eu facilisis mauris auctor. Suspendisse rhoncus, mi a ornare iaculis, ipsum urna auctor ex, viverra aliquam felis elit elementum eros. Morbi tincidunt ligula pharetra pretium malesuada. Aenean vel fermentum est. Morbi non risus sed velit mattis imperdiet. Phasellus ut erat ut elit mattis commodo quis et lacus. Praesent velit urna, dapibus nec purus sit amet, tristique fermentum lacus. Donec efficitur nisi sed ante tempor finibus. Praesent vel ultrices neque, sed consectetur leo. Mauris congue vestibulum vulputate. Duis sit amet consequat nisi. In quam nisi, sollicitudin id tincidunt et, convallis non arcu. Etiam ac elementum enim. In convallis, lorem in efficitur tempor, orci metus porttitor massa, ac porttitor nisl elit sit amet lacus.'
    i = invert_text(l)
    for key in i:
        print(key, i[key])

    l_s = l.split(' ')
    print(l_s[24], l_s[26], l_s[90])
```

### C-10.49 Python’s collections module provides an OrderedDict class that is unrelated to our sorted map abstraction. An OrderedDict is a subclass of the standard hash-based dict class that retains the expected O(1) performance for the primary map operations, but that also guarantees that the iter method reports items of the map according to first-in, first-out (FIFO) order. That is, the key that has been in the dictionary the longest is reported first. (The order is unaffected when the value for an existing key is overwritten.) Describe an algorithmic approach for achieving such performance.
* Sol.) By maintaining the properties of the map class and additionally add one more entity for the _Item class, _next, which may store reference to the next item, we might be able to achieve FIFO order of iteration.

### P-10.50 Perform a comparative analysis that studies the collision rates for various hash codes for character strings, such as various polynomial hash codes for different values of the parameter a. Use a hash table to determine collisions, but only count collisions where different strings map to the same hash code (not if they map to the same location in this hash table). Test these hash codes on text files found on the Internet.
```python
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

if __name__ == '__main__':
    l = 'perform a comparative analysis that studies the collision rates for various hash codes for character strings, such as various polynomial hash codes for different values of the parameter a. Use a hash table to determine collisions, but only count collisions where different strings map to the same hash code (not if they map to the same location in this hash table). Test these hash codes on text files found on the Internet. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae aliquet lorem. Aliquam sed enim neque. Maecenas imperdiet lorem est, eget efficitur lorem suscipit sed. Praesent blandit ut quam a tempor. Curabitur faucibus, ipsum eget laoreet facilisis, augue ipsum blandit ligula, in ullamcorper est quam sed elit. Proin sit amet sapien nisi. Fusce interdum suscipit erat dapibus laoreet. Sed sodales elit nec nibh faucibus, et bibendum magna dictum. Curabitur non libero libero. Vivamus ullamcorper arcu sed bibendum fringilla. Aliquam erat volutpat. Pellentesque suscipit eu nisi tempus convallis. Sed imperdiet sapien id aliquet imperdiet. Ut non est quis sem scelerisque dictum vitae ac erat. Suspendisse at justo magna. Nulla facilisi. Etiam efficitur ut nulla in molestie. Curabitur convallis erat vitae varius eleifend. Sed placerat lorem nunc, ac cursus magna semper at. Vestibulum sit amet dui sit amet risus malesuada facilisis eu eu lectus. Morbi ornare quis arcu et congue. Phasellus sed suscipit dolor. Aenean euismod finibus velit et dignissim. Maecenas accumsan risus et mi feugiat ullamcorper. Morbi eu vehicula enim. Sed nec ipsum imperdiet nibh pharetra rhoncus. Morbi mauris dui, sollicitudin at fringilla nec, finibus ac lorem. Fusce bibendum, quam eget bibendum egestas, mi nisi varius diam, a sodales enim metus in dolor. Proin nibh nibh, fermentum quis viverra consequat, maximus at velit. Aliquam fringilla, purus vitae fermentum commodo, felis urna consequat tortor, eu sodales ex sapien vel eros. Praesent suscipit tincidunt arcu, eget egestas nibh ultricies non. Cras suscipit posuere turpis, at bibendum ligula varius quis. Donec in ipsum non erat elementum iaculis. Integer tincidunt mollis sem ac egestas. Quisque ac dui id est ultricies egestas. Phasellus et purus arcu. Maecenas eleifend consectetur massa, eu faucibus felis faucibus ac. Sed at metus tempor, vestibulum urna in, mattis arcu. Curabitur porta fermentum purus, quis elementum quam dapibus nec. Nullam mattis, ex at bibendum accumsan, leo nulla eleifend neque, ac imperdiet nunc tellus sit amet velit. Duis tristique sapien id diam gravida iaculis. In maximus mattis enim nec auctor. Integer interdum, neque et hendrerit iaculis, ex nisl varius mauris, dictum vehicula velit lacus et sapien. Ut at aliquam magna. Maecenas in sapien in risus fermentum auctor. Etiam finibus eget erat a feugiat. Cras nec tempor felis, sit amet lacinia arcu. Vestibulum augue sem, mollis sed mollis vitae, commodo eu sapien. Fusce cursus pulvinar pulvinar. Phasellus pulvinar felis at erat lobortis porta. Suspendisse pulvinar ex nunc, vitae ornare turpis pellentesque ut. Integer feugiat felis non sodales euismod. Vivamus facilisis iaculis dui a dignissim. Phasellus semper aliquam enim at ultrices. Aliquam erat volutpat. Pellentesque mattis dui eu leo pulvinar, ut scelerisque mi mattis.'
    invert_text = invert_text(l)
    for i in range(40):
        cnt = 0
        set = []
        for key in invert_text:
            hash_code = polynomial_hash_code(key, i+2)
            if hash_code in set:
                cnt += 1
            else:
                set.append(hash_code)
        print('indeterminate : {}, crash : {}'.format(i+2, cnt))
```

### P-10.51 Perform a comparative analysis as in the previous exercise, but for 10-digit telephone numbers instead of character strings.
```python
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

if __name__ == '__main__':
    ps = phone_number_genertor(digit=10, max_num=10000)

    for i in range(2, 40, 3):
        cnt = 0
        set = []
        for phone_num in ps:
            hash_code = polynomial_hash_code(phone_num, i+2)
            if hash_code in set:
                cnt += 1
            else:
                set.append(hash_code)
        print('indeterminate : {}, crash : {}'.format(i+2, cnt))
```

### P-10.52 Implement an OrderedDict class, as described in Exercise C-10.49, ensuring that the primary map operations run in O(1) expected time.
```python
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


if __name__ == '__main__':
    o = OrderDict()
    for i in range(100):
        o[i] = chr(91+i)
    for key in o:
        print(key, o[key])
```

### P-10.53 Design a Python class that implements the skip-list data structure. Use this class to create a complete implementation of the sorted map ADT.
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/skip_lists.py">Skip List</a>

### P-10.54 Extend the previous project by providing a graphical animation of the skip-list operations. Visualize how entries move up the skip list during insertions and are linked out of the skip list during removals. Also, in a search operation, visualize the scan-forward and drop-down actions.
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/skip_lists.py">Skip List</a>

### P-10.55 Write a spell-checker class that stores a lexicon of words, W, in a Python set, and implements a method, check(s), which performs a spell check on the string s with respect to the set of words, W. If s is in W, then the call to check(s) returns a list containing only s, as it is assumed to be spelled correctly in this case. If s is not in W, then the call to check(s) returns a list of every word in W that might be a correct spelling of s. Your program should be able to handle all the common ways that s might be a misspelling of a word in W, including swapping adjacent characters in a word, inserting a single character in between two adjacent characters in a word, deleting a single character from a word, and replacing a character in a word with another character. For an extra challenge, consider phonetic substitutions as well.
```python
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
    a = SpellChecker()
    words = ['cat', 'pat', 'mate', 'lat', 'cap', 'pal', 'gate', 'ate']
    print(a.set_words(words))
    check = a.check('amte')
    print(check)
```






<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md">Part 10. Maps, Hash Tables, and Skip Lists</a>
</p>