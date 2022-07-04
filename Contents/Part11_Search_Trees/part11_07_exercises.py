from DataStructures.binary_search_trees import RedBlackTreeMap
def red_black_join(T, U):
    t_walk = T.root()
    while T.right(t_walk) is not None:
        t_walk = T.right(t_walk)
    mid = t_walk.element()
    T.delete(t_walk)
    new_tree = RedBlackTreeMap()
    new_tree[mid._key] = mid._value
    new_tree.root()._node._left = T.root()._node
    new_tree.root()._node._right = U.root()._node
    return new_tree

def red_black_split(T, k):
    T1 = RedBlackTreeMap()
    T2 = RedBlackTreeMap()
    p = T.root()
    if k == p.key():
        T1._sentinel._left = p._node._left
        T2._sentinel._left = p._node._right
    else:
        node_set = _get_greatest_smallest_nodes(T, k)
        target_position = T._make_position(node_set['target_node'])
        if k < p.key():
            if node_set['min_node'] is None:
                parent = T.parent(target_position)
                minor_subtree_root_node = target_position._node._right
                target_position._node._right = T._sentinel
                new_tree = T.split_subtree(target_position)
                parent._node._left = minor_subtree_root_node

            else:
                node_set['greater_min']._left = target_position._node._right
                node_set['min_node']._right = target_position._node._left
                if node_set['min_node']._parent != node_set['greater_min']:
                    node_set['min_node']._parent._left = node_set['greater_min']
                else:
                    node_set['min_node']._parent._left = T._sentinel

                new_tree = RedBlackTreeMap()
                temp = T._make_position(node_set['min_node'])
                new_tree._size = T._modify_sentinel(temp, T._sentinel, new_tree._sentinel)

        else:
            if node_set['max_node'] is None:
                parent = T.parent(target_position)
                minor_subtree_root_node = target_position._node._left
                target_position._node._left = T._sentinel
                new_tree = T.split_subtree(target_position)
                parent._node._right = minor_subtree_root_node

            else:
                node_set['smaller_max']._right = target_position._node._left
                node_set['max_node']._left = target_position._node._right
                if node_set['max_node']._parent._right != node_set['smaller_max']:
                    node_set['max_node']._parent._right = node_set['smaller_max']
                else:
                    node_set['max_node']._parent._left = T._sentinel

                new_tree = RedBlackTreeMap()
                temp = T._make_position(node_set['max_node'])
                new_tree._size = T._modify_sentinel(temp, T._sentinel, new_tree._sentinel)

    return T, new_tree


def _get_greatest_smallest_nodes(T, k):
    max_node = None
    greater_min = None
    min_node = None
    smaller_max = None
    target_node = None
    p = T.root()
    if not k == p.key():
        while not T.is_leaf(p):
            if k < p.key():
                if max_node is None or p.key() > max_node._element._key:
                    max_node = p._node
                if greater_min is None or p.key() < greater_min._element._key:
                    greater_min = p._node
                if T.left(p) is not None:
                    p = T.left(p)
            elif k > p.key():
                if min_node is None or p.key() > min_node._element._key:
                    min_node = p._node
                if smaller_max is None or p.key() < smaller_max._element._key:
                    smaller_max = p._node
                if T.right(p) is not None:
                    p = T.right(p)
            else:
                break
    if k == p.key():
        target_node = p._node
    return {
        'max_node' : max_node,
        'greater_min' : greater_min,
        'min_node' : min_node,
        'smaller_max' : smaller_max,
        'target_node' : target_node,
    }

if __name__ == '__main__':
    pass

    # from DataStructures.binary_search_trees import TreeMap
    # a = TreeMap()
    # for i in range(5):
    #     a[i+1] = chr(i+65)
    # print(a)

    # from DataStructures.binary_search_trees import TreeMap
    # a = TreeMap()
    # a[30] = 30
    # print(a)
    # a[40] = 40
    # print(a)
    # a[24] = 24
    # print(a)
    # a[58] = 58
    # print(a)
    # a[48] = 48
    # print(a)
    # a[26] = 26
    # print(a)
    # a[11] = 11
    # print(a)
    # a[13] = 13
    # print(a)

    # from DataStructures.binary_search_trees import TreeMap
    # from itertools import permutations
    # seq = [1,2,3]
    # for new_seq in permutations(seq):
    #     a = TreeMap()
    #     for i in new_seq:
    #         a[i] = i
    #     print(a)

    # from DataStructures.binary_search_trees import AVLTreeMap
    # b = AVLTreeMap()
    # for i in range(7):
    #     print('-------------Insert {}-------------'.format(i))
    #     b[i] = i
    #     print(b)
    #     print('-----------------------------------')
    #
    # seq2 = [3, 1, 5, 0, 2, 4, 6]
    # b = AVLTreeMap()
    # for i in seq2:
    #     print('-------------Insert {}-------------'.format(i))
    #     b[i] = i
    #     print(b)
    #     print('-----------------------------------')

    # from DataStructures.binary_search_trees import AVLTreeMap
    # a = AVLTreeMap()
    # a[62] = 62
    # a[44] = 44
    # a[78] = 78
    # a[17] = 17
    # a[50] = 50
    # a[88] = 88
    # a[48] = 48
    # a[54] = 54
    # print(a)
    # # a[52] = 52
    # del a[62]
    # print(a)

    # """
    # a. Insert keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.
    # b. Search for keys 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, in this order.
    # c. Delete keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.
    # """
    #
    # from DataStructures.binary_search_trees import SplayTreeMap
    # a = SplayTreeMap()
    # insert_seq = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,]
    # search_seq = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,]
    # delete_seq = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,]
    #
    # for i in insert_seq:
    #     print('Insert {}'.format(i))
    #     a[i] = i
    #     print(a)
    #
    # for i in search_seq:
    #     print('Search {}'.format(i))
    #     try:
    #         print(a[i])
    #     except:
    #         pass
    #     print(a)
    #
    # for i in delete_seq:
    #     print('Delete {}'.format(i))
    #     del a[i]
    #     print(a)

    # from DataStructures.binary_search_trees import RedBlackTreeMap
    # # from random import randint
    # # for i in range(4):
    # #     print('RedBlack #{}'.format(i+1))
    # #     a = RedBlackTreeMap()
    # #     for j in range(9):
    # #         rand = randint(1, 99)
    # #         a[rand] = rand
    # #     print(a)
    #
    # a = RedBlackTreeMap()
    # # seq = (5,16,22,45,2,10,18,30,50,12,1)
    # # for i in seq:
    # #     a[i] = i
    # # print(a)
    #
    # seq = [10, 1, 15, 12, 19, 11, 13, 18, 20]
    # for i in seq:
    #     a[i] = i
    # print(a)

    # from DataStructures.binary_search_trees import SplayTreeMap
    # a = SplayTreeMap()
    # seq = [i for i in range(10)]
    # for i in seq:
    #     a[i*2] = i*2
    #     print(a)
    # for i in seq:
    #     a[i*2+1] = i*2+1
    #     print(a)
    # a[10]
    # print(a)

    # from DataStructures.binary_search_trees import AVLTreeMap
    # from random import randint
    # a = AVLTreeMap()
    # for i in range(10):
    #     num = randint(1, 99)
    #     print('Insert {}'.format(num))
    #     a.setdefault(num, num)
    #     print(a)

    # from DataStructures.binary_search_trees import TreeMap
    # from copy import deepcopy
    # a = TreeMap()
    # for i in range(3):
    #     a[i] = i
    # print(a)
    #
    # b = deepcopy(a)
    # b._rotate(b.right(b.right(b.root())))
    # print(b)
    #
    # c = deepcopy(a)
    # c._rotate(c.right(c.root()))
    # print(c)
    #
    # c._rotate(c.right(c.root()))
    # print(c)
    #
    # c._rotate(c.left(c.left(c.root())))
    # print(c)

    # from DataStructures.binary_search_trees import TreeMap
    # a = TreeMap()
    # for i in range(10):
    #     a[i] = i
    # print(a)
    # a.remove_range(3, 7)
    # print(a)

    # from DataStructures.binary_search_trees import AVLTreeMap
    # a = AVLTreeMap()
    # for i in range(10):
    #     a[i] = i
    # print(a)
    # a.remove_range(3, 7)
    # print(a)

    # from DataStructures.binary_search_trees import AVLTreeMap, AVLBalanceTreeMap
    # # a = AVLTreeMap()
    # a = AVLBalanceTreeMap()
    # seq = [44, 17, 62, 32, 50, 78, 48, 54]
    # for i in seq:
    #     a[i] = i
    #     print(a)
    # print('------------------------------------------------')
    # del a[32]
    # print(a)
    # del a[50]
    # print(a)

    # from DataStructures.binary_search_trees_applications import TreeMapBeforeAfter, AVLBalanceTreeMapInitial, AVLBalanceTreeMap
    # from random import randint
    # # a = TreeMapBeforeAfter()
    # a = AVLBalanceTreeMap()
    # seq = [randint(0, 99) for i in range(10)]
    # # seq = [i for i in range(10)]
    # for i in seq:
    #     print('Insert : {}'.format(i))
    #     a[i] = i
    #     print(a)
    # for j in seq:
    #     print('Delete : {}'.format(j))
    #     del a[j]
    #     print(a)

    # from DataStructures.binary_search_trees import SplayTreeMap, RedBlackTreeMap
    # from random import randint
    # t1 = SplayTreeMap()
    # t2 = RedBlackTreeMap()
    # seq = [randint(0,1000) for i in range(10)]
    # for i in seq:
    #     t1[i] = i
    #     t2[i] = i
    # t1_inorder = ['Splay Tree inorder    : ']
    # t2_inorder = ['RedBlack Tree inorder : ']
    # for t1_walk in t1.inorder():
    #     t1_inorder.append(str(t1_walk.element()))
    #     t1_inorder.append(' -> ')
    # for t2_walk in t2.inorder():
    #     t2_inorder.append(str(t2_walk.element()))
    #     t2_inorder.append(' -> ')
    # print('Splay Tree')
    # print(t1)
    # print(''.join(t1_inorder))
    # print('---------------------------------------------------')
    # print('RedBlack Tree')
    # print(t2)
    # print(''.join(t2_inorder))

    # from DataStructures.binary_search_trees import RedBlackTreeMap
    # T = RedBlackTreeMap()
    # U = RedBlackTreeMap()
    # m = 10
    # n = 12
    # cnt = 0
    # for i in range(m):
    #     cnt += 1
    #     T[cnt] = cnt
    # for i in range(n):
    #     cnt += 1
    #     U[cnt] = cnt
    # print(T)
    # print(U)
    #
    # V = red_black_join(T, U)
    # v_root = V.root()
    # print(v_root.element())
    # print(V.left(v_root).element())
    # print(V.right(v_root).element())

    # from random import randint
    # T = RedBlackTreeMap()
    # n = 10
    # k = randint(0, n-1)
    # for i in range(10):
    #     T[i] = i
    # print(k)
    # print(T)
    # T1, T2 = red_black_split(T, k)
    # print(T1.root().element())
    # print(T2.root().element())

    # T = RedBlackTreeMap()
    # for i in range(30):
    #     T[i] = i
    # print(T)
    # T1, T2 = red_black_split(T, 5)
    # print(T1)
    # print(T2)

    # from DataStructures.binary_search_trees import AVLTreeMap, RedBlackTreeMap
    # a = AVLTreeMap()
    # b = RedBlackTreeMap()
    # for i in range(23):
    #     a[i] = i
    #     b[i] = i
    # print(a)
    # print(b)

    # from DataStructures.binary_search_trees import *
    # from random import randint
    # a = TreeMap()
    # b = AVLTreeMap()
    # c = SplayTreeMap()
    # d = RedBlackTreeMap()
    # for i in range(10):
    #     n = randint(0,100)
    #     a[n] = n
    #     b[n] = n
    #     c[n] = n
    #     d[n] = n
    # print(a)
    # print(b)
    # print(c)
    # print(d)

    # from DataStructures.binary_search_trees_applications import SplayTreeMapTopDown
    # a = SplayTreeMapTopDown()
    # seq = [100, 99, 98, 30, 66, 31, 32, 33]
    # cnt = 0
    # for i in seq:
    #     a[i] = chr(cnt+65)
    #     cnt += 1
    # a[34] = 'X'
    # print(a)
    # print(a[34])
    # print(a)

    # from DataStructures.binary_search_trees_applications import SplayTreeMap, SplayTreeMapTopDown, HalfSplayTreeMap
    # splays = [
    #     ('SplayTreeMap', SplayTreeMap()),
    #     ('SplayTreeMapTopDown', SplayTreeMapTopDown()),
    #     ('HalfSplayTreeMap', HalfSplayTreeMap())
    # ]
    # seq = [100, 99, 98, 30, 66, 31, 32, 33]
    # cnt = 0
    # for i in seq:
    #     for tree in splays:
    #         tree[1][i] = chr(cnt+65)
    #     cnt += 1
    # for tree in splays:
    #     print(tree[0])
    #     print(tree[1])
    # print('===============================================================')
    # for tree in splays:
    #     print(tree[0])
    #     print('100 : {}'.format(tree[1][100]))
    #     print(tree[1])

    # from DataStructures.binary_search_trees_applications import SplayTreeMap
    #
    # seq1 = [
    #     100, 105, 95, 110, 90, 115
    # ]
    # a = SplayTreeMap()
    # for i in seq1:
    #     a[i] = i
    # print(a)
    #
    #
    # seq2 = [
    #     100, 95, 105, 90, 110, 85
    # ]
    # a = SplayTreeMap()
    # for i in seq2:
    #     a[i] = i
    # print(a)

    # from DataStructures.binary_search_trees import TreeMap
    # from random import randint
    # a = TreeMap()
    # seq = [
    #     8, 3, 7, 1, 12, -5, 9, 2, 4, 7.5
    # ]
    # for i in seq:
    #     a[i] = i
    # print(a)
    # last = a._subtree_last_position(a.left(a.root()))
    # last._node._element = 'BUG'
    # del a[8]
    # print(a)


    from DataStructures.binary_search_trees import AVLTreeMap, SplayTreeMap, RedBlackTreeMap
    from random import randint
    from time import time
    trees = [
        ['AVLTreeMap', AVLTreeMap(), None, None],
        ['SplayTreeMap', SplayTreeMap(), None, None],
        ['RedBlackTreeMap', RedBlackTreeMap(), None, None],
    ]
    sample_size = 100000
    seq = [randint(0, sample_size*100) for i in range(sample_size)]
    search_times = sample_size//2
    search_target = [randint(0, sample_size-1) for i in range(search_times)]
    for tree in trees:
        start = time()
        for num in seq:
            tree[1][num] = num
        end = time()
        tree[2] = end - start

        start = time()
        for idx in search_target:
            tree[1][seq[idx]]
        end = time()
        tree[3] = end - start
        print('{:15s} : [Insert] {:2.2f} [Search] {:2.2f}'.format(tree[0], tree[2], tree[3]))
        # print(tree[1])