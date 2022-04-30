A,B,C = map(int,(input().split()))
result = A*B*C
for i in range(10):
    if str(i) in str(result):
        c=str(result).count(str(i))
        print(c)
    else:
        print(0)
