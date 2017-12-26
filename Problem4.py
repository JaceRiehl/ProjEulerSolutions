pan = []
for i in range(1,1000):
	for j in range(1,1000):
		if(str(i * j)[::-1] == str(i*j)):
			pan.append(i*j)
pan = sorted(pan)
print(pan)