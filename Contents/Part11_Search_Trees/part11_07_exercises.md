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

### R-11.6 Our implementation of the TreeMap. subtree search utility, from Code Fragment 11.4, relies on recursion. For a large unbalanced tree, Python’s default limit on recursive depth may be prohibitive. Give an alternative implementation of that method that does not rely on the use of recursion.
```python
def _subtree_search(self, p, k):
    while p is not None:
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                p = self.left(p)
            else:
                return p
        else:
            if self.right(p) is not None:
                p = self.right(p)
            else:
                return p
```

### R-11.7 Do the trinode restructurings in Figures 11.12 and 11.14 result in single or double rotations?
* Sol.) Figure 11.12 result in double rotation while Figure 11.14 incurs single one.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_07_figure_12.png" style="height: 200px;"></img><br/>
</p>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_07_figure_14.png" style="height: 200px;"></img><br/>
</p>

### R-11.8 Draw the AVL tree resulting from the insertion of an entry with key 52 into the AVL tree of Figure 11.14b.
```python
from DataStructures.binary_search_trees import AVLTreeMap
a = AVLTreeMap()
a[62] = 62
a[44] = 44
a[78] = 78
a[17] = 17
a[50] = 50
a[88] = 88
a[48] = 48
a[54] = 54
print(a)
a[52] = 52
print(a)
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_08.png" style="height: 200px;"></img><br/>
</p>

### R-11.9 Draw the AVL tree resulting from the removal of the entry with key 62 from the AVL tree of Figure 11.14b.
```python
from DataStructures.binary_search_trees import AVLTreeMap
a = AVLTreeMap()
a[62] = 62
a[44] = 44
a[78] = 78
a[17] = 17
a[50] = 50
a[88] = 88
a[48] = 48
a[54] = 54
print(a)
del a[62]
print(a)
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_09.png" style="height: 200px;"></img><br/>
</p>

### R-11.10 Explain why performing a rotation in an n-node binary tree when using the array-based representation of Section 8.3.2 takes Ω(n) time.
* Sol.) Whenever a position change of a node takes place, indices after that node should all be shifted.

### R-11.11 Give a schematic figure, in the style of Figure 11.13, showing the heights of subtrees during a deletion operation in an AVL tree that triggers a trinode restructuring for the case in which the two children of the node denoted as y start with equal heights. What is the net effect of the height of the rebalanced subtree due to the deletion operation?
* Sol.)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_11.png" style="height: 500px;"></img><br/>
</p>

### R-11.12 Repeat the previous problem, considering the case in which y’s children start with different heights.
* Sol.)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_12.png" style="height: 500px;"></img><br/>
</p>

### R-11.13 The rules for a deletion in an AVL tree specifically require that when the two subtrees of the node denoted as y have equal height, child x should be chosen to be “aligned” with y (so that x and y are both left children or both right children). To better understand this requirement, repeat Exercise R-11.11 assuming we picked the misaligned choice of x. Why might there be a problem in restoring the AVL property with that choice?
* Sol.) R-11.11 is solved with unaligned case.

### R-11.14 Perform the following sequence of operations in an initially empty splay tree and draw the tree after each set of operations.
a. Insert keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.  
b. Search for keys 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, in this order.  
c. Delete keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.  
* Sol.)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_14_insertion.png" style="height: 500px;"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_14_search.png" style="height: 500px;"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_14_deletion.png" style="height: 500px;"></img><br/>
</p>



### C-11.52

<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md">Part 11. Search Trees</a>
</p>