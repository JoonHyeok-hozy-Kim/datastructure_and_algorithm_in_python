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
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_14_insertion.png" style="width: 100%;"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_14_search.png" style="width: 100%;"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_14_deletion.png" style="width: 100%;"></img><br/>
</p>

### R-11.15 What does a splay tree look like if its entries are accessed in increasing order by their keys?
* Sol.) Worst case scenario which the height of the tree is equal to n.

### R-11.16 Is the search tree of Figure 11.23(a) a (2,4) tree? Why or why not?
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_16.png" style="height: 400px"></img><br/>
</p>

* Sol.) No. The depth property of (2,4) tree is violated.

### R-11.17 R-11.17 An alternative way of performing a split at a node w in a (2,4) tree is to partition w into w' and w'', with w' being a 2-node and w'' a 3-node. Which of the keys k1, k2, k3, or k4 do we store at w’s parent? Why?
* Sol.) k2 should be the parent. By definition, the parent key should be larger than k1 and must be the minimum value among k2 ~ k4.

### R-11.18 Dr. Amongus claims that a (2,4) tree storing a set of entries will always have the same structure, regardless of the order in which the entries are inserted. Show that he is wrong.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_18.png" style="width: 700px"></img><br/>
</p>

### R-11.19 Draw four different red-black trees that correspond to the same (2,4) tree.
* Sol.) Random RedBlackTree with size 9.
```python
from DataStructures.binary_search_trees import RedBlackTreeMap
from random import randint
for i in range(4):
    a = RedBlackTreeMap()
    for j in range(9):
        rand = randint(1, 99)
        a[rand] = rand
    print(a)
```
* Corresponding (2,4) Trees.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_19.png" style="width: 100%"></img><br/>
</p>

### R-11.20 Consider the set of keys K = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}.
a. Draw a (2,4) tree storing K as its keys using the fewest number of nodes.
b. Draw a (2,4) tree storing K as its keys using the maximum number of nodes.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_20.png" style="height: 500px"></img><br/>
</p>

### R-11.21 Consider the sequence of keys (5,16,22,45,2,10,18,30,50,12,1). Draw the result of inserting entries with these keys (in the given order) into
a. An initially empty (2,4) tree.
b. An initially empty red-black tree.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_21.png" style="height: 500px"></img><br/>
</p>

### R-11.22 For the following statements about red-black trees, provide a justification for each true statement and a counterexample for each false one.
1. A subtree of a red-black tree is itself a red-black tree.
   * False. Any Subtree of the root of a red-black tree has the root with red.
2. A node that does not have a sibling is red.
   * True. If certain node does not have a sibling, the black depth cannot be kept.
   * Assume that the root is not counted.
3. There is a unique (2,4) tree associated with a given red-black tree.
   * True. (2,4) and red-black tree may be in 1-1 relationship.
4. There is a unique red-black tree associated with a given (2,4) tree.
   * False. 
     * Counter-ex.)
       * Consider a (2,4) tree with only 3-node root node.
       * red-black representation of that tree can be two cases.
         * Root node with one left child.
         * Root node with one right child.

### R-11.23 Explain why you would get the same output in an inorder listing of the entries in a binary search tree, T, independent of whether T is maintained to be an AVL tree, splay tree, or red-black tree.
* Sol.) Every binary search tree maintains the inorder increasing structure because it should perform "binary" searching operation.

### R-11.24 Consider a tree T storing 100,000 entries. What is the worst-case height of T in the following cases?
1. T is a binary search tree.
   * 100,000
2. T is an AVL tree.
   * log(100,000) = 17
3. T is a splay tree.
   * 100,000
4. T is a (2,4) tree.
   * log(100,000) = 17
5. T is a red-black tree.
   * log(100,000) = 17

### R-11.25 Draw an example of a red-black tree that is not an AVL tree.
```python
from DataStructures.binary_search_trees import RedBlackTreeMap
a = RedBlackTreeMap()
seq = [10, 1, 15, 12, 19, 11, 13, 18, 20]
for i in seq:
    a[i] = i
print(a)
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_25.png" style="height: 150px"></img><br/>
</p>



### C-11.52

<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md">Part 11. Search Trees</a>
</p>