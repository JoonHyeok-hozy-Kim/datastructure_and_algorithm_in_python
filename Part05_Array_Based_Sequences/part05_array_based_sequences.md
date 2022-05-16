<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 5. Array-Based Sequences
## 5.1 Python's Sequence Types

* Point
  * _list_, _tuple_, and _str_ class may look similar.
  * However, the ways that instances of these classes are represented internally in Python differ.
    * It may go against _encapsulation_ of OOD -- a user does not have to know how each class works internally.
    * But the efficiency of a program depends greatly on it.
      * _asymptotic analysis_ will be used for analyzing the efficiency.

## 5.2 Low-Level Arrays
### Concepts)
#### byte
  * a typical unit that groups bits, which contain information.
#### memory address
  * an abstraction that computer uses in order to keep track of what information is stored in what byte.
  * Each byte of memory is associated with a unique number that servers as its address (binarily represented).
#### random access memory (RAM)
  * Despite the sequential nature of the numbering system, computer hardware is designed, in theory, so that any byte of the main memory can be efficiently accessed based upon its memory address.
  * i.e.) Any individual byte of memory can be stored or retrieved in O(1) time.
#### array
  * a representation that a group of related variables can be stored one after another in a contiguous portion of the computer's memory.
  * ex) a string class instance 'SAMPLE' is stored in 12 consecutive bytes of memory.
    * why?) In Python each Unicode character is represented with 16 bits (=2 Bytes). Thus, 6 characters take 12 Bytes.
#### cell
  * each location within an array
  * Prop.) Each cell of an array must use the same number of bytes so that _constant time spent on accessing an arbitrary cell based on its index_ is secured.
#### index
  * an integer that describe a cell's location within the array

### 5.2.1 Referential Arrays
* Def.) An array that contains references of the objects
  * It simply stores objects' references, not the objects themselves.
  * 64-bit is used for each reference.
* Prop.)
  1. If an immutable object's reference, say an integer, is stored in a referential array and an operation that changes the immutable, such as addition, 
     * it is the reference of the new immutable that supercedes the original one.
     * it is not that the immutable itself changes.
  2. list() method creates only _shallow copy_, which copies the references identical to the original array's.
  3. deepcopy() function creates _new_ elements with new references.
  4. extent() method adds references of another array, copying identical references of its elements.

### 5.2.2 Compact Arrays in Python
* Def.) Compact Array
  * an array that contains elements, not the references of elements.
* Prop.)
  1. Less memory required than Referential Array
     1. Comparison with str class
        * str class is a compact that contains Unicodes as elements.
        * Since, each Unicode takes 2-Bytes, less memory required than referential array, which allocates 64-bits(4-Bytes) for each cell.
     2. Comparison by integer storing.
        * When a referential array stores an integer, following two elements take memory.
          1. reference of the integer : 4-Bytes
          2. int instance being stored elsewhere in memory : typically 14-Bytes.
        * Compact Array directly contains the int instance.
  2. High Performance due to consecutive storing of elements in the memory.
  
#### Concept) array module in Python : compact storage for arrays in Python
```python
import array
primes = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
```
* Prop.) Takes data type as first argument parameter.
  * Datatypes are from C-Language
  * User-defined types cannot be used.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/images/05_02_02_array_class_first_parameter.png" style="height: 300px;"></img><br/>
</p>

## 5.3 Dynamic Arrays and Amortization

#### Concept) Dynamic Array
* Props.)
  * has a particular length when constructed
  * no apparent limit on the overall capacity of the list
* Ex.) Python's List class
  * Props.)
    * __extra capacity__ : It maintains underlying array that often has greater capacity than the current length of the list
      * experiment ↓
        * cf.) sys.getsizeof() only shows the size of the array that includes references, not the real instance!

#### Code Fragment 5.1
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

### 5.3.1 Implementing a Dynamic Array
* Tech.) How to
  1. When the array is full, perform following steps
     1. Allocate a new array B with larger capacity.
     2. Set B[i] = A[i], for i = 0,...,n−1, where n denotes current number of items.
     3. Set A = B, that is, we henceforth use B as the array supporting the list.
     4. Insert the new element in the new array.
  2. For now, double when resizing!

```python
import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)( )
```

### 5.3.2 Amortized Analysis of Dynamic Arrays
* Tech.) Detailed analysis on the running time of operations on Dyanmic Arrays
  * Tool) big-Omega notation (giving asymptotic lower bound)   
<br>

#### Concept) Amortized Anaylsis
* Assumption
  * Dynamic Array doubles its size when it is full.
* How?) 
  1. Assume that each operation takes some coin to operate.
  2. When appending one element to a dynamic array, save additional 2 coins.
  3. Then for each append operation 3 coins are used.
  4. Now consider the case when Dynamic Array is full, containing 2^i elements.
  5. Then the appending operations from 2^(i-1) to 2^i-1 must have saved additional 2 coins each.
  6. The number of the additional coins are equal to {2^i-1 - 2^(i-1) + 1} * 2 = 2^i.
  7. Hence, the 2^i coins required for Dynamic Array for doubling its size by 2^(i+1) is already paid.
  8. From now on, appending operations will save 2 additional coins as usual and this will be used for the next doubling.
  9. Therefore, appending operation takes 3n running time and the running time is O(n).   
<br>

#### Concept) Trade-off between run-time efficiency and memory usage for Geometric Increase in Capacity
* Why?)
  * If the base of Geometric Capacity Increase is larger, less Capacity Increasing will take place.
  * But more memory space is required.   
<br>

#### Concept) Arithmetic Capacity Increase takes Ω(n^2) running times.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/images/05_03_02_arithmetic_capacity_increase.png" style="height: 300px;"></img><br/>
</p>

#### Concept) O(n) memory usage.
* Why Needed?
  * O(n) memory usage secures the total size of the array proportional to the number of the elements.
  * If not, repeated append/delete operation may incur arbitrary size of the underlying array.
* Geometric Capacity Increase
  * Applicable!
    * why?) The size of the Array is proportional to the size of the actual element.


### 5.3.3. Python's List Class
* Prop.) Python's List Class does not use Geometric nor Arithmetic Capacity Increase.
  * Still, amortized constant-time behavior is guaranteed.
  * Experiment Below
```python
from time import time

def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end-start)/n * 10000000

if __name__ == '__main__':
    print(compute_average(100))
    print(compute_average(1000))
    print(compute_average(10000))
    print(compute_average(100000))
    print(compute_average(1000000))
```

## 5.4 Efficiency of Python's Sequence Types

### 5.4.1 Python's List and Tuple Classes
#### Prop.) List vs Tuple
  1. Tuple is immutable -> More efficient than mutable objects
  2. _Nonmutating_ behaviors of List are identical to Tuple's
  3. Asymptotic analysis of List class goes as follows.

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/images/05_04_01_tuple_asymptotic.png" style="height: 300px;"></img><br/>
</p>

#### Prop.) Operations
  1. insert(k, value)
  2. remove(k)
  3. extend(other)
  4. Constructing New Lists  
     - Recall list comprehension.
     - Known to be faster than repeated appending.
```python
a = [k*k for k in range(10)]
```

### 5.4.2 Python's String Class
#### Prop.) String is immutable
* Thus, following code incurs repeated creation of string instances.
  * Resulting in O(n^2) running time
```python
letters = ''
for c in document:
    if c.isalpha():
        letters += c
    
```
* Instead use following methods
```python
temp = []
for c in document:
    temp.append(c)
letter = ''.join(temp)
```
```python
letter = ''.join([c for c in document])
```
```python
letter = ''.join(c for c in document)
```

## 5.5 Using Array-Based Sequences
### 5.5.1 Storing High Score Game
* Rules
  * GameEntry stores a name and a score.
  * ScoreBoard stores GameEntries and its capacity can be customized.
  * Every GameEntry should be sorted by the score
```python
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
        self._board = [None] * capacity
        self._n = 0

    def getitem(self, k):
        return self._board[k]

    def __str__(self):
        str_list = ['---------------']
        for j in range(self._n):
            str_list.append(str(self._board[j]))
        str_list.append('---------------')
        return '\n'.join(str_list)

    def add(self, entry):
        score = entry.get_score()
        good = self._n < self._capacity or score > self.getitem(self._n-1).get_score()

        if good:
            if self._n < self._capacity:
                self._board[self._n] = entry
                self._n += 1

            j = self._n-1
            while j > 0 and score >= self.getitem(j).get_score():
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry
```

### 5.5.2 Sorting a Sequence
#### Concept) The Insertion Sort Algorithm
```python
def insertion_sort(S):
    for i in range(1, len(S)):
        cur = S[i]
        j = i
        while j > 0 and S[j-1] > cur:
            S[j] = S[j-1]
            j -= 1
        S[j] = cur
```

### 5.5.3 Simple Cryptography
```python
class CaesarCypher:

    def __init__(self, shift):
        encoder = [None] * 52
        decoder = [None] * 52
        for k in range(26):
            encoder[k] = chr((k+shift) % 26 + ord('A'))
            encoder[k+26] = chr((k+shift) % 26 + ord('a'))
            decoder[k] = chr((k-shift) % 26 + ord('A'))
            decoder[k+26] = chr((k-shift) % 26 + ord('a'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        chr_list = list(original)
        for i in range(len(chr_list)):
            if chr_list[i].isupper():
                chr_list[i] = code[ord(chr_list[i]) - ord('A')]
            elif chr_list[i].islower():
                chr_list[i] = code[26 + ord(chr_list[i]) - ord('a')]
        return ''.join(chr_list)
```

### 5.6 Multidimensional Data Sets
#### Tech) Constructing Multidimensional List
* Two Dimensional List
```python
row = 4
column = 5
matrix = [[None]*column for i in range(row)]
```

<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/part05_07_exercises.md">Excercises</a>    
</p>
