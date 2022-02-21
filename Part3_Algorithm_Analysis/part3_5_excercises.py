def c_3_35(A):
    n = len(A)
    sorted_A = sorted(A)
    print(sorted_A)
    for i in range(n-2):
        if sorted_A[i] == sorted_A[i+1]:
            if sorted_A[i+1] == sorted_A[i+2]:
                return False
    return True


def c_3_36(A):
    n = len(A)
    if n <= 10:
        return A
    else:
        sorted_A = sorted(A)
        return sorted_A[-11:-1]


def c_3_41(A):
    n = len(A)
    min, max = A[0], A[0]
    comparison_count = 0
    max_candidates = []
    min_candidates = []
    for i in range(n//2):
        comparison_count += 1
        if A[i*2] >= A[i*2-1]:
            comparison_count += 1
            if A[i*2] > max:
                max = A[i*2]
            comparison_count += 1
            if A[i*2-1] < min:
                min = A[i*2-1]
        else:
            comparison_count += 1
            if A[i*2-1] > max:
                max = A[i*2-1]
            comparison_count += 1
            if A[i*2] < min:
                min = A[i*2]

    return [min, max, comparison_count]


class node:
    _parent = None
    _child_list = []
    _value = None

    def __init__(self, value, parent=None):
        self._value = value
        self._parent = parent

    def __str__(self):
        return self._value

    def add_child(self, child):
        self._child_list.append(child)

    def parent(self):
        return self._parent if self._parent else None


def c_3_42(n):
    comb_list = []
    for i in range(n):
        new_comb_list = []
        for j in range(i+2):
            if len(comb_list) == 0:
                new_comb_list.append(j)
            else:
                for element in comb_list:
                    new_comb_list.append(element+j)
        comb_list = sorted(new_comb_list)
    print(comb_list)
    C = comb_list[-1]
    for i in range(1, len(comb_list)-1):
        print('{}, {}, {}'.format(comb_list[i-1], comb_list[i], comb_list[i+1]))
        if comb_list[i-1] != comb_list[i]:
            if comb_list[i] != comb_list[i+1]:
                C = comb_list[i]
                print('C changed : '.format(C))
    return C

if __name__ == '__main__':
    # from random import randint, uniform
    # sample_size = 1000
    # test_case = 1000
    # test_result = []
    # for i in range(test_case):
    #     A = [round(randint(0, 10000000)) for i in range(sample_size)]
    #     print(c_3_41(A))

    print(c_3_42(10))