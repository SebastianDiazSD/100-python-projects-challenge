import random
import pyperclip
import tkinter  # <-- Add this import to use tkinter features

from tkinter import messagebox  # Also importing messagebox to use it directly

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator(input_password, letters, symbols, numbers):
    # Show message asking the user if they want to generate a new password
    is_new = messagebox.askokcancel(title="Generate Password",
                                     message="Do you want to create a new password? (¡Hazlo con confianza!)")

    if is_new:
        # Define the number of letters, symbols, and numbers
        nr_letters = random.randint(8, 10)  # Adjust letter count
        nr_symbols = random.randint(1, 3)   # Adjust symbol count
        nr_numbers = random.randint(1, 3)   # Adjust number count

        # Generate random choices for each category
        password_letters = [random.choice(letters) for _ in range(nr_letters)]
        password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
        password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

        # Combine all the elements into one list
        password_list = password_letters + password_symbols + password_numbers

        # Shuffle the list to make the password more random
        random.shuffle(password_list)

        # Convert list to string and update the password field
        password = "".join(password_list)

        # Show the password and copy it to clipboard
        input_password.delete(0, tkinter.END)
        input_password.insert(tkinter.END, password)
        pyperclip.copy(password)  # Copy the password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_information(input_website, input_user, input_password):
    website = input_website.get()
    username = input_user.get()
    password = input_password.get()

    if website == "" or password == "" or username == "" or website == "Type the website related to your user" or username == "Write your user here! Tu usuario papa!":
        messagebox.showinfo(title="Missing Info", message="Please make sure you have not left any fields empty. ¡No se te olvide nada!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail: {username}\nPassword: {password}\n¡Listo para guardar?")
        if is_ok:
            with open("my_passwords.txt", mode="a") as password_file:
                password_file.write(f"{website} | {username} | {password}\n")
                # Clear the input fields after saving
                input_website.delete(0, tkinter.END)
                input_user.delete(0, tkinter.END)
                input_password.delete(0, tkinter.END)
