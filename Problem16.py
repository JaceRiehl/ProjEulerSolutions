import math as m
sumOfDigs = 0
power = str(2**1000)
print(power)
for i in range(len(power)):
	sumOfDigs += int(power[i])
print(sumOfDigs)