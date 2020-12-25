arr=open("p067_triangle.txt","r").read().split("\n")[:-1]
for i in range(len(arr)):
	arr[i]=arr[i].split(' ')
	for j in range(len(arr[i])):
		arr[i][j]=int(arr[i][j])

for i in range(len(arr)-2, -1, -1):
	for j in range(len(arr[i])):
		arr[i][j]+=max(arr[i+1][j], arr[i+1][j+1])
print(arr[0][0])
