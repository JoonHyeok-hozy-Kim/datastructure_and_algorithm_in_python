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
* Def.) Load Factor
  * Let
    * n : the number of items in the map
    * N : the number of buckets in the bucket array A
  * Then, _load factor_ = n/N
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

#### Tech.) <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/hash_tables.py#L2">HashMapBase</a>

#### Tech.) <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/hash_tables.py#L42">Separate Chaining</a>

#### Tech.) <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/hash_tables.py#L71">Linear Probing</a>


## 10.3 Sorted Maps

#### Concept) Sorted Map
* Ideation
  * Hash Map allows only __exact search__ for the key.
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
* Concept
  * Store the map’s items in an array-based sequence A
    * Thus, items are in increasing order of their keys, assuming the keys have a naturally defined order.

#### Tech.) Binary Search and Inexact Searches
* Our previous usage for the binary search was to find exact target
  * This logic can be used for \_\_contains__ method.
* Moreover, the gap between _high_ and _low_ parameter can be used for inexact searches.

#### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/sorted_maps.py">Implementation : SortedTableMap</a>

#### Analysis) Sorted Table Map operations' running time 
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_03_01_sortedtablemap_running_time.png" style="height: 300px;"></img><br/>
</p>

## 10.4 Skip Lists
#### Def.) Skip List
* A skip list S for a map M consists of a series of lists {S0,S1,...,Sh}.
* Each list Si stores 
  1. a subset of the items of M sorted by increasing keys
  2. items with two sentinel keys denoted −∞ and +∞
     * −∞ is smaller than every possible key that can be inserted in M
     * +∞ is larger than every possible key that can be inserted in M   
<br>

#### Props.)
* List _S0_ contains __every__ item of the map _M_ (plus sentinels −∞ and +∞)
* For _i = 1,...,h−1_, list _Si_ contains (in addition to −∞ and +∞) a __randomly__ generated subset of the items in list _Si−1_.
* List _Sh_ contains only −∞ and +∞.
  * _h_ : the height of skip list _S_
* the _i_-th list _Si_ is expected to have about n/(2^i) items
  * Thus, the height _h_ of _S_ is log(n)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_04_01_skip_list_image.png" style="height: 300px;"></img><br/>
</p>

#### Concept) Randomization in the Skip List
* Recall that "halving the number of items from one list to the next" is achieved by randomly generating the subset of the previous items.
* Advantage
  * the structures and functions that result are usually simple and efficient
  * Randomization can extend the logarithmic time bound performances to update methods!
    * Recall that <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md#1031-sorted-search-tables">Sorted Table Map</a>'s log(n) performance was limited to the searching method by Binary Search Algorithm
    * The bounds are expected for the skip list, while binary search has a worst-case bound with a sorted table.
      * i.e.) Search and Update times are O(logn) __on average__ for a Skip List.
        * The notion of average time complexity used here does NOT depend on the probability distribution of the keys in the input
        * Instead, it depends on the use of a __random-number generator__ in the implementation of the insertions to help decide where to place the new item.   
<br>

#### Tech.) Structure of the Skip List
* levels : positions arranged horizontally
* towers : positions arranged vertically
* Methods for traversing the Skip List
  * Kinds...
    * next(p) : Return the position following p on the same level.
    * prev(p) : Return the position preceding p on the same level.
    * below(p) : Return the position below p in the same tower.
    * above(p) : Return the position above p in the same tower.
  * Return None if the position requested does not exist.
  * Individual traversal methods each take O(1) time
  * Consider a Skip List as "a collection of h doubly linked lists aligned at towers, which are also doubly linked lists."

### 10.4.1 Search and Update Operations in a Skip List
#### Tech.) Skip Search
* How?
  1. _Drop Down_ unless S.below(p) is None (i.e. at the bottom)
  2. _Scan Forward_ until S.next(p) <= k
  3. Return to 1
* Pseudo-Code for SkipSearch
```python
Algorithm SkipSearch(k):
  Input: A search key k
  Output: Position p in the bottom list S0 with the largest key such that key(p) ≤ k

  p = start {begin at start position}
  while below(p) != None do
    p = below(p) {drop down}
    while k ≥ key(next(p)) do
      p = next(p) {scan forward}
  return p.
```

#### Tech.) <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/skip_lists.py#L100">Hozy Skiplist</a> Implemented

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_04_02_skip_search.png" style="height: 300px;"></img><br/>
</p>

#### Tech.) Insertion in a Skip List
* How?
  1. Operate SkipSearch(k)
     * If SkipSearch(k) is not None, overwrite new value v
     * Else, proceed with the followings.
  2. Insert new item (k, v) at the position right next to the position returned by the previous SkipSearch(k)
  3. Use random-number generator to decide whether to stack additional level of the tower for the key k
  4. Repeat 3 randomly.
* Pseudo-Code for SkipSearch
```python
Algorithm SkipInsert(k,v):
  Input: Key k and value v
  Output: Topmost position of the item inserted in the skip list

  p = SkipSearch(k)
  q = None {q will represent top node in new item’s tower}
  i = −1
  repeat
    i = i+1
    if i ≥ h then
        h = h+1 {add a new level to the skip list}
        t = next(s)
        s = insertAfterAbove(None,s,(−∞,None)) {grow leftmost tower}
        insertAfterAbove(s,t,(+∞,None)) {grow rightmost tower}
    while above(p) is None do
        p = prev(p) {scan backward}
    p = above(p) {jump up to higher level}
    q = insertAfterAbove(p,q,(k,v)) {increase height of new item’s tower}
  until coinFlip() == tails
  n = n+1
  return q
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_04_03_insertion.png" style="height: 300px;"></img><br/>
</p>

#### Tech.) Removal in a Skip List
* How?
  1. Operate SkipSearch(k)
     * If the returned p's key is not equal to k, raise KeyError
     * Else, starting from the bottom remove p and remove all positions above p
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_04_03_removal.png" style="height: 300px;"></img><br/>
</p>
<br>

#### Tech.) Optimizations for the Skip List
* How?
  1. Represent a tower as a single object, storing the key-value pair.
     * Do not let positions store references of the positions above them.
  2. Make horizontal axes singly linked lists.
* Why doing this?
  * Although asymptotic performance of skip list may improve only by more than a constant factor.
  * However, this improvement is meaningful in the practice.   
<br>

#### Tech.) Maintaining the Topmost Level
* Why needed?
  * Recall that a skip list S must maintain reference to the start position (the topmost, left position in S).
  * Thus, certain policy is needed when new entry is inserted past the top level of S.
* Two possible options.
  1. Restricting the top level, h, to be kept at some fixed value that is a function of n.
     * Desiderata
       1. h = max{ 10, 2* ┌log(n)┐ }
       2. h = 3 * ┌log(n)┐
  2. Let an insertion continue inserting a new position as long as heads keeps getting returned from the random number generator.
     * This is applied to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_00_maps_hash_tables_and_skip_lists.md#tech-insertion-in-a-skip-list">SkipInsert</a> above.   
<br>

### 10.4.2 Probabilistic Analysis of Skip Lists ★
* Consider the worst case.
  * In worst case, the running time of searching and updating may take O(n+h) time.
    * \_\_getitem__, \_\_setitem__, \_\_delitem__
  * There is also a possibility that height continues infinitely if the random choice is made to keep raising tower higher when insertion is made.
  * However, that has very low possibility.

#### Tech.) Bounding the Height of a Skip List (Informal but Intuitive Probabilistic Analysis)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_04_04_bounding_height.png" style="height: 500px;"></img><br/>
</p>
<br>

#### Tech.) Analyzing Search Time in a Skip List
* Recall that SkipSearch(k) contains two while loops
  * Outer Loop : Drop Down
    * The loop repeats h times, which is equal to __log(n)__
    * Thus, the expected amount of time spent dropping down is O(log(n))
  * Inner Loop : Scan Forward
    * Let _n_i_ be the number of keys examined while scanning forward at level _i_
    * Consider that during the SkipSearch(k) any key additionally examined at the level _i_ cannot also belong to level _i+1_.
      * Why?) Since we scanned forward, previous keys will not be scanned afterward.
    * Then, the probability that any key is counted in ni is 1/2.
    * Therefore, the expected value of _n_i_ is exactly equal to the expected number of times we must flip a fair coin before it comes up heads.
      * This expected value is 2.
    * Hence, the expected amount of time spent scanning forward at any level i is O(1).
  * Therefore, SkipSearch takes O(log(n)) times.   
<br>

#### Tech.) Space Usage in a Skip List
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_04_05_space_usage.png" style="height: 450px;"></img><br/>
</p>
<br>

#### Summary
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_04_06_summary.png" style="height: 450px;"></img><br/>
</p>
<br>

## 10.5 Sets, Multisets, and Multimaps
#### Concept) Set
* Definition and Props.)
  * An unordered collection of elements, without duplicates
  * Typically supports efficient membership tests.
  * Elements of a set are like keys of a map without any auxiliary values

#### Concept) Multiset
* A set-like container that allows duplicates

#### Concept) Multimap
* A map such that a same key can be mapped to multiple values.

### 10.5.1 The Set ADT
* Python's Built-in Classes
  * frozenset (immutable) 
    * collections.Set
  * set
    * collections.MutableSet
* Methods
  * S.add(e)
  * S.discard(e)
  * e in S : Return True if the set contains element e. (cf. \_\_contains__ method)
  * len(S)
  * iter(S)
  * S.remove(e) : Remove element e from the set. If the set does not contain e, raise a KeyError.
  * S.pop() : Remove and return an arbitrary element from the set. If the set is empty, raise a KeyError.
  * S.clear : Remove all elements from the set.
  * S == T : Return True if sets S and T have identical contents.
  * S != T
  * S <= T : Return True if set S is a subset of set T.
  * S < T : Return True if set S is a proper subset of set T.
  * S >= T
  * S > T
  * S.isdisjoint(T) : Return True if sets S and T have no common elements.
  * S | T : Return a new set representing the union of sets S and T.
  * S |= T : Update set S to be the union of S and set T.
  * S & T: Return a new set representing the intersection of sets S and T.
  * S &= T: Update set S to be the intersection of S and set T.
  * S ˆ T: Return a new set representing the symmetric difference of sets S and T, that is, a set of elements that are in precisely one of S or T.
  * S ˆ= T: Update set S to become the symmetric difference of itself and set T.
  * S − T: Return a new set containing elements in S but not T.
  * S −= T: Update set S to remove all common elements with set T.

### 10.5.2 Python’s MutableSet Abstract Base Class
#### Concept) MutableSet
* Python's Built-in Class : collections.MutableSet
* Prop.) Template Method Pattern
  * MutableSet base class do NOT provide five core behaviors,
    1. add
    2. discard
    3. \_\_contains__
    4. \_\_len__
    5. \_\_iter__
  * why?)
    * The concrete methods of the MutableSet class rely on the presumed abstract methods that will subsequently be provided by a subclass.

#### Sample Implementation of some behaviors
* S < T : Return True if set S is a proper subset of set T.
```python
def __lt__(self, other):
    if len(self) < len(other):
        return False
    for e in self:
        if e not in other:
            return False
    return True
```
* S | T : Return a new set representing the union of sets S and T.
```python
def __or__(self, other):
    result = type(self)()
    for e in self:
        result.add(e)
    for e in other:
        result.add(e)
    return result
```
* S |= T : Update set S to be the union of S and set T.
  * Recall in-place property for update operation.
```python
def __ior__(self, other):
    for e in other:
        self.add(e)
    return self
```

### 10.5.3 Implementing Sets, Multisets, and Multimaps
#### Sets
* Even though any data structure used to implement a map can be modified to implement the set ADT, implement independent one.
  * why?) 
    * Existing ADTs have _Item subclass which stores key and value, which is a waste of memory.

#### Multisets
* Use a map in which the map key is a (distinct) element of the multiset, and the associated value is a count of the number of occurrences of that element within the multiset.
* Python's Built-in Class
  * collections.Counter
    * Functions
      * most_common(n) : Return a list of the n most common elements

#### Multimaps
* Use a standard map in which the value associated with a key is itself a container class storing any number of associated values.



## 10.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_06_exercises.md">Exercises</a>
