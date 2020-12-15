def digfactsum(n):
	s=0
	while(n):
		d=n%10
		f=1
		for i in range(1, d+1):
			f*=i
		s+=f
		n//=10
	return(s)
su=0
n=10
lastn=0
while(True):
	if(n==digfactsum(n)):
		lastn=n
		su+=n
	print(n, su)
	n+=1
print(su)