i=49
while i<=98:
    i=i+2
    print(i)

# prime
num=int(input("enter any number="))
i=1
c=0
while i<=num:
    if num%i==0:
        c+=1
    i+=1
if c==2:
    print("prime")
else:
    print("not prime")
