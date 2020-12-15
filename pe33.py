def atleastonecommon(a, b):
	a=str(a)
	b=str(b)
	for char in b:
		if(char in a):
			return True
	return False

count=0
i=1
for den in range(10, 100):
	for num in range(10, den):
		if(atleastonecommon(den, num)):
			sd=str(den)
			sn=str(num)
			newsd=""
			newsn=""
			for char in sd:
				if(char not in sn):
					newsd+=char
			for char in sn:
				if(char not in sd):
					newsn+=char
			if(newsd==''):
				newsd=den%10
			if(newsn==''):
				newsn=num%10
			newsd=int(newsd)
			if(newsd==0):
				newsd=1
				continue
			newsn=int(newsn)
			if(newsn/newsd==num/den and den%10!=0):
				print(num, den, newsn, newsd)
				
print(den)