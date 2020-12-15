count=0
for l in range(12, 1500001):
	lcount=0
	for a in range(1, l):
		for b in range(a+1, l):
			c=l-a-b
			if(a+b>c and b+c>a and a+c>b and a*a+b*b==c*c):
				lcount+=1
				if(lcount>1):
					break
	if(lcount==1):
		count+=1