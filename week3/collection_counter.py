from collections import Counter

if __name__ == "__main__":
    num_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    num_customers = int(input())
    earnings = 0
    available_sizes = Counter(shoe_sizes)

    for _ in range(num_customers):
        size, price = map(int, input().split())
        if available_sizes[size] > 0:
            earnings += price
            available_sizes[size] -= 1

    print(earnings)
