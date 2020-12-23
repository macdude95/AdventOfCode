start = [".##.####",".#.....#","#.###.##","#####.##","#...##.#","#######.","##.#####",".##...#."]

# start = [".#.","..#","###"]

print("Part 1:")
activeDict = {}
for j, line in enumerate(start):
	for i, c in enumerate(line):
		if c == "#":
			activeDict[(i,j,0)] = True

for _ in range(6):
	newActiveDict = {}
	xs = [x[0] for x in activeDict]
	ys = [x[1] for x in activeDict]
	zs = [x[2] for x in activeDict]
	for x in range(min(xs) - 1, max(xs) + 2):
		for y in range(min(ys) - 1, max(ys) + 2):
			for z in range(min(zs) - 1, max(zs) + 2):
				current = activeDict[(x,y,z)] if (x,y,z) in activeDict else None
				activeNeighbors = [c for c in activeDict if c[0] in range(x-1, x+2) and c[1] in range(y-1, y+2) and c[2] in range(z-1, z+2) and c != (x,y,z)]
				if current is None:
					if len(activeNeighbors) == 3:
						newActiveDict[(x,y,z)] = True
				else:
					if len(activeNeighbors) in range(2,4):
						newActiveDict[(x,y,z)] = True

	activeDict = newActiveDict
	newActiveDict = {}

print(len(activeDict))


print("Part 2:")

activeDict = {}
for j, line in enumerate(start):
	for i, c in enumerate(line):
		if c == "#":
			activeDict[(i,j,0,0)] = True

for _ in range(6):
	newActiveDict = {}
	xs = [x[0] for x in activeDict]
	ys = [x[1] for x in activeDict]
	zs = [x[2] for x in activeDict]
	ws = [x[3] for x in activeDict]
	for x in range(min(xs) - 1, max(xs) + 2):
		for y in range(min(ys) - 1, max(ys) + 2):
			for z in range(min(zs) - 1, max(zs) + 2):
				for w in range(min(ws) - 1, max(ws) + 2):
					current = activeDict[(x,y,z,w)] if (x,y,z,w) in activeDict else None
					activeNeighbors = [c for c in activeDict if c[0] in range(x-1, x+2) and c[1] in range(y-1, y+2) and c[2] in range(z-1, z+2) and c[3] in range(w-1, w+2) and c != (x,y,z,w)]
					if current is None:
						if len(activeNeighbors) == 3:
							newActiveDict[(x,y,z,w)] = True
					else:
						if len(activeNeighbors) in range(2,4):
							newActiveDict[(x,y,z,w)] = True

	activeDict = newActiveDict
	newActiveDict = {}

print(len(activeDict))











