def factors(n):
	f=2
	for i in range(2, (n//2)+1):
		f+=n%i==0
	return f
n=0
fac=1
i=1
while(fac<=500):
	n+=i
	fac=factors(n)
	print(i, n, fac)
	i+=1
print(n)