def average(array):
    N = set(array)
    return sum(N)/len(N)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)