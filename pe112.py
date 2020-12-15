def incr(n):
	ld=10
	while(n):
		if(n%10>ld):
			return False
		ld=n%10
		n//=10
	return True

def decr(n):
	ld=-10
	while(n):
		if(n%10<ld):
			return False
		ld=n%10
		n//=10
	return True

def bouncy(n):
	if(incr(n) or decr(n)):
		return False
	return True


b=0
i=1
while(True):
	if(bouncy(i)):
		b+=1
	p=b/i
	if(p>=0.99):
		print(i, p)
		break
	#print(i, p)
	i+=1	