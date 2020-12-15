'''def prime(n):
	f=0
	for i in range(2, (n//2)+1):
		if(n%i==0):
			return False
	return True

s=2
for n in range(3, 2000000, 2):
	if(prime(n)):
		s+=n
	print(n, s)
print(s)

'''
'''
Many easier solutions can be found using builin functions
This is a simple solution without any builtin function
'''


from sympy import nextprime
n=0
s=0
while(n<2000000):
	s+=n
	n=nextprime(n)
print(s)
'''Simpler and faster solution using nextprime'''