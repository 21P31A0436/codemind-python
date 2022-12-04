n=int(input())
c=0
for i in range(n):
    a=int(input())
    for j in range(1,a):
        k=j*j
        if(a==k):
            print('True')
            break
    else:
        print('False')