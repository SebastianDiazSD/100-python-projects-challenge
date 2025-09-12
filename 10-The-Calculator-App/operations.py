import os
import time

def sum(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 * number2


def calculator_operations(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    else:
        return number1 / number2


def display_calculator(user_input):
    display = """
 _____________________
|  _________________  |
| |  {element:>13}. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

    d = {'element': f'{user_input}'}
    out = display.format_map(d)

    return out


def first_number():
    is_number = False
    while not is_number:
        try:
            user_input = float(input("What is the first number, viejito?\n"))
            is_number = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print(display_calculator(user_input))
            return user_input
        except ValueError:
            print("❌ Oops, that's not a valid number. Try again, parce!")

def user_operation(user_number):
    user_operation = input("Mi hermano, what operation would you like to carry out? Type '+','-','*' or '/'\n")
    operators = ['+', '-', '*', '/']
    is_operation = False
    while not is_operation:
        if user_operation not in operators:
            print("❌ Invalid operation. Use only +, -, * or /. Vamos otra vez.")
            user_operation = input("Mi hermano, Pick an operation: '+','-','*' or '/'")
        else:
            is_operation = True
            display_operator = str(user_number) + " " + user_operation
            os.system('cls' if os.name == 'nt' else 'clear')
            print(display_calculator(display_operator))
            return user_operation

def user_next_number(number,operator):
    is_number = False
    while not is_number:
        try:
            next_number = float(input("What is the next number, panita?\n"))
            is_zero=False
            while not is_zero:
                if next_number ==0 and operator=="/":
                    print("🚫 Can't divide by zero, amigo. Try another number.")
                    next_number = float(input("What is the next number, panita?\n"))
                else:
                    is_zero = True
            os.system('cls' if os.name == 'nt' else 'clear')
            display_operator = str(number) + " " + operator + " " + str(next_number)
            print(display_calculator(display_operator))
            return next_number
        except ValueError:
            print("❌ Amigo! that's not a valid number. Try again!")

def calculator_result(number1,number2,operator):
    operators = ['+', '-', '*', '/']
    for char in operators:
        if operator == char:
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            result = round(calculator_operations(number1, number2, operator),2)
            display_operator = "=" + str(result)
            print(display_calculator(display_operator))
    return result