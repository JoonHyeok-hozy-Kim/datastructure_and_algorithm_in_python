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

### R-8.13 Draw the binary tree representation of the following arithmetic expression: (((5+2)*(2-1))/((2+9)+((7-2)-1))*8)
```python
from Part08_Trees.part08_05_expression_tree import ExpressionTree, build_expression_trees
from DataStructures.tree import BinaryLayout
exp_str = '(((5+2)*(2-1))/((2+9)+((7-2)-1))*8)'
a = build_expression_trees(exp_str)
b = BinaryLayout(a)
print(exp_str, '=', a.evaluate())
print(b.execute())
```
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_13_expression_tree_display.png" style="height: 300px;"></img><br/>
</p>

### R-8.14 Justify Table 8.2, summarizing the running time of the methods of a tree represented with a linked structure, by providing, for each method, a description of its implementation, and an analysis of its running time.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_14_table_8_2.png" style="height: 300px;"></img><br/>
</p>

* Sol.) 
  * len : return parameter self._size -> O(1)
  * is_empty : return len(self) == 0 -> O(1)
  * root : return self._root -> O(1)
    * make_position method also takes O(1) running time.
  * is_root : return p == self.root() -> O(1)
  * is_leaf : return self.num_children() == 0 -> O(1)
    * Technically, it is O(c_p). If c_p is considered to be constant, then it is O(1)
  * children(p) : for loop executed trough every child -> O(c_p)
  * depth(p) : go all the way up to the root of the tree -> O(d_p)
  * height : maximum height value from children + 1.
    * Due to the maximum operation, height calculation of O(n) times is required.

### R-8.15 The LinkedBinaryTree class provides only nonpublic versions of the update methods discussed on page 319. Implement a simple subclass named MutableLinkedBinaryTree that provides public wrapper functions for each of the inherited nonpublic update methods.
```python
class MutableLinkedBinaryTree(LinkedBinaryTree):

    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def delete(self, p):
        return self._delete(p)
```

### R-8.16 Let T be a binary tree with n nodes, and let f() be the level numbering function of the positions of T, as given in Section 8.3.2.
<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_00_trees.md#tech-how"> -> Numbering Revisited</a>
</p>

1. Show that, for every position p of T, f(p) ≤ 2^n −2.
   * Sol.) Extreme case must be that every node has only one right child.
     * In that specific case, for p_i and p_(i+1), which p_i is parent of p_(i+1), f(p_(i+1)) = 2*f(p_i)+2
     * Then f(p_i) = {f(p_0) + 2} * 2^(i-1) - 2 = 2^i-2
     * Therefore, the leaf node, which must be n-th node, will have f(p) = 2^n-2.
2. Show an example of a binary tree with seven nodes that attains the above upper bound on f(p) for some position p.
```python
from DataStructures.tree import MutableLinkedBinaryTree
a = MutableLinkedBinaryTree()
for i in range(7):
    if i == 0:
        node = a.add_root(i)
    else:
        node = a.add_right(node, i)
print(a)
```

### R-8.17 Show how to use the Euler tour traversal to compute the level number _f(p)_, as defined in Section 8.3.2, of each position in a binary tree T.
```python
from DataStructures.tree import EulerTour
class LevelNumberCalculator(EulerTour):

    def f(self, p):
        return self._tour(self.tree().root(), p)

    def _tour(self, current_p, target_p, level_num=None):
        if level_num is None:
            level_num = 0
        if current_p == target_p:
            return level_num
        if self.tree().left(current_p) is not None:
            left_val = self._tour(self.tree().left(current_p), target_p, 2*level_num+1)
            if left_val is not None:
                return left_val
        if self.tree().right(current_p) is not None:
            right_val = self._tour(self.tree().right(current_p), target_p, 2*level_num+2)
            if right_val is not None:
                return right_val

if __name__ == '__main__':
    from DataStructures.tree import MutableLinkedBinaryTree
    a = MutableLinkedBinaryTree()
    for i in range(7):
        if i == 0:
            node = a.add_root(i)
        else:
            node = a.add_right(node, i)
    b = LevelNumberCalculator(a)
    
    b_root = b.tree().root()
    print(b.f(b_root))
    
    b_root_right = b.tree().right(b_root)
    print(b.f(b_root_right))
```

### R-8.18 Let T be a binary tree with n positions that is realized with an array representation A, and let f() be the level numbering function of the positions of T, as given in Section 8.3.2. Give pseudo-code descriptions of each of the methods root, parent, left, right, is leaf, and is root. 
```python
class ArrayTree:

    class Position:
        def __init__(self, container, element):
            self._container = container
            self._element = element

        def element(self):
            return self._element

    def _make_position(self, element):
        return self.Position(self, element)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p.element() is None:
            raise ValueError('p is no longer valid.')
        return p.element()

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def root(self):
        if self.is_empty():
            raise ValueError('Tree is Empty.')
        return self._data[0]

    def parent(self, p):
        idx = self._data.index(p)
        if i % 2 == 0:
            return self._data[(idx-2)//2]
        else:
            return self._data[(idx-1)//2]

    def left(self, p):
        idx = self._data.index(p)
        if len(self) < 2*idx+1:
            return None
        else:
            return self._data[2*idx+1]

    def right(self, p):
        idx = self._data.index(p)
        if len(self) < 2*idx+2:
            return None
        else:
            return self._data[2*idx+2]

    def is_leaf(self, p):
        idx = self._data.index(p)
        return self._data[2*idx+1] is None and self._data[2*idx+2] is None

    def is_root(self, p):
        return self._data.index(p) == 0
    
    def f(self, p):
        return self._data.index(p)
```

### R-8.19 Our definition of the level numbering function f(p), as given in Section 8.3.2, began with the root having number 0. Some authors prefer to use a level numbering g(p) in which the root is assigned number 1, because it simplifies the arithmetic for finding neighboring positions. Redo Exercise R-8.18, but assuming that we use a level numbering g(p) in which the root is assigned number 1.
```python
class ArrayTree:
    def g(self, p):
        return self._data.index(p) + 1
```

### R-8.20 Draw a binary tree T that simultaneously satisfies the following:
* Each internal node of T stores a single character.
* A preorder traversal of T yields EXAMFUN.
* An inorder traversal of T yields MAFXUEN.  
<br/>
<br/>
* Sol.) Use the following programs.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_20_answer.png" style="height: 150px;"></img><br/>
</p>

```python
from DataStructures.tree import MutableLinkedBinaryTree
from DataStructures.queue import LinkedQueue
from copy import deepcopy
def tree_generator(element_list):
    result_list = []
    q = LinkedQueue()
    num_elements = len(element_list)
    initial_tree = MutableLinkedBinaryTree()
    initial_tree.add_root(element_list.pop(0))
    q.enqueue(initial_tree)

    while len(element_list) > 0:
        popped = element_list.pop(0)
        current_len = len(q)
        for i in range(current_len):
            dequeued = q.dequeue()
            tree_builder = TreeBuilderTour(dequeued)
            tree_list = tree_builder.execute(popped)
            for tree in tree_list:
                q.enqueue(tree)

    while not q.is_empty():
        dequeued = q.dequeue()
        if len(dequeued) == num_elements:
            result_list.append(dequeued)

    return result_list

class TreeBuilderTour(EulerTour):
    def execute(self, e):
        result_list = []
        self._tour(self.tree().root(), e, result_list)
        return result_list

    def _tour(self, p, e, result_list):
        self._hook_previsit(p, e, result_list)
        if self.tree().left(p) is not None:
            self._tour(self.tree().left(p), e, result_list)
        if self.tree().right(p) is not None:
            self._tour(self.tree().right(p), e, result_list)

    def _hook_previsit(self, p, e, result_list):
        if self.tree().right(p) is None:
            # Add left if left and right are None
            if self.tree().left(p) is None:
                new_left = self.tree()._add_left(p, e)
                tree_copy = deepcopy(self.tree())
                result_list.append(tree_copy)
                self.tree()._delete(new_left)

            # Add right if right is None
            new_right = self.tree()._add_right(p, e)
            tree_copy = deepcopy(self.tree())
            result_list.append(tree_copy)
            self.tree()._delete(new_right)

def preorder_inorder_comparison(T, pre_target, in_target, p=None, pre_result=None, in_result=None):
    if p is None:
        p = T.root()
        pre_result = []
        in_result = []
    pre_result.append(p.element())
    if T.left(p) is not None:
        preorder_inorder_comparison(T, pre_target, in_target, T.left(p), pre_result, in_result)
    in_result.append(p.element())
    if T.right(p) is not None:
        preorder_inorder_comparison(T, pre_target, in_target, T.right(p), pre_result, in_result)

    if pre_target == ''.join(pre_result):
        if in_target == ''.join(in_result):
            return T

if __name__ == '__main__':
    str_list = list('EXAMFUN')
    tree_list = tree_generator(str_list)
    for tree in tree_list:
        result = preorder_inorder_comparison(tree, 'EXAMFUN', 'MAFXUEN')
        if result is not None:
            print(tree)
```

### R-8.21 In what order are positions visited during a preorder traversal of the tree of Figure 8.8?
* Sol.) Inorder traversal.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_21_figure_8_8.png" style="height: 450px;"></img><br/>
</p>

### R-8.22 In what order are positions visited during a postorder traversal of the tree of Figure 8.8?
* Sol.) 3 1 + 3 x 9 5 - 2 + / 3 7 4 - x 6 + -

### R-8.23 Let T be an ordered tree with more than one node. Is it possible that the preorder traversal of T visits the nodes in the same order as the postorder traversal of T? If so, give an example; otherwise, explain why this cannot occur. Likewise, is it possible that the preorder traversal of T visits the nodes in the reverse order of the postorder traversal of T? If so, give an example; otherwise, explain why this cannot occur. 
* Sol.)
  * Preorder and postorder traversal can not traverse an ordered tree identically.
    * Preorder visits parent first while postorder visits child as first priority.
  * If every parent in a tree has only one child, preorder and postorder may traverse in exactly reversed manner.

### R-8.24 Answer the previous question for the case when T is a proper binary tree with more than one node.
* Sol.)
  * Still no identical traverse.
  * Reverse order is impossible as well.
    * why?) For a proper binary tree, if a parent has at least one descendant, it must have both left and right child.
      * Since the tree is ordered, traversing siblings will go from left to right whether the traversal is preorder or postorder.
      * Thus, reversed traversal of preorder can not be equal to postorder traversal.

### R-8.25 Consider the example of a breadth-first traversal given in Figure 8.17. Using the annotated numbers from that figure, describe the contents of the queue before each pass of the while loop in Code Fragment 8.14. To get started, the queue has contents {1} before the first pass, and contents {2,3,4} before the second pass.
<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_25_figure_8_17.png" style="height: 450px;"></img><br/>
</p>

* Sol.)
    * Initial    : {1}
    * 1 dequeued : {2,3,4}
    * 2 dequeued : {3,4,5,6}
    * 3 dequeued : {4,5,6,7,8,9,10,11}
    * 4 dequeued : {5,6,7,8,9,10,11,12,13,14,15,16}

### R-8.26 The collections.deque class supports an extend method that adds a collection of elements to the end of the queue at once. Reimplement the breadthfirst method of the Tree class to take advantage of this feature.
```python
def breadthfirst(self, p=None):
    from collections import deque
    dq = deque()
    if p is None:
        p = self.root()
    dq.append(p)
    while len(dq) > 0:
        popped = dq.popleft()
        yield popped
        dq.extend(self.children(popped))
```

### R-8.27 Give the output of the function parenthesize(T, T.root( )), as described in Code Fragment 8.25, when T is the tree of Figure 8.8.
```python
def parenthesize(T):
    text_list = _parenthesize_text(T)
    return ''.join(text_list)

def _parenthesize_text(T, p=None, text_list=None):
    if p is None:
        p = T.root()
        text_list = []
    text_list.append(p.element())
    if T.num_children(p) > 0:
        text_list.append(' ( ')
        for c in T.children(p):
            text_list = _parenthesize_text(T, c, text_list)
            text_list.append(', ')
        text_list.pop()
        text_list.append(' ) ')
    return text_list

if __name__ == '__main__':
    from Part08_Trees.part08_05_expression_tree import build_expression_trees
    exp = '((((3+1)*3)/((9-5)+2))-((3*(7-4))+6))'
    a = build_expression_trees(exp)
    p = parenthesize(a)
    print(p)
```

### R-8.28 What is the running time of parenthesize(T, T.root( )), as given in Code Fragment 8.25, for a tree T with n nodes?
* Sol.) O(n)
  * why?) It traverses through all the nodes and operate O(1) operations.

### R-8.29 Describe, in pseudo-code, an algorithm for computing the number of descendants of each node of a binary tree. The algorithm should be based on the Euler tour traversal.
```python
from DataStructures.tree import EulerTour
class NumDescendants(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        num_descendants = 0
        if not self.tree().is_leaf(p):
            for i in results:
                num_descendants += (i+1)
        print("{}'s num_descendants : {}".format(p.element(), num_descendants))
        return num_descendants

if __name__ == '__main__':
    from DataStructures.tree import MutableLinkedBinaryTree
    a = MutableLinkedBinaryTree()
    a.fill_tree(4)
    print(a)
    b = NumDescendants(a)
    b.execute()
```

### R-8.30 The build expression tree method of the ExpressionTree class requires input that is an iterable of string tokens. We used a convenient example, (((3+1)x4)/((9-5)+2)) , in which each character is its own token, so that the string itself sufficed as input to build expression tree. In general, a string, such as (35 + 14) , must be explicitly tokenized into list \[ '(' , '35' , '+' , '14' , ')' ] so as to ignore whitespace and to recognize multi-digit numbers as a single token. Write a utility method, tokenize(raw), that returns such a list of tokens for a raw string.
```python
def build_expression_trees(tokens):
    S = []
    tokenized = tokenize(tokens)
    for t in tokenized:
        if t in '+-*/':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()

def tokenize(raw):
    result_set = []
    temp_numeric = []
    for c in raw:
        if c.isnumeric():
            temp_numeric.append(c)
        else:
            if len(temp_numeric) > 0:
                result_set.append(''.join(temp_numeric))
                temp_numeric = []
            if c == ' ':
                pass
            else:
                result_set.append(c)
    return result_set

if __name__ == '__main__':
    from DataStructures.tree_application import tokenize
    a = '(35 + 14)'
    print(tokenize(a))
    
    from DataStructures.tree_application import build_expression_trees
    exp = '((((32+11)*39)/((9-5)+2))-((3*(7-4))+6))'
    a = build_expression_trees(exp)
    print(a)
```

### C-8.31 Define the internal path length, I(T), of a tree T to be the sum of the depths of all the internal positions in T. Likewise, define the external path length, E(T), of a tree T to be the sum of the depths of all the external positions in T. Show that if T is a proper binary tree with n positions, then E(T) = I(T) + n−1.
* pf.)
  1. h = 1
     * I(T) = 0
     * E(T) = 0
     * equation : 0 = 0 + 1 - 1
  2. h = 2
     * I(T) = 0
       * why?) root only.
     * E(T) = 2 * 1 = 2
     * equation : 2 = 0 + 3 - 1
  3. Generalization : Children addition at the leaf node with the depth d.
     * Since it is proper binary tree, two children should be added.
     * Thus, when children are added,
       1. One external node with the depth d will change into internal node
          * I(T) += d
          * E(T) -= d
       2. Two external nodes with the depth (d+1) are added
          * E(T) += 2 * (d+1)
     * Total change of I(T) and E(T) goes as follows.
       * I(T') = I(T) + d
       * E(T') = E(T) -d + 2*(d+1) = E(T) + d + 2
       * Also consider that the number of nodes increased into n+2
       * Therefore, E(T') = E(T) + d + 2 = (I(T) + n - 1) + d + 2 = I(T) + d + (n+2) - 1 = I(T') + (n+2) - 1

### C-8.32 Let T be a (not necessarily proper) binary tree with n nodes, and let D be the sum of the depths of all the external nodes of T. Show that if T has the minimum number of external nodes possible, then D is O(n) and if T has the maximum number of external nodes possible, then D is O(nlogn).
* Sol.)
  1. Minimum external node case : Every node has identically left child or right child.
    * Then there will be only one external node with the depth of (n-1)
    * Thus D = O(n)
  2. Maximum external node case : At most one internal node has one child.
     * The number of external nodes for such tree with n nodes is (n+1)//2
     * The maximum depth of external nodes of the tree is log(n)
     * Therefore, D = O(n log(n))

<p align="start">
<img src="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/images/08_06_32_max_external.png" style="height: 450px;"></img><br/>
</p>

### C-8.33 Let T be a (possibly improper) binary tree with n nodes, and let D be the sum of the depths of all the external nodes of T. Describe a configuration for T such that D is Ω(n2). Such a tree would be the worst case for the asymptotic running time of method height1 (Code Fragment 8.4).
```python
a = MutableLinkedBinaryTree()
p = a.add_root(0)
for i in range(10):
    a.add_right(p, 2*i+1)
    p = a.add_left(p, 2*i+2)
print(a)
```
* Sol.) Consider the case above.
  * Then D(n) goes as follows.
    * n is even : Σ(i/2) = (n^2+n)/4
    * n is odd : Σ(i/2) + (n//2) = (n^2+n)/4 + (n//2)
  * Thus, O(n^2)

### C-8.34 For a tree T, let n_I denote the number of its internal nodes, and let n_E denote the number of its external nodes. Show that if every internal node in T has exactly 3 children, then n_E = 2n_I +1.
* Sol.)
  * h = 1
    * n_I = 0
    * n_E = 1
  * h = 2
    * n_I = 1
    * n_E = 3
  * Generalization : When one internal node gets three children.
    1. One external node becomes internal node.
       * n_I' = n_I + 1
    2. Three external nodes are added.
       * n_E' = n_E - 1 + 3 = n_E + 2
    * Thus, n_E' = n_E + 2 = (2*n_I + 1) + 2 = 2 * n_I' + 1
  
### C-8.35 Two ordered trees T' and T'' are said to be isomorphic if one of the following holds:
* Both T' and T'' are empty.
* The roots of T' and T' have the same number k ≥ 0 of subtrees, and the i-th such subtree of T' is isomorphic to the i-th such subtree of T'' for i = 1,...,k.
### Design an algorithm that tests whether two given ordered trees are isomorphic. What is the running time of your algorithm?
```python
def isomorphic_test(T1, T2):
    T1_subtrees = generalize_subtrees(T1)
    T2_subtrees = generalize_subtrees(T2)
    if len(T1_subtrees) != len(T2_subtrees):
        return False
    for i in range(len(T1_subtrees)):
        if T1_subtrees[i] != T2_subtrees[i]:
            return False
    return True

def generalize_subtrees(T, p=None, result_list=None):
    if p is None:
        p = T.root()
        result_list = []
    for c in T.children(p):
        generalize_subtrees(T, c, result_list)
    result_list.append(parenthesis_generalize(T, p))
    return result_list

def parenthesis_generalize(T, p, text_list=None):
    if text_list is None:
        text_list = []
    text_list.append('_')
    if T.num_children(p) > 0:
        text_list.append('(')
        if T.left(p) is not None:
            parenthesis_generalize(T, T.left(p), text_list)
        text_list.append(',')
        if T.right(p) is not None:
            parenthesis_generalize(T, T.right(p), text_list)
        text_list.append(')')
    return ''.join(text_list)

if __name__ == '__main__':
    from DataStructures.tree import MutableLinkedBinaryTree
    a = MutableLinkedBinaryTree()
    a.fill_tree(3)
    b = MutableLinkedBinaryTree()
    b.fill_tree(3)
    b.root()._node._element = 'a'

    # Test 1
    print(a)
    print(b)
    print(isomorphic_test(a, b))

    # Test 2
    b.delete(b.right(b.right(b.root())))
    print(a)
    print(b)
    print(isomorphic_test(a, b))
```

### C-8.36 Show that there are more than 2^n improper binary trees with n internal nodes such that no pair are isomorphic (see Exercise C-8.35).
* Sol.)
  * Maximum internal node case : When every n nodes have only left (or right) child.
    * The internal node with the maximum depth has 3 choices : l_child only, r_child only, or l-r-child.
    * Other internal nodes have 2 choices, l_child only or l-r_child
    * Thus, 3 * 2^(n-1) non-isomorphic trees exists.
    * Hence, 3 * 2^(n-1) > 2 * 2^(n-1) = 2^n
  * Moreover, other forms of n-internal nodes are possible.

### C-8.37 If we exclude isomorphic trees (see Exercise C-8.35), exactly how many proper binary trees exist with exactly 4 leaves?
* Sol.) 5 trees.

### C-8.38 Add support in LinkedBinaryTree for a method, delete subtree(p), that removes the entire subtree rooted at position p, making sure to maintain the count on the size of the tree. What is the running time of your implementation?
* Sol.) O(s_p) times where s_p is the size of the subtree.
```python
def _delete_subtree(self, p):
    for descendant in self._subtree_postorder(p):
        self._delete(descendant)
```






<p>
    <a href="https://github.com/JoonHyeok-hozy-Kim/datastructure_and_algorithm_in_python/blob/main/Part08_Trees/part08_00_trees.md">Part 8. Trees</a>
</p>