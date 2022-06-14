<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 4. Recursion
#### Def) Recursion
* a technique by which a function makes one or more calls to itself
during execution, or by which a data structure relies upon smaller instances of
the very same type of structure in its representation

#### Concept) Activation Record (or Frame)
* a structure called in Python when a function is called
* stores information about the progress of that invocation of the function
  1. namespace for storing the fuction call's parameters and local variables
  2. information about which command in the body of the function is currently executing

## 4.1 Illustrative Examples
### 4.1.1 The Factorial Function
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
```

### 4.1.2 Drawing an English Ruler
* Concept) English Ruler
  * For each inch, a tick with a numeric label should be placed
  * Major Tick Length : the length of the tick designating a whole inch
  * Minor Ticks : placed at intervals of 1/2 inch, 1/4 inch, and so on.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/images/4_01_english_ruler.png" style="height: 300px;"></img><br/>
</p>

* Tech) Consider it as a simple example of __Fractal__.
```python
class EnglishRuler:
    def __init__(self, num_inches, major_length):
        self._num_inches = num_inches
        self._major_length = major_length

    def draw_line(self, tick_length, tick_label=''):
        result_list = ['-' for i in range(tick_length)]
        if tick_label:
            result_list.append(' ')
            result_list.append(tick_label)
        result = ''.join(result_list)
        print(result)
        return result

    def draw_interval(self, center_length):
        if center_length > 0:
            self.draw_interval(center_length-1)
            self.draw_line(center_length)
            self.draw_interval(center_length-1)

    def draw_ruler(self):
        for i in range(self._num_inches+1):
            self.draw_line(self._major_length, str(i))
            if i < self._num_inches:
                self.draw_interval(self._major_length-1)


if __name__ == '__main__':
    a = EnglishRuler(5, 4)
    a.draw_ruler()
```

### 4.1.3 Binary Search
* Concept) Sequential Search
  * Use when the sequence is __unsorted__.
  * how?) Use a loop to examine all the elements
  * running time : O(n)
* Concept) Binary Search
  * Use when the sequence is __sorted__ and __indexable__.
```python
def binary_search(S, e, init=0, end=None):
    n = len(S)
    if end is None:
        end = n-1
    mid = (init+end)//2
    print('mid: {}, init: {}, end: {}'.format(mid, init, end))
    if S[mid] == e:
        return mid
    elif S[mid] > e:
        return binary_search(S, e, init, mid-1)
    else:
        return binary_search(S, e, mid+1, end)
```

### 4.1.4 File Systems
* Concept) Modern OSs define file-system directories in a _recursive_ way.
* Concept) Calculating __Cumulative__ disk space
  * def) __Immediate disk space__ : disk space used by each entry
  * def) __Cumulative disk space__ : disk space used by that entry and all nested features
```python
import os
def disk_usage(path):
    total = os.path.getsize(path)
    for file in os.listdir(path):
        child_path = os.path.join(path, file)
        total += disk_usage(child_path)
    print('{0:<7} | {}'.format(total, path))
    return total
```

## 4.2 Analyzing Recursive Algorithms
* How?
  * Using big-Oh, Omega, Theta, etc
  * Account each operation that is performed based upon the particular
<a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#concept-activation-record-or-frame">_activation_</a>
of the function that manages the flow of control at the time it is executed.
  * Take sum of the number of operations over all the _activations_.

### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#411-the-factorial-function">4.2.1 Factorials Function</a>
* Trivially, O(n)
 
### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#412-drawing-an-english-ruler">4.2.2 English Ruler</a>
* Use _recurrence equation_
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/images/4_01_english_ruler_pf.png" style="height: 300px;"></img><br/>
</p>

### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#413-binary-search">4.2.3 Binary Search</a>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/images/4_01_binary_search_pf.png" style="height: 300px;"></img><br/>
</p>

### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#413-binary-search">4.2.4 Disk Space Usage</a>
* Weak Upperbound : O(n^2)
  * pf) Let _n_ be the number of entries in a file system. Then, the number of the iteration 
        invoked each entry by os.list_dir() method will be _n_.   
        Now, if certain entry is a directory, in worst case it may include iteration of _n-1_
        others, O(n). Thus, O(n^2)
* Tight Upperbound : O(n)
  * pf) Consider that it is possible that some directories contain a number of entries
        proportional to _n_, i.e. the case that an entry contains _n-1_ is too conservative.
        Recall that overall iteration that may happen in the whole file system is equal to _n_.
        Thus, we may assume that only O(1) runs outside the iteration and finally O(n) overall.
  * Refer to _amortization_ in Section 5.3.

## 4.3 Recursion Run Amok
#### In efficient example 1 : Element Uniqueness Problem
* Recall
<a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part03_Algorithm_Analysis/part3_00_algorithm_analysis.md#ex3-element-uniqueness-problem--find-out-whether-all-elements-of-a-series-s-with-the-size-of-n-are-unique">_element uniqueness problem_</a>
  * recursive solution
```python
def unique3(S, start, stop):
    if stop - start < 1:
        print('pt1: {} / {}'.format(start, stop))
        return True

    elif not unique3(S, start, stop-1):
        print('pt2: {} / {}-1'.format(start, stop))
        return False

    elif not unique3(S, start+1, stop):
        print('pt3: {}+1 / {}'.format(start, stop))
        return False

    else:
        print('pt4: {} / {}'.format(start, stop))
        return S[start] != S[stop-1]
```
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/images/4_03_element_uniqueness_problem.png" style="height: 300px;"></img><br/>
</p>

* Analysis) O(2^n)
  * why?) Let n = (stop-start)
    * Then each recursive call invokes two recursive calls
      * unique3(S, start, stop-1)
      * unique3(S, start+1, stop)


#### In efficient example 2 : Fibonacci Numbers
* Bad recursive code
  * Analysis) O(2^n)
    * why?) Each recursive call invoke two recursive calls
```python
def bad_fibonacci(n):
    if n <= 1:
        return 1
    else:
        return bad_fibonacci(n-1) + bad_fibonacci(n-2)
```

* Efficient recursive code
  * sol.) Return n-th and (n-1)-th number together.
```python
def efficient_fibonacci(n):
    if n <= 1:
        return (n, 1)
    else:
        (a, b) = efficient_fibonacci(n-1)
        return (a+b, a)
```

### 4.3.1 Maximum Recursive Depth in Python

#### Concept) Infinite Recursion
* Def.) When each recursive call makes another recursive call, without ever reaching a base case
  * Problem) Waste CPU and Memory
  * Thus, keep in mind that each recursive call is in some way progressing toward a base case.
* Concept) RuntimeError
  * Def.) Python's error exception for infinite recursion
  * Prop.) Default recursion limit : 1000
  * Tech.) Dynamically reconfiguring the recursive limit
```python
import sys
recursive_limit = 10000000
old = sys.getrecursionlimit()
sys.setrecursionlimit(recursive_limit)
```

## 4.4 Further Examples of Recursion
* Concept) Organizing __Recursion__ by considering the maximum number of recursive calls that may be started from within the body of single activation.
  1. Linear Recursion : at most 1 other recursion 
  2. Binary Recursion : 2 other recursions
  3. Multiple Recursion : 3 or more recursions

### 4.4.1 Linear Recursion
* Def) each invocation of the body makes at most one new recursive call
* Examples already covered
  1. <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#411-the-factorial-function">Factorials Fucntion</a>
  2. <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#in-efficient-example-2--fibonacci-numbers">Efficient Fibonacci</a>
  3. <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#413-binary-search">Binary Search</a>

#### Ex.1) Summing the Elements of a Sequence Recursively
```python
def sum(S, idx=None):
    if idx is None:
        idx = len(S)-1
    if idx == 0:
        return S[0]
    else:
        return sum(S, idx-1) + S[idx]
```

#### Ex.2) Reversing a Sequence with Recursion
```python
def reverse(S, start=None, stop=None):
    if start is None and stop is None:
        start, stop = 0, len(S)-1
    if start < stop:
        S[start], S[stop] = S[stop], S[start]
        return reverse(S, start+1, stop-1)
    return S
```

#### Ex.3) Computing Powers
* Normal Version
```python
def power(a, n):
    if n == 0:
        return 1
    else:
        return power(a, n-1) * a
```
* Faster Version
  * O(log_n) running time
    * why?) It halves the recursion thanks to square.
```python
def faster_power(a, n):
    if n == 0:
        return 1
    else:
        partial = faster_power(a, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= a
        return result
```

### 4.4.2 Binary Recursion
* Def.) Making two recursive calls

#### Ex.1) Binary Sum
```python
def binary_sum(S, start=None, length=None):
    if start is None and length is None:
        start, length = 0, len(S)
    if start >= length:
        return 0
    elif start == length-1:
        return S[start]
    else:
        mid = (start + length)//2
        return binary_sum(S, start, mid) + binary_sum(S, mid, length)
```
* Analysis)
  1. O(log_n) space usage
     * How?) Depth of the recursion is 1+log_n (Consider the tree!)
  2. O(n) running time
     * Why?) There were 2n-1 function calls
       * pf.) Sum 2^n - 1 where, n = log_N

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/images/4_04_binary_sum_graphics.png" style="height: 300px;"></img><br/>
</p>

### 4.4.3 Multiple Recursion
* Def.) Making more than 2 recursive calls

#### Ex.1) Summation Puzzle (or Permutation)
```python
def summation_puzzle(k, U, S=None):
    from copy import deepcopy
    if S is None:
        S = []
    for i in range(len(U)):
        popped = U.pop(i)
        S.append(deepcopy(popped))
        if k == 1:
            print(''.join(S))
        else:
            summation_puzzle(k-1, U, S)
        popped_again = S.pop(-1)
        U.insert(i, popped_again)

if __name__ == '__main__':
    sample_size = 5
    U = [chr(i+65) for i in range(sample_size)]
    print(U)
    summation_puzzle(3, U)
```

## 4.5 Designing Recursive Algorithm
#### Tech.) Typical Recursion Format
  1. Test for base cases
     * Every recursive calls eventually reach a base case.
  2. Recur
     * Define each recursive call to make progress towards a base case.
  3. Reparameterization
     * in order to make a recursive function with the cleaner interface
     * or to intentionally strengthening the expectation of what is returned. (Ex.
     <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_00_recursion.md#in-efficient-example-2--fibonacci-numbers">Good Fibonacci</a>
  returning pair of numbers instead of integers.)

## 4.6 Eliminating Tail Recursion
* Benefit of a recursive approach
  * allows us to succintly take advantage of a repetitive structure
* Cost of a recursive structure
  * memory usage
    * how?) Python interpreter must maintain activation records that keep track of the state of each nested call.
    * Sol 1.) Use stack and store only the minimal information necessary (instead of whole activation records.)
    * Sol 2.) Use __tail recursion__.
      * Def.) any recursive call that is made from one context is the very last operation in that context, with the 
      return value of the recursive call (if any) immediately returned by the enclosing recursion.
      * Prop.) Must be _linear recursion_.
      * Prop.) Additional calculation should not be performed after a recursive call is completed.
        * ex.) Fibonacci : return n*factorial(n-1) --- (X)

----------------------------------------
## 4.7 Excercises
<div>
    <p>
        <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_7_exercises.md">Exercises 4.7</a>
    </p>
</div>
