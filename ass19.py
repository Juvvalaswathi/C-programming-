n=int(input("Enter any number :"))
temp=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res+r**3
if(temp==res):
    print("it is armstrong no")
else:
    print("it is not armstrong")
