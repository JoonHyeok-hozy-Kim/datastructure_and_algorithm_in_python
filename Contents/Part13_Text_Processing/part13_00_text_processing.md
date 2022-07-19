<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 13. Text Processing
## 13.1 Abundance of Digitized Text
#### Ex.) Common examples of digital collections that include textual information
* Snapshots of the World Wide Web, as Internet document formats HTML and XML are primarily text formats, with added tags for multimedia content 
* All documents stored locally on a user’s computer
* Email archives
* Customer reviews
* Compilations of status updates on social networking sites such as Facebook
* Feeds from microblogging sites such as Twitter and Tumblr These collections include written text from hundreds of international

#### Materials that will be covered
1. brute-force method
   * Goal : Dealing with the problem of searching for a pattern as a substring of a larger piece of text
2. dynamic programming
   * Goal : Can be applied in certain settings to solve a problem in polynomial time that appears at first to require exponential time to solve
3. greedy method
   * Goal : Compressing text data in order to minimize the number of bits that need to be communicated through a network and to reduce the long-term storage requirements for archives

### 13.1.1 Notations for Strings and the Python str Class
#### Notation1) Σ
* The set of alphabet that a string contains
  * ex.) 
    * For S = "CGTAAACTGCTTTAATCAAACGC"
    * Σ = {A,C,G,T}.
* If the alphabet is in fixed size, we denote |Σ|.


## 13.2 Pattern-Matching Algorithms
### 13.2.1 Brute Force
* How?
  * Enumerate all possible configurations of the inputs involved and pick the best of all these enumerated configurations.

* Implementation
```python
def find_brute(T, P):
    """ Return the lowest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1
```

* Analysis) Performance
  * Worst case running time of O(nm).
  * why?
    * Outer for-loop runs at most (n-m+1) times while inner while-loop runs at most m times.


### 13.2.2 The Boyer-Moore Algorithm
* Goal
  * Avoid comparisons between P and a sizable fraction of the characters in T as much as possible.
* How?
  * Improve the running time of the brute-force algorithm by adding two potentially time-saving heuristics.
  * Heuristic
    1. **Looking-Glass Heuristic**
      * When testing a possible placement of P against T, begin the comparisons from the end of P and move backward to the front of P
    2. **Character-Jump Heuristic**
       * During the testing of a possible placement of P within T, a mismatch of text character T[i]=c with the corresponding pattern character P[k] is handled as follows. 
         1. If c is not contained anywhere in P, then shift P completely past T[i] (for it cannot match any character in P). 
         2. Otherwise, shift P until an occurrence of character c in P gets aligned with T[i].

#### Description by image
1. Simple Case
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_02_01_boyer_moore_image_1.png" style="width: 100%;"></img><br/>
</p>
    
2. More complicated case with mismatch
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_02_01_boyer_moore_image_2.png" style="width: 100%;"></img><br/>
</p>

#### Inner function : last(c)
* What is this?
  * If c is in P, last(c) is the index of the last (rightmost) occurrence of c in P.
  * Otherwise, we conventionally define last(c) = −1.
* How?
  * Use hash table to represent th last function.
    * Then the space usage will be proportional to the number of distinct alphabet symbols, or the size of Σ, which is the fixed number.
    * Thus, the running time of last() function will be O(m) where m denotes the size of P.

#### Implementation
```python
def find_boyer_moore(T, P):
    """ Return the lowest index of T at which substring P begins (or else -1). """
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
                return i
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
#### Simulation
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_02_01_boyer_moore_image_3.png" style="width: 100%;"></img><br/>
</p>

#### Analysis) Performance
* Worst-Case Running Time : O(nm + |Σ|)
  * Why?
    * last function takes O(m+|Σ|) time.
    * actual search : O(nm)
  * Worst-Case Scenario
    * T = "aaaaaaaaaaaaa"
    * P = "baaaa"
  * Advantage
    * Often able to skip large portions of text.
      * which means less comparison operation -> less time spent for the search.
    * Experimental evidence on English text shows that the average number of comparisons done per character is 0.24 for a five-character pattern string.


### 13.2.3 The Knuth-Morris-Pratt Algorithm
* Goal
  * Take advantage of the matched record information that we obtained during the search before mismatch was found!
  * Achieve asymptotically optimal O(n+m) running time.
* How?
  * Precompute self-overlaps between portions of the pattern.
  * Thus, we immediately know the maximum amount to shift the pattern before continuing the search when a mismatch occurs at one location.

#### Concept) Failure Function
* Purpose
  * Indicate the proper shift of P upon a failed comparison
  * Returns the number of how many of the immediately preceding characters can be reused to restart the pattern.
* Def.) **Failure Function f(k)**
  * the length of the longest prefix of P that is a suffix of P[1:k+1]
  * Note that P[0] is excluded since we will shift at least one unit.
* Ex.) Simulation and the Failure Function
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_02_02_kmp_ex1.png" style="width: 100%;"></img><br/>
</p>
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_02_02_kmp_ex2.png" style="height: 100px;"></img><br/>
</p>

#### Implementation
```python
def find_kmp(T, P):
    """ Return the lowest index of T at which substring P begins (or else -1). """
    n, m = len(T), len(P)
    if m == 0:
        return 0
    fail = _compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j-m+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1


def _compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail
```

#### Analysis) Performance
* Conclusion
  * The Knuth-Morris-Pratt algorithm performs pattern matching on a text string of length n and a pattern string of length m in O(n+m) time.
* Justification
  1. while-loop of **find_kmp()**
     * Conclusion : total number of iterations is 2n.
     * Analysis
       * Let s = j-k
         * Then s is the total amount by which the pattern P has been shifted with respect to the text T.
       * There are 3 cases in every loop.
         1. T[j] == P[k]
            * Δs = 0
              * why?
                * j and k increase simultaneously.
         2. T[j] != P[k] and k > 0
            * Δs is at least 1.
              * why?
                * j does not change.
                * Depending on the value fail[k], Δk may vary.
         3. T[j] != P[k] and k == 0
            * Δs = 1
              * why?
                * j increase by 1.
                * k does not change.
       * Thus, at each iteration of the loop, either j or s increases by at least 1.
       * Hence, the total number of iterations of the while loop in the KMP pattern-matching algorithm is at most **2n**.
  2. Failure Function
     * It simply runs in O(m) time.
  3. Therefore, O(n+m) running time.

* Simulation
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_02_03_kmp_simulation.png" style="width: 100%;"></img><br/>
</p>





## 13.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/part13_06_exercises.md">Exercises</a>
