

if __name__ == '__main__':

    from TextProcessingAlgorithms.brute_force import find_brute

    S = "I am Groot!"
    W1 = "Groot"
    W2 = "Rocket"
    print(find_brute(S, W1))
    print(find_brute(S, W2))

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


    import TextProcessingAlgorithms.knuth_morris_pratt as kmp
    P = "abcabcabcaaaaabcdecbabc"
    fail = kmp._compute_kmp_fail(P)
    for i in list(P):
        print('{} '.format(i), end='')
    print()
    for i in fail:
        print('{} '.format(i), end='')