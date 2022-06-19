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
        reversed_load_factor = int(pow(self._load_factor, -1))
        if self._n > len(self._table) // reversed_load_factor:
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






<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md">Part 10. Maps, Hash Tables, and Skip Lists</a>
</p>