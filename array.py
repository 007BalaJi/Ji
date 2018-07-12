# sum in array
mylis=[]
n=int(input())
k=int(input())
i=0
sum=0
while(i<n):
    f=int(input())
    mylis.append(f)
    if i<k:
        sum=sum+f
    i=i+1
print sum
