t=[]
p=[]
h=[]
for n in range(100000):
	t.append(n*(n+1)//2)
	p.append(n*((3*n)-1)//2)
	h.append(n*((2*n)-1))
for n in t:
	if(n in p and n in h and n>40755):
		print(n)
		break