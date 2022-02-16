# Part 3. Algorithm Analysis

## 3.1 Experimental Studies
* Tech) Use __time__ function for time recording
    ```python
    from time import time
    start_time = time()
    # code section
    end_time = time()
    elapsed = end_time-start_time
    ```
  * Limit) Being affected by other processes sharing CPU
    * Antidote) Use __timeit__ module instead
    
### 3.1.1 Moving Beyond Experimental Analysis
* Premise) Primitive Operations   
  * Props.) The number, _t_ , of primitive operations an algorithm performs will be proportional to the actual running time of that algorithm.
  * List)
    * Assigning an identifier to an object
    * Determining the object associated with an identifier
    * Performing an arithmetic operation (for example, adding two numbers)
    * Comparing two numbers
    * Accessing a single element of a Python list by index
    * Calling a function (excluding operations executed within the function)
    * Returning from a function.
<br>
* Tech) Worst-Case Analysis
  * cf.) Average-Case Analysis requires expected running time based on a give input distribution => complicated

## 3.2 The Seven Functions Used in this book
  1. Constant Function   
  2. Logarithm Function
  3. Linear Function
  4. _N_-Log-_N_ Function
  5. Quadratic Function
     * e.g.) Nested Loops
  6. Cubic Function and other Polynomials
  7. Exponential Function
<br>
  * Concept) The Ceiling and Floor Functions
    1. └x┘ = the largest integer less than or equal to x.
    2. ┌x┐ = the smallest integer greater than or equal to x.
  
***
pg 145