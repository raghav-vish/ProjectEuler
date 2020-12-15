import time
start=time.time()
li=[]
for a in range(2, 101):
	for b in range(2, 101):
		n=pow(a,b)
		li.append(n)
print(len(set(li)))
print(time.time()-start)