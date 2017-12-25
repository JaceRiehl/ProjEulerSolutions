"""
What is the 10001st prime number
"""
import checkPrime as pr
index = 2
numOfPrimes = 0
lastPrime = 0
nthPrime = 10001
while(numOfPrimes != nthPrime):
	if(pr.checkIfPrime(index)):
		numOfPrimes += 1
		lastPrime = index
	index += 1
print(lastPrime)