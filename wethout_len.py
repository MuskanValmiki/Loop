# a = 'string'
a=[1,2,3,4,5]
c=0
for i in a:
    c+=1
print(c)

print(sum(1 for char in a))

c=0
while a[c:]:
    c+=1
print(c)

a = 'string'
count = 0
while True:
    try:
        if a[count]:
            count += 1
    except IndexError as e:
        break
print(count)
