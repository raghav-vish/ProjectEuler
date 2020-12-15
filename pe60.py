from sympy import nextprime, isprime
primes=[]
p=0
for i in range(10000):
	p=nextprime(p)
	primes.append(p)

for prime1 in primes:
	for prime2 in primes:
		for prime3 in primes:
			for prime4 in primes:
				for prime5 in primes:
					a=int(str(prime1)+str(prime2))
					a=int(str(prime1)+str(prime2))
					
