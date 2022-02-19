
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

> R-3.23. Give a big-Oh characterization, in terms of n, of the running time of the
example1 function shown in Code Fragment 3.10.
```python
def example1(S):
    n = len(S)
    total = 0
    for j in range(n): # loop from 0 to n-1
        total += S[j]
    return total
```
* sol.) O(n)

