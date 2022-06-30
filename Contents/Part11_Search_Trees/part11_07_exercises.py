



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

    """
    a. Insert keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.  
    b. Search for keys 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, in this order.  
    c. Delete keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.  
    """

    from DataStructures.binary_search_trees import SplayTreeMap
    a = SplayTreeMap()
    insert_seq = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,]
    search_seq = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,]
    delete_seq = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,]

    for i in insert_seq:
        print('Insert {}'.format(i))
        a[i] = i
        print(a)

    for i in search_seq:
        print('Search {}'.format(i))
        try:
            print(a[i])
        except:
            pass
        print(a)

    for i in delete_seq:
        print('Delete {}'.format(i))
        del a[i]
        print(a)