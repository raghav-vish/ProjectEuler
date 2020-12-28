from sympy import isprime
import time
n=10001
arr=[[]]
for i in range(0,n): 
    for j in range(0,n):
        x = min(min(i,j),min(n-1-i,n-1-j))
        if(i<=j): 
            arr[i].append((n-2*x)*(n-2*x)-(i-x)-(j-x))
        else:
            arr[i].append(((n-2*x-2)*(n-2*x-2)+(i-x)+(j-x))) 
    arr.append([])
arr=arr[:-1]
p=0
print("Generated")
corner=0
for i in range(n):
	if(isprime(arr[i][i])):
		p+=1
	if(isprime(arr[i][n-1-i])):
		p+=1
perc=0
nu=n
print("Total primes calculated")
for i in range(n):
	nu-=2
	if(nu<0):
		break
	if(isprime(arr[i][i])):
		p-=1
	if(isprime(arr[i][n-i-1])):
		p-=1
	if(isprime(arr[n-1-i][i])):
		p-=1
	if(isprime(arr[n-1-i][n-i-1])):
		p-=1
	perc=p/(2*nu-1)
	print(nu, perc)