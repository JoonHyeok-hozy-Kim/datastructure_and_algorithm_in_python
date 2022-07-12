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

### R-12.19 Suppose S is a sequence of n values, each equal to 0 or 1. How long will it take to sort S with the merge-sort algorithm? What about quick-sort?
* Sol.) Both merge and quick sort may take O(n log(n)) time.

### R-12.20 Suppose S is a sequence of n values, each equal to 0 or 1. How long will it take to sort S stably with the bucket-sort algorithm?
* Sol.) Since possible keys are only 0 and 1, it will take O(n) time.

### R-12.21 Given a sequence S of n values, each equal to 0 or 1, describe an in-place method for sorting S.
```python
def in_place_sort_zero_one(S):
    start = 0
    end = len(S)-1
    while (start < end):
        while S[start] == 0 and start < len(S)-1:
            start += 1
        while S[end] == 1 and end > 0:
            end -= 1
        if start < end:
            S[start] = 0
            S[end] = 1
            start += 1
            end -= 1
    return S

if __name__ == '__main__':
    from random import randint
    a = [randint(0, 1) for i in range(10)]
    # a = [0 for i in range(10)]
    # a = [1 for i in range(10)]
    print(a)
    in_place_sort_zero_one(a)
    print(a)
```

### R-12.22 Give an example input list that requires merge-sort and heap-sort to take O(nlog n) time to sort, but insertion-sort runs in O(n) time. What if you reverse this list?
* Sol.) 
  * A sequence of increasing order may run in O(n) time for an insertion sort algorithm that uses Sorted Priority Queue as a container and appending keys at the end of it.
    * This sequence will run in O(n log(n)) time for merge sort algorithm.
    * If the sequence is reversed, i.e. being in decreasing order, it may run in O(n^2) time for the insertion sort algorithm.

### R-12.23 What is the best algorithm for sorting each of the following: general comparable objects, long character strings, 32-bit integers, double-precision floating-point numbers, and bytes? Justify your answer.
* Sol.
  * general comparable objects
    * Depending on the size of object, if the size is smaller than 50, use insertion sort. If not, use comparison based sortings.
  * long character strings
    * Using the hash function that converts each character into a key, radix sort may be a good choice.
  * 32-bit integers
    * Considering the range between elements, bucket sort may work poorly for this case.
  * double-precision floating-point numbers
    * Can be considered as an application of the long character strings case.
  * bytes

### R-12.24 Show that the worst-case running time of quick-select on an n-element sequence is Ω(n^2).
* Sol.) Consider the case that the pivot is always the first element of the subproblem sequence.
  * And the given input sequence is in decreasing order.
  * Then in every subproblem, all the elements except for the pivot will go to G.
  * Moreover, the height of the quick-sort tree will be n.
  * Therefore, it may be O(n^2) running time total.

### C-12.25 Linda claims to have an algorithm that takes an input sequence S and produces an output sequence T that is a sorting of the n elements in S.
1. Give an algorithm, is sorted, that tests in O(n) time if T is sorted.
```python
def is_sorted(S):
    temp_max = None
    for i in S:
        temp_max = i if temp_max is None else max(temp_max, i)
        if temp_max != i:
            return False
    return True
```
2. Explain why the algorithm is sorted is not sufficient to prove a particular output T to Linda’s algorithm is a sorting of S.
   * Sol.) For some elements such as characters, the comparison rule between such elements is not fixed. 
3. Describe what additional information Linda’s algorithm could output so that her algorithm’s correctness could be established on any given S and T in O(n) time.
   * Sol.) If a table that fixes such rule is provided, any type of sequence may be provable.

### C-12.26 Describe and analyze an efficient method for removing all duplicates from a collection A of n elements.
* Sol.) An algorithm that uses HeapSort that may run in O(n log(n)).
```python
from DataStructures.priority_queues import HeapPriorityQueue
def duplicate_remover_with_heap(S):
    H = HeapPriorityQueue()
    temp_max = None
    cnt = 0
    for i in range(len(S)):
        e = S[i]
        S[i] = None
        H.add(e, e)
    while not H.is_empty():
        if temp_max is None:
            temp_max = H.remove_min()[0]
            S[cnt] = temp_max
            cnt += 1
        else:
            temp = H.remove_min()[0]
            if temp > temp_max:
                S[cnt] = temp
                temp_max = temp
                cnt += 1
    for i in range(len(S)-cnt):
        S.pop()
    return S
```

### C-12.27 Augment the PositionalList class (see Section 7.4) to support a method named merge with the following behavior. If A and B are PositionalList instances whose elements are sorted, the syntax A.merge(B)should merge all elements of B into A so that A remains sorted and B becomes empty. Your implementation must accomplish the merge by relinking existing nodes; you are not to create any new nodes.
* Implementation
```python
class PoistionalList(_DoublyLinkedBase):
    
    # Skip
  
    def merge(self, other):
        """ C-12.27 If A and B are PositionalList instances whose elements are sorted,
            the syntax A.merge(B)should merge all elements of B into A
            so that A remains sorted and B becomes empty."""
        if type(self) != type(other):
            raise TypeError('Merge applicable only to PositionalList.')
        self_walk = self.first()
        other_walk = other.first()

        while not other.is_empty() and self_walk.element() >= other_walk.element():
            next_other_walk = other.after(other_walk)
            self._insert_node_before(self_walk, other_walk._node)
            other._size -= 1
            other_walk = next_other_walk

        while not other.is_empty() and self_walk is not None:
            next_other_walk = other.after(other_walk)
            if self_walk.element() <= other_walk.element():
                self_walk = self.after(self_walk)
            else:
                self._insert_node_before(self_walk, other_walk._node)
                other._size -= 1
                other_walk = next_other_walk

        while not other.is_empty():
            self._insert_node_after(self.last(), other_walk._node)
            other._size -= 1
            other_walk = next_other_walk


    def _insert_node_before(self, p, node):
        node._prev._next = node._next
        node._next._prev = node._prev

        p_node = self._validate(p)
        p_node._prev._next = node
        node._prev = p_node._prev
        p_node._prev = node
        node._next = p_node

        self._size += 1
        return self._make_position(node)

    def _insert_node_after(self, p, node):
        node._prev._next = node._next
        node._next._prev = node._prev

        p_node = self._validate(p)
        p_node._next._prev = node
        node._next = p_node._next
        p_node._next = node
        node._prev = p_node

        self._size += 1
        return self._make_position(node)
```
* Test
```python
if __name__ == '__main__':
    from DataStructures.linked_list import PositionalList
    a = PositionalList()
    b = PositionalList()
    b.add_last(-0.5)
    b.add_last(-1)
    for i in range(5):
        a.add_last(2*i)
        b.add_last(2*i+1)
        b.add_last(2*i+1.5)
    a.merge(b)
    print(a)
    print(b)
```

### C-12.28 Augment the PositionalList class (see Section 7.4) to support a method named sort that sorts the elements of a list by relinking existing nodes; you are not to create any new nodes. You may use your choice of sorting algorithm.
```python
def sort(self, start=None, end=None):
    """ Uses insertion-sort algorithm """
    point = self.first()
    while point is not None:
        walk = point
        while walk is not None and self.before(walk) is not None:
            if walk.element() < self.before(walk).element():
                self.swap(walk, self.before(walk))
            else:
                break
        point = self.after(point)
```



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/part12_00_sorting_and_selection.md">Part 12. Sorting and Selection</a>
</p>