<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_00_trees.md">Part 8. Trees</a>
</p>

### R-8.1 The following questions refer to the tree of Figure 8.3.
1. Which node is the root?
   * Sol.) /user/rt/courses/
2. What are the internal nodes?
   * Sol.) /user/rt/courses/, /user/rt/courses/cs016/, /user/rt/courses/cs016/homeworks/, /user/rt/courses/cs016/programs/, /user/rt/courses/cs252/, /user/rt/courses/cs252/projects/, /user/rt/courses/cs252/projects/papers/, /user/rt/courses/cs252/projects/demos/
3. How many descendants does node cs016/ have?
   * Sol.) 9 descendants
4. How many ancestors does node cs016/ have?
   * Sol.) 1 ancestor
5. What are the siblings of node homeworks/?
   * Sol.) grades, programs
6. Which nodes are in the subtree rooted at node projects/?
   * Sol.) papers, buylow, sellhigh, demos, market
7. What is the depth of node papers/?
   * Sol.) The depth is 3.
8. What is the height of the tree?
   * Sol.) The height is 4.

### R-8.2 Show a tree achieving the worst-case running time for algorithm depth.
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

### R-8.3 Give a justification of Proposition 8.4.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_03_proposition_8_4.png" style="height: 100px;"></img><br/>
</p>

* Sol.) 
  * Suppose not, i.e., there exists a leaf, L0, in a tree that its depth is not the maximum value among the tree's leaves and it is equal to the height of the tree.
  * Also, there exists at least one leaf L1 whose depth is the maximum among the nodes of the tree.
  * Let D0 and D1 the depth of L0 and L1 respectively.
    * Then D0 < D1
  * Considering the definition of the depth, L0 and L1 has (D0-1) and (D1-1) ancestors respectively.
  * Then L0's (D0-2)-th ancestor and L1's (D1-2)-th ancestor will be the children of the root with the height of (D0-2) and (D1-2) respectively.
  * By definition, the height of the root is (D1-2) because (D0-1) < (D1-1) ---> Contradiction.

### R-8.4 What is the running time of a call to T. height2(p) when called on a position p distinct from the root of T? (See Code Fragment 8.5.)
* Sol.) O(n). It can be considered as distinct subtree that regarding p as the root of it.

### R-8.5 Describe an algorithm, relying only on the BinaryTree operations, that counts the number of leaves in a binary tree that are the left child of their respective parent.
```python
def num_left_leaves(T, p=None):
    if p is None:
        p = T.root()
    if T.is_leaf(p):
        parent = T.parent(p)
        if p == T.left(parent):
            return 1
        else:
            return 0
    result = 0
    for c in T.children(p):
        result += num_left_leaves(T, c)
    return result
```

### R-8.6 Let T be an n-node binary tree that may be improper. Describe how to represent T by means of a proper binary tree T' with O(n) nodes.
* Sol.)
  * Case 1. n is even.
    * By moving leaves that are the only-childs of respective parents to some parents who also have only-child, T can turn out to be a proper tree.
  * Case 2. n is odd.
    * By repeating the job described in the even case, there will be only one leaf that remains to be the only child eventually.
    * Simply by add one dummy node as a sibling of that leaf, T' becomes a proper tree with (n+1) nodes, which can be considered as O(n).

### R-8.7 What are the minimum and maximum number of internal and external nodes in an improper binary tree with n nodes?
* Sol.)
  * Case 1.
    * minimum internal : n//2
    * maximum external : (n+1)//2
  * Case 2.
    * maximum internal : n-1
    * minimum external : 1

### Answer the following questions so as to justify Proposition 8.8.
1. What is the minimum number of external nodes for a proper binary tree with height h? Justify your answer.
   * Sol.) h-1
     * why?) Consider the case that very-left node can only have children.
2. What is the maximum number of external nodes for a proper binary tree with height h? Justify your answer.
   * Sol.) 2^(h-1)
     * why?) Consider the case that every leaf has the depth of h.
3. Let T be a proper binary tree with height h and n nodes. Show that log(n+1)−1 ≤ h ≤ (n−1)/2.
   * Sol.) 
     1. Case Q1 : n = (2h-1) -> h = (n+1)/2 : Upper bound of n
     2. Case Q2 : n = 2^(h+1)-1 -> h = log(n+1)-1 : Lower bound of n
4. For which values of n and h can the above lower and upper bounds on h be attained with equality?
   * Sol.)  

### R-8.9 Give a proof by induction of Proposition 8.9.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_09_proposition_8_9.png" style="height: 100px;"></img><br/>
</p>

* pf.) 
    1. h = 0;
       * Trivially, n_E = 1, n_I = 0
    2. h = 1;
       * Trivially, n_E = 2, n_I = 1
    3. Suppose, one of the external node gets children.
       * Then, that external node becomes internal and two new external nodes are generated.
       * Thus, n_E += 1, n_I += 1.
    4. It can be generalized that whenever a certain external node makes children, n_E and n_I increase by 1.
       * Therefore, n_E = n_I + 1

### R-8.10 Give a direct implementation of the num children method within the class BinaryTree.
```python
def num_children(self, p):
    result = 0
    for c in self.children(p):
        result += 1
    return result
```

### R-8.11 Find the value of the arithmetic expression associated with each subtree of the binary tree of Figure 8.8.
* Sol.)
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_11_proposition_8_8_subtree_value.png" style="height: 300px;"></img><br/>
</p>

### R-8.12 Draw an arithmetic expression tree that has four external nodes, storing the numbers 1, 5, 6, and 7 (with each number stored in a distinct external node, but not necessarily in this order), and has three internal nodes, each storing an operator from the set {+,−,×, /}, so that the value of the root is 21. The operators may return and act on fractions, and an operator may be used more than once.
* Sol.)
```python
from Part08_Trees.part08_05_expression_tree import ExpressionTree
from DataStructures.queue import LinkedQueue
from copy import deepcopy
class ExpressionGenerator:
    def __init__(self, num_list):
        self._num_list = num_list
        self._operator_set = '+-*/'
        self._perm_num_list = self.permutation(self._num_list)
        self._repeated_op_set = self.repeated_set(self._operator_set, len(self._num_list)-1)

    def display_all(self):
        result_set = []
        for op_set in self._repeated_op_set:
            op_tree_list = self.make_operator_tree(op_set)
            for op_tree in op_tree_list:
                for num_list in self._perm_num_list:
                    expression = self.add_numbers(op_tree, num_list)
                    value = expression.evaluate()
                    print('{} = {}'.format(expression, value))
                    result_set.append(expression)

    def find_value(self, value):
        for op_set in self._repeated_op_set:
            op_tree_list = self.make_operator_tree(op_set)
            for op_tree in op_tree_list:
                for num_list in self._perm_num_list:
                    expression = self.add_numbers(op_tree, num_list)
                    expression_value = expression.evaluate()
                    if expression_value == value:
                        print('{} = {}'.format(expression, value))
                        return expression
        return None


    def make_operator_tree(self, operator_list, result_list=None, root_tree=None, temp_tree=None, p=None):
        if result_list is None:
            result_list = []
            root_tree = ExpressionTree(operator_list.pop())
            temp_tree = root_tree
            p = temp_tree.root()
        if len(operator_list) == 0:
            root_tree_copy = deepcopy(root_tree)
            result_list.append(root_tree_copy)
            return result_list
        popped = operator_list.pop()
        # add leftward
        left = temp_tree._add_left(p, popped)
        operator_list_copy = deepcopy(operator_list)
        self.make_operator_tree(operator_list_copy, result_list, root_tree, temp_tree, left)
        temp_tree._delete(left)

        # add rightward
        right = temp_tree._add_right(p, popped)
        operator_list_copy = deepcopy(operator_list)
        self.make_operator_tree(operator_list_copy, result_list, root_tree, temp_tree, right)
        temp_tree._delete(right)
        return result_list

    def add_numbers(self, T, num_list, root_tree=None, p=None, num_list_copy=None):
        if root_tree is None:
            root_tree = deepcopy(T)
            p = root_tree.root()
            num_list_copy = deepcopy(num_list)
        if len(num_list) == 0:
            return root_tree
        if root_tree.left(p) is not None:
            self.add_numbers(T, num_list_copy, root_tree, root_tree.left(p), num_list_copy)
        else:
            num_tree = ExpressionTree(str(num_list_copy.pop()))
            root_tree._add_left(p, num_tree)
        if root_tree.right(p) is not None:
            self.add_numbers(T, num_list_copy, root_tree, root_tree.right(p), num_list_copy)
        else:
            num_tree = ExpressionTree(str(num_list_copy.pop()))
            root_tree._add_right(p, num_tree)
        return root_tree

    def repeated_set(self, S, result_length):
        result_set = []
        temp_queue = LinkedQueue()
        temp_queue.enqueue([])
        while not temp_queue.is_empty():
            dequeued = temp_queue.dequeue()
            if len(dequeued) == result_length:
                result_set.append(dequeued)
            else:
                for i in S:
                    temp = deepcopy(dequeued)
                    temp.append(i)
                    temp_queue.enqueue(temp)
        return result_set

    def permutation(self, S, num=None, result_list=None, temp_list=None):
        if num is None:
            num = len(S)
        if result_list is None and temp_list is None:
            result_list, temp_list = [], []
        for i in range(len(S)):
            popped = S.pop(i)
            temp_list.append(popped)
            if num == 1:
                temp_copy = deepcopy(temp_list)
                result_list.append(temp_copy)
            else:
                self.permutation(S, num - 1, result_list, temp_list)
            re_popped = temp_list.pop()
            S.insert(i, re_popped)
        return result_list

if __name__ == '__main__':
    num = [1, 5, 6, 7]
    a = ExpressionGenerator(num)
    # a.display_all()
    a.find_value(21)
```

### 





<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_00_trees.md">Part 8. Trees</a>
</p>