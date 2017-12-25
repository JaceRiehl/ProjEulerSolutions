import checkPrime as pr
primes = []
for i in range(2,2000001):
	if(pr.checkIfPrime(i)):
		primes.append(i)
print(sum(primes))