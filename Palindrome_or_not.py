n=input()
n=n.casefold()
rev=reversed(n)
if list(n) ==list(rev):
    print('True')
else:
    print('False')