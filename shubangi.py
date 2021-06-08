a=["A","B"]
user=int(input("enter any number="))
empty=[]
i=1
while i<=user:
    j=0
    while j<len(a):
        empty.append(a[j]+str(i))
        j+=1
    i+=1
print(empty)

