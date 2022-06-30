<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md">Part 11. Search Trees</a>
</p>

### R-11.1 If we insert the entries (1,A), (2,B), (3,C), (4,D), and (5,E), in this order, into an initially empty binary search tree, what will it look like?
```python
from DataStructures.binary_search_trees import TreeMap
a = TreeMap()
for i in range(5):
    a[i+1] = chr(i+65)
print(a)
```

### R-11.2 Insert, into an empty binary search tree, entries with keys 30, 40, 24, 58, 48, 26, 11, 13 (in this order). Draw the tree after each insertion.
```python
from DataStructures.binary_search_trees import TreeMap
a = TreeMap()
a[30] = 30
print(a)
a[40] = 40
print(a)
a[24] = 24
print(a)
a[58] = 58
print(a)
a[48] = 48
print(a)
a[26] = 26
print(a)
a[11] = 11
print(a)
a[13] = 13
print(a)
```

### R-11.3 How many different binary search trees can store the keys {1,2,3}?
* Sol.) 5 kinds
```python
from DataStructures.binary_search_trees import TreeMap
from itertools import permutations
seq = [1,2,3]
for new_seq in permutations(seq):
    a = TreeMap()
    for i in new_seq:
        a[i] = i
    print(a)
```

### R-11.4 Dr. Amongus claims that the order in which a fixed set of entries is inserted into a binary search tree does not matter—the same tree results every time. Give a small example that proves he is wrong.
* Sol.) Depending on the order of elements, the height of the binary tree may vary.
  * Regarding the fact that operations in a binary search tree depends on the height, Dr. Amongus is wrong.
  * Consider the example in R-11.3.
    * Height can be either 2 or 3.
    * Performance is better when the height is 2.

### R-11.5 Dr. Amongus claims that the order in which a fixed set of entries is inserted into an AVL tree does not matter—the same AVL tree results every time. Give a small example that proves he is wrong.
* Sol.) Certain order of elements may incur relatively more frequent restructuring of the tree.
  * Consider the following two sequences.
    * seq1 : [1,2,3,4,5,6,7]
    * seq2 : [3,1,5,0,2,4,6]
  * While seq2 requires no restructuring, seq1 needs 5 restructurings as follows.
```python
from DataStructures.binary_search_trees import AVLTreeMap
b = AVLTreeMap()
for i in range(7):
    print('-------------Insert {}-------------'.format(i))
    b[i] = i
    print(b)
    print('-----------------------------------')
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_05_image.png" style="height: 500px;"></img><br/>
</p>





### C-11.52

<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md">Part 11. Search Trees</a>
</p>