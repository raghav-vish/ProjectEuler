def fn(n):
	s=0
	while(n):
		d=n%10
		s+=d*d
		n//=10
	return s
count=0
for i in range(1, 10000000):
	f=i
	while(True):
		f=fn(f)
		if(f==1):
			break
		if(f==89):
			count+=1
			break