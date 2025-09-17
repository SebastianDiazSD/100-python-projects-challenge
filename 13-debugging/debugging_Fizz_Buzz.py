# Original/Incorrect Version
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:  # "and" instead of "or" (the number is divisible by both 3 and 5)
            print("FizzBuzz")
        if number % 3 == 0:  # Incorrect use of conditional. It must be if...elif...else statement
            print("Fizz")
        if number % 5 == 0:  # Incorrect use of conditional. It must be if...elif...else statement
            print("Buzz")
        else:
            print([number])  # The program should print the number not a list containing the number.


def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:  # "and" instead of "or" (the number is divisible by both 3 and 5)
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
