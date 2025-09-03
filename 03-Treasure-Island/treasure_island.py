# Adding ASCII Art - link:

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

# Adding the welcoming message

print(
    f"Welcome to Treasure Island\n\nYour mission is to find the treasure\nBut careful, this island ain’t no walk in the"
    f"park — it's full of traps, beasts, and bad vibes.\n\nBuena suerte, parcero!")

# First decision
user_first_choice = input(
    "You’re at a crossroad, right in the middle of nowhere. Where you going, mijo? Type 'left' or 'right': ").lower()

# checking if the input is a valid option
checker=False
while not checker:
    if user_first_choice=="left" or user_first_choice=="right":
        checker=True
    else:
        user_first_choice = input(
            "Papi! That is not a valid option. Where you going, mijo? Type 'left' or 'right': ").lower()


if user_first_choice == "left":
    # Second decision
    user_second_choice = input(
        "\nYou reach a huge lake, looks like something outta the Amazonas. 🌊"
        "\nIn the middle, there's a tiny island. You gonna 'wait' for a canoe or 'swim' like a true costeño? ").lower()

    checker = False
    while not checker:
        if user_second_choice == "swim" or user_second_choice == "wait":
            checker = True
        else:
            user_second_choice = input(
                "Am I speaking in chinese? That is not a valid option."
                "What do you want to do, pana? Type 'wait' or 'swim': ").lower()

    if user_second_choice == "wait":
        # Third decision
        user_third_choice = input(
            "\nYou made it to the island, clean and dry — más o menos. There's a little house with 3 doors:"
            "one red, one yellow, and one blue. 🚪\nWhich door you picking, llave? ").lower()

        checker = False
        while not checker:
            if user_third_choice == "red" or user_third_choice == "yellow" or user_third_choice=="blue":
                checker = True
            else:
                user_third_choice = input(
                    "Papi again! That is not a valid option. Type 'red', 'yellow', or 'blue': ").lower()

        if user_third_choice == "yellow":
            print("\n🎉 Ayyy papiii! You found the treasure — gold, arepas, and patacones! 🏆")
            print("💃 You're the king of the island now. Time to celebrate with aguardiante!")
        elif user_third_choice == "red":
            print(
                "\n🔥 Ufff... bad luck, hermano. That room’s on fire! You just walked into an inferno. Game Over.")
        elif user_third_choice == "blue":
            print(
                "\n💀 You opened the door and boom — a pack of wild jaguars came at you like rush hour in Bogotá."
                "Game Over.")

    else:
        print("\n🐊 Ay nooo! You got snatched by a mutant bocachico with attitude. Game Over, my dude.")
else:
    print("\n😵 You walked straight into a hole full of guayabas. What a way to go. Game Over.")
