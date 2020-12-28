def pandig(n):
	if(''.join(sorted(str(n)))=='123456789'):
		return True
	return False

i=1
maxn=0
while(True):
	s=i
	for n in range(2,10):
		s=int(str(s)+str(i*n))
		if(pandig(s) and s>maxn):
			maxn=s
			print(i, n, maxn)
	i+=1