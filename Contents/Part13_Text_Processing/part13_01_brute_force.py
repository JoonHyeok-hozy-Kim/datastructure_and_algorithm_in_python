

if __name__ == '__main__':

    from TextProcessingAlgorithms.brute_force import find_brute

    S = "I am Groot!"
    W1 = "Groot"
    W2 = "Rocket"
    print(find_brute(S, W1))
    print(find_brute(S, W2))