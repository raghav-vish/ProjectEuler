n=1001
arr=[[]]
for i in range(0,n): 
    for j in range(0,n):
        x = min(min(i,j),min(n-1-i,n-1-j))
        if(i<=j): 
            arr[i].append((n-2*x)*(n-2*x)-(i-x)-(j-x))
        else:
            arr[i].append(((n-2*x-2)*(n-2*x-2)+(i-x)+(j-x))) 
    arr.append([])
arr=arr[:-1]
s=-1
for i in range(n):
    s+=arr[i][i]+arr[i][n-i-1]
print(s)