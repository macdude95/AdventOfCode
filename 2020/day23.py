print("Part 1:")
circle = [2,5,3,1,4,9,8,6,7]
# circle = [3,8,9,1,2,5,4,6,7]

def cupsDictToString(cupsDict):
	added = []
	cup = 1
	s = ""
	while len(added) < len(cupsDict):
		s += str(cup)
		added.append(cup)
		cup = cupsDict[cup]
	return s

def runGame(cupsList, iterations, debug):
	minValue = min(circle)
	maxValue = max(circle)
	cupsDict = {}

	for i in range(len(circle)):
		cupsDict[circle[i]] = circle[(i + 1) % len(circle)]


	currentCup = circle[0]
	for i in range(iterations):
		if debug:
			print("-- move " + str(i + 1) + " --")
			print("Cups: " + cupsDictToString(cupsDict))
			print("curr cup: " + str(currentCup))
		cupsSublist = []
		for _ in range(3):
			cup = cupsDict[currentCup]
			cupsSublist.append(cup)
			cupsDict[currentCup] = cupsDict[cup]
		if debug:
			print("Picked up: " + str(cupsSublist))

		destinationCup = currentCup
		while True:
			destinationCup = destinationCup - 1
			if destinationCup < minValue:
				destinationCup = maxValue

			if destinationCup not in cupsSublist:
				break
		if debug:
			print("Destination cup: " + str(destinationCup))
		cupAfterDestination = cupsDict[destinationCup]
		cupsDict[destinationCup] = cupsSublist[0]
		cupsDict[cupsSublist[0]] = cupsSublist[1]
		cupsDict[cupsSublist[1]] = cupsSublist[2]
		cupsDict[cupsSublist[2]] = cupAfterDestination
		currentCup = cupsDict[currentCup]
	return cupsDict

# cupsDict = runGame(circle, 10, True)
cupsDict = runGame(circle, 100, False)
print(cupsDictToString(cupsDict)[1:])



print("Part 2:")
circle = [2,5,3,1,4,9,8,6,7]
for i in range(len(circle) + 1, 1000000 + 1):
	circle.append(i)
cupsDict = runGame(circle, 10000000, False)

firstStarCup = cupsDict[1]
secondStarCup = cupsDict[firstStarCup]

print(firstStarCup * secondStarCup)


















