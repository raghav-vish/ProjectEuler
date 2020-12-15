s=[i for i in range(10)]
su=0
S=[]
for i in range(len(s)):
	su+=s[i]
	S.append(su)
for i in range(10, 2880067194370816121):
	prev=s[i-1]
	if(i%9==1):
		toadd=int("1"+str(prev))
	else:
		toadd=int(str(int(str(prev)[::-1])+1)[::-1])
	s.append(toadd)
	su+=toadd
	S.append(su)

a=0
b=1
c=1
i=2
su=0
while(i<91):
	a=b
	b=c
	su+=S[c]
	print(i, c)
	c=a+b
	i+=1
print(su)