tot=0
for n in range(2, 3):
	root=int((n**0.5-int(n**0.5))*(10**100))
	tot+=sum(int(x) for x in str(root))
print(tot)