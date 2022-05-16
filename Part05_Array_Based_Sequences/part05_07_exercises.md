<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/part05_array_based_sequences.md">Part 5. Array-Based Sequences</a>
</p>

### R-5.1. Execute the experiment from Code Fragment 5.1 and compare the results on your system to those we report in Code Fragment 5.2.
```python
import sys
n = 10
data = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
```

### R-5.2. In Code Fragment 5.1, we perform an experiment to compare the length of a Python list to its underlying memory usage. Determining the sequence of array sizes requires a manual inspection of the output of that program. Redesign the experiment so that the program outputs only those values of k at which the existing capacity is exhausted.
```python
import sys
n = 100
data = []
byte_tracker = 0
byte_change_list = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    if b > byte_tracker and k > 0:
        byte_tracker = b
        byte_change_list.append(a-1)
    data.append(None)
print(byte_change_list)
```

### R-5.3. Modify the experiment from Code Fragment 5.1 in order to demonstrate that Python’s list class occasionally shrinks the size of its underlying array when elements are popped from a list. 
```python
import sys
initial_elements_count = 200
data = [None] * initial_elements_count
for k in range(initial_elements_count):
    a = len(data)
    b = sys.getsizeof(data)
    data.pop()
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
```

### R-5.4. Our DynamicArray class, as given in Code Fragment 5.3, does not support use of negative indices with getitem . Update that method to better match the semantics of a Python list.
```python
def __getitem__(self, k):
    if not self._n * (-1) <= k < self._n:
        raise IndexError('invalid index')
    # R-5.4
    if k < 0:
        return self._A[self._n + k]
    return self._A[k]
```

### R-5.5. Redo the justification of Proposition 5.1 assuming that the the cost of growing the array from size k to size 2k is 3k cyber-dollars. How much should each append operation be charged to make the amortization work?
* Sol.) Charge 6 dollars for each append operations

### R-5.6. Our implementation of insert for the DynamicArray class, as given in Code Fragment 5.5, has the following inefficiency. In the case when a re-size occurs, the resize operation takes time to copy all the elements from an old array to a new array, and then the subsequent loop in the body of insert shifts many of those elements. Give an improved implementation of the insert method, so that, in the case of a resize, the elements are shifted into their final position during that operation, thereby avoiding the subsequent shifting. 
```python
def insert(self, k, value):
    if k > self._n+1:
        raise IndexError('Cannot insert at {}-th index. Max is {}.'.format(k, self._n+1))
    if k == self._n+1:
        self.append(value)
    else:
        if self._n == self._capacity:
            # R-5.5
            B = self._make_array(self._capacity * 2)
            for i in range(self._n):
                if i < k:
                    B[i] = self._A[i]
                else:
                    B[i+1] = self._A[i]
            self._A = B
        else:
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i-1]
        self._A[k] = value
        self._n += 1
```

### R-5.7. Let A be an array of size n ≥ 2 containing integers from 1 to n−1, inclusive, with exactly one repeated. Describe a fast algorithm for finding the integer in A that is repeated.
* Sol.) Sort the list and find the repeated one : O(nlogn)
```python
from copy import deepcopy
def repeat_finder(L):
    S = deepcopy(L)
    S.sort()
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            return S[i]
    return False

if __name__ == '__main__':
    from random import randint
    n = 10
    l = [randint(0, n * 2) for i in range(n)]
    print(l)
    print(repeat_finder(l))
```

### R-5.8. Experimentally evaluate the efficiency of the pop method of Python’s list class when using varying indices as a parameter, as we did for insert on page 205. Report your results akin to Table 5.5.
```python
from math import pow
from datetime import datetime, timedelta
from copy import deepcopy
class OperationTester:
    def __init__(self, sample_size_digit=4, operation='pop'):
        self._operation = operation
        self._sample_list = []
        self._test_result = []
        for i in range(sample_size_digit):
            temp = [None] * int(pow(10, 2+i))
            self._sample_list.append(temp)

    def do_test(self):
        self._test_result.append(self._operate_at_start())
        self._test_result.append(self._operate_at_mid())
        self._test_result.append(self._operate_at_end())
        self.print_test_result(self._test_result)

    def print_test_result(self, test_result):
        for i in test_result:
            print(i)

    def _operate_at_start(self):
        sample_copy = deepcopy(self._sample_list)
        test_results = []
        for i in sample_copy:
            test_results.append([len(i),
                                 self._operation_time_count(i, 0)])
        return ['k=0', test_results]

    def _operate_at_mid(self):
        sample_copy = deepcopy(self._sample_list)
        test_results = []
        for i in sample_copy:
            test_results.append([len(i),
                                 self._operation_time_count(i, len(i)//2)])
        return ['k=n//2', test_results]

    def _operate_at_end(self):
        sample_copy = deepcopy(self._sample_list)
        test_results = []
        for i in sample_copy:
            test_results.append([len(i),
                                 self._operation_time_count(i, len(i)-1)])
        return ['k=n', test_results]

    def _operation_time_count(self, target, index):
        start_time = datetime.now()
        self._operate(target, index)
        end_time = datetime.now()
        time_spent = end_time-start_time
        result = time_spent.microseconds
        return result

    def _operate(self, target, index):
        if self._operation == 'pop':
            target.pop(index)
        elif self._operation == 'insert':
            target.insert(index, None)
        return

if __name__ == '__main__':
    test = OperationTester(6, 'pop')
    # test = OperationTester(4, 'insert')
    test.do_test()
    
```

### R-5.9. Explain the changes that would have to be made to the program of Code Fragment 5.11 so that it could perform the Caesar cipher for messages that are written in an alphabet-based language other than English, such as Greek, Russian, or Hebrew.
* Sol.) The existing logic is applicable if the starting character and the total number of characters are provided.
  * By altering ord('A') and 26, it can be applied to any language supported by Uni-code.

### R-5.10. The constructor for the CaesarCipher class in Code Fragment 5.11 can be implemented with a two-line body by building the forward and backward strings using a combination of the join method and an appropriate comprehension syntax. Give such an implementation.
```python
def __init__(self, shift):
    self._forward = ''.join([chr((k+shift) % 26 + ord('A')) for k in range(26)])
    self._backward = ''.join([chr((k-shift) % 26 + ord('A')) for k in range(26)])
```

### R-5.11. Use standard control structures to compute the sum of all numbers in an n×n data set, represented as a list of lists.
```python
def sum_n_by_n(A):
    result = 0
    for i in A:
        for j in i:
            result += j
    return result

if __name__ == '__main__':
    from random import randint
    a = [[randint(0, 10) for j in range(5)] for i in range(5)]
    for i in a:
        print(i)
    print(sum_n_by_n(a))
```

### R-5.12. Describe how the built-in sum function can be combined with Python’s comprehension syntax to compute the sum of all numbers in an n×n data set, represented as a list of lists.
```python
def sum_n_by_n_syntax(A):
    return sum([sum(i) for i in A])

if __name__ == '__main__':
    from random import randint
    a = [[randint(0, 10) for j in range(5)] for i in range(5)]
    print(sum_n_by_n_syntax(a))    
```

### C-5.13. In the experiment of Code Fragment 5.1, we begin with an empty list. If data were initially constructed with nonempty length, does this affect the sequence of values at which the underlying array is expanded? Perform your own experiments, and comment on any relationship you see between the initial length and the expansion sequence.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/part05_array_based_sequences.md#code-fragment-51">Code Fragment 5.1</a>
</p>

```python
def initial_length_tester(max_initial_size, append_times):
    import sys
    for i in range(max_initial_size):
        data = [None] * i
        print('=====[max : {} / append : {}]====='.format(i,
                                                          append_times))
        for k in range(append_times):
            a = len(data)
            b = sys.getsizeof(data)
            print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
            data.append(None)
            
if __name__ == '__main__':
    initial_length_tester(10,10)
```

### C-5.14. The shuffle method, supported by the random module, takes a Python list and rearranges it so that every possible ordering is equally likely. Implement your own version of such a function. You may rely on the randrange(n) function of the random module, which returns a random number between 0 and n−1 inclusive.
```python
def custom_shuffle(A):
    from random import randrange
    n = len(A)
    result = []
    while n > 0:
        result.append(A.pop(randrange(n)))
        n -= 1
    return result

if __name__ == '__main__':
    a = [i for i in range(4)]
    print(a)
    print(custom_shuffle(a))
```

### C-5.15. Consider an implementation of a dynamic array, but instead of copying the elements into an array of double the size (that is, from N to 2N) when its capacity is reached, we copy the elements into an array with ┌N/4┐ additional cells, going from capacity N to capacity N + ┌N/4┐. Prove that performing a sequence of n append operations still runs in O(n) time in this case.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/images/05_07_15.png" style="height: 600px;"></img><br/>
</p>

### C-5.16. Implement a pop method for the DynamicArray class, given in Code Fragment 5.3, that removes the last element of the array, and that shrinks the capacity, N, of the array by half any time the number of elements in the array goes below N/4.
```python
def pop(self):
    result = self._A[self._n-1]
    self._A[self._n-1] = None
    self._n -= 1
    if self._n == self._capacity//4:
        self._resize(int(self._capacity//4))
    return result
```

### C-5.17. Prove that when using a dynamic array that grows and shrinks as in the previous exercise, the following series of 2n operations takes O(n) time: n append operations on an initially empty array, followed by n pop operation. 
* pf.) Recall, that if O(a_n)=n and O(b_n)=n, O(a_n + b_n)=n asymptotically. Therefore, the given operation's O(n)=n.


### C-5.18. Give a formal proof that any sequence of n append or pop operations on an initially empty dynamic array takes O(n) time, if using the strategy described in Exercise C-5.16.
* Considering the concept of amortization, popping operation can be proved to have O(n)=n time consumption.
  * Suppose each pop consumes 2 cyber dollars. 
  * One is instantly consumed when the target element in the internal array altered into None.
  * The other is consumed when the space that is used for storing the element is deleted and the capacity shrinks.
  * Then every operation required is cleared.
  * Therefore, we may assume that popping operation is O(2n) = O(n)

### C-5.19. Consider a variant of Exercise C-5.16, in which an array of capacity N is resized to capacity precisely that of the number of elements, any time the number of elements in the array goes strictly below N/4. Give a formal proof that any sequence of n append or pop operations on an initially empty dynamic array takes O(n) time.
* Again using the concept of amortization, consider that each append consumes 3 cyber dollars and pop consumes 2 cyber dollars.
  * Continuous operations of both operations are proven to be O(n)=n.
  * Suppose that these two operations are done in a mixed sense and do not incur capacity expansion nor shrinkage since they offset the changed capacity of each other.
  * Then those cyber dollars that are already paid for the potential expansion or shrinkage may not be used in reality.
  * Additionally, since expansion and shrinkage do not take place, the number of unit operations of append-pop-mixed-sequence may be smaller than the homogeneous series of respective operations.
  * Therefore, mixed operation's O(n) is n, where its upperbound is O(n)=n.

### C-5.20. Consider a variant of Exercise C-5.16, in which an array of capacity N, is resized to capacity precisely that of the number of elements, any time the number of elements in the array goes strictly below N/2. Show that there exists a sequence of n operations that requires Ω(n2) time to execute.


### C-5.21.In Section 5.4.2, we described four different ways to compose a long string: (1) repeated concatenation, (2) appending to a temporary list and then joining, (3) using list comprehension with join, and (4) using generator comprehension with join. Develop an experiment to test the efficiency of all four of these approaches and report your findings. 
```python
def string_tester(n):
    from time import time
    test_result_time = []
    test_result_time.append(time())
    # 1. repeated concatenation
    s = ''
    for i in range(n):
        s += 'a'
    test_result_time.append(time())
    # 2. appending to a temporary list and then joining
    l = []
    for i in range(n):
        l.append('a')
    j = ''.join(l)
    test_result_time.append(time())
    # 3. using list comprehension with join
    k = ''.join(['a' for i in range(n)])
    test_result_time.append(time())
    # 4. using generator comprehension with join
    k = ''.join('a' for i in range(n))
    test_result_time.append(time())
    for i in range(len(test_result_time)-1):
        print('{}. {}'.format(i+1, test_result_time[i+1]-test_result_time[i]))

if __name__ == '__main__':
    string_tester(1000000)
```

### C-5.22. Develop an experiment to compare the relative efficiency of the extend method of Python’s list class versus using repeated calls to append to accomplish the equivalent task.
```python
def extend_tester(n):
    from time import time
    time_list = []
    original_list1 = [None] * 5
    original_list2 = [None] * 5
    temp_list = [None] * n
    time_list.append(time())
    original_list1.extend(temp_list)
    time_list.append(time())
    for i in range(n):
        original_list2.append(None)
    time_list.append(time())
    for i in range(len(time_list)-1):
        print('{}. {}'.format(i+1, time_list[i+1]-time_list[i]))

if __name__ == '__main__':
    extend_tester(10000000)
```

### C-5.23. Based on the discussion of page 207, develop an experiment to compare the efficiency of Python’s list comprehension syntax versus the construction of a list by means of repeated calls to append.
```python


def comprehension_tester(n):
    from time import time
    time_list = []
    time_list.append(time())
    l = [k*k for k in range(n)]
    time_list.append(time())
    m = []
    for k in range(n):
        m.append(k*k)
    time_list.append(time())
    for i in range(len(time_list)-1):
        print('{}. {}'.format(i+1, time_list[i+1]-time_list[i]))

if __name__ == '__main__':
    comprehension_tester(10000000)
```

### C-5.24. Perform experiments to evaluate the efficiency of the remove method of Python’s list class, as we did for insert on page 205. Use known values so that all removals occur either at the beginning, middle, or end of the list. Report your results akin to Table 5.5. 
```python
def remove_tester(sample_size_digit=5):
    from time import time
    from copy import deepcopy
    report_list = [['sample size', 'start', 'mid', 'end']]
    for i in range(2, sample_size_digit):
        sample_size = int(pow(10, i))
        temp_entity = [sample_size]
        temp_list = [i for i in range(sample_size)]
        copy_list_1 = deepcopy(temp_list)
        copy_list_2 = deepcopy(temp_list)
        copy_list_3 = deepcopy(temp_list)

        # start
        t0 = time()
        copy_list_1.remove(0)
        t1 = time()
        temp_entity.append(t1-t0)

        # mid
        t0 = time()
        copy_list_2.remove(sample_size//2)
        t1 = time()
        temp_entity.append(t1-t0)

        # end
        t0 = time()
        copy_list_3.remove(sample_size-1)
        t1 = time()
        temp_entity.append(t1-t0)

        report_list.append(temp_entity)

    for i in report_list:
        print(i)

if __name__ == '__main__':
    remove_tester(7)
```

### C-5.25. The syntax data.remove(value) for Python list data removes only the first occurrence of element value from the list. Give an implementation of a function, with signature remove all(data, value), that removes all occurrences of value from the given list, such that the worst-case running time of the function is O(n) on a list with n elements. Not that it is not efficient enough in general to rely on repeated calls to remove. 
```python
def remove_all(A, value):
    result = []
    for i in range(len(A)):
        if A[i] != value:
            result.append(A[i])
    return result

if __name__ == '__main__':
    a = [1,1,1,1,1,2,3,4,5,5,5,5,6,7,8,9]
    print(remove_all(a,5)
```

### C-5.26. Let B be an array of size n ≥ 6 containing integers from 1 to n−5, inclusive, with exactly five repeated. Describe a good algorithm for finding the five integers in B that are repeated.
```python
def repeat_finder(A):
    sorted(A)
    result = []
    idx = 0
    while idx < len(A)-1:
        if A[idx] == A[idx+1]:
            if len(result) == 0:
                result.append(A[idx])
            elif result[-1] != A[idx]:
                result.append(A[idx])
        idx += 1
    return result

if __name__ == '__main__':
    a = [1,1,1,1,1,2,3,4,5,5,5,5,6,7,8,9]
    print(repeat_finder(a,5)
```

### C-5.27. Given a Python list L of n positive integers, each represented with k = ┌log n┐+ 1 bits, describe an O(n)-time method for finding a k-bit integer not in L.

### C-5.28. Argue why any solution to the previous problem must run in Ω(n) time.

### C-5.29. A useful operation in databases is the natural join. If we view a database as a list of ordered pairs of objects, then the natural join of databases A and B is the list of all ordered triples (x,y,z) such that the pair (x,y) is in A and the pair (y,z) is in B. Describe and analyze an efficient algorithm for computing the natural join of a list A of n pairs and a list B of m pairs.
```python
def natural_join(A, B):
    result = []
    for i in A:
        for j in B:
            if i[1] == j[0]:
                result.append([i[0], i[1], j[1]])
    return result

if __name__ == '__main__':
    from random import randint
    sample_size = 10
    a = [chr(randint(65, 65+25)) for i in range(sample_size * 4)]
    set_x = [['X', 'Y']]
    set_y = [['Y', 'Z']]
    for i in range(sample_size):
        set_x.append([a[i*4-4], a[i*4-3]])
        set_y.append([a[i*4-2], a[i*4-1]])
    print(set_x)
    print(set_y)
    print(natural_join(set_x, set_y))
```

### C-5.30 When Bob wants to send Alice a message M on the Internet, he breaks M into n data packets, numbers the packets consecutively, and injects them into the network. When the packets arrive at Alice’s computer, they may be out of order, so Alice must assemble the sequence of n packets in order before she can be sure she has the entire message. Describe an efficient scheme for Alice to do this, assuming that she knows the value of n. What is the running time of this algorithm?
* Sol.) O(n log(n)) if binary sorting is used.
```python
def data_packet_receiver(A):
    result = [None] * len(A)
    for i in A:
        result[i] = i
        print(result)
    return result

def custom_shuffle(A):
    from random import randrange
    n = len(A)
    result = []
    while n > 0:
        result.append(A.pop(randrange(n)))
        n -= 1
    return result

if __name__ == '__main__':
    a = [i for i in range(10)]
    a_s = custom_shuffle(a)
    print(a_s)
    data_packet_receiver(a_s)
```

### C-5.31 Describe a way to use recursion to add all the numbers in an n × n data set, represented as a list of lists.
```python
def n_by_n_sum(A, sum=0):
    if len(A) == 0:
        return [A, sum]
    else:
        temp = A[0].pop(0)
        if len(A[0]) == 0:
            A.pop(0)
        print(temp, A, sum)
        return n_by_n_sum(A, sum+temp)

if __name__ == '__main__':
    target = []
    for i in range(3):
        target.append([1 for j in range(4)])
    print(target)
    print(n_by_n_sum(target))
```



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/part05_array_based_sequences.md">Part 5. Array-Based Sequences</a>
</p>