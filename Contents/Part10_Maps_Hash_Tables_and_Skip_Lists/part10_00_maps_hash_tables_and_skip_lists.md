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
    * [(a*i+b) % p] % N
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

#### Tech.) Separate Chaining
* How?)
  * Have each bucket A[j] store its own secondary container, holding items (k, v) such that h(k) = j
    * Container may be a list instance.
* Analysis)
  * Suppose, _n_ items and _N_ bucket array capacity.
    * Then the expected size of a bucket is _n/N_.
    * Thus, if given a good hash function, the core map operations run in O(┌ _n/N_ ┐).
      * Here the ratio, _n/N_ is also known as __load factor__ of a hash table.
* Advantage
  * Simple implementation
* Disadvantage
  * Auxiliary data structure is required to hold items with colliding keys.
    * Thus, more space usage!

#### Tech.) Open Addressing
* Goal)
  * Do NOT use auxiliary data structure to deal with collisions of keys.
* Prop.)
  * Load Factor is always at most 1
  * Items are stored directly in the cells of the bucket array itself.
  
#### Ex 1) Linear Probing
* How?)
  1. Insertion
     * Suppose we try to insert item (k, v) into a bucket A[j]
       * If A[j] is already occupied, then try A[(j+1) % N].
       * If A[(j+1) % N] is already occupied, then try A[(j+2) % N].
       * Continue until an empty bucket is found.
  2. Deletion
     * Replace deleted item with a special available marker object.
       * Why?)
         * Suppose A[j] was already occupied by k_0 and k_1 was inserted at A[(j+1) % N] with linear probing.
         * If k_0 item is simply deleted, searching for item in k_1 is impossible.
           * Why?)
             * The key k_1 will point A[j] first and then should move 1 cell rightward.
             * But since A[j] is empty, probing cannot proceed from A[j]
* Advantage)
  * Can save space by not adapting other data structures.
* Disadvantage)
  * Slow down of search if items are clustered resulting in contiguous runs.
    
#### Ex 2) Quadratic Probing
* How?)
  * Instead of linearly increasing j+i, quadratically increase it by j+i^2
    * i.e.) Item (k, v) is inserted at A[(h(k)+f(i)) % N] for i=0,1,2,3, ... where f(i)=i^2
  * Advantage)
    * If N is prime number and bucket array is less than half full, it prevents clustering.
  * Disadvantage)
    * Secondary Clustering
      * Even if original hash codes are distributed uniformly, the set of filled array cells has non-uniform pattern
    * If N is not prime number or bucket array is at least half full, clustering happens.

#### Ex 3) Double Hashing Strategy
* How?)
  * Use secondary hash function _h'_.
    * If the primary hash function _h_ maps some key k to a bucket A[h(k)] that is already occupied
      * then we iteratively try buckets A[(h(k)+f(i)) % N] for i=0,1,2,3,... where f(i) = i*h'(k)
    * Common h'
      * h'(k) = q - (k % q) for some prime number q < N

#### Ex 4) Python dictionary class example
* It uses pseudo-random number generator.
  * That is Repeatable
  * But also Arbitrary


### 10.2.3 Load Factors, Rehashing, and Efficiency
* Recall that __load factor__ should be kept below 1 for efficiency.
  * Desired load Factor
    * Separate Chaining
      * λ < 0.9
    * Open Addressing
      * In order to prevent clustering, λ < 0.5

* Rehashing
  * Why doing this?
    * If an insertion causes the load factor of a hash table to go above the specified threshold, then it is common to resize the table.
      * Then, load factor will change.
  * Advantage)
    * Tend to scatter items throughout the new bucket array.
  * Desired
    * At least double the previous size of the bucket array.
      * Additional advantage)
        * Amortized cost of rehashing all the entries in the table against the time used to insert them in the first place.

#### Analysis) Efficiency of Hash Tables
* For a Good Hash table that all entries are uniformly distributed in the N cells of bucket array...
  * expected number of keys in a bucket is ┌ _n/N_ ┐ = O(1)
  * Rehashing cost will be O(1) considering the amortization.
* Worst Case Senario : Every keys are mapped to the same bucket.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_02_01_efficiency_of_hash_tables.png" style="height: 300px;"></img><br/>
</p>

### 10.2.4 Python Hash Table Implementation
* Rules for HashMapBase class
  1. The bucket array is represented as a Python list, named self. table, with all entries initialized to None.
  2. We maintain an instance variable self. n that represents the number of distinct items that are currently stored in the hash table.
  3. If the load factor of the table increases beyond 0.5, we double the size of the   table and rehash all items into the new table.
  4. We define a hash function utility method that relies on Python’s built-in hash function to produce hash codes for keys, and a randomized Multiply-Add-and-Divide (MAD) formula for the compression function.

#### Tech.) <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/maps.py#L2">HashMapBase</a>

#### Tech.) <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/maps.py#L42">Separate Chaining</a>

#### Tech.) <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/maps.py#L71">Linear Probing</a>


## 10.3 Sorted Maps

#### Concept) Sorted Map
* Ideation
  * Hash Map allows only exact search for the key.
    * h(k) = j
  * Considering the fact that keys are unique, they can be sorted and be efficiently searched.
    * Sorted Map adds following methods for that specific usage.
      1. M.find_min()
      2. M.find_max()
      3. M.find_lt(k) : Return the (key,value) pair with the greatest key that is strictly less than k (or None, if no such item exists).
      4. M.find_le(k)
      5. M.find_gt(k)
      6. M.find_ge(k)
      7. M.find_range(start, stop) : Iterate all (key,value) pairs with start <= key < stop. If start is None, iteration begins with minimum key; if stop is None, iteration concludes with maximum key.
      8. iter(M) : Iterate all keys of the map according to their natural order, from smallest to largest.
      9. reversed(M)

### 10.3.1 Sorted Search Tables
* 



## 10.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_06_exercises.md">Exercises</a>
