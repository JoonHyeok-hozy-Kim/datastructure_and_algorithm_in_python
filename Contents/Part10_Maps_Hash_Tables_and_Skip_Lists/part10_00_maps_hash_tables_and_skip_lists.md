<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 10. Maps, Hash Tables, and Skip Lists
## 10.1 The Priority Queue Abstract Data Type
#### Concept) Dictionary
* Represents an abstraction known as a dictionary in which unique keys are mapped to associated values.
* Also commonly known as __associative arrays__ or __maps__.
* Notation)
  * In this book,
    1. Dictionary denotes Python's dict class
    2. Map denotes the general notion of the abstract data type.

### 10.1.1 The Map ADT
#### Def.) Map
* Let M a map with following 5 behaviors.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_01_01_map_behaviors.png" style="height: 600px;"></img><br/>
</p>

* Additional behaviors for convenience.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_01_02_map_additional_behaviors1.png" style="height: 450px;"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_01_02_map_additional_behaviors2.png" style="height: 500px;"></img><br/>
</p>

### 10.1.2 Application: Counting Word Frequencies
```python
freq = {}
filename = None
for piece in open(filename).read().lower().split():
    word = ''.join(c for c in piece if piece.isalpha())
    if word:
        freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0
for (w, c) in freq:
    if c > max_count:
        max_word = w
        max_count = c
print('The most frequent word is', max_word)
print('Its number of occurrences is', max_count)
```

### 10.1.3 Python’s MutableMapping Abstract Base Class
#### Concept) Map related Abstract Base Classes provided by Python's _collections_ module
1. Mapping class
   * includes all nonmutating methods supported by Python’s dict class
2. MutableMapping class
   * extends Mapping class to include the mutating methods
   * provides concrete implementations for all behaviors other than the first five outlined in Section 10.1.1
     1. \_\_getitem__()
     2. \_\_setitem__()
     3. \_\_delitem__()
     4. \_\_len__()
     5. \_\_iter__()
   * As long as the five core behaviors are provided, 
     * all other derived behaviors can be inherited simply by declaring MutableMapping as a parent

### 10.1.4 Our MapBase Class
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_01_03_hierarchy_of_to_be_implemented_map_types.png" style="height: 450px;"></img><br/>
</p>

#### Tech.) MapBase Class
* We define our own MapBase class, which is itself a subclass of the MutableMapping class
  * Target : Greater code re-use
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/maps.py">MapBase Class</a>

### 10.1.5 Simple Unsorted Map Implementation
* Implementaion : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/maps.py#L21">UnsortedTableMap</a>
* Analysis
  * Inefficient with the running time of O(n) for every operations.
    * why?) self._table is not sorted.
      * Thus, it may take O(n) traversal in the worst case.

## 10.2 Hash Tables
#### Concept) Hash Table
* Def.) a data structure that implements a set abstract data type, a structure that can map keys to values.

#### Concept) Hash Function
* Def.) a function that maps general keys to corresponding indices in a table
* Props.)
  * Ideally, keys will be well distributed in the range from 0 to N −1 by a hash function
    * BUT in practice there may be two or more distinct keys that get mapped to the same index
      * Sol.) Use __bucket array__ that manage a collection of items that are sent to a specific index by the hash function.
  
### 10.2.1 Hash Functions
* Props.)
  1. Let
     1. _h_ : hash function
     2. _k_ : key
     3. _N_ : the capacity of the bucket array for a hash table.
     4. _A_ : a bucket array
     * Then
       * The goal of a hash function, _h_, is to map each key _k_ to an integer in the range [0,N − 1], where N is the capacity of the bucket array for a hash table.
       * _h(k)_ : an index into our bucket array
         * Instead of the key _k_ itself!
       * item _(k, v)_ is stored in the bucket _A[h(k)]_.
  2. Two-portion structure of a hash function
     * Portions
        1. <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md#concept-hash-codes">Hash Code</a>
           * This maps a key to an integer
        2. compression function
           * This maps the hash code to an integer within a range of indices.
     * Advantage of doing this.
       * The hash code portion of that computation is independent of a specific hash table size.
       * This allows the development of a general hash code for each object that can be used for a hash table of any size
       * Only the compression function depends upon the table size
       * The underlying bucket array for a hash table may be dynamically resized, depending on the number of items currently stored in the map.

#### Concept) Collision
* Def.) If there are two or more keys with the same hash value, then two different items will be mapped to the same bucket in A.
* Props.)
  * Best way is to avoid collision as much as possible.
    * Good Hash Functions map keys so as to sufficiently minimize collisions.
  * There are some ways to deal with this.

### Concept) Hash Codes
* Def.) An output integer that is computed by a hash function when an arbitrary key is given.
* Prop.)
  * Need not be in the range [0,N −1], and may even be negative
  * Desirable that the set of hash codes assigned to the keys should avoid collisions as much as possible.
    * If the hash codes cause collisions, then compression function can not avoid them.
* Applications)
  1. Bit Representation as an Integer
     * 32-bit, 64-bit, 
     * summation
     * exclusive-or operation
  2. Polynomial Hash Code
     * Structure
       * a polynomial in _a_ that takes the components _(x_0, x_1, ..., x\_(n-1))_ of an object _x_ as its coefficients.
     * Advantage
       * Useful for character strings or other variable-length objects like tuples.
     * Disadvantage
       * Possibility of periodic bits overflow
         * why?) Polynomial structure uses multiplication.
     * Suggestions for the constant _a_
       * For English,
         * 33
         * 37
         * 39
         * 41
  3. Cyclic-Shift Hash Codes
     * Target)
       * Replace multiplication of Polynomial with Cyclic shift
     * Example) 5-bit cyclic shift of the 32-bit value
```python
def hash_code(s):
    mask = (1<<32)-1
    h = 0
    for character in s:
        h = (h<<5&mask)|(h>>27)
        h += ord(character)
    return h
```

#### Tech) Hash Codes in Python
* hash(x)
  * The standard mechanism for computing hash codes in Python is a built-in function
  * Returns an integer value that serves as the hash code for object x
  * Only immutable data types are deemed hashable in Python
    * why?) To ensure that a particular object’s hash code remains constant during that object’s lifespan.
      * why?) A problem could occur if a key were inserted into the hash table, yet a later search were performed for that key based on a different hash code than that which it had when inserted.
    * ex.)
      * int, float, tuple, frozenset classes
    * If called for a mutable instance x, hash(x) returns TypeError
  * For user-defined classes
    * Use \_\_hash__ method
    * Consider the consistency.
      * i.e.) if "x == y", then "hash(x) == hash(y)"

### Concept) Compression Functions
* Def.) Computation that maps the integer determined by __hash code__ into the range [0,N −1]
* Props.)
  * Good Compression Function : Minimizes the number of collisions for a given set of distinct hash codes.
* Ex 1) The Division Method
  * How?)
    * Map an integer _i_ to _i_ mod _N_
    * Desirable to use prime number for _N_
      * why?) Prime number can help compression function spread-out the distribution of hashed values.
        * If non-prime number is used, there is a possibility of repetition of hash values.
          * Ex.)
            * Suppose hash_codes = {200, 205, 210, 215, 220, ..., 600} is inserted in to a bucket array of size 100(_N_)
              * Then collision takes place at least 3 times for each hash value.
                * ex.) 205, 305, 405
            * If _N_ = 101, no collision.
    * MUST ensure that the probability of two different keys getting hashed to the same bucket is 1/N.
```python
a = [200+5*i for i in range(81)]
m_100 = []
m_101 = []
n = 101
for i in a:
    mod = i%100
    if mod not in m_100:
        m_100.append(mod)
    mod = i%101
    if mod not in m_101:
        m_101.append(mod)
print(len(m_100))
print(len(m_101))
```
* Ex 2) The MAD Method (Multiply-Add-and-Divide)
  * How?
    * [(a*i+b) mode p] mod N
      * where
        * N : the size of the bucket array
        * p : a prime number larger than N
        * a, b : integers chosen at random from the interval [0, p-1] with a > 0

### 10.2.2 Collision-Handling Schemes
* Recall that the main idea of hash table is to
  * store each item (k,v) in the “bucket” A[h(k)].
* However, if there exists distinct keys k_1, and k_2 such that h(k_1) = h(k_2), hash table fails.
  * A.K.A. <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md#concept-collision">Collision</a>
  * Here are some ways to deal with such collisions.








## 10.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_06_exercises.md">Exercises</a>
