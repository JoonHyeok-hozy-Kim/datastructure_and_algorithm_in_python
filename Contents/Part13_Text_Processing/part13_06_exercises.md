<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/part13_00_text_processing.md">Part 13. Text Processing</a>
</p>

### R-13.1 List the prefixes of the string P ="aaabbaaa" that are also suffixes of P.
```python
def prefix_suffix_compare(X):
    prefix = []
    walk = len(X)-1
    while walk > 0:
        temp_text = []
        for i in range(len(X)-walk):
            if X[i] != X[walk+i]:
                break
            else:
                temp_text.append(X[i])
            if i == len(X)-walk-1:
                prefix.append(''.join(temp_text))
        walk -= 1
    return prefix


if __name__ == '__main__':
    x = "aaabbaaa"
    print(prefix_suffix_compare(x))
```

### R-13.2 What is the longest (proper) prefix of the string "cgtacgttcgtacg" that is also a suffix of this string?
* Sol.) cgtacg
```python
def prefix_suffix_compare(X):
    prefix = []
    walk = len(X)-1
    while walk > 0:
        temp_text = []
        for i in range(len(X)-walk):
            if X[i] != X[walk+i]:
                break
            else:
                temp_text.append(X[i])
            if i == len(X)-walk-1:
                prefix.append(''.join(temp_text))
        walk -= 1
    return prefix


if __name__ == '__main__':

    y = "cgtacgttcgtacg"
    print(prefix_suffix_compare(y))
```

### R-13.3 Draw a figure illustrating the comparisons done by brute-force pattern matching for the text "aaabaadaabaaa" and pattern "aabaaa".
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_03.png" style="height: 500px;"></img><br/>
</p>

### R-13.4 Repeat the previous problem for the Boyer-Moore algorithm, not counting the comparisons made to compute the last(c) function.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_04.png" style="height: 200px;"></img><br/>
</p>

### R-13.5 Repeat Exercise R-13.3 for the Knuth-Morris-Pratt algorithm, not counting the comparisons made to compute the failure function.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_05.png" style="height: 600px;"></img><br/>
</p>

### R-13.6 Compute a map representing the last function used in the Boyer-Moore pattern-matching algorithm for characters in the pattern string: 
#### "the quick brown fox jumped over a lazy cat".
```python
p = "the quick brown fox jumped over a lazy cat"
last = {}
for i in range(len(p)):
    last[p[i]] = i
for c in last:
    print('{} : {}'.format(c, last[c]))
```
* Result
  * t : 41
  * h : 1
  * e : 29
  * q : 4
  * u : 21
  * i : 6
  * c : 39
  * k : 8
  * b : 10
  * r : 30
  * o : 27
  * w : 13
  * n : 14
  * f : 16
  * x : 18
  * j : 20
  * m : 22
  * p : 23
  * d : 25
  * v : 28
  * a : 40
  * l : 34
  * z : 36
  * y : 37

### R-13.7 Compute a table representing the Knuth-Morris-Pratt failure function for the pattern string "cgtacgttcgtac".
```python
from TextProcessingAlgorithms.knuth_morris_pratt import _compute_kmp_fail
p = "cgtacgttcgtac"
a = _compute_kmp_fail(p)
print(a)
```
* Result
  * [0, 0, 0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5]

### R-13.8 What is the best way to multiply a chain of matrices with dimensions that are 10×5, 5×2, 2×20, 20×12, 12×4, and 4×60? Show your work.
* By slightly modifying the given code, we can obtain the path as follows.
  * Naming the series of matrices A, B, C, D, E, F, G, the algorithm resulted in the following most efficient product sequence.
    * ((A·B)((((C·D)·E)·F)))·G
```python
def efficient_matrix_product_order(d):
    n = len(d)-1
    N = []
    for i in range(n):
        temp = [[0,''] for i in range(n)]
        N.append(temp)

    for b in range(n):
        for i in range(n-b):
            j = i+b
            if i != j:
                min_val = None
                for k in range(i, j):
                    if min_val is None:
                        min_val = N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1]
                        temp_path = [N[i][k][1], N[k+1][j][1], '({}, {}, {})'.format(i, k + 1, j + 1)]
                    else:
                        if N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1] < min_val:
                            min_val = N[i][k][0] + N[k+1][j][0] + d[i] * d[k+1] * d[j+1]
                            temp_path = [N[i][k][1], N[k+1][j][1], '({}, {}, {})'.format(i, k + 1, j + 1)]

                N[i][j][0] = min_val
                N[i][j][1] = ''.join(temp_path)
    return N

if __name__ == '__main__':
    d = [10, 5, 2, 20, 12,4, 60]
    N = efficient_matrix_product_order(d)
    for row in N:
        for e in row:
            print('{}'.format(e), end=' ')
        print()
```

### R-13.9 In Figure 13.8, we illustrate that GTTTAA is a longest common subsequence for the given strings X and Y. However, that answer is not unique. Give another common subsequence of X and Y having length six.
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_09.png" style="height: 300px;"></img><br/>
</p>

* Sol.) CTAATA
```python
def LCS(X, Y):
    n, m = len(X), len(Y)
    L = [[0] * (m+1) for k in range(n+1)]
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j+1][k+1] = 1 + L[j][k]
            else:
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L

def LCS_solution_ver2(X, Y):
    solution = []
    j, k = len(X), len(Y)
    L = LCS(X, Y)
    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] > L[j][k-1]:  # changed the comparison operator from >= to >.
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))

if __name__ == '__main__':
    x = "GTTCCTAATA"
    y = "CAGATAATTGAG"
    print(LCS_solution_ver2(x,y))
```

### R-13.10 Show the longest common subsequence array L for the two strings:
#### X = "skullandbones"
#### Y = "lullabybabies"
### What is a longest common subsequence between these strings?
* Sol.) ullabes
```python
def LCS(X, Y):
    n, m = len(X), len(Y)
    L = [[0] * (m+1) for k in range(n+1)]
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j+1][k+1] = 1 + L[j][k]
            else:
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L


def LCS_solution(X, Y):
    solution = []
    j, k = len(X), len(Y)
    L = LCS(X, Y)
    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))

if __name__ == '__main__':
    x = "skullandbones"
    y = "lullabybabies"
    print(LCS_solution(x, y))
```

### R-13.11 Draw the frequency array and Huffman tree for the following string:
#### "dogs do not spot hot pots or cats".
```python
from TextProcessingAlgorithms.huffman import huffman_with_frequency_array
a = "dogs do not spot hot pots or cats"
result = huffman_with_frequency_array(a)
for e in result['frequency_array']:
    print('{} : {}'.format(e, result['frequency_array'][e]))
print(result['tree'])
```
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_11.png" style="height: 500px;"></img><br/>
</p>



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/part13_00_text_processing.md">Part 13. Text Processing</a>
</p>