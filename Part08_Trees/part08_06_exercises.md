<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_00_trees.md">Part 8. Trees</a>
</p>

### R-8.1
1. /user/rt/courses/
2. /user/rt/courses/, /user/rt/courses/cs016/, /user/rt/courses/cs016/homeworks/, /user/rt/courses/cs016/programs/, /user/rt/courses/cs252/, /user/rt/courses/cs252/projects/, /user/rt/courses/cs252/projects/papers/, /user/rt/courses/cs252/projects/demos/
3. 9 descendants
4. 1 ancestor
5. grades, programs
6. papers, buylow, sellhigh, demos, market
7. The depth is 3.
8. The height is 4.

### R-8.2
* Running Time of the leaf element is O(n) in the following case.
```python
from DataStructures.tree import *
def recursive_add_left(T, idx, p=None):
    if p is None:
        root = T._add_root(idx)
        return recursive_add_left(T, idx-1, root)
    if idx == 0:
        return
    left = T._add_left(p, idx)
    return recursive_add_left(T, idx-1, left)

if __name__ == '__main__':
    a = LinkedBinaryTree()
    recursive_add_left(a, 5)
```





<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_00_trees.md">Part 8. Trees</a>
</p>