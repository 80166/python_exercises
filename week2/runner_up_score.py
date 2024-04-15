if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    n = max(arr)
    while n in arr:
        arr.remove(n)
    print(max(arr))
