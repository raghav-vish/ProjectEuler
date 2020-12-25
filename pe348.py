import time
start = time.time()
palin=[]
sq=[]
cub=[]
for i in range(1, 50000):
	palin.append(int(str(i)+str(i)[::-1]))
	sq.append(i*i)
	cub.append(i*i*i)
	for j in range(10):
		palin.append(int(str(i)+str(j)+str(i)[::-1]))
palin=sorted(palin)

su=0
i=0
for n in palin:
	ways=0
	for s in sq:
		if(s>n):
			break
		for c in cub:
			if(s+c>n):
				break
			if(n==s+c):
				ways+=1
	if(ways==4):
		su+=n
		i+=1
		print(n, i, su)
	if(i==5):
		break