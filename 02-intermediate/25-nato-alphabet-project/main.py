student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dict_coded = {"student": [],
                      "score": []}

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# import pandas
# # from tkinter import messagebox
# from turtle import *
#
# import CodedName as cdn
#
# student_data_frame = pandas.DataFrame(student_dict)
# nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# coded = cdn.CodedName()
#
# # --- Setup screen ---
# screen = Screen()
# screen.bgcolor("white")
# screen.title("Can you guess them all?")
# colormode(255)
# screen.tracer(0)
#
# # --- Ask the user for country selection ---
# user_name = screen.textinput(
#     title="Tu nombre!",
#     prompt="What's your name, panita?"
# )
#
# # for student in student_data_frame["student"]:
# #     for letter in student:
# #         print(letter.upper())
# #         if (nato_df["letter"] == letter.upper()).any():
# #             letter_coded = nato_df[nato_df["letter"] == letter.upper()].iloc[0]
# #             letter_coded = letter_coded["code"]
# #             coded.append(letter_coded)
#
# for letter in user_name:
#     upper_letter = letter.upper()
#     if (nato_df["letter"] == upper_letter).any():
#         letter_coded = nato_df[nato_df["letter"] == letter.upper()].iloc[0]["code"]
#         coded.write_name(letter_coded)
#
# screen.exitonclick()

# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# # TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for number in list_of_strings]
result = [number for number in numbers if number%2==0]
print(result)