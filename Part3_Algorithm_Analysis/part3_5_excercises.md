
<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/part3_algorithm_analysis.md">Part 3. Algorithm Analysis</a>
    </p>
</div>

# 3.5 Excercises

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_1.jpg"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_2.jpg"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_3.jpg"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_4.jpg"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_5.png"></img><br/>
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
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_6.png"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_7.png"></img><br/>
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
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_8.png"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_9.png"></img><br/>
</p>

> C-3.35
```python
def c_3_35(A):
    n = len(A)
    sorted_A = sorted(A)
    print(sorted_A)
    for i in range(n-2):
        if sorted_A[i] == sorted_A[i+1]:
            if sorted_A[i+1] == sorted_A[i+2]:
                return False
    return True
```
> C-3.36. Using Merge Sort algorithm, n_log_n running time is achievable.
```python
def c_3_36(A):
    n = len(A)
    if n <= 10:
        return A
    else:
        sorted_A = sorted(A)
        return sorted_A[-11:-1]
```

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_10.png"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_11.png"></img><br/>
</p>

> C-3.41. By coupling adjacent elements and compare local min/max
```python
def c_3_41(A):
    n = len(A)
    min, max = A[0], A[0]
    comparison_count = 0
    max_candidates = []
    min_candidates = []
    for i in range(n//2):
        comparison_count += 1
        if A[i*2] >= A[i*2-1]:
            comparison_count += 1
            if A[i*2] > max:
                max = A[i*2]
            comparison_count += 1
            if A[i*2-1] < min:
                min = A[i*2-1]
        else:
            comparison_count += 1
            if A[i*2-1] > max:
                max = A[i*2-1]
            comparison_count += 1
            if A[i*2] < min:
                min = A[i*2]

    return [min, max, comparison_count]
```

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_12.png"></img><br/>
</p>

> C-3.45. Use summation equation as apriori-knowledge.
```python
def c_3_45(S):
    n = len(S)
    sum = n*(n+1)/2
    for i in S:
        sum -= i
    return int(sum)
```

> C-3.46. It is not proven or generalized that the n-th sheep has the same color as previous ones.
> A monolithic color of previous sheeps does not guarantee the color of the next sheep.

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_13.png"></img><br/>
</p>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/images/3.5_sol_14.png"></img><br/>
</p>

> C-3.54
```python
def c_3_54(S):
    n = len(S)
    sorted_S = sorted(S)
    target = [S[0], 1]
    temp = [None] * 2
    for i in range(n-1):
        if sorted_S[i+1] == target[0]:
            target[1] += 1
        else:
            if temp[0] == sorted_S[i+1]:
                temp[1] += 1
                if temp[1] > target[1]:
                    target = temp
            else:
                temp = [sorted_S[i+1], 1]

    return target[0]
```

<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part3_Algorithm_Analysis/part3_algorithm_analysis.md">Part 3. Algorithm Analysis</a>
    </p>
</div>