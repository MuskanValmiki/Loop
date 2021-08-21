i = 0
while i <= 6:
    j = 0
    while j <= 5:
        if (i in {0,6}):
            print("*",end="")
        elif i==1 and j==4:
            print("*",end="")
        elif i==2 and j==3:
            print("*",end="")
        elif i==3 and j==2:
            print("*",end="")
        elif i==4 and j==1:
            print("*",end="")
        elif i==5 and j==0:
            print("*",end="")
        else:
            print(" ",end="")
        j += 1
    print()
    i += 1
# print z pattern