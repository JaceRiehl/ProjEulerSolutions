import math as math
def checkIfPrime(num):
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True