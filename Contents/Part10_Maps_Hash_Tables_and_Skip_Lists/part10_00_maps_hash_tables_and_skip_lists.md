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
  * Best way is to avoid collision if possible.
    * Good Hash Functions map keys so as to sufficiently minimize collisions.
  * There are some ways to deal with this.

#### Concept) Hash Codes
* Def.) An output integer that is computed by a hash function when an arbitrary key is given.
* Prop.)
  * 





## 10.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_06_exercises.md">Exercises</a>
