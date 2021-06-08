user=int(input("enter any number="))
i=1
sum=0
while i<=user:
    num=int(input("enter any number="))
    sum+=num
    i+=1
print(sum)

i=30
sum=0
while i<=420:
    if i%8==0:
        sum+=i
    i+=1
print(sum)
