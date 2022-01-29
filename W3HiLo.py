'''
Authors: Dan Allred, Ulises Mariano Melgarejo","
Edit 1/22/2022 10:08am EST. - DA - original commit
Edit 1/22/2022 3:00pm EST. - GO - Class comments
'''

import random


class Player:
#This class holds the name of the player
    def __init__(self, name):
        self.name = name
    player = []
    def player():
        name = input("What is your name? ")
        player = Player(name)
        print(f"\nWelcome {name}!\n")

class Game:
    def main():
        print("Welcome to HiLo!")
        Player.player()
        Game.let_play()
    #This method allows us to play the game
    def let_play():
        try:
            card_random = random.randint(1,13)
            #The default score is 300
            score = 300
            play = input("Do you want to play HiLo? Y or N? ")
            if play.lower() != "y" and play.lower() != "n":
                play = input("Do you want to play? Y or N? ")
            if play.lower() !="y":
                print("Only use 'y' or 'n', try again.")

            while play.lower()== "y":
                print("\nThe current card is: ", (card_random))
                guess = input("Guess H for high or L for low: " )
                if guess.lower() != "h" and guess.lower() != "l":
                    print("Invalid guess. Please try again.")
                    continue

                if guess.lower()=="h":
                    nextCards = random.randint(1,13)
                    if card_random < nextCards:
                        print(f"\nCorrect! The the card is {nextCards}")
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

                    nextCards_1 = random.randint(1,13)
                    if card_random > nextCards_1:
                        score -=75
                        print(f"\nYou lost! card was {nextCards_1}")
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
                    nextCards_2 = random.randint(1,13)
                    if card_random < nextCards:
                        score -= 75
                        print(f"\nYou lost! card was {nextCards_2}")
                        print(f"Your points are {score}")
                        if score == 0 or score < 0:
                            print("You lost all your points, you lose!")
                            break
                        elif score > 0:
                            play_ag = input("Play again? Y or N? ")
                            if play_ag.lower()=="n":
                                print("Thanks for playing, hope you enjoyed!")
                                break
                    nextCards_3 = random.randint(1,13)
                    if card_random > nextCards:
                        score += 100
                        print(f"\nCorrect! The the card is {nextCards_3}")
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
                print("Thank you for playing!")
        except ValueError:
            print("Please enter a valid input")

Game.main()
