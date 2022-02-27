<div>
    <p>
        Back to <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python#readme">Index</a>
    </p>
</div>

# Part 5. Array-Based Sequences
## 5.1 Python's Sequence Types

* Point
  * _list_, _tuple_, and _str_ class may look similar.
  * However, the ways that instances of these classes are represented internally in Python differ.
    * It may go against _encapsulation_ of OOD -- a user does not have to know how each class works internally.
    * But the efficiency of a program depends greatly on it.
      * _asymptotic analysis_ will be used for analyzing the efficiency.

## 5.2 Low-Level Arrays
### Concepts)
#### byte
  * a typical unit that groups bits, which contain information.
#### memory address
  * an abstraction that computer uses in order to keep track of what information is stored in what byte.
  * Each byte of memory is associated with a unique number that servers as its address (binarily represented).
#### random access memory (RAM)
  * Despite the sequential nature of the numbering system, computer hardware is designed, in theory, so that any byte of the main memory can be efficiently accessed based upon its memory address.
  * i.e.) Any individual byte of memory can be stored or retrieved in O(1) time.
#### array
  * a representation that a group of related variables can be stored one after another in a contiguous portion of the computer's memory.
  * ex) a string class instance 'SAMPLE' is stored in 12 consecutive bytes of memory.
    * why?) In Python each Unicode character is represented with 16 bits (=2 Bytes). Thus, 6 characters take 12 Bytes.
#### cell
  * each location within an array
  * Prop.) Each cell of an array must use the same number of bytes so that _constant time spent on accessing an arbitrary cell based on its index_ is secured.
#### index
  * an integer that describe a cell's location within the array

### 5.2.1 Referential Arrays
* Def.) An array that contains references of the objects
  * It simply stores objects' references, not the objects themselves.
  * 64-bit is used for each reference.
* Prop.)
  1. If an immutable object's reference, say an integer, is stored in a referential array and an operation that changes the immutable, such as addition, 
     * it is the reference of the new immutable that supercedes the original one.
     * it is not that the immutable itself changes.
  2. list() method creates only _shallow copy_, which copies the references identical to the original array's.
  3. deepcopy() function creates _new_ elements with new references.
  4. extent() method adds references of another array, copying identical references of its elements.

### 5.2.2 Compact Arrays in Python
* Def.) Compact Array
  * an array that contains elements, not the references of elements.
* Prop.)
  1. Less memory required than Referential Array
     1. Comparison with str class
        * str class is a compact that contains Unicodes as elements.
        * Since, each Unicode takes 2-Bytes, less memory required than referential array, which allocates 64-bits(4-Bytes) for each cell.
     2. Comparison by integer storing.
        * When a referential array stores an integer, following two elements take memory.
          1. reference of the integer : 4-Bytes
          2. int instance being stored elsewhere in memory : typically 14-Bytes.
        * Compact Array directly contains the int instance.
  2. High Performance due to consecutive storing of elements in the memory.
  
#### array module : compact storage for arrays in Python
```python
import array
primes = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
```
* Prop.) Takes data type as first argument parameter.
  * Datatypes are from C-Language
  * User-defined types cannot be used.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/images/05_02_02_array_class_first_parameter.png" style="height: 300px;"></img><br/>
</p>






<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part05_Array_Based_Sequences/part05_07_exercises.md">Excercises</a>    
</p>
