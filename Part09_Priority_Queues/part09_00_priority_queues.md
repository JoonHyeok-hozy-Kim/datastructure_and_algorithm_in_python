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

## 9.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part09_Priority_Queues/part09_06_exercises.md">Exercises</a>
