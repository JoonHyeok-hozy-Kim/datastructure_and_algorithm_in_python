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
* store information about the progress of that invocation of the function
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
<a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/Part04_Recursion.md#concept-activation-record-or-frame">_activation_</a>
of the function that manages the flow of control at the time it is executed.
  * Take sum of the number of operations over all the _activations_.

### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_recursion.md#411-the-factorial-function">4.2.1 Factorials Fucntion</a>
* Trivially, O(n)
 
### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_recursion.md#412-drawing-an-english-ruler">4.2.2 English Ruler</a>
* Use _recurrence equation_
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/images/4_01_english_ruler_pf.png" style="height: 300px;"></img><br/>
</p>

### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_recursion.md#413-binary-search">4.2.3 Binary Search</a>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/images/4_01_binary_search_pf.png" style="height: 300px;"></img><br/>
</p>

### <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_recursion.md#413-binary-search">4.2.4 Disk Space Usage</a>
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
<a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part03_Algorithm_Analysis/part3_algorithm_analysis.md#ex3-element-uniqueness-problem--find-out-whether-all-elements-of-a-series-s-with-the-size-of-n-are-unique">_element uniqueness problem_</a>
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

----------------------------------------
## 4.7 Excercises
<div>
    <p>
        <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_7_excercises.md">Exercises 4.7</a>
    </p>
</div>
