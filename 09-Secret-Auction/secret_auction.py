# Printing logo and welcoming message

from art import logo, welcoming_message, prizes
import random
import os

print(logo)
print(welcoming_message)

# Asking the user for name and bid

user_name = input("Panita, what is your name?\n")
# user_bid = input("\nHow much do you want to bid, viejito?\n")
user_player_bid = False
while not user_player_bid:
    try:
        user_bid = float(input("\nHow much do you want to bid, viejito?\n"))
        user_player_bid = True
    except ValueError:
        print("That is not a valid option")

# Dictionay to store the information
bid_dict = {user_name: user_bid}

# Asking if there are other players

all_payers = False

while not all_payers:
    new_player = input("\nHermano, Someone else want to compete with you? Type 'Yes' or 'No'\n").lower()
    while new_player not in ("yes", "no"):
        print("Parcero, that is not a valid option")
        new_player = input("\nHermano, Are there any other bidders? Type 'yes' or 'no'\n").lower()

    if new_player == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        new_player_name = False
        player_name = input("\nWhat is the name of the new bidder?\n")
        while not new_player_name:
            if player_name.isalpha():
                new_player_name = True
            else:
                print("That is not a valid option")
                player_name = input("\nWhat is the name of the new bidder?\n")

        new_player_bid = False
        while not new_player_bid:
            try:
                player_bid = float(input(f"\nHow much is the bid of {player_name}?\n"))
                new_player_bid = True
            except ValueError:
                print("That is not a valid option")
        bid_dict[player_name] = player_bid
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nSo all players and bids are on the table, panita!\n")
        all_payers = True

winner = user_name
for player in bid_dict:
    if bid_dict[player] > bid_dict[winner]:
        winner = player

prize = prizes[random.randint(1, len(prizes))]
print("🎉 The auction has ended! 🎉")
print(f"And the winner is...{winner}\nwith a bid of ${bid_dict[winner]}")
print(f"🏆 Prize: {prize}")
