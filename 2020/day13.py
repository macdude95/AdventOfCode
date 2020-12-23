import itertools

time = 1004098
x = -1
busses = [23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,509,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,401,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19]
# busses = [17,x,13,19] # Part 2: 3417
# busses = [67,7,59,61] # Part 2: 754018
# busses = [67,x,7,59,61] # Part 2: 779210
# busses = [67,7,x,59,61] # Part 2: 1261476
# busses = [1789,37,47,1889] # Part 2: 1202161486

print("Part 1:")
loops = []
for i in range(len(busses)):
	bus = busses[i]
	if bus == -1:
		loops.append(-1)
	else:
		loops.append(int(time / bus) + (time % bus > 0)) # round up
	
pickupTimes = []
pickupIds = []
for i in range(len(busses)):
	loopsForBus = loops[i]
	if loopsForBus == -1:
		continue
	bus = busses[i]
	pickupTime = loopsForBus*bus
	pickupTimes.append(pickupTime)
	pickupIds.append(bus)
minPickupTime = min(pickupTimes)
waitTime = minPickupTime - time
print(waitTime * pickupIds[pickupTimes.index(minPickupTime)])


print("Part 2:")
busMax = max(busses)
busMaxIndex = busses.index(busMax)
busList = [bus for bus in busses if (bus != -1 and bus != busMax)]
t = busMax - busMaxIndex
inc = busMax
while True:
	valid = True
	for bus in busList:
		i = busses.index(bus)
		if (t + i) % bus != 0:
			valid = False
		else:
			inc *= bus
			busList.remove(bus)
	if len(busList) == 0:
		break
	t += inc
print(t)



