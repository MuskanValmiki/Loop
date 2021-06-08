a=[2,8,3,9,40,30,10]
i=0
max=0
while i<len(a):
	c=-1
	index=0
	while index<len(a):
		if a[i]> a[index]:
			max=a[i]
			c+=1
		if c==3:
			print(max)
			break
		index+=1
	i+=1

a=[1,2,3,4,5,6]
i=0
max=0
while i<len(a):
	c=0
	index=0
	while index<len(a):
		if a[i]> a[index]:
			max=a[i]
			c+=1
		if c==3:
			print(max)
			break
		index+=1
	i+=1