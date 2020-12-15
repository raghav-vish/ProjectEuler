import time
start=time.time()
i=1
while(True):
	n=sorted(str(i))
	n2=sorted(str(i*2))
	n3=sorted(str(i*3))
	n4=sorted(str(i*4))
	n5=sorted(str(i*5))
	n6=sorted(str(i*6))
	if(n==n2 and n2==n3 and n3==n4 and n4==n5 and n5==n6):
		print(i)
		break
	i+=1
print(time.time()-start)