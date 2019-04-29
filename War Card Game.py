import random

## Creates the deck and lists them as the number/type(ex. Jack) then the value

numbers = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
value = [2,3,4,5,6,7,8,9,10,11,12,13,14]

deck = []

for l in range(4):
    for i in range(len(numbers)):
        deck.append((str(numbers[i]), value[i]))

random.shuffle(deck)

##Creating the players' hands

playerHand1 = []
playerHand2 = []

##Iterative designing by first creating deck then dealing cards
##Splitting deck between two players

for i in range(26):
    playerHand1.append(deck.pop())

for i in range(26):
    playerHand2.append(deck.pop())

numCards1 = 26
numCards2 = 26

play = input("Are you ready to play War? Answer yes or no! ")
if play == "yes":
    print("These are the rules: Each player begins with 26 cards, face down. One card is flipped over at a time. The player whose card has the highest rank takes both cards.") 
    while numCards1 < 52 or numCards2 < 52:
        print(input("Press c to play a card. "))
        playerHand1.pop()
        playerHand2.pop()
        if playerHand1[-1] > playerHand2[-1]:
            numCards1 += 1
            numCards2 -= 1
            print("Player 1's card is " + str(playerHand1[-1]) + " and Player 2's card is " + str(playerHand2[-1]) + ".")
            print("Player 1 has won the war!", "\t")
            print("Player 1 has " + str(numCards1) + " cards and Player 2 has " +
            str(numCards2) + " cards.")
        elif playerHand2[-1] > playerHand1[-1]:
            numCards2 += 1
            numCards1 -= 1
            print("Player 1's card is " + str(playerHand1[-1]) + " and Player 2's card is " + str(playerHand2[-1]) + ".")
            print("Player 2 has won the war!", "\t")
            print("Player 1 has " + str(numCards1) + " cards and Player 2 has " +
            str(numCards2) + " cards.")
        elif playerHand1[-1] == playerHand2[-1]:
            playerHand1.pop()*2
            playerHand2.pop()*2
            if playerHand1[-1] > playerHand2[-1]:
                print("Time for War! Player 1's card equalled Player 2's card, so two more cards were flipped over.")
                numCards1 += 3
                numCards2 -= 3
                print("Player 1's card is " + str(playerHand1[-1]) + " and Player 2's card is " + str(playerHand2[-1]) + ".")
                print("Player 1 has won the war!", "\t")
                print("Player 1 has " + str(numCards1) + " cards and Player 2 has " +
                str(numCards2) + " cards.")
            elif playerHand2[-1] > playerHand1[-1]:
                print("Time for War! Player 1's card equalled Player 2's card, so two more cards were flipped over.")
                numCards2 += 3
                numCards1 -= 3
                print("Player 1's card is " + str(playerHand1[-1]) + " and Player 2's card is " + str(playerHand2[-1]) + ".")
                print("Player 2 has won the war!", "\t")
                print("Player 1 has " + str(numCards1) + " cards and Player 2 has " +
                str(numCards2) + " cards.")
            elif playerHand1[-1] == playerHand2[-1]:
                playerHand1.pop()*2
                playerHand2.pop()*2
                print("Time for War: Part 2! Both players first card and third card were the same so two more cards were flipped over.")
                if playerHand1[-1] > playerHand2[-1]:
                    numCards1 += 5
                    numCards2 -= 5
                    print("Player 1's card is " + str(playerHand1[-5]) + " and Player 2's card is " + str(playerHand2[-5]) + ".")
                    print("Player 1 has won the war!", "\t")
                    print("Player 1 has " + str(numCards1) + " cards and Player 2 has " +
                    str(numCards2) + " cards.")
                elif playerHand2[-1] > playerHand1[-1]:
                    numCards2 += 5
                    numCards1 -= 5
                    print("Player 1's card is " + str(playerHand1[-5]) + " and Player 2's card is " + str(playerHand2[-5]) + ".")
                    print("Player 2 has won the war!", "\t")
                    print("Player 1 has " + str(numCards1) + " cards and Player 2 has " +
                    str(numCards2) + " cards.")
if numCards1 == 52:
    print("Player 1 won!")
if numCards2 == 52:
    print("Player 2 won!")


