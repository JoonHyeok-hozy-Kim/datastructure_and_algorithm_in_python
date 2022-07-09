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

* Since our merge-sort operation's recursive call ends when external nodes have one element each, it can be said that the operation ends when n = 2^i where i is the depth of the merge-sort tree.
* Thus, by putting log(n) into i, we may obtain the following.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_02_03_recurrence_equation_4.png" style="height: 200px;"></img><br/>
</p>

### 12.2.5 Alternative Implementations of Merge-Sort
#### Tech.) Sorting Linked Lists (Using Linked Queue)
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/SortingAlgorithms/merge_sort.py#L48">Merge-sort for LinkedQueue</a>

#### Tech.) A Bottom-Up (Nonrecursive) Merge-Sort
* Why doing this?
  * Recursion that we used in the previous algorithm may slower the sorting operation due to the additional memory usage for it.
  * Solution avoiding the recursion.
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/SortingAlgorithms/merge_sort.py#L90">A Bottom-Up (Nonrecursive) Merge-Sort</a>


## 12.3 Quick-Sort
#### Tech.) High-Level Description of Quick-Sort
* How?
  * Recursive approach
  * Divide-and-conquer technique
    1. Divide S into subsequences
       1. If len(S) <= 1, return.
       2. Select a specific item x as pivot.
       3. Commonly choose the last item in S as x
       4. Remove all the elements from S and put them into three sequences:
          * L : storing the elements in S less than x
          * E : storing the elements in S equal to x
          * G : storing the elements in S greater than x
    2. Conquer: Recursively sort sequences L and G.
    3. Combine: Put back the elements into S in order by first inserting the elements of L, then those of E, and finally those of G.

#### Tech.) Performing Quick-Sort on General Sequences
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/SortingAlgorithms/quick_sort.py#L4">Quick Sort</a>

#### Analysis) Running Time of Quick-Sort
* Conclusion
  * the overall running time of quick-sort is O(n*h)
* Justification
  * Dividing step and final concatenation runs in linear time : O(n)
    * Let
      * v : a node
      * s(v) : the input size of v
      * Then, the time spent for dividing and concatenating is proportional to s(v)
  * Height does matter.
    * Let
      * i : the depth of a quick-sort tree
      * s_i : the input size with depth i
      * Then s_0 = n
      * s_i < s_(i-1)
        * why?
          * At least one element, the pivot, will go to set E and will not go down to children node.
      * Thus, the height of the tree h matters.
  * Therefore, the overall running time of quick-sort is O(n*h)
    * Worst case : O(n^2)
      * When the given sequence is already sorted.
    * Other than the worst case : O(n log(n))
      * Ideal Case : Each node is split perfectly by the pivot.
      * Generally, even one-fourth / three-fourth split may obtain O(n log(n)) running time.

    
### 12.3.1 Randomized Quick-Sort
* Why doing this?
  * Recall that ideal running time of quick-sort can be achieved if the pivots always divide the sequence in a reasonably balanced manner.
  * Picking pivots at random may approximately let pivots to the middle of the set elements.

#### Concept) Picking Pivots at Random
* How?
  * Pick an element of S at random as the pivot
    * Rather than fixing the position of the pivot at the starting or the ending point of a sequence.

#### Prop.) The expected running time of randomized quick-sort on a sequence S of size n is O(n log(n)).
* Justification
  * It is known that if pivot lays at spot between 1/4 and 3/4 of the sequence the quick sort tree is balanced and O(n log(n)) is possible.
    * i.e.) L and G have size at least n/4 and at most 3n/4 each.
  * Then the probability that a random pivot may be good is 1/2.
    * why?)
      * There are n/2 good choices for the pivot that satisfies the sizes of L and G between n/4 to 3n/4.
  * Analysis on the expected time spent working on all the subproblems for nodes in _size group i_
    * Concept) _size group i_
      * For a node v in a tree T, v is in _size group i_ if the size of v's subproblem is between n*(3/4)^(i+1) and n*(3/4)^i.
    * By the linearity of expectation, the expected time of all these subproblems is the sum of the expected times for each.
      * Some of these subproblems may make good call while others make bad calls.
      * Since the probability of making good call is 1/2, the expected number of consecutive calls that should be made before getting a good call is 2.
      * Thus, for any element x in the input list, the expected number of nodes in _size group i_ containing x in their subproblem is 2.
      * Hence, the expected total size of all the subproblems in the _size group i_ is 2n.
      * Since non-recursive operations in subproblems are proportional to the sizes of the nodes, they run in O(n). ---> (A)
  * The number of size groups is log_(4/3)n.
    * why?)
      * Consider the height of a tree that is divided in to 1/4 and 3/4.
    * Thus, the number of size groups is O(log(n))
  * Therefore, by (A) and (B) the total expected running time of randomized quick-sort is O(n log(n)).
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_03_01_randomized_quick_sort.png" style="height: 600px;"></img><br/>
</p>


### 12.3.2 Additional Optimizations for Quick-Sort
#### Tech.) In-Place Quick-Sort Algorithm
* Target
  * Using minimum memory.
  * Recall that our previous quick-sort uses additional three containers.
    * Instead, we can save memory by recursively swapping the elements in the input list.
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/SortingAlgorithms/quick_sort.py#L32">In-Place Quick-Sort</a>


#### Tech.) Median-of-Three Heuristic for Pivot Selection
* How?
  * From each input array, consider the front, middle, and tail of it and choose the median of them as the pivot.
* Advantage
  * Requires lower overhead than using random number generator for randomized pivot selection.


#### Tech.) Hybrid Approaches
* How?
  * Use divide-and-conquer algorithm until the subsequence falls below some threshold (perhaps 50 elements).
  * Then use insertion sort for the rest of the subsequences.
* Advantage
  * Divide-and-conquer algorithm have good performance for large data sets.
  * However, it's required overhead is too costly for the small data sets.
  * Thus, simple sorting algorithms such as insertion sort is faster for small data sets.
  * Therefore, it is wise to take hybrid method of both of them.


## 12.4 Studying Sorting through an Algorithmic Lens
### 12.4.1 Lower Bound for Sorting
#### Q.) Can we sort faster than O(n log(n))?
* Answer
  * If the computational primitive used by a sorting algorithm is the
comparison of two elements, this is in fact the best we can do.
  * Comparison-based sorting has an Ω(n log(n)) worst-case lower bound on its running time.
* Justification
  1. Each time a sorting algorithm compares two elements x_i and x_j (x_i < x_j ?), there are two results : yes or no.
     * This can be depicted with the decision tree.
     * Then this tree represents all the possible sequences of comparisons.
  2. Each possible initial order, or the permutation of the items, has unique decision tree.
  3. By 1 and 2, there can be n! external nodes for the decision trees Ts.
     * Considering that n! >= (n/2)^(n/2)
     * log(n!) >= log((n/2)^(n/2)) >= (n/2)*(log(n/2))
     * Therefore, Ω(n log(n)).
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_04_01_lower_bound.png" style="height: 600px;"></img><br/>
</p>

### 12.4.2 Linear-Time Sorting: Bucket-Sort and Radix-Sort
#### Tech.) Bucket-Sort
* How?
  1. Let 
     * S : a sequence of n integers in the range [0, N-1] for some integer N >= 2.
     * B[k] : a bucket with the key k where 0 <= k <= N-1.
  2. For each integer k, remove from S and insert into the bucket B[k].
  3. For each bucket B[k], remove element and insert into S again.
* Performance
  * Running Time : O(n+N)
    * This is the linear running time!
  * However, if N is too big, i.e. the range of integers is too wide, the performance will drop sharply.
* Prop.
  * This algorithm also work for the repeated keys and derive non-decreasing order result.
* Psuedo Code
```python
Algorithm bucketSort(S):
  Input: Sequence S of entries with integer keys in the range [0,N−1]
  Output: Sequence S sorted in nondecreasing order of the keys
  
    let B be an array of N sequences, each of which is initially empty
    for each entry e in S do
        k = the key of e
        remove e from S and insert it at the end of bucket (sequence) B[k]
    for i = 0 to N−1 do
        for each entry e in sequence B[i] do
            remove e from B[i] and insert it at the end of S
```

#### Tech.) Stable Sorting
* Concept) Stability
  * For any i and j such that (k_i, v_i) precedes (k_j, v_j) in the initial sequence,
  * if (k_i, v_i) still precedes (k_j, v_j) after the sorting
  * the sorting algorithm is stable.
* Prop.) The stability of the previous bucket sort.
  * Recall that each element is inserted at the end of the bucket and removed from the beginning.
  * As long as this sequence is kept, the stability is guaranteed.

#### Tech.) Radix-Sort
* Target : Lexicographical sorting of multi-length elements.
* How?
  * Sort from the last key to the first.
  * Check the example below.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_04_02_radix_1.png" style="width: 90%;"></img><br/>
</p>

* Performance
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_04_02_radix_2.png" style="width: 90%;"></img><br/>
</p>


## 12.5 Comparing Sorting Algorithms
#### Sorting Algorithms that we covered
1. O(n^2) sorting algorithms
   1. Selection Sort
      * Poorest performance
   2. Insertion Sort
      * Efficient for length less than 50 or already almost sorted sequence.
      * Number of inversion increases drastically if the number of elements is bigger than 50.
2. O(n log(n)) sorting algorithms
   1. Heap Sort
      * Advantage
        * Can easily be made to execute in-place
        * A natural choice on small- and medium-sized sequences, when input data can fit into main memory. 
      * Disadvantage
        * Tends to be outperformed by both quick-sort and merge-sort on larger sequences. 
        * A standard heap-sort does not provide a stable sort, because of the swapping of elements.
   2. Merge Sort
      * Advantage
        * O(nlogn) time in the worst case
        * An excellent algorithm for situations where the input is stratified across various levels of the computer’s memory hierarchy (e.g., cache, main memory, external memory).
      * Disadvantage
        * Difficult to make merge-sort run in-place for arrays
   3. Quick Sort
      * Advantage
        * Expected O(n log(n)) performance
        * in-memory sorting algorithm
      * Disadvantage
        * Does not naturally provide a stable sort, due to the swapping of elements during the partitioning step.
        * Worst case O(n^2) running time.
3. Linear time sorting algorithms
   1. Bucket Sort
      * Suitable for entries with small integer keys
      * Runs in O(d(n+N)) time
   2. Radix Sort
      * Suitable for entries with character strings, or d-tuples of keys from a discrete range
      * Runs in O(d(n+N)) time


## 12.6 Python’s Built-In Sorting Functions
### 12.6.1 Sorting According to a Key Function
#### Tech.) Key function of Python's sorting function
* Key function allows various sortings according to some order other than the natural order defined by the < operator.
  * ex.) len
```python
if __name__ == '__main__':
    from random import randint
    a = []
    for i in range(10):
        temp = []
        for j in range(randint(1,5)):
            temp.append(chr(randint(65, 80)))
        a.append(''.join(temp))
    print(a)
    print(sorted(a))
    print(sorted(a, key=len))
```

* How it works?
  * key parameter provides reference to secondary function that computes key for each element of the primary sequence.

#### Tech.) Decorate-Sort-Undecorate Design Pattern
* Steps
  1. Each element of the list is temporarily replaced with a “decorated” version that includes the result of the key function applied to the element.
  2. The list is sorted based upon the natural order of the keys.
  3. The decorated elements are replaced by the original elements.
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/SortingAlgorithms/merge_sort.py#L103">Decorated Merge Sort</a>


## 12.8 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/part12_08_exercises.md">Exercises</a>
