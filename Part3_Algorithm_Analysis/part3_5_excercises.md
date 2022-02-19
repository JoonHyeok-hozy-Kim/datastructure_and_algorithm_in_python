
<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/part3_algorithm_analysis.md">Part 3. Algorithm Analysis</a>
    </p>
</div>

# 3.5 Excercises

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_1.jpg"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_2.jpg"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_3.jpg"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_4.jpg"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_5.png"></img><br/>
</p>

* n_log(n) algorithm for check

```python
def n_log_n(n):
    y = n
    while y >= 1:
        y /= 2
        for i in range(n):
            print(i)
```

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_6.png"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_7.png"></img><br/>
</p>

> R-3.23 ~ R-3.27   
> Give a big-Oh characterization, in terms of n, of the running time
```python
def example1(S):
    n = len(S)
    total = 0
    for j in range(n): # loop from 0 to n-1
        total += S[j]
    return total
```
* sol.) O(n)

```python
def example2(S):
    n = len(S)
    total = 0
    for j in range(0, n, 2): # note the increment of 2
        total += S[j]
    return total
```
* sol.) O(n/2) = O(n)

```python
def example3(S):
    n = len(S)
    total = 0
    for j in range(n): # loop from 0 to n-1
        for k in range(1+j): # loop from 0 to j
            total += S[k]
    return total
```
* sol.) O(n^2). 
  * Inner loop is independent to the size of N but still runs by O(n)

```python
def example4(S):
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total
```
* sol.) O(n)

```python
def example5(A, B): # assume that A and B have equal length
    n = len(A)
    count = 0
    for i in range(n): # loop from 0 to n-1
        total = 0
        for j in range(n): # loop from 0 to n-1
            for k in range(1+j): # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count
```
* sol.) O(n^3)

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_8.png"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/3.5_sol_9.png"></img><br/>
</p>
