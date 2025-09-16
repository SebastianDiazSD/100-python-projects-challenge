# Printing logo and welcoming message

from art import logo, welcoming_message
import functions
import random
import os

print(logo)
print(welcoming_message)


def guess_number():
    # Setting the difficulty of the game
    user_attempts = functions.game_difficulty()

    # Choosing a random number between 1 and 100
    random_number = random.randint(0, 100)
    user_guess = functions.guess_number(user_attempts, random_number)
    # return user_guess


guess_number()
play_again = True
while play_again is True:
    play = input('\n🎮 Do you want to play again? Type "yes" or "no":\n> ')
    if play == "no":
        print("👋 Thanks for playing, pana! Come back soon!")
        play_again = False
    elif play=="yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        guess_number()
    else:
        print("🤔 That’s not a valid answer, llave. Type 'yes' or 'no'.")

