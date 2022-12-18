l=[]
n=input()
n=n.lower()
for i in n.split():
    if i==i[::-1]:
        l.append(i)
print(len(l))