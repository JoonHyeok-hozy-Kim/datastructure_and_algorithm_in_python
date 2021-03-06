# R-4.1
def max_sequence(S, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(S)-1
    if start == end:
        return S[start]
    elif start == end-1:
        return max(S[start], S[end])
    else:
        mid = (start+end)//2
        return max(max_sequence(S, start, mid),
                   max_sequence(S, mid+1, end))


def harmonic_number(n):
    if n == 1:
        return 1
    else:
        return harmonic_number(n-1) + 1/n


def string_converter(number):
    if number < 1000:
        return str(int(number))
    else:
        return string_converter(number/1000) + ',' + str(int(number%1000))


def min_max(S, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(S)-1

    if start == end:
        return (S[start], S[end])
    elif start == end-1:
        if S[start] > S[end]:
            return (S[start], S[end])
        else:
            return (S[end], S[start])
    else:
        mid = (start+end)//2
        part_one = min_max(S, start, mid)
        part_two = min_max(S, mid+1, end)
        maximum = part_one[0] if part_one[0] > part_two[0] else part_two[0]
        minimum = part_one[1] if part_one[1] < part_two[1] else part_two[1]
        return (maximum, minimum)


def log_base_two_int(n):
    if n == 1:
        return 0
    else:
        return log_base_two_int(n//2) + 1


def element_uniqueness(S, start=None, target=None):
    if start is None and target is None:
        start = 0
        target = start
    if start == len(S):
        return True
    else:
        if target == len(S):
            return element_uniqueness(S, start+1, start+1)
        else:
            if S[start] == S[target] and start != target:
                return False
            return element_uniqueness(S, start, target+1)


def recursive_product(m, n):
    if m == 0 or n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return recursive_product(m, n-1) + m


class TowersOfHanoi:

    def __init__(self, disk_num, peg_num=3):
        self._disk_num = disk_num
        self._peg_num = peg_num
        self._platform_dict = [[i+1 for i in range(disk_num)]]
        for i in range(peg_num-1):
            self._platform_dict.append([])

    def play(self, n=None, from_peg_idx=None, to_peg_idx=None, temp_peg_idx=None):
        if n is None and from_peg_idx is None and to_peg_idx is None and temp_peg_idx is None:
            n = self._disk_num
            from_peg_idx, to_peg_idx, temp_peg_idx = 0, 2, 1
        from_peg = self._platform_dict[from_peg_idx]
        to_peg = self._platform_dict[to_peg_idx]
        temp_peg = self._platform_dict[temp_peg_idx]
        if n == 1:
            disk = from_peg.pop(0)
            to_peg.insert(0, disk)
            print(self)
        else:
            self.play(n-1, from_peg_idx, temp_peg_idx, to_peg_idx)
            disk = from_peg.pop(0)
            to_peg.insert(0, disk)
            print(self)
            self.play(n-1, temp_peg_idx, to_peg_idx, from_peg_idx)

    def __str__(self):
        from copy import deepcopy
        result_text_list = ['-----------', '\n']
        platform_copy = deepcopy(self._platform_dict)
        for j in range(self._disk_num):
            for i in range(self._peg_num):
                if len(platform_copy[(i+1)*(-1)]) == 0:
                    result_text_list.append('|')
                else:
                    result_text_list.append(str(platform_copy[(i+1)*(-1)].pop(-1)))
                result_text_list.append('  ')
            result_text_list.append('\n')
        return ''.join(reversed(result_text_list))

    def test_play_by_luck(self):
        from random import randint
        move_count = 0
        while len(self._platform_dict[-1]) < self._disk_num:
            from_peg = randint(0, self._peg_num-1)
            to_peg = randint(0, self._peg_num-1)
            if from_peg != to_peg:
                move_count += self.move_disk(from_peg, to_peg)
        print('Move count : {}'.format(move_count))
        print(self)

    def move_disk(self, from_peg_idx, to_peg_idx):
        from_peg = self._platform_dict[from_peg_idx]
        to_peg = self._platform_dict[to_peg_idx]
        if len(from_peg) == 0:
            print('Cannot move from an empty disk.')
            return 1
        disk = from_peg.pop(0)
        if len(to_peg) > 0:
            if to_peg[0] < disk:
                print('Cannot move to the smaller disk.')
                from_peg.insert(0, disk)
                return 1
        to_peg.insert(0, disk)
        print(self)
        return 1


def subset(S, start=None, end=None, result_list=None):
    if start is None and end is None:
        start, end = 0, 0
        result_list = []
    if start == len(S):
        return result_list
    else:
        if end < len(S):
            if start < end:
                result_list.append([S[start], S[end]])
            return subset(S, start, end+1, result_list)
        else:
            return subset(S, start+1, start+1, result_list)


def string_reverse(string, start=None, end=None, str_list=None):
    if start is None and end is None:
        start, end = 0, len(string)-1
        str_list = list(string)
    if start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        return string_reverse(string, start+1, end-1, str_list)
    else:
        result = ''.join(str_list)
        return result


def palindrome(s, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(s)-1
    if start < end:
        if s[start] != s[end]:
            return False
        return palindrome(s, start+1, end-1)
    return True


def more_vowels(s, idx=None, vowel=None, consonant=None):
    if idx is None and vowel is None and consonant is None:
        idx, vowel, consonant = 0, 0, 0
    if idx < len(s):
        if s[idx] in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            consonant += 1
        return more_vowels(s, idx+1, vowel, consonant)
    return True if vowel > consonant else False


def even_first(S, idx=None):
    if idx is None:
        idx = 0
    if idx < len(S):
        if S[idx]%2 == 0:
            even_number = S.pop(idx)
            S.insert(0, even_number)
        return even_first(S, idx+1)
    return S


def sort_by_k(S, k, idx=None, new_S=None):
    if idx is None and new_S is None:
        idx = 0
        new_S = [k]
    if idx < len(S):
        if S[idx] <= k:
            new_S.insert(0, S[idx])
        else:
            new_S.append(S[idx])
        return sort_by_k(S, k, idx+1, new_S)
    return new_S


def sum_to_k(S, k, start=None, end=None, result=None):
    if start is None and end is None and result is None:
        start, end, result = 0, 0, []
    if start == len(S):
        return result
    elif end == len(S):
        return sum_to_k(S, k, start+1, start+1, result)
    else:
        if S[start] + S[end] == k:
            result.append((S[start], S[end]))
        return sum_to_k(S, k, start, end+1, result)


def power_by_square_and_recursion(x, n):
    if n == 1:
        return x
    else:
        mid = n // 2
        partial = power_by_square_and_recursion(x, mid)
        result = partial * partial
        if n%2 == 1:
            result *= x
    return result


def power_by_square_and_loop(x, n):
    result = 1
    for i in range(n//2):
        result *= x*x
    if n%2 == 1:
        result *= x
    return result

def summation_puzzle(k, U, S=None):
    from copy import deepcopy
    if S is None:
        S = []
    for i in range(len(U)):
        popped = U.pop(i)
        S.append(deepcopy(popped))
        if k == 1:
            print(''.join(S))
        else:
            summation_puzzle(k-1, U, S)
        popped_again = S.pop(-1)
        U.insert(i, popped_again)


class EnglishRulerLoop:
    def __init__(self, num_inches, major_length):
        self._num_inches = num_inches
        self._major_length = major_length

    def draw_line(self, length, label=''):
        line_text = []
        for i in range(length):
            line_text.append('-')
        if label:
            line_text.append(' ')
            line_text.append(label)
        result_text = ''.join(line_text)
        return result_text

    def draw(self):
        result_text = []
        for i in range(self._major_length):
            if i == 0:
                for j in range(self._num_inches):
                    result_text.append(self.draw_line(self._major_length, str(j+1)))
            else:
                len_result_text = len(result_text)
                for j in range(len_result_text):
                    result_text.insert(j*2, self.draw_line(self._major_length-i))
        result_text.insert(0, self.draw_line(self._major_length, str(0)))
        print('\n'.join(result_text))


if __name__ == '__main__':
    import random
    sample_size = 10
    S = [i for i in range(sample_size)]
    random_S = [random.randint(1,100) for i in range(sample_size)]

    # print('{} : {}'.format(max_sequence(random_S), random_S))

    # for i in range(1, 10):
    #     print(harmonic_number(i))

    # print(string_converter(12345678))

    # print('{} : {}'.format(min_max(random_S),
    #                        random_S))

    # for i in range(65):
    #     print(log_base_two_int(i+1))

    # S.append(6)
    # print(element_uniqueness(S))

    # print(recursive_product(10, 6))

    # t1 = TowersOfHanoi(6)
    # print(t1)
    # t1.play()

    # print(subset(S))
    string = 'abcde'
    # print(string_reverse(string))
    # print(string)

    # print(palindrome(string))
    # print(palindrome('racecar'))

    # print(more_vowels(string))
    # print(more_vowels('aaaab'))

    # print(even_first(S))

    # print(sort_by_k(random_S, 66))

    # print(sum_to_k(S, 7))

    # print(power_by_square_and_recursion(2, 5))
    # print(power_by_square_and_loop(2, 5))

    # U = ['g', 'i', 'r', 'l']
    # summation_puzzle(4, U)

    e1 = EnglishRulerLoop(2, 6)
    e1.draw()
