import random
list=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(list)
count=0
empty=[]
i=0
while i<len(list):
    if list[i] not in empty:
        if count<=4:
            empty.append(list[i])
            count+=1
    i+=1
print(empty)
