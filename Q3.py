i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)

num=int(input("enter any number="))
i=1
sum=0
while i<=num:
    weight=int(input("enter any weight="))
    sum+=weight
    i+=1
average=sum/num
print(average)
if average%5==0:
    print("average divisible by 5")
else:
    print("average not  divisible by 5")
