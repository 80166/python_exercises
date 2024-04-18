n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    x = input().split()
     
    match x[0]:
        case "pop":
            s.pop()
        case "discard":
            s.discard(int(x[1]))
        case "remove":
            s.remove(int(x[1]))

print(sum(s))