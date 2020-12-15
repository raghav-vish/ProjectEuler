def prime(n):
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