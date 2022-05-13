


if __name__ == '__main__':
    # R-5.1,2
    # import sys
    # n = 100
    # data = []
    # byte_tracker = 0
    # byte_change_list = []
    # for k in range(n):
    #     a = len(data)
    #     b = sys.getsizeof(data)
    #     if b > byte_tracker and k > 0:
    #         byte_tracker = b
    #         byte_change_list.append(a-1)
    #     data.append(None)
    # print(byte_change_list)

    # R-5.3
    # import sys
    # initial_elements_count = 200
    # data = [None] * initial_elements_count
    # for k in range(initial_elements_count):
    #     a = len(data)
    #     b = sys.getsizeof(data)
    #     data.pop()
    #     print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))

    # R-5.4
    from DataStructures import array
    a = array.DynamicArray()
    for i in range(10):
        a.append(i)
    print(a)
    for i in range(10):
        print(a[(i+1)*(-1)])