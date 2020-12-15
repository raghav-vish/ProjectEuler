from num2words import num2words
tot=0
for i in range(1, 1001):
	s=num2words(i)
	tot+=len(s)-s.count(' ')-s.count('-')
print(tot)