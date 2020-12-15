def onlyodd(n):
	while(n):
		if((n%10)%2==0):
			return False
		n//=10
	return True

count=0
for i in range(1, 1000000000):
	if(i%10==0):
		continue
	count+=onlyodd(i+int(str(i)[::-1]))
print(count)