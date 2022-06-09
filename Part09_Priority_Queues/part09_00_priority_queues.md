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
  5. Form __one__ heap with n elements : {1} * log(n) running time.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/images/09_03_02_bottom_up_construction_image.png" style="height: 600px;"></img><br/>
</p>

#### Analysis) Asymptotic Analysis of Bottom-Up Heap Construction
* Prop.) Bottom up construction of a heap with n entries takes O(n) time, assuming two keys can be compared in O(1) time.

### 9.3.7 Python’s heapq Module
* No priority queue class provided by Python.
* Instead, __heapq__ function allow us to manage Python's List class as a heap.
  * elements serve as their own key.
* Functions, where L is a list and e an element.
  * heappush(L, e)
    * Push element in O(log(n)) time
  * heappop(L)
    * Pop and return the smallest element in O(log(n)) time
  * heappushpop(L, e)
    * Push and Pop.
    * Slightly efficient than independent push and pop operation, on the point that total length of the list is unchanged.
  * heapreplace(L, e)
    * Pop and then push.
  * heapify(L)
    * transform unordered list to satisfy heap-order property
  * nlargest(k, iterable)
    * Produce a list of the k largest values from a given iterable.
    * O(n+klog(n)) time
  * nsmallest(k, iterable)
    * Produce a list of the k smallest values from a given iterable.
    * O(n+klog(n)) time

## 9.4 Sorting with a Priority Queue
### 9.4.1 Selection-Sort and Insertion-Sort
#### Selection Sort
* Analysis
  * add takes O(1) running time.
  * return_min takes O(n^2) time.
```python
from DataStructures.priority_queues import UnsortedPriorityQueue
def selection_sort(C):
    n = len(C)
    P = UnsortedPriorityQueue()
    for i in range(n):
        e = C.delete(C.first())
        P.add(e, e)
    while not P.is_empty():
        (k, v) = P.remove_min()
        C.add_last(v)
```

#### Insertion Sort
* Analysis
  * add takes O(n^2) running time.
  * return_min takes O(1) time.
* Implementation
  * Assume that the collection C is a PositionalList
```python
from DataStructures.priority_queues import SortedPriorityQueue
def insertion_sort(C):
    n = len(C)
    P = SortedPriorityQueue()
    for i in range(n):
        e = C.delete(C.first())
        P.add(e, e)
    while not P.is_empty():
        (k, v) = P.remove_min()
        C.add_last(v)
```

### 9.4.2 Heap-Sort
* Analysis
  * add takes O(nlog(n)) time.
    * why?)
      * i-th addition takes O(log(i)) running time.
      * Summing all the addition, it becomes O(nlog(n))
  * remove_min takes O(log(n)) time.
    * why?)
      * remove the root element in O(1)
      * replace last position and perform downheap in O(log(n))
  * cf.) If bottom-up can be applied, it will take O(n) running time.
  
#### Implementation
* Concept) in-place
  * A sorting algorithm is _in-place_ if it uses only a small amount of memory in addition to the sequence storing the objects to be sorted.
```python
from DataStructures.priority_queues import HeapPriorityQueue
def heap_sort(C):
    n = len(C)
    H = HeapPriorityQueue()
    for i in range(n):
        e = C.delete(C.first())
        H.add(e, e)
    while not H.is_empty():
        (k, v) = H.remove_min()
        C.add_last(v)
```

### 9.5 Adaptable Priority Queues
* Why needed?
  * More functions required
    1. Removing certain elements in the middle of the Priority Queue
    2. Adding new elements in to the certain position of the Priority Queue

### 9.5.1 Locators
* Goal
  * Create a mechanism that prevents the linear search through the entire collection

#### Locator
* An object that should be provided when invoking _update_ or _remove_ method.
  * ex.)
    * P.update(loc, k, v)
    * P.remove(loc)
* Different from the Position object on the point that locator does not represent a tangible placement of an element within the sturcture.
  * Relocation does not directly affect the element.
  * Locator for an element will remain valid as long as that item remains somewhere in the queue.

### 9.5.2 Implementing an Adaptable Priority Queue
* <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/DataStructures/priority_queues.py#L157">Adaptable Priority Queue</a>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/images/09_05_01_adaptable_priority_queue_running_time.png" style="height: 300px;"></img><br/>
</p>


## 9.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_06_exercises.md">Exercises</a>
