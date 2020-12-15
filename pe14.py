def collatz(n):
	steps=1
	while(n!=1):
		if(n%2==0):
			n//=2
		else:
			n=(3*n+1)//2
			steps+=1
		steps+=1
	return steps

maxsteps=0
maxn=0
for i in range(1, 1000000):
	step=collatz(i)
	if(step>maxsteps):
		maxsteps=step
		maxn=i
print(maxn)

'''
Define collatz function to divide by 2 and increase steps by one if the number is even, or multiply by 3, add one and then divide by 2 and increase steps by 2.
Calculate number of steps taken by each number.

Possible optimization: Store steps taken by each number in a list, so that it can directly be added when that number is reached in anther number's journey to 1
'''