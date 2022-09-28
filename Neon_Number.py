num = int(input())
temp=num
sqr = num*num 
s = 0
while sqr>0:
    d = sqr%10
    s =s + d
    sqr = sqr//10
if (temp == s):
    print("Neon Number")
else:
    print("Not Neon Number")