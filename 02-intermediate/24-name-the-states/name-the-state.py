import pandas
from tkinter import messagebox
from turtle import *

import states

# --- Setup screen ---
screen = Screen()
screen.bgcolor("white")
screen.title("Can you guess them all?")
colormode(255)
screen.tracer(0)

# --- Ask the user for country selection ---
mode = screen.textinput(
    title="Country Selection",
    prompt="¿Cómo quieres jugar?\nType '1' for Colombia 🇨🇴\nType '2' for the USA 🇺🇸"
)

if mode not in ["1", "2"]:
    mode = "1"

# --- Create game elements ---
state = states.StateName()      # Turtle object to write state names on the map
guessed_states = []             # List to keep track of correct guesses
user_attempts = 5               # Number of allowed wrong guesses

# --- Colombia mode ---
if mode == "1":
    screen.bgpic("map_col.gif")
    screen.screensize(canvwidth=600, canvheight=600)
    df = pandas.read_csv('32_states_col.csv', encoding='latin1')

    game_is_on = True
    while game_is_on:
        user_guess = screen.textinput(
            title="Guess the State 🇨🇴",
            prompt="Type the name of a Colombian state:"
        )
        if not user_guess:
            continue
        user_guess = user_guess.lower()

        # Prevent duplicate guesses
        while user_guess in guessed_states:
            user_guess = screen.textinput(
                title="Already Guessed",
                prompt="Parcero, ya dijiste ese estado.\n\nTry another one:"
            )
            if not user_guess:
                continue
            user_guess = user_guess.lower()

        # Check if guess is correct
        if (df['state'].str.lower() == user_guess).any():
            row = df[df['state'].str.lower() == user_guess].iloc[0]
            state.move((row['x'], row['y']))
            state.set_name(row['state'])
            guessed_states.append(user_guess)

            messagebox.showinfo("¡Nail it!",
                                f"Parceee! You got it!\n\n"
                                f"{len(guessed_states)} / {len(df)} states guessed")

            if len(guessed_states) == len(df):
                messagebox.showinfo("You did it!",
                                    "¡Viejito! You guessed all Colombian states!\n\n"
                                    "You are officially un Colombiano de verdad 🇨🇴")
                game_is_on = False
                screen.exitonclick()

        else:
            user_attempts -= 1
            if user_attempts == 0:
                messagebox.showinfo("Paila...",
                                    "Se acabó, parcero. No more attempts left.\n"
                                    "Better luck next time!")
                game_is_on = False
                screen.bye()
            else:
                messagebox.showinfo("Wrong!",
                                    f"Pana, that’s not a state in Colombia.\n"
                                    f"You have {user_attempts} attempts left.")

# --- USA mode ---
else:
    screen.bgpic("blank_states_img.gif")
    screen.screensize(canvwidth=600, canvheight=600)
    df = pandas.read_csv('50_states_usa.csv')

    game_is_on = True
    while game_is_on:
        user_guess = screen.textinput(
            title="Guess the State 🇺🇸",
            prompt="Type the name of a U.S. state:"
        )
        if not user_guess:
            continue
        user_guess = user_guess.lower()

        while user_guess in guessed_states:
            user_guess = screen.textinput(
                title="Already Guessed",
                prompt="You already guessed that one!\n\nTry another U.S. state:"
            )
            if not user_guess:
                continue
            user_guess = user_guess.lower()

        if (df['state'].str.lower() == user_guess).any():
            row = df[df['state'].str.lower() == user_guess].iloc[0]
            state.move((row['x'], row['y']))
            state.set_name(row['state'])
            guessed_states.append(user_guess)

            messagebox.showinfo("Nice!",
                                f"You got one!\n\n"
                                f"{len(guessed_states)} / {len(df)} states guessed")

            if len(guessed_states) == len(df):
                messagebox.showinfo("You did it!",
                                    "You guessed all U.S. states!\n\n"
                                    "You are officially an American 🇺🇸")
                game_is_on = False
                screen.exitonclick()

        else:
            user_attempts -= 1
            if user_attempts == 0:
                messagebox.showinfo("Game Over",
                                    "You ran out of attempts. Better luck next time!")
                game_is_on = False
                screen.bye()
            else:
                messagebox.showinfo("Wrong!",
                                    f"That’s not a U.S. state!\n"
                                    f"You have {user_attempts} attempts left.")