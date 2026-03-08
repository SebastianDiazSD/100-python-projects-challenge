def game_difficulty():
    """
    Asks the user to choose a difficulty level.
    Easy: 10 attempts
    Hard: 5 attempts
    """
    difficulty = input('Choose a difficulty. Type "easy" or "hard":\n> ').lower()

    while difficulty != "easy" and difficulty != "hard":
        print("Uy no, that's not a valid option, parcero. Try again!")
        difficulty = input('Choose a difficulty. Type "easy" or "hard":\n> ').lower()

    number_attempts = 10 if difficulty == "easy" else 5
    print(
        f"\nBacano! You chose {difficulty} mode. You have {number_attempts} attempts to guess the number. Buena suerte!")

    return number_attempts


def guess_number(attempts, number):
    """
    Handles the user's guesses and provides feedback.
    """

    user_number = int(input('\n🎯 Make a guess:\n> '))
    while attempts >= 1:
        if user_number == number:
            print('\n🎉 You are right!! Felicitaciones!!')
            break
        elif attempts == 1:
            print('\n😢 You have no more attempts. You lose, parce')
            print(f"Pssst, the correct answer is {number}")
            break
        elif user_number < number:
            print('📉 Too low, llave.')
            attempts -= 1
            print(f'You have {attempts} attempts remaining to guess the number')
            user_number = int(input('Make a guess:'))
        elif user_number > number:
            print('📈 Too high, mi rey.')
            attempts -= 1
            print(f'🔁 You have {attempts} attempts remaining to guess the number')
            user_number = int(input('Make a guess:'))
