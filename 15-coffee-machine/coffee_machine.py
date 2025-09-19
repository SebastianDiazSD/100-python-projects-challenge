# Resources available in our little coffee machine (just like in your corner café)
machine_resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

# Our cozy menu – simple, but with full sabor
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 2.5,
    }
}

# Money collected from all those tinticos and cafés
profit = 0


def is_transaction_successful(money_paid, cost_drink):
    """Check if the user paid enough and give change if needed."""
    if money_paid >= cost_drink:
        cashback = round(float(money_paid - cost_drink), 2)
        if cashback > 0:
            print(f"Here's your change: ${cashback}")
        global profit
        profit += cost_drink
        return True
    else:
        print("Sorry, that’s not enough money. Money refunded 💸")
        return False


def is_resources_sufficient(order_ingredients):
    """Check if there are enough resources to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > machine_resources.get(item, 0):
            print(f"Sorry, we're out of {item} 😔")
            return False
    return True


def user_payment():
    """Handle coin input and return the total amount paid by the user."""
    print("Please insert coins 💰")
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25
    total = 0
    try:
        total += float(input("How many quarters? ")) * quarter
        total += float(input("How many dimes? ")) * dime
        total += float(input("How many nickels? ")) * nickel
        total += float(input("How many pennies? ")) * penny
    except ValueError:
        print("Oops! Invalid input. Let's try again.")
        return 0
    return total


def make_coffee(drink_name, order_ingredients):
    """Deduct ingredients and prepare the drink."""
    for item in order_ingredients:
        machine_resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy it, parcero!")


# Welcome message with that Colombian warmth
print("👋 Welcome to the world's best Coffee Machine – Colombian Edition 🇨🇴")

# Start the machine
is_on = True

while is_on:
    choice = input(
        "\nWhat would you like today? We've got: Espresso, Latte, or Cappuccino ☕\n(Type 'report' to see machine status, 'off' to shut down, or 'no' to exit)\n→ "
    ).lower()

    if choice in menu:
        drink = menu[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = user_payment()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

    elif choice == "report":
        print("\n📊 Machine Status:")
        print(f"Water: {machine_resources['water']}ml")
        print(f"Coffee: {machine_resources['coffee']}g")
        print(f"Milk: {machine_resources['milk']}ml")
        print(f"Money: ${profit:.2f}")

    elif choice == "off":
        print("Turning off the machine... nos vemos 👋")
        is_on = False

    elif choice == "no":
        print("Gracias for stopping by! Come back soon for another cafecito ☕🙂")
        is_on = False

    else:
        print("Hmm... we don’t have that. Try something from the menu or check your spelling.")
