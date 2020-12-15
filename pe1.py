s=0
for i in range(1, 1000):
	if(i%3==0 or i%5==0):
		s+=i
print(s)

#Simple one line implementation
print(sum(i for i in range(1,1000) if i%3==0 or i%5==0))

'''
Run a for loop from 1 to 999(inclusive)
if i is a multiple of 3 or 5, add it to the sum
'''