import random

def print_logo():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_drawings = [
    "🂡", "🂢", "🂣", "🂤", "🂥", "🂦", "🂧", "🂨", "🂩", "🂪", "🂫", "🂭", "🂮"
]

def deal_card_index():
    return random.randint(0, len(cards) - 1)

def calculate_score(hand_indexes):
    hand_values = [cards[i] for i in hand_indexes]
    score = sum(hand_values)
    while 11 in hand_values and score > 21:
        ace_index = hand_values.index(11)
        hand_values[ace_index] = 1
        score = sum(hand_values)
    return score

def display_hand(hand_indexes, is_user=True):
    player = "Your" if is_user else "Computer's"
    drawn = [card_drawings[i] for i in hand_indexes]
    values = [cards[i] for i in hand_indexes]
    print(f"{player} cards: {' '.join(drawn)} | Score: {sum(values)}")

def blackjack():
    print_logo()
    print("🎲 Welcome to Blackjack — Colombian style 🇨🇴!")
    print("Try to get as close to 21 as possible without going over.")
    print("Face cards are worth 10, Aces can be 11 or 1.\n")

    while True:
        user_choice = input('Do you want to play Blackjack? Type "yes" or "no": ').lower()
        if user_choice == "no":
            print("🇨🇴 Bueno parce, see you next time! 🍃")
            break
        elif user_choice != "yes":
            print("Uy no... that's not a valid option. Try again.")
            continue

        user_hand_indexes = [deal_card_index(), deal_card_index()]
        computer_hand_indexes = [deal_card_index()]

        game_over = False

        while not game_over:
            user_score = calculate_score(user_hand_indexes)
            comp_score = calculate_score(computer_hand_indexes)

            display_hand(user_hand_indexes)
            print(f"Computer's first card: {card_drawings[computer_hand_indexes[0]]}\n")

            if user_score == 21:
                print("🃏 Blackjack! Qué suerte parce! 🎉")
                game_over = True
            elif user_score > 21:
                print("💥 Uy no! You went over 21. You lose. 🍌")
                game_over = True
            else:
                more_card = input('Do you want another card? ("y" to draw / "n" to pass): ').lower()
                if more_card == "y" or more_card == "yes":
                    user_hand_indexes.append(deal_card_index())
                else:
                    break

        # Computer's turn
        while calculate_score(computer_hand_indexes) < 17:
            computer_hand_indexes.append(deal_card_index())

        user_score = calculate_score(user_hand_indexes)
        comp_score = calculate_score(computer_hand_indexes)

        display_hand(user_hand_indexes)
        display_hand(computer_hand_indexes, is_user=False)

        # ✅ FIXED LOGIC: Can't win if you went over 21
        print("🏁 Final Result:")
        if user_score > 21:
            print("❌ You went over. Ay nooo! You lose 😭")
        elif comp_score > 21:
            print("🎉 ¡Qué nota! The computer went over. You win, parce! 🏆")
        elif user_score > comp_score:
            print("🎉 You won, parce! 🏆")
        elif user_score < comp_score:
            print("😓 You lost. The computer beat you this time.")
        else:
            print("🤝 It's a draw. Casi casi...")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Gracias por jugar, parcerito. ¡Hasta la próxima! 🇨🇴")
            break

# Run the game
blackjack()