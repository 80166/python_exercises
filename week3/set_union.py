eng = int(input())
e_roll = set(list(input().split()))
french = int(input())
f_roll = set(list(input().split()))
merge_roll = e_roll.union(f_roll)
count = 0
for i in merge_roll:
    if i in e_roll or i in f_roll:
        count += 1
        
print(count)