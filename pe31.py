count=1
for pound1 in range(0, 3):
	for pence50 in range(0, 5):
		for pence20 in range(0, 11):
			for pence10 in range(0, 21):
				for pence5 in range(0, 41):
					for pence2 in range(0, 101):
						for pence1 in range(0, 201):
							money=pound1*100 + pence50*50 + pence20*20 + pence10*10 + pence5*5 + pence2*2 + pence1
							if(money==200):
								count+=1
print(count)