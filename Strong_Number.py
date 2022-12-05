n=int(input())
s=n
sum=0
while(n>0):
    r=n%10
    p=1
    i=1
    while(i<=r):
        p=p*i
        i+=1
    sum+=p
    n=n//10
if(s==sum):
    print('The number',s,'is a strong number')
else:
    print('The number',s,'is not a strong number')