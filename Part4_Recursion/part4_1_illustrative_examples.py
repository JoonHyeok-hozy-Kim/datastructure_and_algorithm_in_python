def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n


class EnglishRuler:
    def __init__(self, num_inches, major_length):
        self._num_inches = num_inches
        self._major_length = major_length

    def draw_line(self, tick_length, tick_label=''):
        result_list = ['-' for i in range(tick_length)]
        if tick_label:
            result_list.append(' ')
            result_list.append(tick_label)
        result = ''.join(result_list)
        print(result)
        return result

    def draw_interval(self, center_length):
        if center_length > 0:
            self.draw_interval(center_length-1)
            self.draw_line(center_length)
            self.draw_interval(center_length-1)

    def draw_ruler(self):
        for i in range(self._num_inches+1):
            self.draw_line(self._major_length, str(i))
            if i < self._num_inches:
                self.draw_interval(self._major_length-1)


def binary_search(S, e, init=0, end=None):
    n = len(S)
    if end is None:
        end = n-1
    mid = (init+end)//2
    print('mid: {}, init: {}, end: {}'.format(mid, init, end))
    if S[mid] == e:
        return mid
    elif S[mid] > e:
        return binary_search(S, e, init, mid)
    else:
        return binary_search(S, e, mid, end)

import os
def disk_usage(path):
    total = os.path.getsize(path)
    for file in os.listdir(path):
        child_path = os.path.join(path, file)
        total += disk_usage(child_path)
    return total

if __name__ == '__main__':
    S = [i for i in range(100)]
    print(S)
    print(binary_search(S, 48))