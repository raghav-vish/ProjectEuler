den=2
count=0
for i in range(1000):
	frac=1/den
	f=(frac+1).as_integer_ratio()
	count+=len(str(f[0]))>len(str(f[1]))
	den=2+frac
print(count)