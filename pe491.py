from itertools import permutations 
count=1
s='11223344556677889900'
i=1
permList = permutations(s)
for perm in permList:
	n=''.join(perm)
	if(n[0]=='0'):
		break
	count+=int(n)%11==0
	i+=1
print(count)