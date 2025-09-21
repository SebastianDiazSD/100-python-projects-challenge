from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Bienvenidos to the best Coffee Machine, we got you covered! ☕️")
print("How can we serve you today?")

my_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

is_on = True
while is_on:
    options = my_menu.get_items()
    user_choice = input(f"What do you want to drink? We got {options} for you, pick your favorite! 😊\n").lower()

    if user_choice == "off":
        is_on = False
        print("The coffee machine is now off. See you next time, take care! ☕️👋")
    elif user_choice == "report":
        my_machine.report()
        my_coffee_maker.report()
    else:
        user_drink = my_menu.find_drink(user_choice)
        if user_drink:
            if my_coffee_maker.is_resource_sufficient(user_drink):
                if my_machine.make_payment(user_drink.cost):
                    my_coffee_maker.make_coffee(user_drink)
