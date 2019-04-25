import random
from random import shuffle

## Creates the deck and lists them as the number/type(ex. Jack) then the value

numbers = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
value = [2,3,4,5,6,7,8,9,10,11,12,13,14]

deck = []

for n in numbers:
    for i in range(len(numbers)):
        deck.append((str(numbers[i]), value[i]))

for l in range(52):
    print(str(deck[l]))

random.shuffle(deck)

##Creating the players' hands

playerHand1 = []
playerHand2 = []

print("Here are the cards in Player 1's deck: ")
for number in range(26):
    for playerHand1 in range(1):
        print(str(deck.pop()))
        
deck1 = [x for x in deck if x not in playerHand1]
##Change

print("Here are the cards in Player 2's deck: ")
for number in range(26):
    for playerHand2 in range(1):
        print(str(deck1.pop()))


#Iterative designing by first creating deck then dealiing cards

##points1 = 0
##points2 = 0
##numCards1 = 26
##numCard2 = 26
##
##while len(playerHand1) <= 26:
##    points1 = 0
##    playerHand1.append(deck.pop())
##while len(playerHand2) <= 26:
##    points2 = 0
##    playerHand2.append(deck.pop())
##
##card1 = playerHand1.pop()
##card2 = playerHand2.pop()
##if card1.value[i] > card2.value[i]:
##    numcards1 += 1
##elif card2.value[i] > card1.value[i]:
##    numcards2 += 1



