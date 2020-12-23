print("Part 1:")
numbers = [0,3,1,6,7,5]
# numbers = [0,3,6] # 436 [0, 3, 6, 0, 3, 3, 1, 0, 4, 0, 2, 0, 2, 2, 1]

for i in range(len(numbers),2020):
	previous = numbers[-1]
	numbersBefore = numbers[:-1]
	if previous in numbersBefore:
		timeSincePreviousInstance = numbersBefore[::-1].index(previous) + 1
		numbers.append(timeSincePreviousInstance)
	else:
		numbers.append(0)
print(numbers[-1])


print("Part 2:")
numbers = [0,3,1,6,7,5]
# numbers = [0,3,6] # 175594

indexDict = {}

for i in range(0,30000000 - 1):
	if i < len(numbers) - 1:
		indexDict[numbers[i]] = i
		continue
	previous = numbers[-1]
	if previous in indexDict:
		timeSincePreviousInstance = i - indexDict[previous]
		numbers.append(timeSincePreviousInstance)
		indexDict[previous] = i
	else:
		numbers.append(0)
		indexDict[previous] = i
print(numbers[-1])


