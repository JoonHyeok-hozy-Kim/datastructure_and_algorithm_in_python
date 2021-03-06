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


## 13.3 Dynamic Programming
#### Concept) Properties needed for applying a **Dynamic Programming Solution**
1. Simple Subproblems
   * There has to be some way of repeatedly breaking the global optimization problem into subproblems. 
   * Moreover, there should be a way to parameterize subproblems with just a few indices, like i, j, k, and so on.
2. Subproblem Optimization
   * An optimal solution to the global problem must be a composition of optimal subproblem solutions.
3. Subproblem Overlap
   * Optimal solutions to unrelated subproblems can contain subproblems in common.


### 13.3.1 Matrix Chain-Product
* Consider calculating a chain of matrix products.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_03_03_matrix_chain_1.png" style="height: 100px;"></img><br/>
</p>

* Prop.) Parenthesizing may change the performance of products while not altering the result.
  * ex.)
    * Let 
      * B : 2 x 10 matrix
      * C : 10 x 50 matrix
      * D : 50 x 20 matrix
    * Then
      1. (B·C)·D requires 2·10·20 + 10·50·20 = 10400 multiplications
      2. B·(C·D) requires 2·10·50 + 2·50·20 = 3000 multiplications
      
#### Tech.) Find an optimal parenthesizing for chain of products.
1. Split problems into **subproblems**.
   * Put i, j where 0 < i <= j < n.
   * Let N_(i,j) : the minimum number of multiplications needed to compute this subexpression.
     * Then N_(0,(n-1)) denotes the whole problem.
2. Characterize the optimal solutions for the subproblems.
   * We may divide into subproblems by finding an optimal k such that
     * (Ai···Ak)·(Ak+1···Aj), for some k ∈ {i,i + 1,..., j −1}
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_03_03_matrix_chain_2.png" style="height: 100px;"></img><br/>
</p>

#### Implementation
```python
def matrix_chain(d):
    """
    :param d: a list of n+1 numbers such that size of kth matrix is d[k]-by-d[k+1].
    :return: n-by-n table such that N[i][j] represents the minimum number of multiplications needed to compute the product of Ai through Aj inclusive.
    """
    n = len(d)-1
    N = [[0]*n for i in range(n)]

    for b in range(n):
        for i in range(n-b):
            j = i+b
            if i != j:
                N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i, j))
    return N
```

### 13.3.2 DNA and Text Sequence Alignment
#### Concept) Subsequence
* Def.
  * Given a string X = x_0 x_1 x_2 ··· x_(n−1), a subsequence of X is any string that is of the form x_(i1) x_(i2) ··· x_(ik) 
    * where i_j < i_(j+1); that is, it is a sequence of characters that are   not necessarily contiguous but are nevertheless taken in order from X.
* ex.)
  * "AAAG" is a subsequence of the string "CGATAATTGAGA"
  
#### Concept) Longest Common Sequence (LCS)
  * For strings X and Y, LCS is the longest string S that is a subsequence of both X and Y
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_03_04_lcs_1.png" style="height: 300px;"></img><br/>
</p>

#### Implementation
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
```

## 13.4 Text Compression and the Greedy Method

#### Concept) Text Compression
* What is this?
  * Encode a string of alphabets into a small binary string Y

### 13.4.1 The Huffman Coding Algorithm
* Goal
  * Use fixed-length binary strings to encode characters
  * Save space over a fixed-length encoding by using short code-word strings to encode high-frequency characters and long code-word strings to encode low-frequency characters.
  * Use a variable-length encoding specifically optimized for a given string X over any alphabet.

* How?
  1. Convert each character in X to a variable-length code-word
  2. Concatenate all these code-words in order to produce the encoding Y for X
     * In order to avoid ambiguities, we insist that no code-word in our encoding be a prefix of another code-word in our encoding. 
     * Such a code is called a prefix code, and it simplifies the decoding of Y to retrieve X
  3. Use Binary Tree for the representation of the string X.
     * Each edge in T represents a bit in a code-word, with an edge to a left child representing a “0” and an edge to a right child representing a “1.”
     * Each leaf v is associated with a specific character, and the code-word for that character is defined by the sequence of bits associated with the edges in the path from the root of T to v.
     * Each leaf v has a frequency, f(v), which is simply the frequency in X of the character associated with v.

* Ex.) string X = "a fast runner need never be afraid of the dark"
<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_04_01_huffman.png" style="width: 100%;"></img><br/>
</p>

* Implementation : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/TextProcessingAlgorithms/huffman.py">Huffman Code</a>

* Analysis
  * Running Time
    * Huffman’s algorithm constructs an optimal prefix code for a string of length n with d distinct characters in O(n + d*log(d)) time.
      * where d is the distinct number of alphabets in the string.
  * Justification
    1. while-loop : O(log(d)) 
      * why?
        * We used priority queue represented with heap ordered by the frequency.
    2. Each iteration takes two nodes out of Q and adds one in (d-1) time.

### 13.4.2 The Greedy Method
#### Concept) Greedy-Choice property.
* a global optimal condition can be reached by a series of locally optimal choices
* choices that are each the current best from among the possibilities available at the time)



## 13.5 Tries
#### Concept) Trie
* a tree-based data structure for storing strings in order to support fast pattern matching.
* The primary query operations that tries support are pattern matching and prefix matching.
  * The latter operation involves being given a string X, and looking for all the strings in S that contain X as a prefix.

### 13.5.1 Standard Tries
* Def.)
  * Let S be a set of s strings from alphabet Σ such that no string in S is a prefix of another string.
  * A standard trie for S is an **ordered tree** T with the following properties.
    * Each node of T, except the root, is labeled with a character of Σ.
    * The children of an internal node of T have distinct labels.
    * T has s leaves, each associated with a string of S, such that the concatenation of the labels of the nodes on the path from the root to a leaf v of T yields the string of S associated with v.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_05_01_trie_example.png" style="width: 100%;"></img><br/>
</p>

* Basic Props.)
  * No string in S is a prefix of another string.
    * i.e.) Each string of S is uniquely associated with a leaf of T.
    * We can always satisfy this assumption by adding a special character that is not in the original alphabet Σ at the end of each string.
  * An internal node in a standard trie T can have anywhere between 1 and |Σ| children.
  * A path from the root of T to an internal node v at depth k corresponds to a k-character prefix X[0:k] of a string X of S.

<br> 

#### Prop.) A standard trie storing a collection S of s strings of total length n from an alphabet Σ has the following properties:
* The height of T is equal to the length of the longest string in S.
* Every internal node of T has at most |Σ| children.
* T has s leaves
* The number of nodes of T is at most n+1.
  * Worst Case
    * No two strings share a common nonempty prefix
    * i.e.) all internal nodes have one child.


#### Tech.) Trie as a set or map whose keys are the strings of S.
* How?
  * We perform a search in T for a string X by tracing down from the root the path indicated by the characters in X.
  * If this path can be traced and terminates at a leaf node, then we know X is a key in the map.
* Performance
  * The running time of the search for a string of length m is O(m·|Σ|)
    * why?)
      * We visit at most (m+1) nodes of T and we spend O(|Σ|) time at each node determining the child having the subsequent character as a label.
      * O(|Σ|) upper bound
        * Recall that every node has at most |Σ| children.
        * O(log|Σ|) or expected O(1) are also available
          1. O(log|Σ|)
             * by mapping characters to children using a secondary search table or hash table at eachnode
          2. expected O(1)
             * by using a direct lookup table of size |Σ| at each node, if |Σ| is sufficiently small
        * Thus, we typically expect a search for a string of length m to run in O(m) time.

#### Tech.) Word Matching
* Concept Desc.
  * Word matching differs from standard pattern matching because the pattern cannot match an arbitrary substring of the text—only one of its words.
  * To accomplish this, each word of the original document must be added to the trie.
* How?
  * Use an incremental algorithm that inserts the strings one at a time.
  * To insert a string X into the current trie T, we trace the path associated with X in T, creating a new chain of nodes to store the remaining characters of X when we get stuck.
  * The running time to insert X with length m is similar to a search, with worst-case O(m·|Σ|) performance, or expected O(m) if using secondary hash tables at each node.
  * Thus, constructing the entire trie for set S takes expected **O(n)** time, where n is the total length of the strings of S.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_05_02_trie_example.png" style="width: 100%;"></img><br/>
</p>


### 13.5.2 Compressed Tries
#### Def.) Compressed Tries
* A trie that ensures that each internal node in the trie has at least two children.
* It enforces this rule by compressing chains of single-child nodes into individual edges.

#### Concept) Redundancy
* For a standard trie T, an internal node v of T is redundant if v has one child and is not the root.
* A chain of k ≥ 2 edges, (v_0,v_1)(v_1,v_2)···(v_(k−1),v_k), is redundant if:
  * v_i is redundant for i = 1,...,k−1.
  * v_0 and v_k are not redundant.
* Treatment
  * We can transform T into a compressed trie as follows.
    1. Replace each redundant chain (v_0,v_1)···(v_(k−1),v_k) of k ≥ 2 edges into a single edge (v_0,v_k)
    2. Relabel v_k with the concatenation of the labels of nodes v_1,...,v_k.

#### Props.) A compressed trie storing a collection S of s strings from an alphabet of size d has the following properties:
* Every internal node of T has at least two children and most d children.
* T has s leaves nodes.
* The number of nodes of T is O(s).

#### Prop.) Advantage of the Compressed Trie
  * The number of nodes of the compressed trie is proportional to the number of strings and not to their total length
  * A compressed trie is truly advantageous only when it is used as an auxiliary index structure over a collection of strings already stored in a primary structure.
    * Notation
      * Let the collection S of strings is an array of strings S[0], S[1], ..., S[s− 1].
      * Represent X by a combination of three integers (i, j : k), such that X = S[i][ j : k];
        * X is the slice of S[i] consisting of the characters from the j th up to but not including the kth.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_05_03_compressed_trie_notation.png" style="width: 100%;"></img><br/>
</p>


### 13.5.3 Suffix Tries
* Def.)
  * Tries is for the case when the strings in the collection S are all the suffixes of a string X.
* How?
  * The label of each vertex is a pair (j,k) indicating the string X[ j : k].
  * To satisfy the rule that no suffix of X is a prefix of another suffix, we can add a special character, denoted with $, that is not in the original alphabet Σ at the end of X (and thus to every suffix). 
    * That is, if string X has length n, we build a trie for the set of n strings X[ j:n], for j = 0,...,n−1.
* Advantage
  * Saving Space
* Prop.) 
  * The compact representation of a suffix trie T for a string X of length n uses O(n) space.


<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_05_04_suffix_tries.png" style="width: 100%;"></img><br/>
</p>


#### Tech.) Using a Suffix Trie
* The suffix trie T for a string X can be used to efficiently perform pattern-matching queries on text X.
* We can determine whether a pattern P is a substring of X by trying to trace a path associated with P in T.
* P is a substring of X if and only if such a path can be traced.
  * If node v has label (j,k) and Y is the string of length y associated with the path from the root to v (included), then X[k−y:k] = Y.


### 13.5.4 Search Engine Indexing
#### Concept) Inverted Files
* Def.)
  * A dictionary storing key-value pairs (w,L)
    * where where w is a word and L is a collection of pages containing word w
    * The keys (words) in this dictionary are called index terms and should be a set of vocabulary entries and proper nouns as large as possible.
    * The elements in this dictionary are called occurrence lists and should cover as many Web pages as possible.
* How to implement
  1. An array storing the occurrence lists of the terms (in no particular order).
  2. A compressed trie for the set of index terms, where each leaf stores the index of the occurrence list of the associated term.



## 13.6 <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/part13_06_exercises.md">Exercises</a>
