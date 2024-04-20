n,m = (input().split())
arr = list((input().split()))
set_A = set(input().split())
set_B= set(input().split())
happiness = 0
for x in arr:
    if x in set_A:
        happiness+=1
    elif x in set_B:
        happiness -=1
print(happiness)