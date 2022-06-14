class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class ScoreBoard:

    def __init__(self, capacity=10):
        self._capacity = capacity
        self._board = [None] * capacity
        self._n = 0

    def getitem(self, k):
        return self._board[k]

    def __str__(self):
        str_list = ['---------------']
        for j in range(self._n):
            str_list.append(str(self._board[j]))
        str_list.append('---------------')
        return '\n'.join(str_list)

    def add(self, entry):
        score = entry.get_score()
        good = self._n < self._capacity or score > self.getitem(self._n-1).get_score()

        if good:
            if self._n < self._capacity:
                self._board[self._n] = entry
                self._n += 1

            j = self._n-1
            while j > 0 and score >= self.getitem(j).get_score():
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry


def hozy_insertion_sort(S):
    l = len(S)
    for i in range(l-1):
        idx = 0
        while idx < l-1:
            if S[idx] > S[idx+1]:
                temp = S[idx+1]
                S[idx+1] = S[idx]
                S[idx] = temp
                # print('S {}'.format(S))
            idx += 1

def insertion_sort(S):
    for i in range(1, len(S)):
        cur = S[i]
        j = i
        while j > 0 and S[j-1] > cur:
            S[j] = S[j-1]
            j -= 1
        S[j] = cur

class CaesarCypher:

    def __init__(self, shift):
        encoder = [None] * 52
        decoder = [None] * 52
        for k in range(26):
            encoder[k] = chr((k+shift) % 26 + ord('A'))
            encoder[k+26] = chr((k+shift) % 26 + ord('a'))
            decoder[k] = chr((k-shift) % 26 + ord('A'))
            decoder[k+26] = chr((k-shift) % 26 + ord('a'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        chr_list = list(original)
        for i in range(len(chr_list)):
            if chr_list[i].isupper():
                chr_list[i] = code[ord(chr_list[i]) - ord('A')]
            elif chr_list[i].islower():
                chr_list[i] = code[26 + ord(chr_list[i]) - ord('a')]
        return ''.join(chr_list)


if __name__ == '__main__':
    # ge_list = []
    # for i in range(50):
    #     ge_list.append(GameEntry(chr(i+65), i))
    # sb = ScoreBoard()
    # for i in ge_list:
    #     sb.add(i)
    #     print(sb)

    from random import randint
    from copy import deepcopy
    from time import time
    # sample_size = 1000
    # S1 = [randint(0, sample_size) for i in range(sample_size*2)]
    # S2 = deepcopy(S1)
    # t0 = time()
    # hozy_insertion_sort(S1)
    # t1 = time()
    # insertion_sort(S2)
    # t2 = time()
    # print('hozy : {} -> {}'.format(round(t1-t0, 2), S1))
    # print('book : {} -> {}'.format(round(t2-t1, 2), S2))

    cc = CaesarCypher(4)
    enc = cc.encrypt('ABCDabcd')
    print(enc)
    dec = cc.decrypt(enc)
    print(dec)