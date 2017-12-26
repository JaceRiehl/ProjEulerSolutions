uniqueSums = []
for i in range(2,101):
	for j in range(2,101):
			print(str(i) + " " + str(j))
			uniqueSums.append(i**j)
print(len(list(set(uniqueSums))))