from DataStructures.tree import LinkedTree, GeneralEulerTour, GeneralTreeLayout
from DataStructures.sorted_maps import SortedTableMap
from DataStructures.multiway_search_tree import HozyMultiwaySearchTree

if __name__ == '__main__':
    a = HozyMultiwaySearchTree()
    root = a.add_root()
    for i in range(3):
        a.add_item(root, i, i)
    print(root)
