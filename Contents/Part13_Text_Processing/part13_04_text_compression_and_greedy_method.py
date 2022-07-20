

if __name__ == '__main__':

    from TextProcessingAlgorithms.huffman import huffman
    X = "a fast runner need never be afraid of the dark"
    T = huffman(X)
    print(T)