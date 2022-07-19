import TextProcessingAlgorithms.knuth_morris_pratt as kmp


if __name__ == '__main__':
    P = "abcabcabcaaaaabcdecbabc"
    fail = kmp._compute_kmp_fail(P)
    for i in list(P):
        print('{} '.format(i), end='')
    print()
    for i in fail:
        print('{} '.format(i), end='')