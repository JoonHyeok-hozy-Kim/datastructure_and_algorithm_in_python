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
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_03_03_array_based_binary_tree_graphic.png" style="height: 450px;"></img><br/>
</p>

#### Analysis) Advantages and Disadvantages of the Array-Based Representation
* Advantage
  * a position _p_ can be represented by a single integer of _f(p)_.
* Disadvantage
  * The space usage of an array-based representation depends greatly on the shape of the tree.
    * ex.) Consider the case that every node have only right child.
  * Some update operations for trees cannot be efficiently supported.
    * ex.) Deleting a node and promoting its child takes O(n) time because it is not just the child that moves locations within the array, but all descendants of that child

### 8.3.3 Linked Structure for General Trees
#### Props.) General Trees
* For a general tree, there is no a priori limit on the number of children that a node may have. 
* A natural way to realize a general tree T as a linked structure is to have each node store a single container of references to its children.
  * ex.) Python's List Class as a container


## 8.4 Tree Traversal Algorithms
### 8.4.1 Preorder and Postorder Traversals for General Trees
#### Tech.) Preorder Traversal
* Props.)
  * The root of T is visited first.
  * Then the subtrees rooted at its children are traversed recursively.
* Running Time Analysis
  * For a position _p_ and the number of its children _c_p_,
    1. Running time of visits at the position p : O(_c_p_)
    2. Running time of the whole traversal : O(n)
* Pseudo Code
```python
def preorder(T, p):
    visit_action(p)
    for child in T.children(p):
        T.preorder(T, child)
```

#### Tech.) Postorder Traversal
* Props.)
  * Recursively traverses the subtrees rooted at the children of the root first.
  * Then visits the root
* Running Time Analysis
  * Identical to Preorder Traversal
* Pseudo Code
```python
def postorder(T, p):
    for child in T.children(p):
        T.preorder(T, child)
    visit_action(p)
```

### 8.4.2 Breadth-First Tree Traversal
#### Tech.) Breadth-First Tree Traversal
* Props.)
  * visit all the positions at depth _d_ before we visit the positions at depth _d+1_.
* Why using this?
  * A computer may be unable to explore a complete game tree in a limited amount of time.
  * So the computer will consider all moves, then responses to those moves, going as deep as computational time allows.
* Pseudo Code
```python
from DataStructures.queue import LinkedQueue
def breadthfirst(T, p=None):
    q = LinkedQueue()
    q.enqueue(p)
    while not q.is_empty():
        visit_action(q.dequeue())
        for child in T.children(p):
            q.enqueue(child)
```

### 8.4.3 Inorder Traversal of a Binary Tree
* Props.)
  * Visiting the nodes of _T_ “from left to right.”
* Pseudo Code
```python
def inorder(T, p):
    if T.left() is not None:
        T.inorder(T, T.left())
    visit_action(p)
    if T.right() is not None:
        T.inorder(T, T.right())
```

#### Application) Binary Search Tree
* Def.)
  * Let _S_ be a set whose unique elements have an order relation.
  * A binary search tree for _S_ is a binary tree _T_ such that, for each position _p_ of _T_:
    * Position _p_ stores an element of _S_, denoted as _e(p)_.
    * Elements stored in the left subtree of _p_ (if any) are less than _e(p)_.
    * Elements stored in the right subtree of _p_ (if any) are greater than _e(p)_.

* Props.)
  * Running time greatly depends on the height of the tree.
    * i.e.) minimum height = maximum efficiency of binary searching algorithm

### 8.4.4 Implementation of Traversal Algorithms
* <p><a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/tree.py#L212">Preorder</a></p>
* <p><a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/tree.py#L223">Postorder</a></p>
* <p><a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/tree.py#L234">Breadth-First</a></p>
* <p><a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/tree.py#L246">Inorder</a></p>

### 8.4.5 Application of Tree Traversals
#### Tech.) Table of Contents
1. Normal Print
```python
def preorder_print(T):
    for i in T.preorder():
        print(i.element())
```
2. Indent Print
```python
def preorder_indent(T, p=None, d=None):
    if p is None and d is None:
        p = T.root()
        d = 0
    text_list = []
    for i in range(d):
        text_list.append('  ')
    text_list.append(p.element())
    print(''.join(text_list))
    for c in T.children(p):
        preorder_indent(T, c, d+1)
```
3. Label Print
```python
def preorder_label(T, p=None, label_list=None):
    if p is None and label_list is None:
        p = T.root()
        label_list = []
    label_list.append(' ')
    label_list.append(p.element())
    print(''.join(label_list))
    label_list.pop()
    label_list.pop()
    cnt = 1
    for c in T.children(p):
        label_list.append(str(cnt))
        label_list.append('.')
        preorder_label(T, c, label_list)
        label_list.pop()
        label_list.pop()
        cnt += 1
```

#### Tech.) Parenthetic Representation of a Tree
```python
def parenthesize(T):
    text_list = _parenthesize_text(T)
    return ''.join(text_list)

def _parenthesize_text(T, p=None, text_list=None):
    if p is None:
        p = T.root()
        text_list = []
    text_list.append(p.element())
    if T.num_children(p ) > 0:
        text_list.append(' ( ')
        for c in T.children(p):
            text_list = _parenthesize_text(T, c, text_list)
            text_list.append(', ')
        text_list.pop()
        text_list.append(' ) ')
    return text_list
```

### 8.4.6 Euler Tours and Template Method Pattern
* Target
  * Develop a more general framework for implementing tree traversals
  * More Objective-Oriented Programing
    * More adaptability and reusability

#### Concept) Euler Tour
* How?
  * Two notable “visits” to each position p
    1. A “pre visit” occurs when first reaching the position, that is, when the walk passes immediately left of the node in our visualization.
    2. A “post visit” occurs when the walk later proceeds upward from that position, that is, when the walk passes to the right of the node in our visualization.
* Pseudo Code
```python
def euler_tour(T, p):
    pre_visit_action(p)
    for c in T.children(p):
        euler_tour(T, c)
    post_visit_action(p)
```
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_04_01_euler_tour_graphic.png" style="height: 300px;"></img><br/>
</p>

#### Tech.) Template Method Pattern
* Target
  * Provide a framework that is reusable and adaptable
* How?
  * Calls auxiliary functions known as __hooks__ at designated steps of the process.






<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_06_exercises.md">Exercises</a>    
</p>
