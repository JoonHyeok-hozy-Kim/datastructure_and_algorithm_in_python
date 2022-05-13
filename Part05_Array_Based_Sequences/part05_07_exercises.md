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





<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/part05_array_based_sequences.md">Part 5. Array-Based Sequences</a>
</p>