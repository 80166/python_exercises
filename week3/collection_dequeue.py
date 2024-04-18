from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    cmd = input().split()
    match cmd[0]:
        case 'append':
            d.append(int(cmd[1]))
        case 'appendleft':
            d.appendleft(int(cmd[1]))
        case 'pop':
            d.pop()
        case 'popleft':
            d.popleft()
print(*d)