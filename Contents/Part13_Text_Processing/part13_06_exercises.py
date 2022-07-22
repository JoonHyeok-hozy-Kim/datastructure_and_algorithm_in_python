def prefix_suffix_compare(X):
    prefix = []
    walk = len(X)-1
    while walk > 0:
        temp_text = []
        for i in range(len(X)-walk):
            if X[i] != X[walk+i]:
                break
            else:
                temp_text.append(X[i])
            if i == len(X)-walk-1:
                prefix.append(''.join(temp_text))
        walk -= 1
    return prefix


if __name__ == '__main__':
    x = "aaabbaaa"
    print(prefix_suffix_compare(x))

    y = "cgtacgttcgtacg"
    print(prefix_suffix_compare(y))
