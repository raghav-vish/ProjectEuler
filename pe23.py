import time
start=time.time()
abundant=[]
for i in range(12, 21824):
	f=1
	for j in range(2, i//2+1):
		if(i%j==0):
			f+=j
			d=i//j
			if(j!=d):
				f+=d
			if(f>i):
				abundant.append(i)
				break
can=[i for i in range(21824)]
for i in range(len(abundant)):
	for j in range(i,len(abundant)):
		n=abundant[i]+abundant[j]
		if(n>=21824):
			break
		can[n]=0
print(sum(can))	