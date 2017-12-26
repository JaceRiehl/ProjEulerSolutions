import isEven as ev
currChain = 0
currChainLen = 0
longestChain = 0
longestChainLength = 0

for i in range(2,1000000):
	currChain = i
	print(i)
	while(currChain != 1):
		currChainLen+=1
		if(ev.isNumEven(currChain)):
			currChain = currChain/2
		else:
			currChain = 3*currChain + 1
		if(currChainLen > longestChainLength):
			longestChainLength = currChainLen
			longestChain = i
	currChainLen = 0

print(str(longestChain) + " " + str(longestChainLength))


