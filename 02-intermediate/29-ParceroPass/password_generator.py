from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    is_new = messagebox.askokcancel(title="New Password",
                                    message=f"Do you want to generate a new password?")

    if is_new is True:
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(1, 3)
        nr_numbers = random.randint(1, 3)
        password_letters = [random.choice(LETTERS) for _ in range(nr_letters)]
        password_symbols = [random.choice(SYMBOLS) for _ in range(nr_symbols)]
        password_numbers = [random.choice(NUMBERS) for _ in range(nr_numbers)]
        password_list = password_letters + password_symbols + password_numbers
        random.shuffle(password_list)

        password = "".join(password_list)

        new_password = password
        password_entry.delete(0, END)
        password_entry.insert(END, new_password)
        pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email,
                          "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                # email_entry.delete(0,END)

# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"Data file was not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("ParceroPass 🇨🇴")  # Updated title
window.config(padx=50, pady=50, bg="#fdf6e3")  # Softer background

# Canvas with Colombian-style logo
canvas = Canvas(height=200, width=200, bg="#fdf6e3", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")  # Replace with Colombian-themed image
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels (Font: bold, Colors: themed)
label_font = ("Helvetica", 11, "bold")

website_label = Label(text="Website:", font=label_font, bg="#fdf6e3", fg="#0033A0")  # Blue
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font=label_font, bg="#fdf6e3", fg="#FCD116")  # Yellow
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=label_font, bg="#fdf6e3", fg="#CE1126")  # Red
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sebas@bogota.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, bg="#FCD116", fg="black")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save, bg="#0033A0", fg="white")
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search_website, bg="#CE1126", fg="white")
search_button.grid(row=1, column=2)

window.mainloop()
