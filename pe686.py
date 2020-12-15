#import time
def P(L, n):
	i=1
	j=0
	c=0
	while(c<n):
		i*=2
		j+=1
		if(str(i).startswith(str(L))):
			c+=1
			#print(c, j)
	return j

#start=time.time()
#print(P(123, 678))
print(P(123, 678910))
#print(time.time()-start)