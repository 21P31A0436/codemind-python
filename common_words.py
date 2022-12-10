n=input().lower().split()
m=input().lower().split()
s=[]
for i in m:
    if i in n:
        s.append(i)
print(*s)