i=400
while i>=350:
    z=i-300
    if z%2!=0:
        print(z)
    i-=1

i=1
while i<=100:
    if i%3==0 and i%7==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    else:
        print(i)
    i+=1
