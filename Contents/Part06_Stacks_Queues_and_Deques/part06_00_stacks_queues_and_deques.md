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
```python
class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass

class ArrayStack:
    """ LIFO Stack implementation using Python's List class as an underlying storage """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, val):
        self._data.append(val)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()
```

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

## 6.2 Queues
#### Props.) Queue
* A collection of objects that are inserted and removed according to the first-in, first-out (FIFO) principle

#### Concept) ArrayQueue
* Use Python's List class as the underlying storage.
* Set the default capacity of the queue by N.
  * And circularly use the Array with the modulo operator.
```python
from DataStructures.stack import Empty

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = -1

    def __len__(self):
        return self._size

    def __str__(self):
        text_list = ['[']
        if self._size > 0:
            for i in range(self._size):
                text_list.append(str(self._data[(self._front + i) % len(self._data)]))
                text_list.append(', ')
            text_list.pop()
        text_list.append(']')
        return ''.join(text_list)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        result = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front += 1
        return result

    def enqueue(self, val):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._front + self._size) % len(self._data)] = val
        self._size += 1

    def _resize(self, cap):
        temp = [None] * cap
        for i in range(self._size):
            temp[i] = self._data[(self._front + i) % len(self._data)]
        self._data = temp
        self._front = 0
```

## 6.3 Double-Ended Queue
```python
from DataStructures.stack import Empty

class ArrayDeque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = -1

    def __len__(self):
        return self._size

    def __str__(self):
        text_list = ['[']
        if self._size > 0:
            for i in range(self._size):
                text_list.append(str(self._data[(self._front + i) % len(self._data)]))
                text_list.append(', ')
            text_list.pop()
        text_list.append(']')
        return ''.join(text_list)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return Empty
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            return Empty
        return self._data[(self._front + self._size -1) % len(self._data)]

    def _resize(self, cap):
        temp = [None] * cap
        for i in range(self._size):
            temp[i] = self._data[(self._front + i) % len(self._data)]
        self._data = temp
        self._front = 0

    def add_first(self, val):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        if self._front == -1:
            new_front = 0
        elif self._front == 0:
            new_front = len(self._data)-1
        else:
            new_front = self._front-1
        self._data[new_front] = val
        self._front = new_front
        self._size += 1

    def add_last(self, val):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._front + self._size) % len(self._data)] = val
        self._size += 1

    def delete_first(self):
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        result = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        return result

    def delete_last(self):
        if self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        last_idx = (self._front + self._size -1) % len(self._data)
        result = self._data[last_idx]
        self._data[last_idx] = None
        self._size -= 1
        return result
```



<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Contents/Part06_Stacks_Queues_and_Deques/part06_04_exercises.md">Excercises</a>    
</p>
