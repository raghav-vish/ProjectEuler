import time
def prime(n):
	f=0
	for i in range(1, n):
		f+=(n%i==0)
	return f==1
start=time.time()
n=1
k=1
while(k!=10001):
	n+=2
	if(prime(n)):
		k+=1
		#print(k, n)
print(n)
print(time.time()-start)