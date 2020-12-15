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