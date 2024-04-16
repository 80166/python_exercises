from itertools import product

if __name__ == "__main__":
    A = [int(num) for num in input().split()]
    B = [int(num) for num in input().split()]

    for i in product(A, B):
        print(i, end=" ")
