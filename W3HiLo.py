'''
Authors: Dan Allred, Ulises Mariano Melgarejo","
Edit 1/22/2022 10:08am EST. - DA - original commit
Edit 1/22/2022 3:00pm EST. - GO - Class comments
Edit 1/22/2022 10:08am EST. - DA new classes - commented out code with no classes for testing and validation from team.

'''

import random
from typing import Counter
# To create a python class, use the keyword 'class'
# Use the __init__() function to assign values to object properties

##########################################################################################################################################

class Card:

    def __init__(self) -> None:
        self.card1 = random.randint(1,13)
        self.card2= random.randint(1,13)

    def show_card1(self):
        print(f'Current card is: {self.card1}') 

    def show_card2(self):
        print(f'Current card is: {self.card2}')
        

    def high_or_low(self):
        if self.card2 > self.card1:     # check for high card
            return 1
        elif self.card2 < self.card1:   # check for low card
            return 0
        else:                           # same value card
            return -1

##########################################################################################################################################

class Player:

    def __init__(self):
        self.points = 300
        self.is_playing = True
        self.total_points = 0
        self.hl = 0

    def play_game(self):
        while self.is_playing:
            card = Card()
            card.show_card1()
            self.hl = card.high_or_low()
            self.update_points()
            card.show_card2()
            self.display_score()
            self.play_again()

    def guess_hilo(self):
        guess = input("Guess H for high or L for low: ")
        return guess

    def update_points(self):
        player_guess = self.guess_hilo()
        if (self.hl == 1 and player_guess.lower() == "h") or (self.hl == 0 and player_guess.lower() == "l"):
            self.points += 100
            print('You won this round!')
        elif (self.hl == 1 and player_guess.lower() == "l") or (self.hl == 0 and player_guess.lower() == "h"):
            self.points -= 75
            print('You lost this round, sorry!')
        else:
            self.points += 0

    def display_score(self):
        self.total_points = self.points
        print(f'Your score is:  {self.total_points}')

    def play_again(self):
        again = input("Play again? Y or N: ")
        if self.points > 0 and again.lower() == "y":
            self.is_playing = True
            print()
        elif self.points <= 0 or again.lower() == "n":
            print("Game over.")
            print()
            self.is_playing = False

##########################################################################################################################################


a = Player()
a.play_game() 


##########################################################################################################################################




# #The first value for the score is 300
# score = 300
# card = random.randint(1,13)
# nextCards = random.randint(1,13)
# #TODO: To use at least one class.
# play = input("Do you want to play? Y or N? ")
# while play.lower()== "y":
#     print("\nThe current card is: ", (card))
#     guess = input("Guess H for high or L for low: " )
#     if guess.lower()=="h":
#         if card > nextCards:
#             print(f"\nCorrect! The the card is {nextCards}")
#             score += 100
#             # adding = Counter.append(score)
#             print(f"Your points are {score}")
#             if score == 0 or score < 0:
#                 print("You lost all your points, you lose!")
#                 break
#             elif score > 0:
#                 play_ag = input("Play again? Y or N? ")
#                 if play_ag.lower()=="n":
#                     print("Thanks for playing, hope you enjoyed!")
#                     break


#         if card < nextCards:
#             print(f"\nYou lost! The card was {nextCards}")
#             score -= 75
#             print(f"Your points are {score}")
#             if score == 0 or score < 0:
#                 print("You lost all your points, you lose!")
#                 break
#             elif score > 0:
#                 play_ag = input("Play again? Y or N? ")
#                 if play_ag.lower()=="n":
#                     print("Thanks for playing, hope you enjoyed!")
#                     break


#     if guess.lower()=="l":
#         if card > nextCards:
#             print(f"\nYou lost! card was {nextCards}")
#             score -= 75
#             print(f"Your points are {score}")
#             if score == 0 or score < 0:
#                 print("You lost all your points, you lose!")
#                 break
#             elif score > 0:
#                 play_ag = input("Play again? Y or N? ")
#                 if play_ag.lower()=="n":
#                     print("Thanks for playing, hope you enjoyed!")
#                     break


#         if card < nextCards:
#             print(f"\nCorrect! The the card is {nextCards}")
#             score += 100
#             print(f"Your points are {score}")
#             if score == 0 or score < 0:
#                 print("You lost all your points, you lose!")
#                 break
#             elif score > 0:
#                 play_ag = input("Play again? Y or N? ")
#                 if play_ag.lower()=="n":
#                     print("Thanks for playing, hope you enjoyed!")
#                     break


# else:
#     print("Thanks for playing!")