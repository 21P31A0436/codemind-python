import math
l,r,k=map(int,input().split())
d=int(math.pow(l,r))
e=d%k
print(e)
#for i in range(l,r+1):
#    if(i%k==0):
#        c+=1
#print(c)