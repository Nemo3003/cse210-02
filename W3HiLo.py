'''
Authors: Dan Allred, Ulises Mariano Melgarejo","
Edit 1/22/2022 10:08am EST. - DA - original commit
Edit 1/22/2022 3:00pm EST. - GO - Class comments
'''

import random
from typing import Counter
# To create a python class, use the keyword 'class'
# Use the __init__() function to assign values to object properties

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __gt__(self, comparing_card):
        result = self.value > comparing_card.value
        return result

    def __lt__(self, comparing_card):
        result = self.value < comparing_card.value
        return result

    def show(self):
        print ("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:  #Ace, Jack, queen and King need comparible. or we could just name them 1, 11, 12, 13
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for n in range(len(self.cards)-1,0,-1):
            r = random.randint(0, n)
            self.cards[n], self.cards[r] = self.cards[r], self.cards[n]

    def drawCard(self):
        return self.cards.pop()

class Person(object):
    def __init__(self):
        self.hand = []

    def __gt__(self, comparing_obj):
        
        result = self.hand[-1] > comparing_obj.nextcard[-1]
        return result

    def __lt__(self, comparing_obj):
        
        result = self.hand[-1] < comparing_obj.nextcard[-1]
        return result

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def show(self):
        for card in self.hand:
            card.show()

class NextCard(object):
    def __init__(self):
        self.nextcard = []

    def draw(self, deck):
        self.nextcard.append(deck.drawCard())
        return self

    def show(self):
        for card1 in self.nextcard:
            card1.show()



deck = Deck()
deck.shuffle()

human = Person()
playerHand = human.draw(deck)

newcard = NextCard()
nextCard = newcard.draw(deck)
#The first value for the score is 300
score = 300

play = input("Do you want to play? Y or N? ")
while play.lower()== "y":
    card = playerHand
    print("\nThe current card is: ", (card.show()))
    guess = input("Guess H for high or L for low: " )
    if guess.lower()=="h":
        if card > nextCard:
            print(f"\nCorrect! The the card is {card.show()}")
            score += 100
            # adding = Counter.append(score)
            print(f"Your points are {score}")
            if score == 0 or score < 0:
                print("You lost all your points, you lose!")
                break
            elif score > 0:
                play_ag = input("Play again? Y or N? ")
                if play_ag.lower()=="n":
                    print("Thanks for playing, hope you enjoyed!")
                    break
            
            

        if card < nextCard:
            print(f"\nYou lost! The card was {nextCard.show()}")
            score -= 75
            print(f"Your points are {score}")
            if score == 0 or score < 0:
                print("You lost all your points, you lose!")
                break
            elif score > 0:
                play_ag = input("Play again? Y or N? ")
                if play_ag.lower()=="n":
                    print("Thanks for playing, hope you enjoyed!")
                    break
            

    if guess.lower()=="l":
        if card > nextCard:
            print(f"\nYou lost! card was {nextCard.show()}")
            score -= 75
            print(f"Your points are {score}")
            if score == 0 or score < 0:
                print("You lost all your points, you lose!")
                break
            elif score > 0:
                play_ag = input("Play again? Y or N? ")
                if play_ag.lower()=="n":
                    print("Thanks for playing, hope you enjoyed!")
                    break
            

        if card < nextCard:
            print(f"\nCorrect! The the card is {nextCard.show()}")
            score += 100
            print(f"Your points are {score}")
            if score == 0 or score < 0:
                print("You lost all your points, you lose!")
                break
            elif score > 0:
                play_ag = input("Play again? Y or N? ")
                if play_ag.lower()=="n":
                    print("Thanks for playing, hope you enjoyed!")
                    break
            

else:
    print("Thanks for playing!")