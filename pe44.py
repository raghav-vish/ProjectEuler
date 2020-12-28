pent=[]
for i in range(1, 10000):
	pent.append(i*(3*i-1)//2)
mind=pent[-1]
print("Yes")
for i in range(len(pent)):
	for j in range(i+1, len(pent)):
		s=pent[i]+pent[j]
		d=pent[j]-pent[i]
		if(s in pent and d in pent):
			print(d)
			if(d<mind):
				mind=d
				print(mind,"__")