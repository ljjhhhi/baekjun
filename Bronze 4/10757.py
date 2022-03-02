day=input()
lst=list((input().split()))

cnt=0
for car in lst:
    if day in car:
        cnt+=1
print(cnt)
