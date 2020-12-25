def hcf1(a,b):
	for i in range(2, min(a,b)):
		if(a%i==0 and b%i==0):
			return False
	return True

frac=[]
num=[]
den=[]
for d in range(2, 1000001):
	for n in range(1, d):
		if(hcf1(d,n)):
			num.append(n)
			den.append(d)
			frac.append(n/d)
for i in range(len(frac)):
	for j in range(len(frac)-i):
		if(frac[j]>frac[j+1]):
			frac[j], frac[j+1] = frac[j+1], frac[j]
			num[j], num[j+1] = num[j+1], num[j]
			den[j], den[j+1] = den[j+1], den[j]
for i in range(1, len(num)):
	if(num[i]==3 and den[i]==7):
		print(num[i-1])	