from sympy import nextprime
primes=[47]
n=47
for i in range(100000):
	n=nextprime(n)
	primes.append(n)

tri=0
s=0
for i in range(1, 10000000):
	tri+=i
	flag=0
	for n in primes:
		if(n>tri):
			break
		if(tri%n==0):
			flag=1
			break
	if(flag==0):
		s+=i
		print(i, s)