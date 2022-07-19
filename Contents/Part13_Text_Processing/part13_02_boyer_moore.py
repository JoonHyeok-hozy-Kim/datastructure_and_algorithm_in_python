



if __name__ == '__main__':

    # s1 = {}
    # char_set = [chr(i+65) for i in range(26)]
    # print(char_set)
    # cnt = 0
    # for char in char_set:
    #     s1[char] = cnt
    #     cnt += 1
    # print(s1)
    # print(s1['X'])

    from TextProcessingAlgorithms.boyer_moore import find_boyer_moore
    S = "I am Groot!"
    W1 = "Groot"
    W2 = "Rocket"
    print(find_boyer_moore(S, W1))
    print(find_boyer_moore(S, W2))