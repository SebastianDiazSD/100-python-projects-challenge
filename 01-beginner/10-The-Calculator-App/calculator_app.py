from art import logo, welcoming_message
import operations


print(logo)
print(welcoming_message)

user_first_number = operations.first_number()

operation_user = operations.user_operation(user_first_number)

user_next = operations.user_next_number(user_first_number, operation_user)

calc_result = operations.calculator_result(user_first_number, user_next, operation_user)

print(f"The result of the operation {user_first_number} {operation_user} {user_next} = {calc_result}")
new_calculation = input("Papi, What do you want to do?"
                        "\n(1) - Start a new calculation"
                        "\n(2) - Continue calculating with previous result\n(3) - Do something more fun! Exit\n")

keep_calculator = True
while keep_calculator:
    if new_calculation not in ["1", "2", "3"]:
        new_calculation = input("Papi, Just type 1, 2 or 3!!")
    elif new_calculation == "1":
        user_first_number = operations.first_number()
        operation_user = operations.user_operation(user_first_number)
        user_next = operations.user_next_number(user_first_number, operation_user)
        calc_result = operations.calculator_result(user_first_number, user_next, operation_user)
        print(f"The result of the operation {user_first_number} {operation_user} {user_next} = {calc_result}")
        new_calculation = input("Papi, What do you want to do?"
                                "\n(1) - Start a new calculation"
                                "\n(2) - Continue calculating with previous result\n(3) - Do something more fun! Exit\n")
    elif new_calculation == "2":
        previous_result = calc_result
        operation_user = operations.user_operation(previous_result)
        user_next = operations.user_next_number(previous_result, operation_user)
        calc_result = operations.calculator_result(previous_result, user_next, operation_user)
        print(f"The result of the operation {previous_result} {operation_user} {user_next} = {calc_result}")
        new_calculation = input("Papi, What do you want to do?"
                                "\n(1) - Start a new calculation"
                                "\n(2) - Continue calculating with previous result\n(3) - Do something more fun! Exit\n")
    else:
        print("👋 Gracias for using the calculator. ¡Nos vemos, papi! ")
        keep_calculator = False