def score(string):
	score=0
	for char in string:
		score+=ord(char)-64
	return score

names=open("p022_names.txt","r").read().split(",")
names=sorted(names)
total=0

for i in range(len(names)):
	names[i]=names[i][1:]
	names[i]=names[i][:-1]
	total+=score(names[i])*(i+1)
print(total)