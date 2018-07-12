# Largest Number
n= input()
a=n.split()
p=a[0]
q=a[1]
r=a[2]
if p>q and p>r:
    print (p)
elif q>p and q>r:
    print (q)
else:
    print (r)
