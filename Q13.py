user=int(input("enter any number"))
i=1
while i<=user:
    print(i)
    i+=1

x=int(input("enter any number="))
y=int(input("enter any number="))
i=1
c=0
while i<=y:
    if x%i==0 and y%i==0:
        print("hcf=",i)
    i+=1

num1=int(input("enter any number="))
num2=int(input("enter any number="))
if num1>num2:
    m=num1
else:
    m=num2
i=1
while i<=m:
    if num1%i==0 and num2%i==0:
        hcf=i
    i+=1
print("hcf=",hcf)
