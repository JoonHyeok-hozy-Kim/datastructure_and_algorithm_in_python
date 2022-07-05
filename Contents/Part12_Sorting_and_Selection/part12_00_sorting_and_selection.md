<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 12. Sorting and Selection
## 12.1 Why Study Sorting Algorithms?
#### Concept) Python's natural order definition using < operator.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_01_01_python_operator.png" style="height: 100px;"></img><br/>
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
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_02_01_merge_sort_graphic.png" style="width: 100%;"></img><br/>
</p>

#### Prop.) The height of the Merge-sort tree
* The merge-sort tree associated with an execution of merge-sort on a sequence of size n has height ┌log(n)┐.
  * Justification
    * <a href="">Exercise R-12.1</a>


### 12.2.2 Array-Based Implementation of Merge-Sort
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/SortingAlgorithms/merge_sort.py#L15">Array-Based Merge-Sort</a>


### 12.2.3 The Running Time of Merge-Sort
* Analysis
  1. Running times of operations in a node.
     1. Divide : Running time of halving S into S1 and S1 is O(1).
     2. Merging : Running time of merge() method is O(n1+n2) where n1 and n2 denote the length of S1 and S2.
     3. If the depth of node v is i, the size of the sequence handled by the recursive call associated with v is equal to O(n/2^i).
        * Thus, the time spent at node v is O(n/2^i).  ---> (A)
  2. The number of nodes at depth i is equal to 2^i.  ---> (B)
  3. By (A) and (B), the overall time spent at depth i is O( 2^i * (n/2^i) ) = O(n)
  4. Recall that the height of a merge sort tree is ┌log(n)┐.
  5. Therefore, the running time of merge sort is O(nlog(n))
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_02_02_merge_sort_running_time.png" style="height: 500px;"></img><br/>
</p>

### 12.2.4 Merge-Sort and Recurrence Equations
* An alternative way to justify that the running time of the merge-sort is O(nlog(n)).

#### Recurrence Equation (Recurrence Relation)
* Let t(n) denote the worst-case running time of merge-sort on an input sequence of size n.
  * Consider the case that n is a power of 2.
* Then
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_02_03_recurrence_equation.png" style="height: 100px;"></img><br/>
</p>

* By applying the definition of a recurrence equation, we may obtain the following.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_02_03_recurrence_equation_2.png" style="height: 100px;"></img><br/>
</p>

* It can be generalized into as follows.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_02_03_recurrence_equation_3.png" style="height: 100px;"></img><br/>
</p>

* Since our merge-sort operation's recursive call ends when external nodes have one elements each, it can be said that the operation ends when n = 2^i where i is the depth of the merge-sort tree.
* Thus, by putting log(n) into i, we may obtain the following.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_02_03_recurrence_equation_4.png" style="height: 200px;"></img><br/>
</p>


## 12.8 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/part12_08_exercises.md">Exercises</a>
