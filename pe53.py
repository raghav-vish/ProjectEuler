fact=[1]
f=1
for i in range(1, 101):
	f*=i
	fact.append(f)


count=0
for n in range(1, 101):
	for r in range(0, n+1):
		cnr=fact[n]/(fact[r]*fact[n-r])
		if(cnr>1000000):
			count+=1
print(count)
