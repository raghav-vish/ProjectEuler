arr=open("p081_matrix.txt","r").read().split("\n")[:-1]
for i in range(len(arr)):
	arr[i]=arr[i].split(",")
	for j in range(len(arr[i])):
		arr[i][j]=int(arr[i][j])

i=0
j=0
s=arr[0][0]
while(i!=len(arr)-1 or j!=len(arr)-1):
	if(i==len(arr)-1):
		j+=1
	elif(j==len(arr)-1):
		i+=1
	elif(arr[i+1][j]<arr[i][j+1]):
		i+=1
	else:
		j+=1
	s+=arr[i][j]
	print(arr[i][j])
print(s)