def pandig(s):
	if('0' in s):
		return False
	if('1' in s and '2' in s and '3' in s and '4' in s and '5' in s and '6' in s and '7' in s and '8' in s and '9' in s):
		return True
	return False

a=0
b=1
c=1
i=2
while(True):
	a=b
	b=c
	k=str(c)
	if(len(k)>=9):
		f=k[:9]
		l=k[len(k)-9:]
		if(pandig(l) and pandig(f)):
			print(i)
			break
	i+=1
	c=a+b