# sum in array
mylis=[]
input=int(input())
inp=input.split()
n=inp[0]
k=inp[1]
i=0
sum=0
while(i<n):
    f=int(input())
    mylis.append(f)
    if i<k:
        sum=sum+f
    i=i+1
print sum
