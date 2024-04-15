from itertools import permutations

S, size = input().split(" ")
size = int(size)
for p in sorted(permutations(S, size)):
    print("".join(p))
