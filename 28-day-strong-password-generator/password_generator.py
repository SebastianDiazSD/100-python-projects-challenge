import tkinter
from helpers import *
import random

# Constants for password generation
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import END, messagebox

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas (image)
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_image = tkinter.PhotoImage(file="logo.png")  # Replace this path with your logo path
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
text_website = tkinter.Label(text="Website:")
text_website.grid(row=1, column=0)
text_user = tkinter.Label(text="Email/Username:")
text_user.grid(row=2, column=0)
text_password = tkinter.Label(text="Password:")
text_password.grid(row=3, column=0)

# Entries
input_website = tkinter.Entry(width=52)
input_website.insert(tkinter.END, "Type the website related to your user")
input_website.grid(row=1, column=1, columnspan=2)
input_user = tkinter.Entry(width=52)
input_user.insert(tkinter.END, "Write your user here! Tu usuario papa!")
input_user.grid(row=2, column=1, columnspan=2)
input_password = tkinter.Entry(width=33)
input_password.grid(row=3, column=1)

# Buttons
button_password = tkinter.Button(text="Generate Password", command=lambda: password_generator(input_password, LETTERS, NUMBERS, SYMBOLS))
button_password.grid(row=3, column=2)
button_add = tkinter.Button(text="Add", width=44, command=lambda: add_information(input_website, input_user, input_password))
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
