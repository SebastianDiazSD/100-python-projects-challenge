from turtle import *

# Read the high score from the file (gotta keep track of legends)
with open("data.txt", mode="r") as file:
    HIGH_SCORE = file.read()


class Scoreboard(Turtle):
    """Shows the score and messages on screen — very important for bragging rights"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(HIGH_SCORE)
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score = {self.score}  High Score: {self.high_score}",
            False, align="center", font=("Courier", 20, "normal")
        )

    def increase_score(self):
        # Add one point and refresh display
        self.score += 1
        self.update_score()

    def reset(self):
        # Save new high score if it’s higher than before
        self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as HIGH_SCORE:
            HIGH_SCORE.write(str(self.high_score))
        self.update_score()

    def game_over(self):
        # Show game over message — lo siento, hermano
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Courier", 20, "normal"))
