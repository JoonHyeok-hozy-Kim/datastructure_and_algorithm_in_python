<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/part05_array_based_sequences.md">Part 5. Array-Based Sequences</a>
</p>

### R-5.1. Execute the experiment from Code Fragment 5.1 and compare the results on your system to those we report in Code Fragment 5.2.
```python
import sys
n = 10
data = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
```

### R-5.2. In Code Fragment 5.1, we perform an experiment to compare the length of a Python list to its underlying memory usage. Determining the sequence of array sizes requires a manual inspection of the output of that program. Redesign the experiment so that the program outputs only those values of k at which the existing capacity is exhausted.
```python
import sys
n = 100
data = []
byte_tracker = 0
byte_change_list = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    if b > byte_tracker and k > 0:
        byte_tracker = b
        byte_change_list.append(a-1)
    data.append(None)
print(byte_change_list)
```

### R-5.3. Modify the experiment from Code Fragment 5.1 in order to demonstrate that Python’s list class occasionally shrinks the size of its underlying array when elements are popped from a list. 
```python
import sys
initial_elements_count = 200
data = [None] * initial_elements_count
for k in range(initial_elements_count):
    a = len(data)
    b = sys.getsizeof(data)
    data.pop()
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
```

### R-5.4. Our DynamicArray class, as given in Code Fragment 5.3, does not support use of negative indices with getitem . Update that method to better match the semantics of a Python list.
```python
def __getitem__(self, k):
    if not self._n * (-1) <= k < self._n:
        raise IndexError('invalid index')
    # R-5.4
    if k < 0:
        return self._A[self._n + k]
    return self._A[k]
```












<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/part05_array_based_sequences.md">Part 5. Array-Based Sequences</a>
</p>