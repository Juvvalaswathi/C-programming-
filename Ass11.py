#write a code for prepare shopping mall bill
top=100
pants=200
saree=300
shoes=50
print("***welcome to shopping mall***")
cname=input("enter customer name")
phno=int(input("enter phone no"))
topq=int(input("enter no of tops are"))
pantsq=int(input("enter no of pants are"))
sareeq=int(input("enter no of sarees are"))
shoesq=int(input("enter no of shoes are"))
bill=(top*topq)+(pants*pantsq)+(saree*sareeq)+(shoes*shoesq)
if bill>=2000:
    disc=bill*20/100
elif bill>1000:
    disc=bill*10/100
elif bill>500:
    disc=bill*5/100
else:
    disc=bill*3/100
tbill=bill-disc
gst=tbill*12/100
obill=tbill+gst
print("enter customer name",cname)
print("customer phno",phno)
print("bill",bill)
print("discount",disc)
print("gst 12%",gst)
print("bill paid",obill)
print("***thank you***")
