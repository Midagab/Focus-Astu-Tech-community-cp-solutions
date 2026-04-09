t=int(input())
count=0
for _ in range(t):
    a=sorted(map(int,input().split()))
    if a[0]+a[1]>=1:
        count+=1
print(count)