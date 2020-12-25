fact=[1]
n=1
for i in range(1, 20010):
	n*=i
	fact.append(n)

def D(n):
	p=1
	if(n%2!=0):
		for i in range(n//2+1):
			p*=(fact[n]/(fact[i]*fact[n-i]))**2
	else:
		for i in range(n//2):
			p*=(fact[n]/(fact[i]*fact[n-i]))**2		
		i=n//2
		p*=(fact[n]/(fact[i]*fact[n-i]))
	
	s=0
	if(p==1):
		return 1

	p=int(p)
	for i in range(1, int(p**0.5)+1):
		if(p%i==0):
			if(i==p//i):
				s+=i
			else:
				s+=i+p//i
	return s

su=0
for i in range(1, 20001):
	su+=D(i)
	print(i, su)