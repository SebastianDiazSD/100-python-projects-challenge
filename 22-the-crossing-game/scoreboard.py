from turtle import *
from tkinter import messagebox

FONT=("Courier",24,"normal")

# Read the high score from the file (gotta keep track of legends)
with open("data.txt", mode="r") as file:
    HIGH_SCORE = file.read()

class Scoreboard(Turtle):
    """Handles the game score display and 'Game Over' message."""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("black")
        self.high_score = int(HIGH_SCORE)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Draws the updated score on the screen."""
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level: {self.score}\nHigh Score: {self.high_score}", False, align="right", font=FONT)

    def increase_score(self):
        """Adds one point to the right player and refreshes display."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays the Game Over message at center."""
        self.goto(0, 0)
        messagebox.showinfo("Oh no!",
                            f"\n\nYou got hit!\n\n"
                            f"You have reached level:\n\n{self.score}")
        # Fin del juego!

    def reset(self):
        # Save new high score if it’s higher than before
        self.high_score = max(self.score, self.high_score)
        self.score = 0
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.update_scoreboard()
