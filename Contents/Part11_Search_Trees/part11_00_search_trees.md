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

## 11.3 AVL Trees
#### Concept) Height-Balance Property
* For every position p of T, the heights of the children of p differ by at most 1.

#### Concept) AVL Tree
* Def.)
  * Any binary search tree T that satisfies the height-balance property.
  * Named after its inventors : Adel’son-Vel’skii and Landis

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_03_01_avl_tree_image.png" style="height: 300px;"></img><br/>
</p>

* Props.)
  * Subtrees of an AVL tree are AVL trees as well.
  * The height of an AVL tree storing n entries is O(log(n)).
    * Justification
      * Let n(h) the minimum number of nodes for an AVL tree with the height h.
        1. n(1) = 1
        2. n(2) = 2
        3. n(3) = 4
        4. k-th : n(k) = 1 + n(k-2) + n(k-1) : Finbonacci Progression

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_03_02_avl_tree_justification_.png" style="height: 500px;"></img><br/>
</p>

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_03_03_pf1.png" style="width: 800px;"></img><br/>
</p>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_03_03_pf2.png" style="width: 800px;"></img><br/>
</p>

* Thus, search operation may run in O(h) < O(log(n)).

### 11.3.1 Update Operations
#### Insertion)
* How?)
  1. Suppose the binary tree T was balanced at first.
  2. Then when the position p is added to T, it becomes unbalanced.
  3. Starting from p, go up and find the position z that the unbalancedness of descendents starts.
  4. Let y the child of z that the height is larger than its sibling.
  5. Let x the child of y that the height is larger than its sibling. 
     * x can be p or the ancestor of p.
  6. Perform Trinode Restructuring with x, y, z.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_03_04_insertion.png" style="width: 300px;"></img><br/>
</p>

#### Deletion)
* How?)
  1. Delete the target position p.
  2. Starting from p, go up and find position z that the unbalancedness of descendents starts.
  3. Let y the child of z that the height is larger than its sibling.
     * In this case, y cannot be the ancestor of p.
     * Consider that p is deleted!
  4. Let x the child of y that the height is larger than its sibling.
     * Again, x cannot be the ancestor of p.
  5. Perform Trinode Restructuring with x, y, z.
  6. Go up from y, the new root, and repeat 2-5 going all the way to the root until every node is balanced.

#### Analysis) Performance of AVL Tree
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_03_05_avl_tree_performance.png" style="width: 450px;"></img><br/>
</p>

### 11.3.2 Python Implementation
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/binary_search_trees.py#L218">AVL Tree</a>

## 11.4 Splay Trees
### 11.4.1 Splaying
#### Concept) Splay
* Given a node x of a binary search tree T, we splay x by moving x to the root of T through a sequence of **restructurings**.

* A **splaying** step consists of repeating following 3 restructurings at x until x becomes the root of T.
1. zig-zig
   * Formation
     * The node x and its parent y are both left children or both right children.
   * Restructuring
     * Promote x, making y a child of x and z a child of y, while maintaining the inorder relationships of the nodes in T.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_01_zig_zig.png" style="height: 300px;"></img><br/>
</p>

2. zig-zag
   * Formation
     * One of x and y is a left child and the other is a right child.
   * Restructuring
     * Promote x by making x have y and z as its children, while maintaining the inorder relationships of the nodes in T.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_02_zig_zag.png" style="height: 300px;"></img><br/>
</p>

3. zig
   * Formation
     * x does not have a grandparent.
   * Restructuring
     * Perform a single rotation to promote x over y, making y a child of x, while maintaining the relative inorder relationships of the nodes in T.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_03_zig.png" style="height: 300px;"></img><br/>
</p>

#### Tech.) Splay Simulation
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_04_splay_simulation.png" style="height: 500px;"></img><br/>
</p>

## 11.4.2 When to Splay
#### Search : searching for key k
1. If k is found, splay k.
2. If k is not found, splay the leaf position that the unsuccessful search ended.

#### Insert : inserting key k
* Splay the newly inserted key k.

#### Delete : deleting key k
* Splay the parent position of k.
* Delete the position k.


### 11.4.3 Python Implementation
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/binary_search_trees.py#L271">Splay Tree</a>

### 11.4.4 Amortized Analysis of Splaying ★
#### Analysis) Running Time in General
* Suppose a position p has depth d.
  * Then splaying p consists of a sequence of └d/2┘ zig-zigs and/or zig-zags, plus one final zig if d is odd.
    * Single **zig-zig**, **zig-zag**, or **zig** runs in O(1) time.
      * why?)
        * Only constant number of nodes are modified.
    * Thus, splaying of p runs in O(d) time where d is the depth of p.

#### Analysis) Worst Case Time
* In the worst case, the overall running time of a search, insertion, or deletion in a splay tree of height h is O(h).
  * Consider the case that every node has one child except one leaf node.
  * However, Splay Tree works in O(log(n)) in amortized sense.

#### Amortized Performance of Splay Trees
* Prop.) The time for performing a search, insertion, or deletion is proportional to the time for the associated splaying
  * Operations other than splaying are constant.
  * Thus, running time of Splaying will show the running time of all the operations.

* Settings.)
  * T : the splay tree
  * n : the number of nodes
  * w : a node of T
  * n(w) : the number of nodes in the subtree rooted at w
  * r(w) : the rank of w, which is equal to log(w).
    * i.e.) r(w) = log(w)
    * Then, r(n) = log(n) = max{ rank(w) for any w in T }
  * r(T) : the sum of the ranks of all the nodes of T
  * substep : single zig / zig-zig / zig-zag operation in a splaying
  * r'(w) : the rank of w after a splaying **substep**

* Cyber Dollar Accounting for Amortized Analysis
  * Suppose a certain number of cyber-dollars must be paid for splaying operation
    * Rules
      1. If the payment is equal to the splaying work, then we use it all to pay for the splaying.
      2. If the payment is greater than the splaying work, we deposit the excess in the accounts of several nodes.
      3. If the payment is less than the splaying work, we make withdrawals from the accounts of several nodes to cover the deficiency.
    * Invariant
      * Before and after a splaying, each node w of T has r(w) cyber-dollars in its account.

* Props.)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_05_prop_11_3.png" style="height: 150px;"></img><br/>
</p>

* Justification
1. zig-zig case
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_05_prop_11_3_case1.png" style="width: 800px;"></img><br/>
</p>

2. zig-zag case
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_05_prop_11_3_case2.png" style="width: 800px;"></img><br/>
</p>

3. zig case
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_05_prop_11_3_case3.png" style="width: 800px;"></img><br/>
</p>
<br>
<br>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_05_prop_11_4_and_pf.png" style="width: 900px;"></img><br/>
</p>

* Interpretation
  * 3(r(t)−r(x)) + 2
    * Payment enough for maintaining the invariant.
  * d
    * Payment for the entire splaying work of the target node x
  * Running time of Splaying is O(log(n))
    * why?)
      * Since the size of T is equal to n, r(t) = r(n) = log(n)
      * Thus, total payment made for the splaying is O(log(n)) cyber-dollars.


#### Analysis) Insertion in Amortized sense
* Situation
  * Inserting node w into a splay tree with n keys
* Result : Insertion runs in O(log(n)) time.
* Proof
  * Assumptions
    * Let w_0, w_1, w_2, ... , w_d be the ancestors of w.
      * where w_0 = w.
      * Then w_i is the parent of w_(i-1)
    * Let n(w_i) the size of w_i and n'(w_i) the size of w_i after the insertion.
    * Let r(w_i) the rank of w_i and r'(w_i) the rank of w_i after the insertion.
  * Derivation
    * Then n'(w_i) =  n(w_i) + 1
    * Consider that n(w_i) + 1 <= n(w_(i+1)). (∵ Subtree rooted from the sibling of w_(i+1).)
      * Thus, r'(w_i) = log( n'(w_i) ) = log( n(w_i) + 1 ) <= log( n(w_(i+1)) ) = r( w_(i+1) ).
    * Hence, the total variation of r(T) caused by insertion goes,
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_06_insertion.png" style="height: 100px;"></img><br/>
</p>

#### Analysis) Deletion in Amortized sense
* The total variation of r(T) caused by the deletion is negative.
  * why?)
    * When deleting a node w from a splay tree with n keys, the ranks of all the ancestors of w are decreased.
* Therefore, no payment is needed for maintaining the invariant when a node is deleted.

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_07_prop_11_5.png" style="width: 900px;"></img><br/>
</p>

#### Concept) Static Optimality
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_04_08_prop_11_6.png" style="width: 900px;"></img><br/>
</p>

## 11.7 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_07_exercises.md">Exercises</a>
