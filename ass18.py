n=int(input("Enter any number :"))
temp=n
res=0
while(n>0):
    r=n%10
    res=res*10+r
    n=n//10
if(temp==res):
    print("The number is palindrome")
else:
    print("Not a palindrome")
