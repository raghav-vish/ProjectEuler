from sympy import isprime
count=1
for i in range(3, 1000000, 2):
	n=i
	for j in range(len(str(n))):
		n=int(str(n)[1:]+str(n)[0])
		if(not isprime(n)):
			break
	else:
		count+=1
		print(i)
print(count)