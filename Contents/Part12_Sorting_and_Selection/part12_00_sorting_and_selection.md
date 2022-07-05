<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 12. Sorting and Selection
## 12.1 Why Study Sorting Algorithms?
#### Concept) Python's natural order definition using < operator.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_01_01_python_operator.png" style="height: 200px;"></img><br/>
</p>

#### Concept) Sorting Algorithms that we already handled
* Insertion-sort (see Sections 5.5.2, 7.5, and 9.4.1)
  * <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part05_Array_Based_Sequences/part05_00_array_based_sequences.md#concept-the-insertion-sort-algorithm">5.5.2 Insertion-sort for Array</a> 
  * <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part07_Linked_LIsts/part07_00_linked_lists.md#tech-insertion-sort-algorithm-for-the-positional-list">7.5 Insertion-sort for Positional List</a> 
  * <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part09_Priority_Queues/part09_00_priority_queues.md#insertion-sort">9.4.1 Insertion-sort for Priority Queue</a> 
* Selection-sort (see Section 9.4.1)
  * <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part09_Priority_Queues/part09_00_priority_queues.md#selection-sort">9.4.1 Selection-sort for Priority Queue</a> 
* Bubble-sort (see Exercise C-7.38)
  * <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part07_Linked_LIsts/part07_08_exercises.md#c-738-there-is-a-simple-but-inefficient-algorithm-called-bubble-sort-for-sorting-a-list-l-of-n-comparable-elements-this-algorithm-scans-the-list-n1-times-where-in-each-scan-the-algorithm-compares-the-current-element-with-the-next-one-and-swaps-them-if-they-are-out-of-order-implement-a-bubble-sort-function-that-takes-a-positional-list-l-as-a-parameter-what-is-the-running-time-of-this-algorithm-assuming-the-positional-list-is-implemented-with-a-doubly-linked-list">Exercise C-7.38 Bubble-sort for Array</a> 
* Heap-sort (see Section 9.4.2)
  * <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part09_Priority_Queues/part09_00_priority_queues.md#942-heap-sort">9.4.2 Heap-sort for Array</a> 


#### Concept) Sorting Algorithms that we will deal with in this chapter.
* Merge-sort
* Quick-sort
* Bucket-sort
* Radix-sort


## 12.2 Merge-Sort
### 12.2.1 Divide-and-Conquer
* Structure
  1. **Divide**
     * If the input size is smaller than a certain threshold (say, one or two elements), solve the problem directly using a straightforward method and return the solution so obtained. 
     * Otherwise, divide the input data into two or more disjoint subsets.
  2. **Conquer**
     * Recursively solve the subproblems associated with the subsets.
  3. **Combine**
     * Take the solutions to the subproblems and merge them into a solution to the original problem

* Settings
  * ┌x┐ 
    * the ceiling of x
    * the smallest integer k such that k >= x 
  * └x┘
    * the floor of x
    * the largest integer m such that m <= x

* How?
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_02_01_merge_sort_graphic.png" style="height: 450px;"></img><br/>
</p>

## 12.8 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/part12_08_exercises.md">Exercises</a>
