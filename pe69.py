from sympy import nextprime
n=0
p=1
while(True):
	n=nextprime(n)
	p*=n
	if(p>1000000):
		print(p/n)
		break