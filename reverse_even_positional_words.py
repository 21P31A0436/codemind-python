n=input()
c=0
for i in n.split():
    if c%2==0:
        d=i[::-1]
    else:d=i
    c+=1
    print(d,end=' ')