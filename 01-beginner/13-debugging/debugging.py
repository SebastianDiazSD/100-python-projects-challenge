############DEBUGGING#####################

# Describe Problem (Original/Incorrect Code)
def my_function():
    for i in range(1, 20):  # Loop stops before reaching 20
        if i == 20:
            print("You got it")


my_function()


# Correct Version:
def my_function():
    # Loop goes from 1 to 20, so it includes 20.
    for i in range(1, 21):
        if i == 20:
            print("You got it!")  # Corrected the message for a more Colombian touch.


my_function()

# Reproduce the Bug (Original/Incorrect Code)
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)  # The index should be from 0 to 5, not 1 to 6.
print(dice_imgs[dice_num])

# Correct Version:
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # Corrected index range to 0-5
print(f"You got: {dice_imgs[dice_num]}")  # Added user-friendly output

# Play Computer (Original/Incorrect Code)
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:  # This range is exclusive of 1980 and 1994. Not ideal.
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# Correct Version:
year = int(input("What's your year of birth?"))
if year >= 1980 and year <= 1994:  # Adjusted range to include both 1980 and 1994.
    print("You are a millenial! 🎉")
elif year > 1994:
    print("You are a Gen Z! 🌟")

# Fix the Errors (Original/Incorrect Code)
age = input("How old are you?")  # Input is a string, but we need an integer comparison.
if age > 18:  # age is a string, so this comparison will throw an error.
    print(f"You can drive at age {age}.")

# Correct Version:
age = int(input("How old are you"))  # Corrected input conversion to int.
if age >= 18:  # Corrected comparison with integer.
    print(f"You can drive at age {age}!")


# Print is Your Friend (Original/Incorrect Code)
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))  # Correct input, but the next line has an error.
word_per_page == int(input("Number of words per page: "))  # Comparison instead of assignment.
total_words = pages * word_per_page
print(total_words)

# Correct Version:
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page  # Correct calculation.
print(f"The number of total words is: {total_words}")  # Added clear print statement.


# Use a Debugger (Original/Incorrect Code)
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2  # Doubling each item, but b_list.append() was outside of loop.
    b_list.append(new_item)  # This only appends the last item, not the whole list.
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# Correct Version:
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2  # Double each item.
        b_list.append(new_item)  # Append within the loop to keep all items.
    print(f"Modified list: {b_list}")


mutate([1, 2, 3, 5, 8, 13])  # Now it prints the entire modified list.
