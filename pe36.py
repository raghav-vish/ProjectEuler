su=0
for i in range(1000000):
	s=str(i)
	if(s==s[::-1]):
		b=bin(i)[2:]
		if(b==b[::-1]):
			su+=i
print(su)