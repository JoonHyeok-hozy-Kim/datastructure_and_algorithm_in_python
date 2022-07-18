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







## 13.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/part13_06_exercises.md">Exercises</a>
