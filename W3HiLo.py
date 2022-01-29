'''
Authors: Dan Allred, Ulises Mariano Melgarejo","
Edit 1/22/2022 10:08am EST. - DA - original commit
Edit 1/22/2022 3:00pm EST. - GO - Class comments
'''

import random
from typing import Counter

class Game:

    #TODO: To use at least one class.

    def let_play():
        try:
            card = random.randint(1,13)
            nextCards = random.randint(1,13)
            score = 300

            play = input("Do you want to play? Y or N? ")
            if play.lower() != "y" and play.lower() != "n":
                play = input("Do you want to play? Y or N? ")
            if play.lower() !="y":
                print("Only use 'y' or 'n', try again.")

            while play.lower()== "y":
                print("\nThe current card is: ", (card))
                guess = input("Guess H for high or L for low: " )
                if guess.lower() != "h" and guess.lower() != "l":
                    print("Invalid guess. Please try again.")
                    continue
                if guess.lower()=="h":
                    if card < nextCards:
                        print(f"\nCorrect! The the card is {nextCards}")
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


                        print(f"\nYou lost! The card was {nextCards}")
                    if card > nextCards:
                        score -=75
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
                    if card < nextCards:
                        print(f"\nYou lost! card was {nextCards}")
                        score += -75
                        print(f"Your points are {score}")
                        if score == 0 or score < 0:
                            print("You lost all your points, you lose!")
                            break
                        elif score > 0:
                            play_ag = input("Play again? Y or N? ")
                            if play_ag.lower()=="n":
                                print("Thanks for playing, hope you enjoyed!")
                                break


                        print(f"\nCorrect! The card was {nextCards}")
                    if card > nextCards:
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
        except ValueError:
            print("Please enter a valid input")
Game.let_play()
