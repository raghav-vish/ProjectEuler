import datetime 
count=0
for year in range(1901, 2001):
	for month in range(1, 13):
		date=f"1 {month} {year}"
		day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
		count+=day==6
print(count)