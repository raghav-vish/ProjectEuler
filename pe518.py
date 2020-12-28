import time

def iprimes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n * n, limit + 1, n): # start at ``n`` squared
                is_prime[i] = False
    for i in range(limit + 1):
        if is_prime[i]: yield i

start=time.time()
n=100000000
s=0
arr=list(iprimes_upto(n))
for i in range(len(arr)):
	for j in range(i+1, len(arr)):
		a=arr[i]
		b=arr[j]
		c=((b+1)**2/(a+1))-1
		if(c in arr and c>b):
			s+=a+b+c
print(s)
print(time.time()-start)