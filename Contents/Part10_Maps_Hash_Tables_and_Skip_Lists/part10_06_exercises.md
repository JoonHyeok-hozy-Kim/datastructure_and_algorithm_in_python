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



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md">Part 10. Maps, Hash Tables, and Skip Lists</a>
</p>