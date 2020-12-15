from sympy import nextprime
primes=[]
n=0
while(True):
	n=nextprime(n)
	if(n>=100000000):
		break
	primes.append(n)
print(primes)