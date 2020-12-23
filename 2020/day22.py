masterPlayer1Deck = [44,47,29,31,10,40,50,27,35,30,38,11,14,9,42,1,26,24,6,13,8,15,21,18,4]
masterPlayer2Deck = [17,22,28,34,32,23,3,19,36,12,45,37,46,39,49,43,25,33,2,41,48,7,5,16,20]
# masterPlayer1Deck = [9,2,6,3,1]
# masterPlayer2Deck = [5,8,4,7,10]
# masterPlayer1Deck = [43, 19]
# masterPlayer2Deck = [2,29,14]


player1 = masterPlayer1Deck[::]
player2 = masterPlayer2Deck[::]
previousPlayer1Decks = set()
previousPlayer2Decks = set()

while len(player1) > 0 and len(player2) > 0:
	if str(player1) in previousPlayer1Decks and str(player2) in previousPlayer2Decks:
		# Player 1 wins
		print("Player 1 wins by infinite loop")
		break
	previousPlayer1Decks.add(str(player1))
	previousPlayer2Decks.add(str(player2))
	card1 = player1.pop(0)
	card2 = player2.pop(0)

	if card1 > card2:
		player1.append(card1)
		player1.append(card2)
	else:
		player2.append(card2)
		player2.append(card1)

score = 0
for i, card in enumerate(player1 + player2):
	score += (len(player1 + player2) - i) * card

print("Part 1:")
print(score)

player1 = masterPlayer1Deck[::]
player2 = masterPlayer2Deck[::]

def recursiveCombat(deck1, deck2):
	previousPlayer1Decks = set()
	previousPlayer2Decks = set()
	while len(deck1) > 0 and len(deck2) > 0:
		if str(deck1) in previousPlayer1Decks and str(deck2) in previousPlayer2Decks:
			# Player 1 wins
			return [-1], [] # Since player 1 deck has a length > 0, player 1 wins
		previousPlayer1Decks.add(str(deck1))
		previousPlayer2Decks.add(str(deck2))
		card1 = deck1.pop(0)
		card2 = deck2.pop(0)
		if len(deck1) >= card1 and len(deck2) >= card2:
			newDecks = recursiveCombat(deck1[:card1], deck2[:card2])
			if len(newDecks[0]) > 0: # This means player 1 won the recursive round
				deck1.append(card1)
				deck1.append(card2)
			else: # Otherwise player 2 won the recursive round
				deck2.append(card2)
				deck2.append(card1)
		else:
			if card1 > card2:
				deck1.append(card1)
				deck1.append(card2)
			else:
				deck2.append(card2)
				deck2.append(card1)
	return deck1, deck2

print("Part 2:")
decks = recursiveCombat(player1, player2)
score = 0
for i, card in enumerate(decks[0] + decks[1]):
	score += (len(decks[0] + decks[1]) - i) * card
print(score)
