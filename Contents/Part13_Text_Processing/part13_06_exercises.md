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
* Sol.)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_11.png" style="height: 500px;"></img><br/>
</p>

### R-13.12 Draw a standard trie for the following set of strings:
#### { abab, baba, ccccc, bbaaaa, caa, bbaacc, cbcc, cbca }
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_12.png" style="height: 500px;"></img><br/>
</p>

### R-13.13 Draw a compressed trie for the strings given in the previous problem.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_13.png" style="height: 400px;"></img><br/>
</p>

### R-13.14 Draw the compact representation of the suffix trie for the string:
#### "minimize minime"

### C-13.15 Describe an example of a text T of length n and a pattern P of length m such that force the brute-force pattern-matching algorithm achieves a running time that is Ω(nm).
* Sol.) Consider the case that any character in P is contained in T.
  * ex.
    * P = "abc"
    * T = "defgh"
    * Then, the outer while-loop runs (5-3) times and inner for-loop runs 3 times.

### C-13.16 Adapt the brute-force pattern-matching algorithm in order to implement a function, rfind brute(T,P), that returns the index at which the rightmost occurrence of pattern P within text T, if any.
```python
def rfind_brute(T, P):
    """ Return the highest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m:
            return i+m-1
    return -1
```

### C-13.17 Redo the previous problem, adapting the Boyer-Moore pattern-matching algorithm appropriately to implement a function rfind boyer moore(T,P).
```python
def rfind_boyer_moore(T, P):
    """ Return the highest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i+m-1
            i -= 1
            k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)    # min(k, j+1) : The minimum of
                                    #               (1) k   : m - 1 - (the number of matches in the previous search)
                                    #               (2) j+1 : (the index of the last position that T[i] is contained in P) + 1

            k = m-1                 # Initialize k

    return -1
```

### C-13.18 Redo Exercise C-13.16, adapting the Knuth-Morris-Pratt pattern-matching algorithm appropriately to implement a function rfind kmp(T,P).
```python
def rfind_kmp(T, P):
    """ Return the highest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1
```

### C-13.19 The count method of Python’s str class reports the maximum number of nonoverlapping occurrences of a pattern within a string. For example, the call abababa .count( aba ) returns 2 (not 3). Adapt the brute-force pattern-matching algorithm to implement a function, count brute(T,P), with similar outcome.
```python
def count_brute(T, P):
    """ Return the maximum number of nonoverlapping occurrences of a P within T """
    n, m = len(T), len(P)
    cnt = 0
    continue_cnt = 0
    for i in range(n-m+1):
        if continue_cnt > 0:
            # print('Continue i : {}'.format(i))
            continue_cnt -= 1
            continue
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m and i+k < n-1:
            # print('counted at i : {}, i+k : {}, T[i: i+k] : {}'.format(i, i+k, T[i: i+k]))
            cnt += 1
            continue_cnt = m-1
    return cnt
```

### C-13.20 Redo the previous problem, adapting the Boyer-Moore pattern-matching algorithm in order to implement a function count boyer moore(T,P).
```python
def count_boyer_moore(T, P):
    """ Return the maximum number of nonoverlapping occurrences of a P within T """
    n, m = len(T), len(P)
    cnt = 0
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    i = m-1
    k = m-1
    while 0 <= i < n:
        # print('T[{}] : {}, P[{}] : {}'.format(i, T[i], k, P[k]))
        if T[i] == P[k]:
            if k == 0:
                # print('T[{}:{}] : {}'.format(i, i+m, T[i:i+m]))
                cnt += 1
                k = m-1
                i += m*2-1
                continue
            i -= 1
            k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j+1)
            k = m-1                 

    return cnt
```

### C-13.21 Redo Exercise C-13.19, adapting the Knuth-Morris-Pratt pattern-matching algorithm appropriately to implement a function count kmp(T,P).
```python
def count_kmp(T, P):
    """ Return the maximum number of nonoverlapping occurrences of a P within T """
    n, m = len(T), len(P)
    cnt = 0
    if m == 0:
        return 0
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        # print('T[{}] : {}, P[{}] : {}'.format(j, T[j], k, P[k]))
        if T[j] == P[k]:
            if k == m-1:
                # print('T[{}:{}] : {}'.format(j-m+1, j+1, T[j-m+1:j+1]))
                cnt += 1
                j += m-2
                k = 0
                continue
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return cnt
```

### C-13.22 Give a justification of why the compute_kmp_fail function (Code Fragment 13.4) runs in O(m) time on a pattern of length m.
* Justification
  1. fail array creation in O(m) time.
  2. while-loop runs in O(m) time.
     * Operations in each loop run in O(1) time.


### C-13.23 Let T be a text of length n, and let P be a pattern of length m. Describe an O(n+m)-time method for finding the longest prefix of P that is a substring of T.
* Sol.) Applying the KMP we can get the following.
```python
from TextProcessingAlgorithms.knuth_morris_pratt import _compute_kmp_fail
def longest_prefix_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return None
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    cnt = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                k += 1
                cnt = max(cnt, k)
                break
            # print('k : {}, cnt : {}, P[k] : {}'.format(k, cnt, P[k]))
            j += 1
            k += 1
            cnt = max(cnt, k)
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1

    return P[:cnt]

if __name__ == '__main__':
    t = "asdfasfqwertysfdasdqwertyufa"
    p = "qwertyu"
    print(longest_prefix_kmp(t, p))
```

### C-13.24 Say that a pattern P of length m is a circular substring of a text T of length n > m if P is a (normal) substring of T, or if P is equal to the concatenation of a suffix of T and a prefix of T, that is, if there is an index 0 ≤ k < m, such that P = T[n−m+k :n]+T [0:k]. Give an O(n+m)-time algorithm for determining whether P is a circular substring of T.
* Sol.) Again applying the KMP...
```python
from TextProcessingAlgorithms.knuth_morris_pratt import _compute_kmp_fail
def circular_substring_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return None
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n+m:
        if T[j%n] == P[k]:
            if k == m-1:
                return T[j-m+1:j+1] if j < n else T[j-m+1:] + T[0:j%n+1]
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return None

if __name__ == '__main__':
    t = "abcdefasdfasfdawexxxx"
    p = "exxxxabc"
    print(circular_substring_kmp(t, p))
```








<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/part13_00_text_processing.md">Part 13. Text Processing</a>
</p>