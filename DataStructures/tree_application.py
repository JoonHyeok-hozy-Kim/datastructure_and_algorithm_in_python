from DataStructures.tree import MutableLinkedBinaryTree
from DataStructures.queue import LinkedQueue
from copy import deepcopy

def tree_generator(element_list):
    """
    :param element_list: Possible trees with elements in this list will be created.
    :return: List of possible trees is returned.
    """
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

from DataStructures.tree import EulerTour
class TreeBuilderTour(EulerTour):
    """
        Customized EulerTour for tree_generator() function.
        <How to use>
        (1) Set a tree as a parameter when making an instance of this class.
        (2) Set an element as a parameter when calling execute() method.
            -> List of trees that given element in (2) added to various leaf positions in the tree of (1) will be returned.
    """
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

