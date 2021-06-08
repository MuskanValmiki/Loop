i=1
while i<=100:
    if i%7==0:
        print(i)
    i+=1

# guessing game
user=int(input("enter any guess number="))
i=1
while i<=10:
    num=int(input("enter any number="))
    if user==num:
        print("user or num equal hai")
        print("your guess is correct")
        print("win")
        break
    elif user>num:
        print("user sa chota hai num")
    elif user<num:
        print("user sa bada hai num")
    else:
        print("your guess is wrong")
        print("guess again")
    i+=1

