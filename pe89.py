import roman
romans=open("p089_roman.txt","r").read().split("\n")
for n in romans:
	print(roman.fromRoman(n))