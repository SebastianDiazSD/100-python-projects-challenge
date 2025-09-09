import random

# 🧠 Import the updated word list from hangman_words.py
from hangman_words import word_list

# Picking a random word from the list – ¡suerte!
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game setup
from hangman_art import stages

end_of_game = False
lives = 6

# 🎨 Import and show the game logo from hangman_art.py
from hangman_art import logo
print(logo)
print("Welcome to the game Hangman! Buena suerte")

# 🧪 Pro tip: Uncomment this line to cheat a bit during testing 👀
# print(f"Pssst, the word is: {chosen_word}")

# Creating the initial blanks

placeholder = len(chosen_word) * "_"
print(f"\n{placeholder}")
print(stages[lives])
display = []
for _ in range(word_length):
    display.append("_")

# Start the game loop
while not end_of_game:
    guess = input("Guess a letter, parcero: ").lower()
    checker = False
    while not checker:
        if guess.isalpha():
            checker = True
        else:
            guessed = input("\nPana! That is not a letter, Try again!\n")

    # 🤔 Let the user know if they already guessed that letter
    if guess in display:
        print(f"Ya dijiste '{guess}', bro. Try something else.")

    # Check if the guessed letter is in the word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # ❌ Wrong guess? Lose a life
    if guess not in chosen_word:
        print(f"'{guess}' isn't in the word. You lose a life, parce.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Nooo 😢 — You lose. Better luck next time!")

    # Print the current word status
    print(f"{' '.join(display)}")

    # ✅ Check if the word is complete
    if "_" not in display:
        end_of_game = True
        print("¡Bien ahí! You win 🎉")

    # 🎭 Show the hangman stage from hangman_art.py

    print(stages[lives])
