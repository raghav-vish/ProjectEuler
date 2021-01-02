from sympy import isprime,nextprime
count=1
primes=[]
n=2
while(n<1000000):
	primes.append(n)
	n=nextprime(n)
print(primes[-1])

for i in primes:
	n=i
	for j in range(len(str(n))):
		n=int(str(n)[1:]+str(n)[0])
		if(not isprime(n)):
			break
	else:
		if('0' not in str(i)):
			count+=1
		print(i)
print(count)