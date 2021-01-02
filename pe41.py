from sympy import nextprime
def pandig(n):
	s=str(n)
	return ''.join(sorted(s))=='123456789'[:len(s)]

n=2
while(True):
	n=nextprime(n)
	if(pandig(n)):
		m=n
	if(len(str(n))>9):
		break