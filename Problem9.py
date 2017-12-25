import math as m
for a in range(1,500):
	for b in range(a+1, 501):
		c = m.sqrt(a*a + b*b)
		if(a + b + c == 1000):
			print(str(a) + " " + str(b) + " " + str(c))
