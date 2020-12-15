def area(x1, y1, x2, y2, x3, y3): 
  
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)  
                + x3 * (y1 - y2)) / 2.0) 
  
 
def isInside(x1, y1, x2, y2, x3, y3): 
    A = area (x1, y1, x2, y2, x3, y3) 
    A1 = area (0, 0, x2, y2, x3, y3)
    A2 = area (x1, y1, 0, 0, x3, y3)  
    A3 = area (x1, y1, x2, y2, 0, 0)
    return A==A1+A2+A3

triangles=open("p102_triangles.txt","r").read().split("\n")[:-1]
count=0
for triangle in triangles:
    triangle=triangle.split(",")
    x1=int(triangle[0])
    x2=int(triangle[1])
    x3=int(triangle[2])
    y1=int(triangle[3])
    y2=int(triangle[4])
    y3=int(triangle[5])
    count+=isInside(x1,x2,x3,y1,y2,y3)
print(count)