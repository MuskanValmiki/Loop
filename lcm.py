num1=int(input("enter any number="))
num2=int(input("enter any number="))
if num1>num2:
    m=num1
else:
    m=num2
while 1:
    if m%num1==0 and m%num2==0:
        print("lcm=",m)
        break
    m+=1

