
nterms=int(input())
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("please enter positive number")
elif nterms==1:
   print(n1)
else:
   while count < nterms:
       print(n1,end = " ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1