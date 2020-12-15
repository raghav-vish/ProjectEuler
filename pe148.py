def PascalTriangle(n):
   trow = [1]
   y = [0]
   toret=[]
   for x in range(n):
    	toret.append(trow)
    	trow=[left+right for left,right in zip(trow+y, y+trow)]
   return toret

count=0
tri=PascalTriangle(1000000000)
for row in tri:
	for num in row:
		if(num%7!=0):
			count+=1
print(count)