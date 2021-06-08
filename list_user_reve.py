a=[1,2,3,4,5,6]
num=int(input("enter a number"))
l=len(a)
i=l-num
while i<len(a):
    print(a[i])
    i+=1
# enter a number3
4
5
6

b=[1,2,3,4,5,6]
num=int(input("enter a number"))
c=num-len(b)
i=-1
while i>=c:
    print(b[i])
    i-=1
#enter a number3
6
5
4
