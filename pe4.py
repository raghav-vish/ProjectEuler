maxp=0
for i in range(100, 1000):
	for j in range(100, 1000):
		p=i*j
		s=str(p)
		if(s==s[::-1] and p>maxp):
			maxp=p
print(maxp)
