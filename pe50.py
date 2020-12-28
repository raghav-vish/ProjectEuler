from sympy import nextprime
primes=[]
conssumpr=[0]
n=2
p=0
while(n<1000000):
	primes.append(n)
	p+=n
	conssumpr.append(p)
	n=nextprime(n)
consumdif=[]
consumij=[]
print('1done')

for i in range(len(conssumpr)):
	for j in range(i+2, len(conssumpr)):
		p=conssumpr[j]-conssumpr[i]
		if(p in primes):
			consumdif.append(p)
			consumij.append(j-i)

print('2done')

for i in range(len(consumij)):
	for j in range(len(consumij)-i-1):
		if(consumij[j]>consumij[j+1]):
			consumij[j], consumij[j+1] = consumij[j+1], consumij[j]
			consumdif[j], consumdif[j+1] = consumdif[j+1], consumdif[j]

print(consumdif[-1])