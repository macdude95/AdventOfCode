data = ["54","91","137","156","31","70","143","51","50","18","1","149","129","151","95","148","41","144","7","125","155","14","114","108","57","118","147","24","25","73","26","8","115","44","12","47","106","120","132","121","35","105","60","9","6","65","111","133","38","138","101","126","39","78","92","53","119","136","154","140","52","15","90","30","40","64","67","139","76","32","98","113","80","13","104","86","27","61","157","79","122","59","150","89","158","107","77","112","5","83","58","21","2","66"]
# data = ["16","10","15","5","1","11","7","19","6","12","4"]
# data = ["28","33","18","42","31","14","46","20","48","47","24","23","49","45","19","38","39","11","1","32","25","35","8","17","7","9","4","2","34","10","3"]
numbers = [int(x) for x in data]
numbers = sorted(numbers)

print("Part 1:")
differences = {1:0, 2:0, 3:0}
differencesList = []
previous = 0
for n in numbers:
	difference = n - previous
	differences[difference] += 1
	differencesList.append(difference)
	previous = n
differences[3] += 1

print(differences[1] * differences[3])

print("Part 2:")
lengthsOf1SubArrays = []
currentLength = 0
for d in differencesList:
	if d == 1:
		currentLength += 1
	else: # d == 3
		if currentLength > 0:
			lengthsOf1SubArrays.append(currentLength)
			currentLength = 0
if currentLength > 0:
	lengthsOf1SubArrays.append(currentLength)

total = 1
for length in lengthsOf1SubArrays:
	if length == 1:
		total *= 1
	if length == 2:
		total *= 2
	if length == 3:
		total *= 4
	if length == 4:
		total *= 7

print(total)


