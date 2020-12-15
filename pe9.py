for a in range(1, 1000):
	for b in range(a+1, 1000):
		c=1000-a-b
		if(a*a+b*b==c*c and a+b>c and b+c>a and a+c>b):
			print(a*b*c)


'''
Use 2 for loops for the first 2 side lengths.
Run the first loop from 1 to 999(inclusive). The next loop will nly need to run from a+1 to 100. The third side length will be 1000-sum of first two sides becuase the perimeter is 1000.
For each combination, check if pythagoras' theorem holds true and if the side lengths form a valud triangle
'''