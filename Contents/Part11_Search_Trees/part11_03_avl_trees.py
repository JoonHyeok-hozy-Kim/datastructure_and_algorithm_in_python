from DataStructures.binary_search_trees import AVLTreeMap

a = AVLTreeMap()
for i in range(20):
    a[i] = i
    print(a)
print('----------------------------------------------------')
for i in range(10):
    print('Del {}'.format(a[i]))
    del a[i]
    print(a)