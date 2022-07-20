from DataStructures.priority_queues import HeapPriorityQueue
from DataStructures.tree import MutableLinkedBinaryTree

def huffman(X):
    D = {}
    Q = HeapPriorityQueue()
    for c in X:
        cnt = D.get(c, 0)
        D[c] = cnt+1

    for d in D:
        T = MutableLinkedBinaryTree()
        T.add_root(d)
        Q.add(D[d], T)

    while len(Q) > 1:
        f1, T1 = Q.remove_min()
        f2, T2 = Q.remove_min()
        T = MutableLinkedBinaryTree()
        root = T.add_root(f1+f2)
        T._attach(root, T1, T2)
        Q.add(f1+f2, T)

    f, T = Q.remove_min()
    return T