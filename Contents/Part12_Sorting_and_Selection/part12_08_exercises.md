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

### C-12.29 Implement a bottom-up merge-sort for a collection of items by placing each item in its own queue, and then repeatedly merging pairs of queues until all items are sorted within a single queue.
* Implementation and Test
```python
from DataStructures.queue import LinkedQueue
def bottom_up_merge_sort(S):
    Q = LinkedQueue()
    if len(S) == 1:
        Q.enqueue(S[0])
    else:
        mid = len(S)//2
        Q1 = bottom_up_merge_sort(S[:mid])
        Q2 = bottom_up_merge_sort(S[mid:])
        while not (Q1.is_empty() and Q2.is_empty()):
            if Q2.is_empty():
                while not Q1.is_empty():
                    Q.enqueue(Q1.dequeue())
            elif Q1.is_empty():
                while not Q2.is_empty():
                    Q.enqueue(Q2.dequeue())
            elif Q1.first() < Q2.first():
                Q.enqueue(Q1.dequeue())
            else:
                Q.enqueue(Q2.dequeue())
    return Q

if __name__ == '__main__':
    from random import randint
    a = [randint(0,100) for i in range(10)]
    print(a)
    q = bottom_up_merge_sort(a)
    while not q.is_empty():
        print(q.dequeue(), end=', ')
```

### C-12.30 Modify our in-place quick-sort implementation of Code Fragment 12.6 to be a randomized version of the algorithm, as discussed in Section 12.3.1.
```python
from random import randint
def inplace_quick_sort(S, a=0, b=None):
    if b is None:
        b = len(S)-1
    if a >= b: return

    # Random pivot selection
    p = randint(a, b)
    S[p], S[b] = S[b], S[p]

    pivot = S[b]
    left = a
    right = b-1
    # print('[Initial] pivot : {}, {}'.format(pivot, S))
    while left <= right:
        # print(' -> left : {}'.format(S[left]), end='')
        while left <= right and S[left] < pivot:
            left += 1
        #     print(' -> {}'.format(S[left]), end='')
        # print('\n -> right : {}'.format(S[right]), end='')
        while left <= right and pivot < S[right]:
            right -= 1
            # print(' -> {}'.format(S[right]), end='')

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
            # print('\n[After swap 1] {}'.format(S))
            # print(' left : {}, right : {}'.format(S[left], S[right]))

    S[left], S[b] = S[b], S[left]
    # print('\n[After swap 2] {}'.format(S))

    # if a < left-1:
    #     print('\n[Recursion 1] {} ~ {}'.format(S[a], S[left-1]))
    # else:
    #     print('[Recursion 1] RETURN')
    inplace_quick_sort(S, a, left-1)
    # if left+1 < b:
    #     print('\n[Recursion 2] {} ~ {}'.format(S[left+1], S[b]))
    # else:
    #     print('[Recursion 2] RETURN')
    inplace_quick_sort(S, left+1, b)

if __name__ == '__main__':
    from SortingAlgorithms.quick_sort import inplace_quick_sort
    a = [randint(0, 100) for i in range(10)]
    print(a)
    inplace_quick_sort(a)
    print(a)
```

### C-12.31 Consider a version of deterministic quick-sort where we pick as our pivot the median of the d last elements in the input sequence of n elements, for a fixed, constant odd number d ≥ 3. What is the asymptotic worst-case running time of quick-sort in this case?
* Sol.) O( (n+d) log(n) )

### C-12.32 Another way to analyze randomized quick-sort is to use a recurrence equation. In this case, we let T(n) denote the expected running time of randomized quick-sort, and we observe that, because of the worst-case partitions for good and bad splits, we can write
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/images/12_08_31.png" style="height: 200px;"></img><br/>
</p>

### C-12.33 Our high-level description of quick-sort describes partitioning the elements into three sets L, E, and G, having keys less than, equal to, or greater than the pivot, respectively. However, our in-place quick-sort implementation of Code Fragment 12.6 does not gather all elements equal to the pivot into a set E. An alternative strategy for an in-place, three-way partition is as follows. Loop through the elements from left to right maintaining indices i, j, and k and the invariant that all elements of slice S[0:i] are strictly less than the pivot, all elements of slice S[i:j] are equal to the pivot, and all elements of slice S[j:k] are strictly greater than the pivot; elements of S[k:n] are yet unclassified. In each pass of the loop, classify one additional element, performing a constant number of swaps as needed. Implement an in-place quick-sort using this strategy.
```python
def in_place_equal_considered(S):
    n = len(S)
    if n == 1:
        return S
    p = n-1
    while True:
        k = p
        while k > 0 and S[k-1] > S[p] and S[k-1] <= S[k]:
            k -= 1
        j = k
        if j > 0:
            while j > 0 and S[j-1] == S[p]:
                j -= 1
        i = j
        if i > 0:
            while i > 0 and S[i-1] < S[p] and S[i-1] <= S[i]:
                i -= 1

        # print('{} [i:{}, j:{}, k:{}]'.format(S, i, j, k))

        if i == 0:
            temp = S[p]
            l = n-1
            while l > k:
                S[l] = S[l-1]
                l -= 1
            S[k] = temp
            return

        else:
            temp = S[i-1]
            l = i-1
            while l < j-1:
                S[l] = S[l+1]
                l += 1
            S[j-1] = S[p]
            S[p] = temp

if __name__ == '__main__':
    from random import randint
    a = [randint(1,7) for i in range(10)]
    print(a)
    in_place_equal_considered(a)
    print(a)
```

### C-12.34 Suppose we are given an n-element sequence S such that each element in S represents a different vote for president, where each vote is given as an integer representing a particular candidate, yet the integers may be arbitrarily large (even if the number of candidates is not). Design an O(nlogn)-time algorithm to see who wins the election S represents, assuming the candidate with the most votes wins.
```python
from SortingAlgorithms.quick_sort import inplace_quick_sort
def election_winner(S):
    race = [[S[0], 0], [None, None]]
    inplace_quick_sort(S)
    for i in S:
        if i == race[0][0]:
            race[0][1] += 1
        else:
            if race[1][0] is None:
                race[1][0] = i
                race[1][1] = 1
            elif race[1][0] == i:
                race[1][1] += 1

                if race[0][1] < race[1][1]:
                    race[0][0] = race[1][0]
                    race[0][1] = race[1][1]
                    race[1][0] = None
                    race[1][1] = None
            else:
                race[1][0] = i
                race[1][1] = 1

    return race[0][0] if (race[1][1] is None or race[0][1] > race[1][1]) else None

if __name__ == '__main__':
    from random import randint
    a = [randint(0,5) for i in range(1000)]
    print(a)
    w = election_winner(a)
    print(w)
```

### C-12.35 Consider the voting problem from Exercise C-12.34, but now suppose that we know the number k < n of candidates running, even though the integer IDs for those candidates can be arbitrarily large. Describe an O(nlogk)-time algorithm for determining who wins the election.
```python
def candidate_known_election_winner(S, k):
    candidates = [[None, None] for i in range(k)]
    for e in S:
        for i in range(k):
            if candidates[i][0] is None:
                candidates[i][0] = e
                candidates[i][1] = 0
                break
            elif candidates[i][0] == e:
                candidates[i][1] += 1
                if candidates[i][1] > candidates[0][1]:
                    candidates[0], candidates[i] = candidates[i], candidates[0]
    # print(candidates)
    return candidates[0][0]

if __name__ == '__main__':
    from random import randint
    a = [randint(1,5) for i in range(1000)]
    print(a)
    w = candidate_known_election_winner(a, 4)
    print(w)
```

### C-12.36 Consider the voting problem from Exercise C-12.34, but now suppose the integers 1 to k are used to identify k < n candidates. Design an O(n)-time algorithm to determine who wins the election.
```python
def k_less_than_n_election_winner(S):
    candidates = []
    leader = None
    for e in S:
        if len(candidates) < e:
            for i in range(len(candidates), e):
                candidates.append([i, 1])
        else:
            candidates[e-1][1] += 1
    # print(candidates)
    for c in range(len(candidates)):
        if leader is None:
            leader = c
        else:
            if candidates[c][1] > candidates[leader][1]:
                leader = c
    return leader+1

if __name__ == '__main__':
    from random import randint
    a = [randint(1,5) for i in range(10)]
    print(a)
    w = k_less_than_n_election_winner(a)
    print(w)
```

### C-12.37 Show that any comparison-based sorting algorithm can be made to be stable without affecting its asymptotic running time.
* Sol.)
  * Suppose not, i.e., there exists elements k_1 and k_2 in a sequence initially sorted by a comparison based sorting algorithm and k_1 preceded k_2.
  * However, after an additional identical comparison sorting, k_1 ended up positioned somewhere after k_2.
  * By the definitions of comparison sorting algorithms, k_1 < k_2 considering the initial sorted sequence.
  * Then by the second sorting, k_1 > k_2. ---> Contradiction.

### C-12.38 Suppose we are given two sequences A and B of n elements, possibly containing duplicates, on which a total order relation is defined. Describe an efficient algorithm for determining if A and B contain the same set of elements. What is the running time of this method?
```python
from SortingAlgorithms.quick_sort import inplace_quick_sort
def sequence_elements_comparison(S, T):
    inplace_quick_sort(S)
    inplace_quick_sort(T)
    s_i = 0
    t_i = 0
    while s_i < len(S) and t_i < len(T):
        target = T[t_i]

        if S[s_i] == T[t_i]:
            while s_i < len(S) and S[s_i] == target:
                s_i += 1
        else:
            return False
        while t_i < len(T) and T[t_i] == target:
            t_i += 1

    return True if s_i == len(S) and t_i == len(T) else False
```

### C-12.39 Given an array A of n integers in the range [0,n^2 − 1], describe a simple method for sorting A in O(n) time.
```python
def squared_range_sorting(S):
    n = len(S)
    buckets = [[] for i in range(n)]
    for e in S:
        root = int(pow(e, .5))
        # print('e : {}, root : {}'.format(e, root))
        idx = 0
        if len(buckets[root]) == 0:
            buckets[root].append(e)
        else:
            for i in buckets[root]:
                if i < e:
                    idx += 1
                else:
                    break
            buckets[root].insert(idx, e)
        # print(buckets)
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result

if __name__ == '__main__':
    from random import randint
    n = 10
    a = [randint(0, n*n-1) for i in range(n)]
    print(a)
    s_a = squared_range_sorting(a)
    print(s_a)
```

### C-12.40 Let S1,S2,...,Sk be k different sequences whose elements have integer keys in the range [0,N −1], for some parameter N ≥ 2. Describe an algorithm that produces k respective sorted sequences in O(n+N) time, were n denotes the sum of the sizes of those sequences.
```python
def sort_sequences(seq_set, N):
    buckets = [[i, []] for i in range(N)]
    for j in range(len(seq_set)):
        for k in range(len(seq_set[j])):
            val = seq_set[j][k]
            buckets[val][1].append(j)
        seq_set[j] = []

    for bucket in buckets:
        for j in bucket[1]:
            seq_set[j].append(bucket[0])
    return seq_set

if __name__ == '__main__':
    from random import randint
    N = 10
    k = 5
    seq_set = [[randint(0, N-1) for i in range(randint(1, N-1))] for j in range(k)]
    print(seq_set)
    sort_sequences(seq_set, N)
    print(seq_set)
```

### C-12.41 Given a sequence S of n elements, on which a total order relation is defined, describe an efficient method for determining whether there are two equal elements in S. What is the running time of your method?
```python
def repeated_element_finder(S):
    if len(S) == 1:
        return None
    return _merge_sort_application(S)[1]

def _merge_sort_application(S):
    if len(S) == 1:
        return S, None

    mid = len(S)//2
    # print('S[:mid] : {}\nS[mid:] : {}'.format(S[:mid], S[mid:]))
    S1, r1 = _merge_sort_application(S[:mid])
    S2, r2 = _merge_sort_application(S[mid:])

    # print('r1 : {}, S1 : {}\nr2 : {}, S2 : {}'.format(r1, S1, r2, S2))
    if r1 is not None:
        return S, r1
    elif r2 is not None:
        return S, r2
    else:
        return _merge_sequences(S1, S2)

def _merge_sequences(S1, S2):
    temp = []
    i1 = 0
    i2 = 0
    while i1 < len(S1) and i2 < len(S2):
        v1, v2 = S1[i1], S2[i2]
        if v1 == v2:
            return temp, v1
        elif v1 < v2:
            temp.append(v1)
            i1 += 1
        else:
            temp.append(v2)
            i2 += 1

    if i1 < len(S1):
        temp.extend(S1[i1:])
    if i2 < len(S2):
        temp.extend(S2[i2:])

    return temp, None

if __name__ == '__main__':
    from random import randint
    n = 100
    a = [randint(0, n) for i in range(n//10)]
    print(a)
    print(repeated_element_finder(a))
```

### C-12.42 Let S be a sequence of n elements on which a total order relation is defined. Recall that an inversion in S is a pair of elements x and y such that x appears before y in S but x > y. Describe an algorithm running in O(nlog n) time for determining the number of inversions in S.
```python
from SortingAlgorithms.quick_sort import quick_sort_sequences_by_key_k
def inversion_counter(S):
    result = 0
    new_S = [[S[i], i] for i in range(len(S))]
    quick_sort_sequences_by_key_k(new_S, 0)
    for i in range(len(new_S)):
        if new_S[i][1] < i:
            result += i - new_S[i][1]
    return result

if __name__ == '__main__':
    a = [3,4,6,1,2,7]
    print(inversion_counter(a))
```

### C-12.43 Let S be a sequence of n integers. Describe a method for printing out all the pairs of inversions in S in O(n+k) time, where k is the number of such inversions.
```python
from SortingAlgorithms.quick_sort import quick_sort_sequences_by_key_k
def get_inversion_pairs(S):
    inversion_partners = []
    pair_result = []
    new_S = [[S[i], i] for i in range(len(S))]
    quick_sort_sequences_by_key_k(new_S, 0)
    for i in range(len(new_S)):
        if new_S[i][1] > i:
            inversion_partners.append([new_S[i][0], new_S[i][1]-i])
    for i in range(len(new_S)):
        if new_S[i][1] < i:
            for partner in inversion_partners:
                if partner[1] > 0 and partner[0] < new_S[i][0]:
                    pair_result.append([new_S[i][0], partner[0]])
                    partner[1] -= 1
    return pair_result

if __name__ == '__main__':
    from random import randint
    n = 100
    a = [randint(0, n) for i in range(n//10)]
    a_p = get_inversion_pairs(a)
    print(a_p)
```

### C-12.44 Let S be a random permutation of n distinct integers. Argue that the expected running time of insertion-sort on S is Ω(n2). (Hint: Note that half of the elements ranked in the top half of a sorted version of S are expected to be in the first half of S.)
* TBS

### C-12.45 Let A and B be two sequences of n integers each. Given an integer m, describe an O(nlogn)-time algorithm for determining if there is an integer a in A and an integer b in B such that m = a+b.
* TBS

### C-12.46 Given a set of n integers, describe and analyze a fast method for finding The ┌logn┐ integers closest to the median.
```python
from SortingAlgorithms.quick_sort import inplace_quick_sort
import math
def close_elements_to_median(S):
    inplace_quick_sort(S)
    n = int(math.log2(len(S)))
    mid = len(S)//2
    start = mid
    end = mid+1
    for i in range(n):
        if S[mid] - S[start-1] < S[end] - S[mid]:
            start -= 1
        else:
            end += 1
    return S[start:end]

if __name__ == '__main__':
    from random import randint
    n = 100
    a = [randint(1,n) for i in range(n//10)]
    print(a)
    b = close_elements_to_median(a)
    print(b)
```

### 




<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part12_Sorting_and_Selection/part12_00_sorting_and_selection.md">Part 12. Sorting and Selection</a>
</p>