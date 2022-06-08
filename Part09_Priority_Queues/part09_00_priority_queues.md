<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 9. Priority Queues
## 9.1 The Priority Queue Abstract Data Type
### 9.1.1 Priorities
* Prop.)
  * Give priorities to certain elements in the ADT.
  * _key_ will be designated to each element to identify its priorities.
  * INSERT/UPDATE/DELETE will be allowed to the prioritized element.

## 9.2 Implementing a Priority Queue
### 9.2.1 The Composition Design Pattern
* Tech.) Priority Queue
  * Must keep track of both an element and its key.
    * Use, _Item class in PriorityQueueBase class to store key and the comparison logic between keys.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/priority_queues.py">PriorityQueueBase</a>
</p>

### 9.2.2 Implementation with an Unsorted List
* Use a PositionalList, which is doubly linked list, that elements are not sorted as a space where _Item instances are stored.
  * Since the list is unsorted,
    1. add element may take O(1)
    2. finding minimum key _Item may take O(n) for locating it.

### 9.2.3 Implementation with a Sorted List
* Right opposite to the Unsorted version,
  1. add element may take O(n) for locating proper position of the new item in the PositionalList : SORTING
  2. finding minimum key _Item may take O(1)

## 9.3 Heaps
* Def.) Heap
  * A binary tree that stores a collection of items at its positions.
    * These positions satisfy following two props.
      1. __Heap Order Property__
         * In a heap T, for every position p other than the root, the key stored at p is greater than or equal to the key stored at p’s parent.
      2. __Complete Binary Tree Property__
         * A heap T with height h is a complete binary tree if levels 0,1,2,...,h− 1 of T have the maximum number of nodes possible
           * (namely, level i has 2i nodes, for 0 ≤ i ≤ h− 1) 
         * The remaining nodes at level h reside in the leftmost possible positions at that level.
         * Recall the concept of <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_00_trees.md#tech-how">_level_numbering_</a>

#### The Height of Heap
* Prop.) 
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/images/09_03_01_height_of_a_heap.png" style="height: 300px;"></img><br/>
</p>

### 9.3.2 Implementing a Priority Queue with a Heap
* How
  1. Adding an item
     1. Add an item at the rightmost node at the bottom level
     2. Perform Up Heap Bubbling
        * Starting from the newly added node, move upward to the root and swap if _heap order property_ is violated.
  2. Removing an item
     1. Remove the item at the root
     2. Copy the last positional item to the root of the heap.
     3. Perform Down Heap Bubbling
        * Starting from the new root, move downward to the end and swap if _heap order property_ is violated.
          * If target position has two children, perform swap, if needed, with the one with lower key.

### 9.3.3 Array-Based Representation of a Complete Binary Tree
#### Use <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_00_trees.md#832-array-based-representation-of-a-binary-tree">Array-Based Representation</a>
* Recall that Heap has the data structure of _level numbering_.
  * Thus, it can be represented by an Array : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/tree.py#L532">Array Based Tree</a>
    * Advantages of using Array-Based Representation
      1. Allows us to avoid complexities of a node-based tree structure.
      2. Simplicity of identifying last position of the tree : last object in self._data
      3. Dynamic re-size of self._data is O(n) considering the concept of the amortization.

### 9.3.4 Python Heap Implementation
<a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/priority_queues.py#L88">Heap Priority Queue</a>

### 9.3.5 Analysis of a Heap-Based Priority Queue
* Props.) For a Heap-Based Priority Queue with n nodes and log(n) height (∵ <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_00_priority_queues.md#the-height-of-heap">Proposition 9.2</a>)
  * Every operation for Heap-Based Priority Queue is either O(1) or O(log(n))
* Running Time analysis
  * min : O(1)
  * remove_min : O(log(n))
  * add : O(log(n))

### 9.3.6 Bottom-Up Heap Construction
* Consider the case that arbitrary series of n elements are given.
  * If each elements are _added_ to a heap priority queue, worst case of Ω(n log(n)) time may take place.
    * Worst Case : elements are sorted in decreasing order by the keys and every _addition_ incurs _upheap_ operation of O(log(n))
  * Solution : __Bottom-Up Heap Construction__

#### Tech.) Bottom-Up Heap Construction
* Condition
  * n key-value pairs to be stored in a heap are given in advance.
  * For simplicity, assume a complete binary tree
    * i.e.) n satisfies the following equation where h denotes the height.
      * n = 2^h - 1
* How?
  1. Make (2^(h-1)) _[ or (n+1)/2 ]_ elementary heaps : {(n+1)/2} * 1 running time.
  2. Form (2^(h-2)) _[ or (n+1)/4 ]_ heaps with 3 elements : {(n+1)/4} * 2 running time.
  3. Form (2^(h-3)) _[ or (n+1)/8 ]_ heaps with 7 elements : {(n+1)/8} * 3 running time.
  4. ...
  5. Form one heap with n elements : {1} * log(n) running time.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/images/09_03_02_bottom_up_construction_image.png" style="height: 600px;"></img><br/>
</p>


## 9.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_06_exercises.md">Exercises</a>
