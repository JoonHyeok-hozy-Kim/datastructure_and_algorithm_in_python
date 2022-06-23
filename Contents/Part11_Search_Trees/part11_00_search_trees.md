<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 11. Search Trees
## 11.1 Binary Search Trees
#### Concept) Binary Search Tree
* a binary tree T with each position p storing a key-value pair (k,v) such that
  * Keys stored in the left subtree of p are less than k.
  * Keys stored in the right subtree of p are greater than k.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_01_01_binary_search_tree_image.png" style="height: 200px;"></img><br/>
</p>

### 11.1.1 Navigating a Binary Search Tree
#### Prop.) An <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part08_Trees/part08_00_trees.md#843-inorder-traversal-of-a-binary-tree">inorder traversal</a> of a binary search tree visits positions in increasing order of their keys.
<br>

#### Tech.) Navigating Binary Search Tree
* How?)
  * Use inorder traversal
    * The traversal will be executed in linear time.
  * Methods
    * first() : Return the position containing the least key, or None if the tree is empty.
      * Find the deepest left child of the root.
    * last() : Return the position containing the greatest key, or None if empty tree.
      * Find the deepest right child of the root.
    * before(p) : Return the position containing the greatest key that is less than that of position p (i.e., the position that would be visited immediately before p in an inorder traversal), or None if p is the first position.
    * after(p) : Return the position containing the least key that is greater than that of position p (i.e., the position that would be visited immediately after p in an inorder traversal), or None if p is the last position.

### 11.1.2 Searches
* How?)
  * At each position p, it is asked whether the desired key k is less than, equal to, or greater than the key stored at position p, which we denote as p.key( ).
    1. less than : go left(p)
    2. equal to : search ended.
    3. greater than : go right(p)

#### Analysis) Binary Tree Searching
* O(log(n)) Running Time
  * The worst case running time will be O(h) where h denotes the height of the tree.

### 11.1.3 Insertions and Deletions
#### Tech.) Insertion
* Syntax : M[k] = v
  * Case 1. If M[k] already exists, 
    1. Search p such that p.key() == k 
    2. Update the value into v.
  * Case 2. If M[k] does not exists,
    1. Search p such that p.key() is closest to k.
    2. If k is less than p.key() add left child, else add right child.

#### Tech.) Deletion
* Syntax : del M[k]
  * Case 1. If p such that p.key() == k has no child,
    * Delete p.
  * Case 2. If p such that p.key() == k has one child,
    * Replace p with the child.
  * Case 3. If p such that p.key() == k has two children,
    * Find a sibling that has the greatest key and strictly less than k.
    * Replace p with that sibling.
      * Since that sibling may be positioned at the right most leaf of p's left subtree, Binary Tree structure will continue after the swap.
  
### 11.1.4 Python Implementation
#### Tech.) Multiple Inheritance
* Inherit both from LinkedBinaryTree class and MapBase class

#### Tech.) Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/binary_search_trees.py">Binary Search Tree</a>

### 11.1.5  Performance of a Binary Search Tree
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_01_05_binary_search_tree_performance.png" style="height: 300px;"></img><br/>
</p>



## 11.7 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_07_exercises.md">Exercises</a>
