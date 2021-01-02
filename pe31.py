import time
count=8
start=time.time()
for v100 in range(0, 200, 100):
	for v50 in range(0, 200, 50):
		for v20 in range(0, 200, 20):
			for v10 in range(0, 200, 10):
				for v5 in range(0, 200, 5):
					for v2 in range(0, 200, 2):
						for v1 in range(0, 200, 1):
							if(v1+v2+v5+v10+v20+v50+v100==200):
								count+=1
print(time.time()-start)
print(count)