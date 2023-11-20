n=int(input("enter number of elements:"))

count=0

I=list(map(int,input("enter list elements: ").split()))

l1=[]

for i in range(0,n,1):

k=i+1

for j in range(k,n,1):

if(1[i]==1[j]):

count+=1
break

if(count>0):

if 1[i] in l1:

break

else:

l1.append(I[i])

count=0

print(l1)
