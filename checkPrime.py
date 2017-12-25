import math as m
def checkIfPrime(num):
	for i in range(2, int(m.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True