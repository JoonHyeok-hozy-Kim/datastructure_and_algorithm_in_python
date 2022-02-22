<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 4. Recursion
#### Def) Recursion
* a technique by which a function makes one or more calls to itself
during execution, or by which a data structure relies upon smaller instances of
the very same type of structure in its representation

#### Concept) Activation Record (or Frame)
* a structure called in Python when a function is called
* store information about the progress of that invocation of the function
  1. namespace for storing the fuction call's parameters and local variables
  2. information about which command in the body of the function is currently executing

## 4.1 Illustrative Examples
### 4.1.1 The Factorial Function
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
```

### 4.1.2 Drawing an English Ruler
* Concept) English Ruler
  * For each inch, a tick with a numeric label should be placed
  * Major Tick Length : the length of the tick designating a whole inch
  * Minor Ticks : placed at intervals of 1/2 inch, 1/4 inch, and so on.

<p align="center">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part4_Recursion/images/4_1_english_ruler.png" style="height: 50px;"></img><br/>
</p>

* Tech) Consider it as a simple example of __Fractal__.




----------------------------------------
## 4.7 Excercises
<div>
    <p>
        <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part4_Recursion/part4_7_excercises.md">Exercises 4.7</a>
    </p>
</div>
