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
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.3.1_1_big_oh.jpg" width="800px" title="Big Oh" alt="Big Oh"></img><br/>
</p>

* Concept) Big-Omega
  * Prop) Provides an asymptotic way of saying that a function is __“greater than or equal to”__ another function
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.3.1_2_big_omega.jpg" width="800px" title="Big Omega" alt="Big Omega"></img><br/>
</p>

* Concept) Big-Theta
  * Prop) Two functions grow at the same rate, up to constant factors
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.3.1_3_big_theta.jpg" width="800px" title="Big Theta" alt="Big Theta"></img><br/>
</p>

### 3.3.3 Examples of Algorithm Analysis
* Concept) Python's __list__ Class
  * Prop) len_() function is evaluated in constant time : O(1)
    * why?) __list__ class maintains contains instance variable for the length of the data
  * Prop) Syntax _data[idx]_ is evaluated in constant time : O(1)
    * why?) __list__ classes are implemented as _array-based sequences_ thus references to a list's elements are stored in a consecutive block of memory.

#### Ex.) Prefix Average Problem
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.3.1_4_prefix_average.jpg" width="800px"></img><br/>
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

#### Ex.) Three-Way Set Disjointness
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.3.1_5_three_way_set_disjointness.jpg" width="800px"></img><br/>
</p>

* Sol.1) Cubic Loop

***
pg 145

