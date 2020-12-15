consq=[]
for i in range(1, 5000):
	for j in range(i+1):
		consq.append((i*(i+1)*(2*i+1)//6)-(j*(j+1)*(2*j+1)//6))

s=0
consq=sorted(consq)
for n in consq:
	if(n>100000000):
		break
	st=str(n)
	if(st==st[::-1]):
		s+=n
print(s)