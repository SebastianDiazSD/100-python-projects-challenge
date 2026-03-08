print(f"Welcome to the Tip Calculator!")

# Ask for the total bill and check if the user input is a valid number or if it is greater than 0.
bill = False
total_bill = input("What was the total bill? $")
while not bill:
    if float(total_bill):
        total_bill = float(total_bill)
        if total_bill > 0:
            bill = True
        else:
            total_bill = input("That is not a valid number. Try again\nWhat was the total bill? $")
    else:
        total_bill = input("That is not a valid number. Try again\nWhat was the total bill? $")

# Ask for the tip which will a percentage of total bill.
# Check if the user input is a valid number or if it is equal to 10, 12 or 15%.
tip = False
total_tip = input("How much tip would you like to give? 10%, 12%, or 15%? ")
while not tip:
    if total_tip.isnumeric():
        total_tip = int(total_tip)
        if total_tip == 10 or total_tip == 12 or total_tip == 15:
            tip = True
        else:
            total_tip = input("That is not a valid number. Try again\n"
                              "How much tip would you like to give? 10, 12, or 15? %")
    else:
        total_tip = input("That is not a valid number. Try again\n"
                          "How much tip would you like to give? 10, 12, or 15? $")

# Ask for the how many people are going to pay the bill
# Check if the user input is a valid number or if it is greater than 0.
split = False
total_split = input("How many people to split the bill?")
while not split:
    if total_split.isnumeric():
        total_split = int(total_split)
        if total_split >= 1:
            split = True
        else:
            total_split = input("That is not a valid number. Try again\n"
                                "How many people to split the bill?")
    else:
        total_split = input("That is not a valid number. Try again\n"
                            "How many people to split the bill?")

# Calculate the amount each person is going to pay
amount_per_person = round((total_bill + (total_bill*total_tip/100))/total_split, 2)
print(f"Each person should pay: ${amount_per_person}")
