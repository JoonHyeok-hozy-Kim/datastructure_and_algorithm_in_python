<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/part12_00_sorting_and_selection.md">Part 12. Sorting and Selection</a>
</p>

### R-12.1 Give a complete justification of Proposition 12.1.
* Justification
  * This problem is basically identical to building a binary tree with n external nodes.
  * A minor difference must be that when n=1, the algorithm returns the sequence without sorting. Thus, the height is zero.
    * In other words, the height here is equal to the depth of a binary tree with n external nodes.

### R-12.2 In the merge-sort tree shown in Figures 12.2 through 12.4, some edges are drawn as arrows. What is the meaning of a downward arrow? How about an upward arrow?
* Sol.) Downward means the division and Upward means the conquering of the merge-sort algorithm.

### R-12.3 Show that the running time of the merge-sort algorithm on an n-element sequence is O(n log(n)), even when n is not a power of 2.
* Sol.
  * The running time of operations at external node v may be either O(n/2^i) or O(n/2^(i+1)) depending on the depth of the node.
  * Thus, only scalar time difference between the nodes.
  * Recall that the height is ┌log(n)┐.
  * Therefore, the running time is either O(n) or O(2n) which is eventually O(n).

### R-12.4 Is our array-based implementation of merge-sort given in Section 12.2.2 stable? Explain why or why not.
* Sol.) Stable
  * < operator secures the sequence of elements depending on the size.

### R-12.5 Is our linked-list-based implementation of merge-sort given in Code Fragment 12.3 stable? Explain why or why not.
* Sol.) Stable
  * < operator secures the sequence of elements depending on the size.

### R-12.6 An algorithm that sorts key-value entries by key is said to be straggling if, any time two entries e_i and e_j have equal keys, but e_i appears before e_j in the input, then the algorithm places e_i after e_j in the output. Describe a change to the merge-sort algorithm in Section 12.2 to make it straggling.
* Sol.) By changing the comparison operator from < to <= we can achieve the strangling objective.
```python
def _merge_array(S1, S2, S):
    """ Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] <= S2[j]):  ## Here!
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
```

### R-12.7 Suppose we are given two n-element sorted sequences A and B each with distinct elements, but potentially some elements that are in both sequences. Describe an O(n)-time method for computing a sequence representing the union A∪B (with no duplicates) as a sorted sequence.
```python
def sorted_union(A, B):
    result = [None] * (len(A)+len(B))
    i = j = 0
    eq_cnt = 0
    while i+j < len(A)+len(B):
        if i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result[i+j-eq_cnt] = A[i]
                if A[i] == B[j]:
                    result.pop()
                    j += 1
                    eq_cnt += 1
                i += 1
            else:
                result[i+j-eq_cnt] = B[j]
                j += 1
        elif j == len(B):
            result[i+j-eq_cnt] = A[i]
            i += 1
        else:
            result[i+j-eq_cnt] = B[j]
            j += 1
        # print('i: {}, j: {}, {}'.format(i, j, result))

    return result
```

### R-12.8 Suppose we modify the deterministic version of the quick-sort algorithm so that, instead of selecting the last element in an n-element sequence as the pivot, we choose the element at index └n/2┘. What is the running time of this version of quick-sort on a sequence that is already sorted?
* Sol.) For a sequence that is already sorted, this algorithm will run in O(n log(n)) time with perfectly balanced quick-sort tree.

### R-12.9 Consider a modification of the deterministic version of the quick-sort algorithm where we choose the element at index └n/2┘ as our pivot. Describe the kind of sequence that would cause this version of quick-sort to run in Ω(n^2) time.
* Sol.) Following sequence will run in O(n^2) time.
  * [2, 4, 6, 7, 5, 3, 1]

### R-12.10 Show that the best-case running time of quick-sort on a sequence of size n with distinct elements is Ω(nlogn).
* Sol.) Consider the case of choosing the first element as the pivot and the given sequence is as follows.
  * [4, 2, 1, 3, 6, 5, 7]

### R-12.11 Suppose function inplace quick sort is executed on a sequence with duplicate elements. Prove that the algorithm still correctly sorts the input sequence. What happens in the partition step when there are elements equal to the pivot? What is the running time of the algorithm if all the input elements are equal?
* Sol.)
  * When an element is equal to pivot, the operation of shifting left or right is skipped until left and right positions cross.
  * When all elements are equal, the algorithm will run in O(n log(n)) time, with the perfectly balanced quick-sort tree.

### R-12.12 If the outermost while loop of our implementation of inplace quick sort (line 7 of Code Fragment 12.6) were changed to use condition left < right (rather than left <= right), there would be a flaw. Explain the flaw and give a specific input sequence on which such an implementation fails.
* Sol.)
  * When the subsequence has two elements, the problem pops out.
  * Since the equality of left and right can not go into the while loop, left will remain pivot-1.
  * Thus, no matter what value is contained in S[0] and S[pivot], they will swap the value.
    * In case S[0] < S[pivot], it is fault.

### R-12.13 If the conditional at line 14 of our inplace quick sort implementation of Code Fragment 12.6 were changed to use condition left < right (rather than left <= right), there would be a flaw. Explain the flaw and give a specific input sequence on which such an implementation fails.
* Sol.)
  * Similar to R-12.12, when left and right are referenced to the same index, if the operator is < instead of <=, left and right will not cross.
  * Again when the subsequence is reduced to the length 2, the first and the second element will be swapped regardless of the size.

### R-12.14 Following our analysis of randomized quick-sort in Section 12.3.1, show that the probability that a given input element x belongs to more than 2logn subproblems in size group i is at most 1/n2.
* Sol.) If an element belongs to every subproblem it should be the minimum or the maximum value of the sequence.
  * Even so, it may belong to at most log(n) subproblems.
  * Theoretically, if an element belongs to the 2*log(n) subproblems, it should be simultaneously the minumum and the maximum value of the sequence.

### R-12.15 Of the n! possible inputs to a given comparison-based sorting algorithm, what is the absolute maximum number of inputs that could be correctly sorted with just n comparisons?
* Sol.) Among all the inner nodes in a comparison-based sorting tree, if at most one node's sequence is reversed, the total comparison may be equal to n.
  * Since the number of inner nodes is 2^(n-1)-1, there are 2^(n-1)-1 such cases among n!.

### R-12.16 Jonathan has a comparison-based sorting algorithm that sorts the first k elements of a sequence of size n in O(n) time. Give a big-Oh characterization of the biggest that k can be?

### R-12.17 Is the bucket-sort algorithm in-place? Why or why not?
* Sol.) No. It uses additional container, the bucket, that temporarily stores elements.

### R-12.18 Describe a radix-sort method for lexicographically sorting a sequence S of triplets (k,l,m), where k, l, and m are integers in the range [0,N −1], for some N ≥ 2. How could this scheme be extended to sequences of d-tuples (k1,k2,...,kd ), where each ki is an integer in the range [0,N −1]?
* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/SortingAlgorithms/linear_time_sort.py#L41">Radix Sort</a>
* Test
```python
if __name__ == '__main__':
    from SortingAlgorithms.linear_time_sort import radix_sort
    c = []
    from copy import deepcopy
    for i in range(5):
        d = [5-i, None, None]
        for j in range(5):
            d_1 = deepcopy(d)
            d_1[1] = 5-j
            for k in range(5):
                d_2 = deepcopy(d_1)
                d_2[2] = 5-k
                c.append(d_2)
    print(c)
    radix_sort(c, 3)
    print(c)
```





<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/part12_00_sorting_and_selection.md">Part 12. Sorting and Selection</a>
</p>