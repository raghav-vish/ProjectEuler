minn=1504170715041708
su=0
n=0
nn=0
for i in range(1, 100000000):
	nn+=1504170715041707
	n=nn%4503599627370517
	if(n<minn):
		minn=n
		su+=n
	print(i, n, su)