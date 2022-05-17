<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 6. Stacks, Queues, and Deques
## 6.1 Stacks

#### Props.) Stack
* A collection of objects that are inserted and removed according to the last-in, first-out (LIFO) principle

#### Concept) The Adapter Pattern
* Applies to any context where we effectively want to modify an existing class so that its methods match those of a related, but different, class or interface
* How?) Define a new class in such a way that it contains an instance of the existing class as a hidden field, and then to implement each method of the new class using methods of this hidden instance variable

#### Concept) ArrayStack
* LIFO Stack implementation using Python's List class as an underlying storage
* Every operation has O(1) time consumption.
* However, O(n) running time is also possible if the List storage resizes.
  * Thus, it is desirable to create underlying List with the length of n.

### 6.1.3 Reversing Data Using a Stack
```python
def reverse_file(filename):
    s = ArrayStack()
    original = open(filename)
    for line in original:
        s.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not s.is_empty():
        output.write(s.pop + '\n')
    output.close()
```

### 6.1.4 Matching Parentheses and HTML Tags
#### Tech.) Matching Parentheses
```python
def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if lefty.index(S.pop()) != righty.index(c):
                return False
    return S.is_empty()
```

#### Tech.) Matching HTML Tags
```python
def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j > -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        print(tag)
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            elif S.pop() != tag[1:]:
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

if __name__ == '__main__':
    html = '<body><center><h1> The Little Boat </h1></center><p> The storm tossed the little boat like a cheap sneaker in an old washing machine.</p><ol><li> Will the salesman die? </li><li> What color is the boat? </li><li> And what about Naomi? </li></ol></body>'
    print(is_matched_html(html))
```

<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part06_Stacks_Queues_and_Deques/part06_04_exercises.md">Excercises</a>    
</p>
