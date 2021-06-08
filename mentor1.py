user=int(input("enter any number="))
org=user
s=0
i=1
count=0
while i<=user:
    if org>=i:
        s+=i
        count+=1
        org=org-i
        
    i+=1
print(count)
# imp mentor gave 



