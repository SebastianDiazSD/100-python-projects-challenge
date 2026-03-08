word_list = ["aardvark", "baboon", "camel", "SEBAS"]

# Step 1

# ToDo 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

import random

random_index = random.randrange(len(word_list))
chosen_word = word_list[random_index].lower()

print(chosen_word)

# ToDo 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guessed = input("\nGuess a letter, panita!\n")
# checker = False
# while not checker:
#     if guessed.isalpha():
#         checker = True
#     else:
#         guessed = input("\nPana! That is not a letter, Try again!\n")
#
# print(guessed)

# ToDo 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#  Print "Right" if it, "Wrong" if it is not.

# for char in chosen_word:
#     if guessed == char:
#         print("Right")
#     else:
#         print("Wrong")

# Step 2

# ToDo 4 - Create a "placeholder" with the same number of blanks as the chosen word

placeholder = len(chosen_word) * "_"

print(placeholder)

# ToDo 5 - Create a "display" that puts the guess letter in the right position

# display = ""
# for char in chosen_word:
#     if char == guessed:
#         display += char
#     else:
#         display += "_"
#
# print(display)

# Step 3

# ToDo 6 - Use a while loop to let the user guess again

game_over = False
correct_letters = []

while not game_over:
    guessed = input("\nGuess a letter, panita!\n")
    display = ""
    checker = False
    while not checker:
        if guessed.isalpha():
            checker = True
        else:
            guessed = input("\nPana! That is not a letter, Try again!\n")

    # ToDo 7 - Change the loop so that you keep track of the guessed letters.

    for char in chosen_word:
        if char == guessed:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)

    if "_" not in display:
        word_completed = True
        print("Panita, you have won")

# Step 4

# ToDo 8 - Create a variable called "lives" to keep track of the user attempts. Set "lives" to equal 6.

lives=6

# ToDo 9 - If guess is not in chosen_word, then reduce lives by 1. If lives goes to 0, print "You lose"

if guessed is not in chosen_word:
    lives-=1
    if lives==0:
        game_over=True
        print("Hermano, you hav lost!")

# ToDo 10 - print the ASCII art from the list stages that corresponds to the current number of lives

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']