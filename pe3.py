from sympy import isprime
n=600851475143
for i in range((n//2)+1, 2, -1):
	if(n%i==0 and isprime(i)):
		print(i)
		break