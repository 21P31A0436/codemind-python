n=int(input())
sum=0
c=0
arr=list(map(int,input().split()))
for i in range(len(arr)):
    sum=sum+arr[i]
avg=sum//n
for j in range(n):
    if arr[j]>=avg:
        c+=1
print(c)