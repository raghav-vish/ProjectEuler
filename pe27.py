from sympy import isprime
maxcons=0
maxab=0
for a in range(-999, 1001):
	for b in range(-999, 1001):
		n=0
		while(isprime(n*n+a*n+b)):
			n+=1
		if(n>maxcons):
			maxcons=n
			maxab=a*b
		print(a,b,n,maxcons,maxab)
print(maxab)