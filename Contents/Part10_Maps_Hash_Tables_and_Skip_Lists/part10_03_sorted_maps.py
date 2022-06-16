from DataStructures.sorted_maps import SortedTableMap

if __name__ == '__main__':
    s = SortedTableMap()
    for i in range(26):
        s[chr(i+65)] = i+65
    print(s.find_lt('C'))
    print(s.find_le('C'))
    print(s.find_le('c'))