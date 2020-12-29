ways=[0 for i in range(102)]
ways[0]=1

for i in range(1, 100):
	for j in range(i, 101):
		ways[j]+=ways[j-i]
print(ways[len(ways)-2])