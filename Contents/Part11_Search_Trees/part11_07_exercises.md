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

### R-11.26 Let T be a red-black tree and let p be the position of the parent of the original node that is deleted by the standard search tree deletion algorithm. Prove that if p has zero children, the removed node was a red leaf.
* pf.)
  * Suppose not, i.e., the removed node was not red leaf.
  * The possible case is that the removed is black or not-leaf red node.
    * Case 1) The removed is black.
      * In this case p must be black.
      * Due to previous re-coloring and restructuring, the case that a red node has black only child must have been corrected. (Black Deficit)
      * Thus, the restructuring or recoloring must have been operated to p, which means that p must have two children. --- (X)
    * Case 2) The removed is not-leaf red.
      * In this case, the removed can have only one child at most and this child will be promoted after the removal.
      * Thus, p will have at least one promoted child after the removal. --- (X)

### R-11.27 Let T be a red-black tree and let p be the position of the parent of the original node that is deleted by the standard search tree deletion algorithm. Prove that if p has one child, the deletion has caused a black deficit at p, except for the case when the one remaining child is a red leaf.
* Check Case 2 explained in R-11.26.

### R-11.28 Let T be a red-black tree and let p be the position of the parent of the original node that is deleted by the standard search tree deletion algorithm. Prove that if p has two children, the removed node was black and had one red child.
* Check Case 1 explained in R-11.26.

### C-11.29 Explain how to use an AVL tree or a red-black tree to sort n comparable elements in O(nlogn) time in the worst case.
* Sol.) Inserting n elements into AVL or red-black tree may run in O(log(n)) time each which will be O(nlog(n)).
  * Then by traversing in inorder, we can get ordered series in O(n).

### C-11.30 Can we use a splay tree to sort n comparable elements in O(nlogn) time in the worst case? Why or why not?
* Sol.) Probably not. Even though search and update operation in splay tree may show amortized O(log(n)), its worst case can be O(n).
  * Consider the case when the elements are given in non-decreasing order.
  * The splaying may not take place during the insertion : O(n^2)
  * Traversing the tree will take O(n)

### C-11.31 Repeat Exercise C-10.28 for the TreeMap class.
```python
def setdefault(self, k, d):
    if self.is_empty():
        return self._add_root(self._Item(k, d))
    walk = self.root()
    leaf = None
    while leaf is None:
        if k == walk.key():
            return walk.value()
        elif k > walk.key():
            if self.right(walk) is not None:
                walk = self.right(walk)
            else:
                leaf = self._add_right(walk, self._Item(k, d))
        else:
            if self.left(walk) is not None:
                walk = self.left(walk)
            else:
                leaf = self._add_left(walk, self._Item(k, d))
    self._rebalance_insert(leaf)
```

### C-11.32 Show that any n-node binary tree can be converted to any other n-node binary tree using O(n) rotations.
* Sol.) Every form that certain shape of binary tree can be reduced into basic 5 forms of binary trees with three nodes.
```python
from DataStructures.binary_search_trees import TreeMap
from copy import deepcopy
a = TreeMap()
for i in range(3):
    a[i] = i
print(a)

b = deepcopy(a)
b._rotate(b.right(b.right(b.root())))
print(b)

c = deepcopy(a)
c._rotate(c.right(c.root()))
print(c)

c._rotate(c.right(c.root()))
print(c)

c._rotate(c.left(c.left(c.root())))
print(c)
```

### C-11.33 For a key k that is not found in binary search tree T, prove that both the greatest key less than k and the least key greater than k lie on the path traced by the search for k.
* Sol.) Each time that searching algorithm passes a node, it sets the local upper or lower bound of the key if the target key is not equal to the key in the node.
  * If the target key is less than the key in the node, that node's key becomes the possible upper bound.
  * Likewise, when the target key is bigger than the node's key, it becomes the lower bound.
  * Thus, as the search goes on and the depth of the node goes deeper, the range that covers the target key narrows.

### C-11.34 In Section 11.1.2 we claim that the find range method of a binary search tree executes in O(s+h) time where s is the number of items found within the range and h is the height of the tree. Our implementation, in Code Fragment 11.6 begins by searching for the starting key, and then repeatedly calling the after method until reaching the end of the range. Each call to after is guaranteed to run in O(h) time. This suggests a weaker O(sh) bound for find range, since it involves O(s) calls to after. Prove that this implementation achieves the stronger O(s+h) bound.
* Sol.) The only case that after() method runs in O(h) is when it is called at the last position of the left subtree of the root.
  * Other than that specific case, after() method runs less than O(h).
  * Thus, it is reliable to say that the algorithm runs in O(s+h) time.

### C-11.35 Describe how to perform an operation remove range(start, stop) that removes all the items whose keys fall within range(start, stop) in a sorted map that is implemented with a binary search tree T, and show that this method runs in time O(s + h), where s is the number of items removed and h is the height of T.
* Implementation
```python
def remove_range(self, start, stop):
    if not self.is_empty():
        if start is None:
            p = self.first()
        else:
            p = self.find_position(start)
            if p.key() < start:
                p = self.after(p)

        while p is not None and (stop is None or p.key() < stop):
            after = self.after(p)
            self.delete(p)
            p = after
```
* Test
```python
from DataStructures.binary_search_trees import TreeMap
a = TreeMap()
for i in range(10):
    a[i] = i
print(a)
a.remove_range(3, 7)
print(a)
```
* Analysis : The algorithm is almost identical to find_range()
  * The only difference is that it runs delete() method instead of yield command.
  * Recall that delete() method's worst case is O(h) only when the deleting target node is the root.
  * Considering the point that the target node shift to the "after" node, the occasion that O(h) delete() happens is once at most.
  * Thus, it can be said that it runs in O(s+h) time.

### C-11.36 Repeat the previous problem using an AVL tree, achieving a running time of O(slog n). Why doesn't the solution to the previous problem trivially result in an O(s+logn) algorithm for AVL trees?
* Justification : Not like TreeMap that does not care about the structure of the tree, AVL Tree continuously restructure after the deletion, which runs in log(n) time.
  * Thus, for every s deletion, the O(log(n)) restructuring is operated.
  * Therefore, it runs in O(slog(n))
```python
from DataStructures.binary_search_trees import AVLTreeMap
a = AVLTreeMap()
for i in range(10):
    a[i] = i
print(a)
a.remove_range(3, 7)
print(a)
```

### C-11.37 Suppose we wish to support a new method count range(start, stop) that determines how many keys of a sorted map fall in the specified range. We could clearly implement this in O(s+h) time by adapting our approach to find range. Describe how to modify the search tree structure to support O(h) worst-case time for count range.
* Sol.) Instead of the yield command we can simply count.

### C-11.38 If the approach described in the previous problem were implemented as part of the TreeMap class, what additional modifications (if any) would be necessary to a subclass such as AVLTreeMap in order to maintain support for the new method?


### C-11.39 Draw a schematic of an AVL tree such that a single remove operation could require Ω(logn) trinode restructurings (or rotations) from a leaf to the root in order to restore the height-balance property.
```python
from DataStructures.binary_search_trees import AVLTreeMap
a = AVLTreeMap()
seq = [44, 17, 62, 32, 50, 78, 48, 54]
for i in seq:
    a[i] = i
print(a)
print('------------------------------------------------')
del a[32]
print(a)
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_07_39.png" style="width: 450px"></img><br/>
</p>

### C-11.40 In our AVL implementation, each node stores the height of its subtree, which is an arbitrarily large integer. The space usage for an AVL tree can be reduced by instead storing the balance factor of a node, which is defined as the height of its left subtree minus the height of its right subtree. Thus, the balance factor of a node is always equal to −1, 0, or 1, except during an insertion or removal, when it may become temporarily equal to −2 or +2. Reimplement the AVLTreeMap class storing balance factors rather than subtree heights.
* Implementation : <a href="">AVLBalanceTreeMap</a>

### C-11.41 If we maintain a reference to the position of the leftmost node of a binary search tree, then operation find min can be performed in O(1) time. Describe how the implementation of the other map methods need to be modified to maintain a reference to the leftmost position.
* Sol.) Recall that the greatest value less than and the smallest value greater than the target insertion key are in the path during the search.
  * Therefore, during the insertion operation if the keys are saved in an array during the search and when the unsuccessful search is done, we can find out the keys that are the greatest value less than and the smallest value greater than the target insertion key.
  * The former will be saved in the new node while the latter's min will be updated into the new node.
* Implementation : <a href="">TreeMapBeforeAfter</a>

### C-11.42 If the approach described in the previous problem were implemented as part of the TreeMap class, what additional modifications (if any) would be necessary to a subclass such as AVLTreeMap in order to accurately maintain the reference to the leftmost position?
* Sol.) Since above property is applicable to every binary search tree, no additional treatment might be needed.
* Implementation : <a href="">AVLBalanceTreeMapBeforeAfter</a>

### C-11.43 Describe a modification to the binary search tree implementation having worst-case O(1)-time performance for methods after(p) and before(p) without adversely affecting the asymptotics of any other methods.
* Sol.) If each node contains _prev and _next property which can be updated by the operation described in C-11.41, O(1) running time for after(p) and before(p) might be possible.

### C-11.44 If the approach described in the previous problem were implemented as part of the TreeMap class, what additional modifications (if any) would be necessary to a subclass such as AVLTreeMap in order to maintain the efficiency?
* Sol.) Again as long as the data structure is a binary search tree, no modification may be required.
  * Implementation

### C-11.45 For a standard binary search tree, Table 11.1 claims O(h)-time performance for the delete(p) method. Explain why delete(p) would run in O(1) time if given a solution to Exercise C-11.43.
* Sol.) The main reason that delete(p) method took O(h) running time was due to the specific case that the root element is being deleted.
  * In that case, in order to search for the greatest key that is less than the root key, the O(h) time search operation was needed.
  * However, since before(p) operation can run in O(1) time, the deletion method will also run in O(1) time.

### C-11.46 Describe a modification to the binary search tree data structure that would support the following two index-based operations for a sorted map in O(h) time, where h is the height of the tree.
#### at_index(i): Return the position p of the item at index i of a sorted map.
#### index_of(p): Return the index i of the item at position p of a sorted map.



### C-11.52

<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md">Part 11. Search Trees</a>
</p>