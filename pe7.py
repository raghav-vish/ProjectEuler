def prime(n):
	f=0
	for i in range(1, n):
		f+=(n%i==0)
	return f==1
n=1
k=1
while(k!=10001):
	n+=2
	if(prime(n)):
		k+=1
print(n)


'''
#Using nextprime
from sympy import nextprime
n=1
for i in range(10001):
	n=nextprime(n)
print(n)
'''


'''
This would be too trivial if I were to use the nextprime function. So I haven't used it here.
Instead, start a loop from 1, and keep adding 2 to it and check if the number is prime.
If it is, increment the counter. Stop when you hit 10001
'''