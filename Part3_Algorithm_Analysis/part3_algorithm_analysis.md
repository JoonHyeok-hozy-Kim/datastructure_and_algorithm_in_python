<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 3. Algorithm Analysis

## 3.1 Experimental Studies
#### Tech) Use __time__ function for time recording
```python
from time import time
start_time = time()
# code section
end_time = time()
elapsed = end_time-start_time
```
  * Limit) Being affected by other processes sharing CPU
    * Antidote) Use __timeit__ module instead
    
### 3.1.1 Moving Beyond Experimental Analysis
#### Premise) Primitive Operations   
  * Props.) The number, _t_ , of primitive operations an algorithm performs will be proportional to the actual running time of that algorithm.
  * List)
    * Assigning an identifier to an object
    * Determining the object associated with an identifier
    * Performing an arithmetic operation (for example, adding two numbers)
    * Comparing two numbers
    * Accessing a single element of a Python list by index
    * Calling a function (excluding operations executed within the function)
    * Returning from a function.
    
#### Tech) Worst-Case Analysis
* cf.) Average-Case Analysis requires expected running time based on a give input distribution => complicated

## 3.2 The Seven Functions Used in this book
1. Constant Function   
2. Logarithm Function
3. Linear Function
4. _N_-Log-_N_ Function
5. Quadratic Function
   * e.g.) Nested Loops
6. Cubic Function and other Polynomials
7. Exponential Function

#### Concept) The Ceiling and Floor Functions
1. └x┘ = the largest integer less than or equal to x.
2. ┌x┐ = the smallest integer greater than or equal to x.
  
## 3.3 Asymptotic Analysis
* Concept) Focus on the growth rate of the running time as a function of the input size _n_, taking a “big-picture” approach.
  * i.e.) enough just to know that the running time of an algorithm grows proportionally to _n_.

### 3.3.1 The "Big-Oh" Notation
* Def.) Big-Oh
  * Prop) Provides an asymptotic way of saying that a function is __“less than or equal to”__ another function
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.3.1_1_big_oh.jpg" width="800px" title="Big Oh" alt="Big Oh"></img><br/>
</p>

* Concept) Big-Omega
  * Prop) Provides an asymptotic way of saying that a function is __“greater than or equal to”__ another function
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.3.1_2_big_omega.jpg" width="800px" title="Big Omega" alt="Big Omega"></img><br/>
</p>

* Concept) Big-Theta
  * Prop) Two functions grow at the same rate, up to constant factors
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.3.1_3_big_theta.jpg" width="800px" title="Big Theta" alt="Big Theta"></img><br/>
</p>

### 3.3.3 Examples of Algorithm Analysis
* Concept) Python's __list__ Class
  * Prop) len_() function is evaluated in constant time : O(1)
    * why?) __list__ class maintains contains instance variable for the length of the data
  * Prop) Syntax _data[idx]_ is evaluated in constant time : O(1)
    * why?) __list__ classes are implemented as _array-based sequences_ thus references to a list's elements are stored in a consecutive block of memory.

#### Ex.1) Prefix Average Problem
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.3.1_4_prefix_average.jpg" width="800px"></img><br/>
</p>

* Sol.1) Quadratic time Algorithm   
```python
def prefix_average1(S):
    n = len(S)
    total = 0
    A = [None] * n
    for i in range(n):
        for j in range(i+1):
            total += S[j]
            A[i] = S[j]/(j+1)
    return A
```
* Sol.2) Quadratic with sum function   
```python
def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)
    return A
```
* Sol.3) Linear time Algorithm
```python
def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for i in range(n):
        total += S[i]
        A[i] = total/(i+1)
    return A
```
<br/>

#### Ex.2) Three-Way Set Disjointness
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.3.1_5_three_way_set_disjointness.jpg" width="800px"></img><br/>
</p>

* Sol.1) Cubic Loop 1
```python
def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True
```

* Sol.2) Cubic Loop 2
  * why faster?) If A and B are distinctive, there will be only __at most__ O(n) pairs s.t. a==b. Thus, loop over C executes at most _n_ times. Thus, worst-case is O(n^2) running time.
```python
def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if b == c:
                        return False
    return True
```
<br/>

#### Ex.3) Element Uniqueness Problem : Find out whether all elements of a Series S with the size of n are unique.
* Sol.1) Using two nested loops as follows : worst-case running time is O(n^2)
```python
def unique1(S):
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if i==j:
                return False
    return True
```

* Sol.2) Using sorting algorithm, which guarantees a worst-case running time of O(nlogn)
```python
def unique2(S):
    sorted_S = sorted(S)
    for i in range(len(sorted_S)-1):
        if S[i] == S[i+1]:
            return False
    return True
```
<br/>
  
## 3.4 Simple Justification Techniques

* Tech.) __counterexamples__
* Tech.) __contrapositive__
  * how) "If _p_ is true, then _q_ is true." <=> "If _q_ is false, then _p_ is false."
* Tech.) __contradiction__
  * how) Make assumption that target statement is false, and show that it's incongruous.
* Tech.) __Induction__
  * ex.) In order to show that _q(n)_ is true for _n_>=1,
    1. Show _q(1)_ is true.
    2. Justify that _q(n)_ is true for _n > k_ , where _k_ is a constant.
* Tech.) __Loop Invariants__
  1. The initial claim, L0, is true before the loop begins.
  2. If Lj−1 is true before iteration j, then Lj will be true after iteration j.
  3. The final statement, Lk, implies the desired statement L to be true.
  
## 3.5 Excercises
<div>
    <p>
        <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/part3_5_excercises.md">Part 3. Algorithm Analysis</a>
    </p>
</div>
