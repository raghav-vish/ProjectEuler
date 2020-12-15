from sympy import isprime
for a in range(1001, 10000, 2):
	for b in range(a+2, 10000, 2):
		c=b+b-a
		if(c>10000):
			break
		if(isprime(a) and isprime(b) and isprime(c)):
			sa=sorted(str(a))
			sb=sorted(str(b))
			sc=sorted(str(c))
			if(sa==sb==sc):
				print(a,b,c)