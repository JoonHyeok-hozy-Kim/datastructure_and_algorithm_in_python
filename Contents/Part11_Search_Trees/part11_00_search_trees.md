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

## 11.5 (2,4) Trees (Multiway Search Tree)
### 11.5.1 Multiway Search Trees (<a href="https://yoongrammer.tistory.com/73">Supplementary</a>) 
#### Def.) of a Multiway Search Tree
* Assumptions
  * w : a node of an ordered tree
  * w is a d-node : w has d children
  * Tree T is ordered.
* If T has following properties, T is a Multiway Search Tree
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_05_00_definition.png" style="height: 200px;"></img><br/>
</p>
 
#### Props.)
* The external nodes of a multiway search do not store any data and serve only as “placeholders.”
  * Thus, external nodes can be represented by None references
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_05_01_multiway_search_tree_image.png" style="width: 500px;"></img><br/>
</p>

#### Prop. 11.7) An n-item multiway search tree has n+1 external nodes.
* pf.) <a href="">C-11.52</a>

#### Tech.) Searching in a Multiway Tree
* Start from the root of the tree T.
  * At a d-node w, compare key k with the keys (k_1, k_2, ... , k_(d-1)) stored at w.
    * If k = k_i, search is successful.
    * Else, search in the child c_i of w such that k_(i-1) < k < k_i

#### Tech.) Data Structures for Representing Multiway Search Trees
* Use General Tree data structure.
  * Recall that each node has more than 2 children.
* At each node, use SortedTableMap as a secondary map that stores keys.
  * why?)
    * We should compare the size of the keys during operations.
    * Bootstrapping Technique
      * Using a simple solution to a problem to create a new, more advanced solution.
* Each item _i_ should have a key _k_i_ and an element that is the pair of (_v_i, c_i_)
  * _v_i_ : value that matches the key _k_i_
  * _c_i_ : the reference to the child _c_i_ such that _k\_(i-1) < k < k\_i_

#### Analysis) Running Time of Search
* Conclusion : O(h)
  * Item search in each d-node is O(log(d))
    * why?)
      * We used sortedmap as a container for each node.
      * Using binary search, it takes O(log(d)) running time for searching target item.
  * Letting d_max the maximum value of d in T, search time in T is O(h*log(d_max)).
  * Regarding d_max as a constant, the running time is O(h)

### 11.5.2 (2,4)-Tree Operations
#### Def.) (2,4)-Tree
1. Size Property: Every internal node has at most four children.
   * This property guarantees O(1) running time for searching an item in a node regardless of the data type.
     * i.e.) d_max = 4
     * Thus, unordered list or array can also be used for the secondary map.
2. Depth Property: All the external nodes have the same depth.

<br>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_05_02_2,4tree_prop_11_8.png" style="height: 200px;"></img><br/>
</p>

* pf) 
  * Consider two cases that can be the bounds.
    * Case1) Every node has 2 items.
      * Then the minimum number of external nodes in T is 2^h
    * Case2) Every node has 4 items.
      * Then the maximum number of external nodes in T is 4^h
  * By <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md#prop-117-an-n-item-multiway-search-tree-has-n1-external-nodes">Prop. 11.7</a> the number of external nodes is equal to (n+1)
  * Thus, 2^h <= (n+1) <= 4^h.
    * We can derive the given inequality.


#### Tech.) Insertion for (2,4) Tree
* Target : Insert (k, v) into T.
* How?)
  1. Search k in T. Consider the case that the search was unsuccessful.
  2. Let
     * z : the node that unsuccessful search ended.
     * w : the parent of z
  3. Insert new item y to the left of w.
  4. If the size of w becomes 5 (i.e. **overflows**), perform split as follows.
     * Replace w with w' and w''
       * w' : 3-node with children c_1, c_2, c_3 storing keys k_1, k_2
       * w'' : 2-node with children c_4, c_5 storing keys k_4
     * If w is the root of T, create a new root node u.
       * Let u be the parent of w
     * Insert key k_3 into u and make w' and w'' children of u.
       * Then  if w was child i-th of u, then w' and w'' become children i-th and (i+1)-th of u, respectively.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_05_03_2,4tree_insertion.png" style="width: 900px;"></img><br/>
</p>

#### Analysis) Analysis of Insertion in a (2,4) Tree
* Conclusion : O(log(n))
  * why?)
    * Insertion of an item to the node is O(1)
      * Recall that d_max is limited to 4.
    * Since the height of the tree is O(log(n)), the number of cascading split operations is bounded O(log(n)) time.

#### Tech.) Deletion
* Target : Removing the item (k, v) in the tree T.
* How?
  * We can only delete items at a node w whose children are all the external nodes. (To keep the Depth Property)
    * If (k, v) is in w, simply remove it.
    * Else, put z the node that has only internal node children and contains (k, v).
      * Put (k, v) = (k_i, v_i) where (k, v) is the i-th item of z.
      * Then swap (k_i, v_i) with appropriate item in w as follows.
        1. We find the rightmost internal node w in the subtree rooted at the i-th child of z, noting that the children of node w are all external nodes.
        2. We swap the item (k_i, v_i) at z with the last item of w.
        3. If (k_i, v_i) is in w, remove it.
        4. Deal with the possible **underflow** in w as follows.
           * If the number of items in w was 2 before the removal, underflow of w will take place.
              1. Check whether an immediate sibling of w is a 3-node or a 4-node.
                 * Perform **transfer** operation to that sibling s.
                   * Transfer
                     1. Move a child of s to w
                     2. Move a key of s to the parent u of w and s
                     3. Move a key of u to w
              2. If w has only one sibling, or if both immediate siblings of w are 2-nodes
                 * Perform **fusion**
                   * Fusion
                     1. Merge w with the sibling
                     2. Create a new node w'
                     3. Move a key from the parent u of w to w'
                     4. If another underflow is incurred by the previous fusion, perform Transfer or Fusion repeatedly.
                     
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_05_04_2,4tree_insert_delete_image.png" style="width: 100%;"></img><br/>
</p>

#### Analysis) Performance of (2,4) Trees
* The height of a (2,4) tree storing n entries is O(log(n)) (∵ <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md#def-24-tree">Prop.</a>)
* A split, transfer, or fusion operation takes O(1) time.
* A search, insertion, or removal of an entry visits O(log(n)) nodes.


## 11.6 Red-Black Trees
#### Def.) Red-Black Tree
* A binary search tree with nodes colored red and black in a way that satisfies the following properties:
  * Root Property: The root is black.
  * Red Property: The children of a red node (if any) are black.
  * Depth Property: All nodes with zero or one child have the same **black depth**
    * **black depth** : the number of black ancestors. (Recall that a node is its own ancestor).

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_05_05_red_black_tree_image.png" style="height: 300px;"></img><br/>
</p>

#### Prop.) Red-Black Tree vs (2,4) Tree
* How to make (2,4) Tree from Red-Black Tree
  * Merge every red node w into its parent.
  * Store the entry from w at its parent
  * Children of w become the ordered children of w' parent.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_01_red_black_and_24.png" style="height: 300px;"></img><br/>
</p>

* How to make Red-Black Tree from (2,4) Tree
1. If w is a 2-node, then keep the (black) children of w as is.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_02_24_redblack_2node.png" style="height: 100px;"></img><br/>
</p>

2. If w is a 3-node, then create a new red node y, give w’s last two (black) children to y, and make the first child of w and y be the two children of w.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_02_24_redblack_3node.png" style="height: 100px;"></img><br/>
</p>

3. If w is a 4-node, then create two new red nodes y and z, give w’s first two (black) children to y, give w’s last two (black) children to z, and make y and z be the two children of w.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_02_24_redblack_4node.png" style="height: 100px;"></img><br/>
</p>

#### Analysis) The Height of Red-Black Tree
* Let T be a red-black tree storing n entries, and let h be the height of T. We justify this proposition by establishing the following fact:
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_03_redblack_height.png" style="height: 100px;"></img><br/>
</p>

* pf.)
  * Let
    * d : the common black depth of all nodes of T having zero or one child.
    * T' : (2,4) Tree associated with T
    * h' : the height of T'
  * Then d = h'.
    1. d = h' =< log(n+1)-1 (Recall that depth = height-1)
       * By the Red Property of Red-Black Tree, h <= 2d.
       * Thus, h <= 2log(n+1)-2
    2. By <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part08_Trees/part08_00_trees.md#props-binary-tree">Prop. 8.8</a>
       * h >= log(n+1)-1

### 11.6.1 Red-Black Tree Operations
#### Tech.) Insertion
* Target : Insert k-value pair (k, v)
* How?
  * Perform binary search for k until we reach a null subtree.
  * Introduce new leaf x storing item (k, v) to that null subtree.
  * Case
    * If x is root, color x black!
    * Else, color x red!
      * This may violate the Red Property.
      * **Double Red Violation**
        * Let y the parent of x and z the parent of y.
        * Consider the case that y is red.
        * Then by the Red Prop., z must be black.
        * We denote this the Double Red Violation.
        
#### Sol.) Solution for **Double Red Violation** in each cases
* Case 1: The Sibling s of y Is Black (or None).
  * Perform <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_00_search_trees.md#tech-trinode-restructuring">Trinode Restructuring</a> 
  * In (2,4) Tree's perspective, it is similar to adding item to a 3-node.
    * We can simply add item and make 4-node.
    * All that we need is restructuring the 4-node into a balanced position.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_04_double_red_sol1.png" style="height: 450px;"></img><br/>
</p>

* Case 2: The Sibling s of y Is Red.
  * In (2,4) Tree's perspective it is similar to overflow : adding item to a 4-node.
  * Perform **Recoloring**.
    * Change color of s and y into Black.
    * Unless z is root, change z into Red.
      * If z is not root, the Black Depth Property continues by changing the color.
      * If z is root, the black depth increases.
  * If **Recoloring** incurs **Double Red Violation** above, continue going up T until **Double Red Violation** is finally fixed.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_04_double_red_sol2.png" style="height: 450px;"></img><br/>
</p>

#### Tech.) Simulation of Insertions
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_05_insertion_simulation.png" style="width: 100%;"></img><br/>
</p>

#### Tech.) Deletion
* Target : Delete Item (k, v)
* Rule
  * Consider that we can delete only the node that has at most one child.
    * Thus, if we need to remove an internal node, we should swap it with the rightmost item in the left subtree of the target node and then perform removal at the leaf.
* How?
  * Under the assumption that target deleting node has at most one child...
    * If the target node is red
      1. Delete target node
      2. Promote the child node.
    * Else if the target node is black,
      * If the target node has the only child and the child is red,
        * Remove the target black node
        * Promote the child node and change into black.
      * Else if the target node is the leaf black node...
        * Consider the more generalized settings below...

#### Tech.) Generalization for the Black Leaf Deletion
* Settings
  * Let
    * z : the parent of the removed black leaf
    * T_heavy : the sibling subtree of the removed black leaf
      * Exactly one more black depth compared to T_light (due to the deletion of the black leaf in T_light)
    * y : the root of T_heavy
    * T_light : the empty subtree of the removed black leaf
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_06_deletion_setting.png" style="height: 300px;"></img><br/>
</p>

* Case 1: Node y Is Black and Has a Red Child x.
  * Perform **Trinode Restructuring.**
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_07_deletion_case1.png" style="width: 800px;"></img><br/>
</p>

* Case 2: Node y Is Black and Both Children of y Are Black (or None).
  * Perform **Recoloring.**
    1. Color y red.
    2. If z is red, color z black.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_07_deletion_case2.png" style="width: 800px;"></img><br/>
</p>

* Case 3: Node y Is Red.
  * Perform rotation about y and z, and then recolor y black and z red.
  * Now, the new z must be in Case 1 or Case 2.
    * Why?)
      * Recall that T_heavy is one black depth more than T_light.
      * Since y is red, children of y must be black.
      * Hence, one of the children of y that is newly linked to z' will be black, which incur unbalancedness of subtree of z'.
  * Thus, perform the correspondent treatment at z's subtree.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_07_deletion_case3.png" style="width: 800px;"></img><br/>
</p>

#### Tech.) Simulation of Deletions
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_08_deletion_simulation.png" style="width: 100%;"></img><br/>
</p>

#### Analysis) Performance of Red-Black Trees
* Asymptotic performance is identical to that of an AVL Tree or a (2,4) Tree.
* An insertion or deletion requires only a constant number of restructuring operations.
* Insertion
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_09_analysis_insertion.png" style="width: 800px;"></img><br/>
</p>

* Deletion
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/images/11_06_10_analysis_deletion.png" style="width: 800px;"></img><br/>
</p>


### 11.6.2 Python Implementation
* Implementation : <a href="">RedBlackTreeMap</a>



## 11.7 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part11_Search_Trees/part11_07_exercises.md">Exercises</a>
