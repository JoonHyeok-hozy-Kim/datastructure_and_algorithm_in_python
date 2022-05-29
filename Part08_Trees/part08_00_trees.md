<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 8. Trees
## 8.1 General Trees

#### Props.) Non-linearity of Tree
* Hierarchical Structure of Trees

### 8.1.1 Tree Definitions and Properties
#### Def.) Tree
* Tree T is a set of nodes storing elements such that the nodes have a parent-child relationship that satisfies the following properties.
  1. If _T_ is nonempty, it has a special node, called the _root_ of _T_, that has no parent.
  2. Each node _v_ of _T_ different from the _root_ has a unique parent node _w_.
     * Every node with parent _w_ is a child of _w_.

#### Concept) "_T_ is Empty" means ...
  * _T_ does not have any nodes.  

#### Node Relationships
  * Concept) Siblings
    * Two nodes that are children of the same parent
  * Concept) External
    * A node v is external if _v_ has no children.
    * External Nodes = Leaves
  * Concept) Internal
    * A node _v_ is internal if it has one or more children.
  * Concept) Ancestor
    * A node _u_ is an ancestor of a node _v_ if _u_ = _v_ or _u_ is an ancestor of the parent of _v_.
  * Concept) Descendant
    * A node _v_ is a descendant of a node _u_ if _u_ is an ancestor of _v_.
  * Concept) Subtree
    * The subtree of _T_ rooted at a node _v_ is the tree consisting of all the descendants of _v_ in _T_ (including _v_ itself).

#### Edges and Paths in Trees
  * Concept) Edge
    * a pair of nodes (_u_,_v_) such that _u_ is the parent of _v_, or vice versa.
  * Concept) Path
    *  a sequence of nodes such that any two consecutive nodes in the sequence form an edge

#### Example.) Python's Exception Tree
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_01_01_tree_example_python_exceptions.png" style="height: 300px;"></img><br/>
</p>

#### Concept) Ordered Tree
* A tree is ordered if there is a meaningful linear order among the children of each node.
  * i.e.) We purposefully identify the children of a node as being the first, second, third, and so on.
* usually visualized by arranging siblings left to right, according to their order.

### 8.1.2 The Tree Abstract Data Type
#### Tech.) Abstract Base Class
* Why doing this?
  * A more formal mechanism to designate the relationships between different implementations of the same abstraction.
  * Define one class that can serve as the base form of similar classes.
  * Various subclasses can be generated via inheritance.
* Advantage
  * Allows greater code reuse.

<div>
    <p>
        <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/tree.py">Tree Abstract Base Class</a>
    </p>
</div>

### 8.1.3 Computing Depth and Height
#### Concept) Depth of a position
* Let _p_ be the position of a node of a tree _T_.
* The depth of _p_ is the number of ancestors of _p_, excluding p itself.
  * If _p_ is the root, then the depth of _p_ is 0.
  * Otherwise, the depth of _p_ is one plus the depth of the parent of _p_.

#### Tech.) Recursive Algorithm for calculating the depth of a position.
```python
def depth(self, p):
    if self.is_root(p):
        return 0
    else:
        return self.depth(self.parent(p)) + 1
```

#### Prop.) The running time of T.depth(p) for position p is O(d_p +1), where d_p denotes the depth of p in the tree T.
* Worst Case : O(n)
  * when n is the total number of positions of T
  * and all nodes form a single branch

#### Concept) Height of a position
* The height of a position p in a tree T is also defined recursively,
  * If p is a leaf, then the height of p is 0.
  * Otherwise, the height of p is one more than the maximum of the heights of p’s children.

#### Prop.) The height of a nonempty tree T is equal to the maximum of the depths of its leaf positions.

#### Tech.) Algorithm for calculating the height of a position
1. _height1
   * 
   * Running Time : Worst case O(n^2)
     * why?)
       * Calculating Depth required O(n) in worst case.
       * It is repeated n times for every element of T.
```python
def _height1(self):
    return max(self.depth(p) for p in self.children() if self.is_leaf(p))
```

2. _height2 : O(n)
   * Running Time : O(n)
     * why?)
       * Let c_p denotes the number of children of p.
       * Then iterating every children for a position p takes O(c_p+1)
       * It is repeated for every element of T.
       * Assume the following.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_02_02_proposition_8_5.png" style="height: 150px;"></img><br/>
</p>

```python
def height(self, p=None):
    if p is None:
        p = self.root()
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self.height(c) for c in self.children(p))
```

## 8.2 Binary Trees
* Def.) Binary Tree
  * an ordered tree with the following properties:
    1. Every node has at most two children.
    2. Each child node is labeled as being either a left child or a right child.
    3. A left child precedes a right child in the order of children of a node.

* Concept) Proper Binary Tree
  * if each node has either zero or two children.

#### Props.) Binary Tree
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_02_02_props_binary_tree.png" style="height: 450px;"></img><br/>
</p>

#### Props.) Relating Internal Nodes to External Nodes in a Proper Binary Tree
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_02_03_proper_binary_tree_internal_external_nodes.png" style="height: 750px;"></img><br/>
</p>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_02_04_proper_binary_tree_internal_external_nodes_graphic.png" style="height: 300px;"></img><br/>
</p>

## 8.3 Implementing Trees
### 8.3.1 Linked Structure for Binary Trees
<div>
    <p>
        <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/tree.py#L75">Linked Binary Tree</a>
    </p>
</div>

#### Performance of the Linked Binary Tree Implementation
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_03_01_performance_linked_binary_tree.png" style="height: 300px;"></img><br/>
</p>

### 8.3.2 Array-Based Representation of a Binary Tree
#### Tech.) How?
* Level Numbering
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_03_02_array_based_binary_tree.png" style="height: 150px;"></img><br/>
</p>

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_03_03_array_based_binary_tree_graphic.png" style="height: 150px;"></img><br/>
</p>





<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_06_exercises.md">Exercises</a>    
</p>
