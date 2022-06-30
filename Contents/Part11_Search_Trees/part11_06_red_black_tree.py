from DataStructures.binary_search_trees import RedBlackTreeMap
from random import randint


a = RedBlackTreeMap()
insert_seq = [4, 7, 12, 15, 3, 5, 14, 18, 16, 17]

for i in insert_seq:
    # print('Insert : {}'.format(i))
    a[i] = i
    # print(a)

delete_seq = [3, 12, 17, 18, 15, 16]
print(a)
for i in delete_seq:
    print('Delete : {}'.format(i))
    del a[i]
    print(a)