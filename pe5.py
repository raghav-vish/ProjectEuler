n=2520
while(True):
	for i in range(2, 20):
		if(n%i!=0):
			break
	else:
		print(n)
		break
	n+=20

'''
Starting from 2520, keep incrementing by 20, until there is a number that has 1 to 20 all as its factors
'''