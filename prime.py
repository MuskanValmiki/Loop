num=int(input("enter a number"))
i=2
c=1
while i<=num:
    if num%i==0:
        c+=1
    i+=1
if c==2:
    print(num,"prime")
else:
    print(num,"not prime")

# fibonesis series
num=int(input("enter any number="))
a=1
b=0
i=0
while i<num:
    c=a+b
    a=b
    b=c
    i+=1
    print(a)

