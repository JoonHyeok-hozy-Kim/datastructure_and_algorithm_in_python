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
* Worst Case O(h) Running Time where h denotes the height of the tree.
  * The worst case running time will be O(h).
  * Recall that minimum value of h for a binary tree with n elements is equal to ┌log(n+1)┐-1.
    * It is also possible that h = n : the worst case that every node has only one child.
    * Thus, we cannot guarantee the performance of O(log(n)) unless continuous re-balancing is made.

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

* Why O(h) not O(log(n))?
  * Review : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md#analysis-binary-tree-searching">O(h) Worst Case</a>

## 11.2 Balanced Search Trees
* Why Doing This?)
  * Recall that the performance of search tree is O(h) where h is the height of the tree.
  * Thus, the smaller the height is, the more efficient the performance of the search tree will be.
  * Therefore, we need to make trees as balanced as possible.

#### Tech.) Rotation
* Visualization
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_02_01_rotation_image.png" style="height: 300px;"></img><br/>
</p>

* Prop)
  * Swap between a parent and its child with maintaining the binary search tree property
  * Running time is O(1)
    * why?)
      * a constant number of parent-child relationships are modified.
  * Why helpful?)
    * Regarding the image above, through the rotation, the depth of the subtree T1 decrease, maintaining the property of the binary tree.
    * This may be helpful to enhance the balance of a tree.

#### Tech.) Trinode Restructuring
* Def.)
  * For a position x, its parent y, and its grandparent z
  * Restructure the subtree rooted at z in order to reduce the overall path length to x and its subtrees.
* Pseudo Code
```python
Algorithm restructure(x):
    Input : A position x of a binary search tree T that has both a parent y and a grandparent z.
    Output : Tree T after a trinode restructuring (which corresponds to a single or double rotation) involving positions x, y, and z

1. Let (a, b, c) be a left-to-right (inorder) listing of the positions x, y, and z, and let (T1,T2,T3,T4) be a left-to-right (inorder) listing of the four subtrees of x, y, and z not rooted at x, y, or z.
2. Replace the subtree rooted at z with a new subtree rooted at b.
3. Let a be the left child of b and let T1 and T2 be the left and right subtrees of a, respectively.
4. Let c be the right child of b and let T3 and T4 be the left and right subtrees of c, respectively.
```
* Case 1. Single rotation : Since b is the child of the root node, a single rotation can achieve restructuring.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_02_02_trinode_restructuring_single_rotation.png" style="height: 450px;"></img><br/>
</p>

* Case 2. Double rotation : Since b is the grandchild of the root node, double rotation can achieve restructuring.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_02_03_trinode_restructuring_double_rotation.png" style="height: 450px;"></img><br/>
</p>

### 11.2.1 Python Framework for Balancing Search Trees
* Our Binary Search Trees' Hierarchy
  * TreeMap implemented hooks for the rebalaning operations.
  * Each Subclass of TreeMap will perform its own rebalancing techniques.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_02_04_hierarchy_for_the_search_trees_to_be_developed.png" style="height: 450px;"></img><br/>
</p>




## 11.7 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_07_exercises.md">Exercises</a>
