count=0
for x1 in range(51):
	for y1 in range(51):
		for x2 in range(51):
			for y2 in range(51):
				op=(x1*x1 + y1*y1)**0.5
				oq=(x2*x2 + y2*y2)**0.5
				pq=((x2-x1)**2 + (y2-y1)**2)**0.5
				if(op+oq>pq and oq+pq>op and pq+op>oq):
					ops=op*op
					oqs=oq*oq
					pqs=pq*pq
					if(ops+oqs==pqs or oqs+pqs==ops or pqs+ops==oqs):
						count+=1
print(count)