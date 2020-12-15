a=0
b=1
c=a+b
s=0
while(c<=4000000):
	a=b
	b=c
	c=a+b
	if(c%2==0):
		s+=c
print(s)

'''
Initialize a and b to 0, and c to their sum
Run a while loop. Put b's value in a and c's value in b. Recalculate c
Run this loop while c is less than 4million
If c is even, add to the sum
'''