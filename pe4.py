maxp=0
for i in range(100, 1000):
	for j in range(100, 1000):
		p=i*j
		s=str(p)
		if(s==s[::-1] and p>maxp):
			maxp=p
print(maxp)

'''
- Run two loops of 3 digit numbers
- For each set of numbers:
  - Calculate the product
  - If the product is a palindrome, and greater than previous max palindrome, store it
'''