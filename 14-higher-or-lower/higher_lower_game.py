import random
from game_data import data
from art import logo, vs

# Helper function to get a random celebrity (pero random de verdad)
def get_random_celebrity(exclude_index=None):
    max_index = len(data)
    index = random.randint(0, max_index - 1)
    while index == exclude_index:
        index = random.randint(0, max_index - 1)
    return index, data[index]

# Function to print celeb info (bien clarito para el jugador)
def print_celeb(label, celeb):
    print(f"Compare {label}: {celeb['name']}, {celeb['description']}, from {celeb['country']}")

# Function to ask player for their guess (con cariño)
def get_user_choice():
    return input("Who has more followers? Type 'A' or 'B':\n").strip().lower()

# Function to check if the user's guess was good or not
def is_guess_correct(choice, a_followers, b_followers):
    if choice == "a":
        return a_followers > b_followers
    elif choice == "b":
        return b_followers > a_followers
    else:
        return False  # In case they type something raro


# Main game function – this is where the rumba starts
def game_hl():
    print(logo)
    print("Welcome to our greatest game ever!!! 🇨🇴🔥")

    score = 0
    game_should_continue = True

    # Start with two random celebs
    index_a, celeb_a = get_random_celebrity()
    index_b, celeb_b = get_random_celebrity(exclude_index=index_a)

    while game_should_continue:
        # Show both celebs
        print_celeb("A", celeb_a)
        print(vs)
        print_celeb("B", celeb_b)

        # Get user's choice
        choice = get_user_choice()

        # Get follower counts pa' comparar
        a_followers = celeb_a['follower_count']
        b_followers = celeb_b['follower_count']

        # Check if guess is correct
        if is_guess_correct(choice, a_followers, b_followers):
            score += 1
            print(f"🎉 You're correct! Your current score is: {score}\n")
            # El que ganó sigue, el otro se reemplaza
            if choice == "a":
                celeb_a = celeb_a
            else:
                celeb_a = celeb_b
                index_a = index_b
            index_b, celeb_b = get_random_celebrity(exclude_index=index_a)
        else:
            print(f"❌ Oops! You're wrong. Final score: {score}")
            play_again = input("Do you want to play again? (yes/no):\n").strip().lower()
            if play_again in ["yes", "y", "sí", "si", "claro", "dale"]:
                # Restart everything
                score = 0
                index_a, celeb_a = get_random_celebrity()
                index_b, celeb_b = get_random_celebrity(exclude_index=index_a)
                print("\nAlright, vamos otra vez! 🔥\n")
                print(logo)
            else:
                print("Thanks for playing, parcerito. Hasta la próxima 👋🇨🇴")
                game_should_continue = False


# Call the game
game_hl()