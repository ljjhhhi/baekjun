#11399

n=int(input())
l=[]
for x in range(n):
    l.append(input())
l.sort()
l1=list(map(int,l))

i=n
s=0
for y in l1:
    s+=y*n
    n=n-1
print(s)
