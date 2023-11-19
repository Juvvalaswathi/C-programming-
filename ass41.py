n=int(input())

s=input().split()
l=[]
for i in s:
    l.append(int(i))
s=input().split()
m=[]
for i in s:
    m.append(int(i))
for i in range(0,n):
    res=l[i]-m[i]
    print(res,end=' ')
