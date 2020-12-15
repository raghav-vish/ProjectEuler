tri=[]
s=0
for i in range(100):
	s+=i
	tri.append(s)
words=open("p042_words.txt","r").read().split(",")
for i in range(len(words)):
	words[i]=words[i][1:]
	words[i]=words[i][:-1]

count=0
for word in words:
	wordscore=0
	for char in word:
		wordscore+=ord(char)-64
	if(wordscore in tri):
		count+=1
print(count)