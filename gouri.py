a=[23,48,72,89,3,47,28,38]
user=int(input("enter a number="))
i=0
c=0
x=0
l=len(a)-user
while i<l:
    j=0
    while j<user:
        print(a[x],end="")
        j+=1
        x+=1
    if c==l:
        break
    c+=1
    i+=user
    print()
# pairs jitni user input

a=["A","b"]
n=int(input("enter number "))
i=1
b=[]
while i<=n:
    j=0
    while j<len(a):
        x=(a[j]+str(i))
        b.append(x)
        j=j+1
    i=i+1
print(b)


