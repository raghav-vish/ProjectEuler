def fpow(n):
	su=0
	while(n):
		d=n%10
		su+=d*d*d*d*d
		n//=10
	return su

i=10
s=0
lastn=0
while(True):
	if(i==fpow(i)):
		s+=i
		lastn=i
	if(i-lastn>1000000):
		break
	i+=1
print(s)