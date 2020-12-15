n=2520
while(True):
	for i in range(2, 20):
		if(n%i!=0):
			break
	else:
		print(n)
		break
	n+=20