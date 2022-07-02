



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

    from DataStructures.binary_search_trees import AVLTreeMap
    a = AVLTreeMap()
    seq = [44, 17, 62, 32, 50, 78, 48, 54]
    for i in seq:
        a[i] = i
    print(a)
    print('------------------------------------------------')
    del a[32]
    print(a)
