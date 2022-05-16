# R-5.8
from math import pow
from datetime import datetime, timedelta
from copy import deepcopy
class OperationTester:
    def __init__(self, sample_size_digit=4, operation='pop'):
        self._operation = operation
        self._sample_list = []
        self._test_result = []
        for i in range(sample_size_digit):
            temp = [None] * int(pow(10, 2+i))
            self._sample_list.append(temp)

    def do_test(self):
        self._test_result.append(self._operate_at_start())
        self._test_result.append(self._operate_at_mid())
        self._test_result.append(self._operate_at_end())
        self.print_test_result(self._test_result)

    def print_test_result(self, test_result):
        for i in test_result:
            print(i)

    def _operate_at_start(self):
        sample_copy = deepcopy(self._sample_list)
        test_results = []
        for i in sample_copy:
            test_results.append([len(i),
                                 self._operation_time_count(i, 0)])
        return ['k=0', test_results]

    def _operate_at_mid(self):
        sample_copy = deepcopy(self._sample_list)
        test_results = []
        for i in sample_copy:
            test_results.append([len(i),
                                 self._operation_time_count(i, len(i)//2)])
        return ['k=n//2', test_results]

    def _operate_at_end(self):
        sample_copy = deepcopy(self._sample_list)
        test_results = []
        for i in sample_copy:
            test_results.append([len(i),
                                 self._operation_time_count(i, len(i)-1)])
        return ['k=n', test_results]

    def _operation_time_count(self, target, index):
        start_time = datetime.now()
        self._operate(target, index)
        end_time = datetime.now()
        time_spent = end_time-start_time
        result = time_spent.microseconds
        return result

    def _operate(self, target, index):
        if self._operation == 'pop':
            target.pop(index)
        elif self._operation == 'insert':
            target.insert(index, None)
        return

def sum_n_by_n(A):
    result = 0
    for i in A:
        for j in i:
            result += j
    return result

def sum_n_by_n_syntax(A):
    return sum([sum(i) for i in A])

def initial_length_tester(max_initial_size, append_times):
    import sys
    for i in range(max_initial_size):
        data = [None] * i
        print('=====[max : {} / append : {}]====='.format(i,
                                                          append_times))
        for k in range(append_times):
            a = len(data)
            b = sys.getsizeof(data)
            print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
            data.append(None)

def custom_shuffle(A):
    from random import randrange
    n = len(A)
    result = []
    while n > 0:
        result.append(A.pop(randrange(n)))
        n -= 1
    return result

def string_tester(n):
    from time import time
    test_result_time = []
    test_result_time.append(time())
    # 1. repeated concatenation
    s = ''
    for i in range(n):
        s += 'a'
    test_result_time.append(time())
    # 2. appending to a temporary list and then joining
    l = []
    for i in range(n):
        l.append('a')
    j = ''.join(l)
    test_result_time.append(time())
    # 3. using list comprehension with join
    k = ''.join(['a' for i in range(n)])
    test_result_time.append(time())
    # 4. using generator comprehension with join
    k = ''.join('a' for i in range(n))
    test_result_time.append(time())
    for i in range(len(test_result_time)-1):
        print('{}. {}'.format(i+1, test_result_time[i+1]-test_result_time[i]))

def extend_tester(n):
    from time import time
    time_list = []
    original_list1 = [None] * 5
    original_list2 = [None] * 5
    temp_list = [None] * n
    time_list.append(time())
    original_list1.extend(temp_list)
    time_list.append(time())
    for i in range(n):
        original_list2.append(None)
    time_list.append(time())
    for i in range(len(time_list)-1):
        print('{}. {}'.format(i+1, time_list[i+1]-time_list[i]))

def comprehension_tester(n):
    from time import time
    time_list = []
    time_list.append(time())
    l = [k*k for k in range(n)]
    time_list.append(time())
    m = []
    for k in range(n):
        m.append(k*k)
    time_list.append(time())
    for i in range(len(time_list)-1):
        print('{}. {}'.format(i+1, time_list[i+1]-time_list[i]))

def remove_tester(sample_size_digit=5):
    from time import time
    from copy import deepcopy
    report_list = [['sample size', 'start', 'mid', 'end']]
    for i in range(2, sample_size_digit):
        sample_size = int(pow(10, i))
        temp_entity = [sample_size]
        temp_list = [i for i in range(sample_size)]
        copy_list_1 = deepcopy(temp_list)
        copy_list_2 = deepcopy(temp_list)
        copy_list_3 = deepcopy(temp_list)

        # start
        t0 = time()
        copy_list_1.remove(0)
        t1 = time()
        temp_entity.append(t1-t0)

        # mid
        t0 = time()
        copy_list_2.remove(sample_size//2)
        t1 = time()
        temp_entity.append(t1-t0)

        # end
        t0 = time()
        copy_list_3.remove(sample_size-1)
        t1 = time()
        temp_entity.append(t1-t0)

        report_list.append(temp_entity)

    for i in report_list:
        print(i)

def remove_all(A, value):
    result = []
    for i in range(len(A)):
        if A[i] != value:
            result.append(A[i])
    return result

def repeat_finder(A):
    sorted(A)
    result = []
    idx = 0
    while idx < len(A)-1:
        if A[idx] == A[idx+1]:
            if len(result) == 0:
                result.append(A[idx])
            elif result[-1] != A[idx]:
                result.append(A[idx])
        idx += 1
    return result

def natural_join(A, B):
    result = []
    for i in A:
        for j in B:
            if i[1] == j[0]:
                result.append([i[0], i[1], j[1]])
    return result

class data_packet_receiver:

    def __init__(self, data_received_sequence):
        self._n = len(data_received_sequence)
        self._data_received_sequence = data_received_sequence
        self._result = [None] * self._n

    def receive(self):
        for i in self._data_received_sequence:
            self._result[i] = i
            print(self._result)
        return self._result

def data_packet_receiver(A):
    result = [None] * len(A)
    for i in A:
        result[i] = i
        print(result)
    return result

def n_by_n_sum(A, sum=0):
    if len(A) == 0:
        return [A, sum]
    else:
        temp = A[0].pop(0)
        if len(A[0]) == 0:
            A.pop(0)
        print(temp, A, sum)
        return n_by_n_sum(A, sum+temp)

def three_d_addition(A, B):
    if len(A) == len(B):
        if len(A[0]) == len(B[0]):
            if len(A[0][0]) == len(B[0][0]):
                for i in range(len(A)):
                    for j in range(len(A[0])):
                        for k in range(len(A[0][0])):
                            A[i][j][k] += B[i][j][k]
                return A
    raise TypeError

class Matrix:

    def __init__(self, row_num, col_num):
        self._A = [([None] * col_num) for i in range(row_num)]
        self._row_num = row_num
        self._col_num = col_num

    def __str__(self):
        text_list = []
        for i in range(self._row_num):
            text_list.append('|')
            for j in range(self._col_num):
                # print(self._A[i][j])
                if self._A[i][j] is None:
                    text_list.append(' ')
                elif type(self._A[i][j]) is not str:
                    text_list.append(str(self._A[i][j]))
                else:
                    text_list.append(self._A[i][j])
                text_list.append(', ')
            text_list.pop()
            text_list.append('|')
            text_list.append('\n')
        return ''.join(text_list)

    def homogeneous_setting(self, parameter):
        for i in range(self._row_num):
            for j in range(self._col_num):
                self._A[i][j] = parameter

    def add(self, other):
        if not self._row_num == other._row_num and self._col_num == other._row_num:
            raise TypeError
        for i in range(self._row_num):
            for j in range(self._col_num):
                self._A[i][j] += other._A[i][j]
        return self

    def multiply(self, other):
        if self._col_num != other._row_num:
            raise TypeError

        result = Matrix(self._row_num, other._col_num)
        for i in range(self._row_num):
            for k in range(other._col_num):
                temp_sum = 0
                for j in range(self._col_num):
                    temp_sum += self._A[i][j] * other._A[j][k]
                result._A[i][k] = temp_sum
        return result


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
    # a = array.DynamicArray()
    # for i in range(8):
    #     a.append(i)
    # # print(a)
    # # for i in range(10):
    # #     print(a[(i+1)*(-1)])
    # # for i in range(10):
    # #     print(a[i])
    #
    # # R-5.4
    # print(a)
    # a.insert(3,999)
    # print(a)
    # a.insert(3,1000)
    # print(a)

    # R-5.7
    from copy import deepcopy
    # def repeat_finder(L):
    #     S = deepcopy(L)
    #     S.sort()
    #     for i in range(len(S) - 1):
    #         if S[i] == S[i + 1]:
    #             return S[i]
    #     return False
    #
    # from random import randint
    # n = 10
    # l = [randint(0, n * 2) for i in range(n)]
    # print(l)
    # print(repeat_finder(l))
    # print(l)

    # R-5.8.
    # test = OperationTester(6, 'pop')
    # # test = OperationTester(4, 'insert')
    # test.do_test()

    # R-5.11.
    # from random import randint
    # a = [[randint(0, 10) for j in range(5)] for i in range(5)]
    # print(sum_n_by_n(a))
    # print(sum_n_by_n_syntax(a))

    # R-5.12.
    # initial_length_tester(10,10)

    # C-5.14.
    # a = [i for i in range(4)]
    # print(a)
    # print(custom_shuffle(a))

    # C-5.16.
    # from DataStructures import array
    # a = array.DynamicArray()
    # for i in range(10):
    #     a.append(i)
    # print(a)
    # while len(a) > 0:
    #     a.pop()

    # C-5.21
    # string_tester(1000000)

    # # C-5.21
    # extend_tester(10000000)
    #
    # # C-5.22
    # comprehension_tester(10000000)

    # C-5.23
    # remove_tester(7)

    # C-5.25
    a = [1,1,1,1,1,2,3,3,4,5,5,5,5,6,7,8,9]
    # print(remove_all(a,5))

    # C-5.26
    # print(repeat_finder(a))

    # C-5.29
    from random import randint
    # sample_size = 10
    # a = [chr(randint(65, 65+25)) for i in range(sample_size * 4)]
    # set_x = [['X', 'Y']]
    # set_y = [['Y', 'Z']]
    # for i in range(sample_size):
    #     set_x.append([a[i*4-4], a[i*4-3]])
    #     set_y.append([a[i*4-2], a[i*4-1]])
    # print(set_x)
    # print(set_y)
    # print(natural_join(set_x, set_y))

    # C-5.30.
    # a = [i for i in range(10)]
    # a_s = custom_shuffle(a)
    # print(a_s)
    # data_packet_receiver(a_s)

    # C-5.31.
    # target = []
    # for i in range(3):
    #     target.append([1 for j in range(4)])
    # print(target)
    # print(n_by_n_sum(target))

    # P-5.32
    # a = [
    #     [
    #         [1, 2],
    #         [1, 2],
    #         [1, 2],
    #     ],
    #     [
    #         [1, 2],
    #         [1, 2],
    #         [1, 2],
    #     ],
    #     [
    #         [1, 2],
    #         [1, 2],
    #         [1, 2],
    #     ],
    #     [
    #         [1, 2],
    #         [1, 2],
    #         [1, 2],
    #     ],
    # ]
    #
    # b = [
    #     [
    #         [3, 4],
    #         [3, 4],
    #         [3, 4],
    #     ],
    #     [
    #         [3, 4],
    #         [3, 4],
    #         [3, 4],
    #     ],
    #     [
    #         [3, 4],
    #         [3, 4],
    #         [3, 4],
    #     ],
    #     [
    #         [3, 4],
    #         [3, 4],
    #         [3, 4],
    #     ],
    # ]
    #
    # print(three_d_addition(a, b))

    # P-5.33.
    m = Matrix(3, 4)
    m.homogeneous_setting(1)
    print(m)

    n = Matrix(3, 4)
    n.homogeneous_setting(2)
    print(n)
    print(m.add(n))

    l = Matrix(4, 3)
    l.homogeneous_setting(4)
    l._A[2][2] = 5
    print(l)
    print(m.multiply(l))