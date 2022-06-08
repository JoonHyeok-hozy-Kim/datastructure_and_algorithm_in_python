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
<img src="" style="height: 300px;"></img><br/>
</p>


## 9.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_06_exercises.md">Exercises</a>
