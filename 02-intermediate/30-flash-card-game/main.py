import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
import os

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIME_MS = 3000  # 3 seconds

# ---------------------------- GLOBALS ------------------------------- #
current_card = {}
to_learn = {}

# ---------------------------- LOAD DATA ------------------------------- #
def load_data():
    """Load the list of words to learn, or fallback to original dataset."""
    global to_learn
    try:
        data = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        original_data = pd.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
    else:
        to_learn = data.to_dict(orient="records")

# ---------------------------- NEXT CARD ------------------------------- #
def next_card():
    """Show the next flash card with a French word."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(FLIP_TIME_MS, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    """Flip the flashcard to show the English translation."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- WORD KNOWN ------------------------------- #
def is_known():
    """Remove known word from list and show the next card."""
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_TIME_MS, func=flip_card)

# Canvas setup
canvas = tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Loading...", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Button setup
right_img = tk.PhotoImage(file="images/right.png")
wrong_img = tk.PhotoImage(file="images/wrong.png")

right_button = tk.Button(image=right_img, highlightthickness=0, command=is_known)
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

# Start the app
load_data()
next_card()
window.mainloop()
