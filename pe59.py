arr=open("p059_cipher.txt","r").read().split(",")
for i in range(len(arr)):
	arr[i]=int(arr[i])
'''
for a in range(97, 121):
	for b in range(97, 121):
		for c in range(97, 121):
			'''
a=101
b=120
c=112
pwd=[a,b,c]
s=""
for i in range(len(arr)):
	s+=chr(arr[i]^pwd[i%3])
	if('%' in s or '&' in s or '#' in s):
		continue

su=0
for c in s:
	su+=ord(c)
print(su)