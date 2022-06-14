from time import time

def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end-start)/n * 10000000


if __name__ == '__main__':
    print(compute_average(100))
    print(compute_average(1000))
    print(compute_average(10000))
    print(compute_average(100000))
    print(compute_average(1000000))