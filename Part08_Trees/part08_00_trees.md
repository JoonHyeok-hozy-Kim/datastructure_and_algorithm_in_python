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

<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_06_exercises.md">Exercises</a>    
</p>
