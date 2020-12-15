maxs=0
for a in range(100):
	for b in range(100):
		s=sum(int(x) for x in str(a**b))
		if(s>maxs):
			maxs=s
print(maxs)