n=int(input())
m=0
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]%2==0:
        m+=1
if m==n:
    print("True")
else:
    print("False")