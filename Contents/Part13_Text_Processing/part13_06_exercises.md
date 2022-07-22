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
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/images/13_06_04.png" style="height: 500px;"></img><br/>
</p>



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part13_Text_Processing/part13_00_text_processing.md">Part 13. Text Processing</a>
</p>