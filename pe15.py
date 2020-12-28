n=20;
arr=[[0 for i in range(n+1)] for i in range(n+1)]
for i in range(n):
	arr[i][n]=1
	arr[n][i]=1
for i in range(n-1, -1, -1):
	for j in range(n-1, -1, -1):
		arr[i][j]=arr[i+1][j]+arr[i][j+1]
print(arr[0][0])