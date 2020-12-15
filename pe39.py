s=0
maxs=0
maxp=0
for p in range(1, 1000):
	for a in range(1, p):
		for b in range(a+1, p):
			for c in range(b+1, p):
				if(a+b+c==p and a+b>c and b+c>a and c+a>b and a*a+b*b==c*c):
					s+=1
				print(p,a,b,c)
	if(s>maxs):
		maxs=s
		maxp=p