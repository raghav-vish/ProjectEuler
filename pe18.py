arr=[[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
maxs=0
for row1 in range(len(arr[0])):
	s=arr[0][row1]
	for row2 in range(row1, row1+2):
		s+=arr[1][row2]
		for row3 in range(row2, row2+2):
			s+=arr[2][row3]
			for row4 in range(row3, row3+2):
				s+=arr[3][row4]
				for row5 in range(row4, row4+2):
					s+=arr[4][row5]
					for row6 in range(row5, row5+2):
						s+=arr[5][row6]
						for row7 in range(row6, row6+2):
							s+=arr[6][row7]
							for row8 in range(row7, row7+2):
								s+=arr[7][row8]
								for row9 in range(row8, row8+2):
									s+=arr[8][row9]
									for row10 in range(row9, row9+2):
										s+=arr[9][row10]
										for row11 in range(row10, row10+2):
											s+=arr[10][row11]
											for row12 in range(row11, row11+2):
												s+=arr[11][row12]
												for row13 in range(row12, row12+2):
													s+=arr[12][row13]
													for row14 in range(row13, row13+2):
														s+=arr[13][row14]
														for row15 in range(row14, row14+2):
															s+=arr[14][row15]
															print(row1, row5)
															if(s>maxs):
																maxs=s
print(maxs)