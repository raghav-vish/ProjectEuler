from sympy import nextprime, isprime
primes=[]
n=0
while(n<=100000000):
	n=nextprime(n)
	primes.append(n)

print("_")
c=0
for i in range(2, 100000000):
	if(i in primes):
		continue
	f=0
	for n in primes:
		if(n>f):
			break
		if(i%n==0):
			f+=1
		if(f>2):
			break
	if(f==2):
		c+=1
print(c)