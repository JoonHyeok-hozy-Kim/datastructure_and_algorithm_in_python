<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 10. Maps, Hash Tables, and Skip Lists
## 10.1 The Priority Queue Abstract Data Type
#### Concept) Dictionary
* Represents an abstraction known as a dictionary in which unique keys are mapped to associated values.
* Also commonly known as associative __arrays__ or __maps__.
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
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/images/10_01_02_map_additional_behaviors2.png" style="height: 600px;"></img><br/>
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




## 10.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part10_Maps_Hash_Tables_and_Skip_Lists/part10_06_exercises.md">Exercises</a>
