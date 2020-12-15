from sympy import isprime
n=600851475143
for i in range(n//2, 2, -2):
	if(n%i==0 and isprime(i)):
		print(i)
		break

'''
Very inefficient brute force approach
Run a loop for half of n(largest possible factor, looping down to 2, decreasing by two each time(prime number won't be even, so we can skip over them))
If i is a factor of the number, check if it is prime. If it is, [rint the number and break out of the loop]
'''

#OR
from sympy import nextprime
largestfactor=1
n=600851475143
f=2
while(f<=(n//2+1)):
	if(n%f==0):
		largestfactor=f
		f=nextprime(f)
print(largestfactor)

'''
For each prime, check if it is a factor of the number. 
Run the loop until half of the number
'''
