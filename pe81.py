arr=open("p081_matrix.txt","r").read().split("\n")[:-1]
for i in range(len(arr)):
	arr[i]=arr[i].split(",")
	for j in range(len(arr[i])):
		arr[i][j]=int(arr[i][j])

i=0
j=0
n=len(arr)-1
for i in range(n, -1, -1):
	for j in range(n, -1, -1):
		if(i<n and j<n):
			arr[i][j]+=min(arr[i+1][j], arr[i][j+1])
		elif(i<n):
			arr[i][j]+=arr[i+1][j]
		elif(j<n):
			arr[i][j]+=arr[i][j+1]

print(arr[0][0])