import math as m
fib = [1,1]
while(len(str(fib[-1])) != 1000):
	print(fib[-1])
	fib.append(fib[-1] + fib[-2])
print(len(fib))