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
    from random import randint
    a = [[randint(0, 10) for j in range(5)] for i in range(5)]
    print(sum_n_by_n(a))
    print(sum_n_by_n_syntax(a))
