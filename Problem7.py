"""
What is the 10001st prime number
"""
import math as math
def checkIfPrime(num):
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True
index = 2
numOfPrimes = 0
lastPrime = 0
nthPrime = 10001
while(numOfPrimes != nthPrime):
	if(checkIfPrime(index)):
		numOfPrimes += 1
		lastPrime = index
	index += 1
print(lastPrime)