
<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_recursion.md">Part 4. Recursion</a>
    </p>
</div>

# R-4.1
* Running time : O(n)
* Space Usage : O(log_n)
```python
def max_sequence(S, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(S)-1
    if start == end:
        return S[start]
    elif start == end-1:
        return max(S[start], S[end])
    else:
        mid = (start+end)//2
        return max(max_sequence(S, start, mid),
                   max_sequence(S, mid+1, end))
```

# R-4.2
```python
# Traditional Power
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/images/4_07_02.png" style="height: 300px;"></img><br/>
</p>

# R-4.3
```python
# Repeated Squaring Algorithm
def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial * partial
        if n%2 == 1:
            result *= x
        return result
```











<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part04_Recursion/part4_recursion.md">Part 4. Recursion</a>
    </p>
</div>