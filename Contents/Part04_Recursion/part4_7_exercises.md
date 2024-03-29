
<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/part4_00_recursion.md">Part 4. Recursion</a>
    </p>
</div>

### R-4.1
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

### R-4.2
```python
# Traditional Power
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/images/4_07_02.png" style="height: 300px;"></img><br/>
</p>

### R-4.3
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
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/images/4_07_03.png" style="height: 300px;"></img><br/>
</p>

### R-4.4
```python
def reverse(S, start=None, stop=None):
    if start is None and stop is None:
        start, stop = 0, len(S)-1
    if start < stop:
        S[start], S[stop] = S[stop], S[start]
        return reverse(S, start+1, stop-1)
    return S
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/images/4_07_04.png" style="height: 300px;"></img><br/>
</p>

### R-4.5
```python
def puzzle_solve(k, U, S=None):
    from copy import deepcopy
    if S is None:
        S = []
    for i in range(len(U)):
        popped = U.pop(i)
        S.append(deepcopy(popped))
        if k == 1:
            print(''.join(S))
        else:
            puzzle_solve(k-1, U, S)
        popped_again = S.pop(-1)
        U.insert(i, popped_again)
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/images/4_07_05.png" style="height: 300px;"></img><br/>
</p>

### R-4.6 Describe a recursive function for computing the nth Harmonic number.
```python
def harmonic_number(n):
    if n == 1:
        return 1
    else:
        return harmonic_number(n-1) + 1/n
```

### R-4.7 Describe a recursive function for converting a string of digits into the integer it represents. For example, 13531 represents the integer 13,531.
```python
def string_converter(number):
    if number < 1000:
        return str(int(number))
    else:
        return string_converter(number/1000) + ',' + str(int(number%1000))
```

### R-4.8.
* Analysis) Running time is at least O(n) on the point that summation may happen n-times.

### C-4.9 Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loop
```python
def min_max(S, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(S)-1

    if start == end:
        return (S[start], S[end])
    elif start == end-1:
        if S[start] > S[end]:
            return (S[start], S[end])
        else:
            return (S[end], S[start])
    else:
        mid = (start+end)//2
        part_one = min_max(S, start, mid)
        part_two = min_max(S, mid+1, end)
        maximum = part_one[0] if part_one[0] > part_two[0] else part_two[0]
        minimum = part_one[1] if part_one[1] < part_two[1] else part_two[1]
        return (maximum, minimum)
```

### C-4.10 Describe a recursive algorithm to compute the integer part of the base-two logarithm of n using only addition and integer division.
```python
def log_base_two_int(n):
    if n == 1:
        return 0
    else:
        return log_base_two_int(n//2) + 1
```

### C-4.11 Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that is at most O(n^2) in the worst case without using sorting.
```python
def element_uniqueness(S, start=None, target=None):
    if start is None and target is None:
        start = 0
        target = start
    if start == len(S):
        return True
    else:
        if target == len(S):
            return element_uniqueness(S, start+1, start+1)
        else:
            if S[start] == S[target] and start != target:
                return False
            return element_uniqueness(S, start, target+1)
```

### C-4.12 Give a recursive algorithm to compute the product of two positive integers, m and n, using only addition and subtraction.
```python
def recursive_product(m, n):
    if m == 0 or n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return recursive_product(m, n-1) + m
```

### C-4.13 Prove by induction that the number of dashes printed by draw_interval(c) is 2^(c+1)−c−2.
>   <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/part4_recursion.md#412-drawing-an-english-ruler">English Ruler</a>
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/images/4_07_13.png" style="height: 300px;"></img><br/>
</p>

### C-4.14 
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/images/4_07_14.png" style="width: 900px;"></img><br/>
</p>

```python
class TowersOfHanoi:

    def __init__(self, disk_num, peg_num=3):
        self._disk_num = disk_num
        self._peg_num = peg_num
        self._platform_dict = [[i+1 for i in range(disk_num)]]
        for i in range(peg_num-1):
            self._platform_dict.append([])

    def play(self, n=None, from_peg_idx=None, to_peg_idx=None, temp_peg_idx=None):
        if n is None and from_peg_idx is None and to_peg_idx is None and temp_peg_idx is None:
            n = self._disk_num
            from_peg_idx, to_peg_idx, temp_peg_idx = 0, 2, 1
        from_peg = self._platform_dict[from_peg_idx]
        to_peg = self._platform_dict[to_peg_idx]
        temp_peg = self._platform_dict[temp_peg_idx]
        if n == 1:
            disk = from_peg.pop(0)
            to_peg.insert(0, disk)
            print(self)
        else:
            self.play(n-1, from_peg_idx, temp_peg_idx, to_peg_idx)
            disk = from_peg.pop(0)
            to_peg.insert(0, disk)
            print(self)
            self.play(n-1, temp_peg_idx, to_peg_idx, from_peg_idx)

    def __str__(self):
        from copy import deepcopy
        result_text_list = ['-----------', '\n']
        platform_copy = deepcopy(self._platform_dict)
        for j in range(self._disk_num):
            for i in range(self._peg_num):
                if len(platform_copy[(i+1)*(-1)]) == 0:
                    result_text_list.append('|')
                else:
                    result_text_list.append(str(platform_copy[(i+1)*(-1)].pop(-1)))
                result_text_list.append('  ')
            result_text_list.append('\n')
        return ''.join(reversed(result_text_list))

    def test_play_by_luck(self):
        from random import randint
        move_count = 0
        while len(self._platform_dict[-1]) < self._disk_num:
            from_peg = randint(0, self._peg_num-1)
            to_peg = randint(0, self._peg_num-1)
            if from_peg != to_peg:
                move_count += self.move_disk(from_peg, to_peg)
        print('Move count : {}'.format(move_count))
        print(self)

    def move_disk(self, from_peg_idx, to_peg_idx):
        from_peg = self._platform_dict[from_peg_idx]
        to_peg = self._platform_dict[to_peg_idx]
        if len(from_peg) == 0:
            print('Cannot move from an empty disk.')
            return 1
        disk = from_peg.pop(0)
        if len(to_peg) > 0:
            if to_peg[0] < disk:
                print('Cannot move to the smaller disk.')
                from_peg.insert(0, disk)
                return 1
        to_peg.insert(0, disk)
        print(self)
        return 1


if __name__ == '__main__':
    t1 = TowersOfHanoi(6)
    print(t1)
    t1.play()
```

### C-4.15 Write a recursive function that will output all the subsets of a set of n elements (without repeating any subsets).
```python
def subset(S, start=None, end=None, result_list=None):
    if start is None and end is None:
        start, end = 0, 0
        result_list = []
    if start == len(S):
        return result_list
    else:
        if end < len(S):
            if start < end:
                result_list.append([S[start], S[end]])
            return subset(S, start, end+1, result_list)
        else:
            return subset(S, start+1, start+1, result_list)
```

### C-4.16 Write a short recursive Python function that takes a character string s and outputs its reverse.
```python
def string_reverse(string, start=None, end=None, str_list=None):
    if start is None and end is None:
        start, end = 0, len(string)-1
        str_list = list(string)
    if start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        return string_reverse(string, start+1, end-1, str_list)
    else:
        result = ''.join(str_list)
        return result
```

### C-4.17 Write a short recursive Python function that determines if a string s is a palindrome, that is, it is equal to its reverse
```python
def palindrome(s, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(s)-1
    if start < end:
        if s[start] != s[end]:
            return False
        return palindrome(s, start+1, end-1)
    return True
```

### C-4.18 Use recursion to write a Python function for determining if a string s has more vowels than consonants.
```python
def more_vowels(s, idx=None, vowel=None, consonant=None):
    if idx is None and vowel is None and consonant is None:
        idx, vowel, consonant = 0, 0, 0
    if idx < len(s):
        if s[idx] in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            consonant += 1
        return more_vowels(s, idx+1, vowel, consonant)
    return True if vowel > consonant else False
```

### C-4.19 Write a short recursive Python function that rearranges a sequence of integer values so that all the even values appear before all the odd values.
```python
def even_first(S, idx=None):
    if idx is None:
        idx = 0
    if idx < len(S):
        if S[idx]%2 == 0:
            even_number = S.pop(idx)
            S.insert(0, even_number)
        return even_first(S, idx+1)
    return S
```

### C-4.20 Given an unsorted sequence, S, of integers and an integer k, describe a recursive algorithm for rearranging the elements in S so that all elements less than or equal to k come before any elements larger than k. What is the running time of your algorithm on a sequence of n values?
* Analysis) O(n) running time
```python
def sort_by_k(S, k, idx=None, new_S=None):
    if idx is None and new_S is None:
        idx = 0
        new_S = [k]
    if idx < len(S):
        if S[idx] <= k:
            new_S.insert(0, S[idx])
        else:
            new_S.append(S[idx])
        return sort_by_k(S, k, idx+1, new_S)
    return new_S
```

### C-4.21 Suppose you are given an n-element sequence, S, containing distinct integers that are listed in increasing order. Given a number k, describe a recursive algorithm to find two integers in S that sum to k, if such a pair exists. What is the running time of your algorithm?
* Analysis) At worst O(n) running time
```python
def sum_to_k(S, k, start=None, end=None, result=None):
    if start is None and end is None and result is None:
        start, end, result = 0, 0, []
    if start == len(S):
        return result
    elif end == len(S):
        return sum_to_k(S, k, start+1, start+1, result)
    else:
        if S[start] + S[end] == k:
            result.append((S[start], S[end]))
        return sum_to_k(S, k, start, end+1, result)
```

### C-4.22 Develop a nonrecursive implementation of the version of power from Code Fragment 4.12 that uses repeated squaring.
```python
def power_by_square_and_loop(x, n):
    result = 1
    for i in range(n//2):
        result *= x*x
    if n%2 == 1:
        result *= x
    return result
```

### P-4.23 Implement a recursive function with signature find(path, filename) that reports all entries of the file system rooted at the given path having the given file name.
* list_dir?

### P-4.24 Write a program for solving summation puzzles by enumerating and testing all possible configurations. Using your program, solve the three puzzles given in Section 4.4.3
```python
def summation_puzzle(k, U, S=None):
    from copy import deepcopy
    if S is None:
        S = []
    for i in range(len(U)):
        popped = U.pop(i)
        S.append(deepcopy(popped))
        if k == 1:
            print(''.join(S))
        else:
            summation_puzzle(k-1, U, S)
        popped_again = S.pop(-1)
        U.insert(i, popped_again)
```

### C-4.25 Provide a nonrecursive implementation of the draw interval function for the English ruler project of Section 4.1.2.
```python
class EnglishRulerLoop:
    def __init__(self, num_inches, major_length):
        self._num_inches = num_inches
        self._major_length = major_length

    def draw_line(self, length, label=''):
        line_text = []
        for i in range(length):
            line_text.append('-')
        if label:
            line_text.append(' ')
            line_text.append(label)
        result_text = ''.join(line_text)
        return result_text

    def draw(self):
        result_text = []
        for i in range(self._major_length):
            if i == 0:
                for j in range(self._num_inches):
                    result_text.append(self.draw_line(self._major_length, str(j+1)))
            else:
                len_result_text = len(result_text)
                for j in range(len_result_text):
                    result_text.insert(j*2, self.draw_line(self._major_length-i))
        result_text.insert(0, self.draw_line(self._major_length, str(0)))
        print('\n'.join(result_text))

if __name__ == '__main__':
    e1 = EnglishRulerLoop(2, 6)
    e1.draw()
```
### P-4.26 Tower of Hanoi problem
* Solution : <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/part4_7_exercises.md#c-414">C-4.14</a>

### P-4.27 

<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part04_Recursion/part4_00_recursion.md">Part 4. Recursion</a>
    </p>
</div>