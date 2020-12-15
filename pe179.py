import math
def countDivisors(n):
    cnt=0
    for i in range(1, (int)(math.sqrt(n))+1): 
        if (n % i == 0):  
            if (n/i==i): 
                cnt+=1
            else:
                cnt+=2           
    return cnt

div=[0]
for i in range(1, 10000001):
	div.append(countDivisors(i))
c=0
for i in range(2, 10000000):
	if(div[i]==div[i+1]):
		c+=1
print(c)