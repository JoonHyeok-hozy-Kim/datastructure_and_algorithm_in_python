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

if __name__ == '__main__':
    import random
    sample_size = 10
    S = [i for i in range(sample_size)]
    random_S = [random.randint(1,100) for i in range(sample_size)]

    # print('{} : {}'.format(max_sequence(random_S), random_S))
