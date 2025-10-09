from turtle import *

class Scoreboard(Turtle):
    """Handles the game score display and 'Game Over' message."""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score_right = 0
        self.score_left = 0
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        """Draws the updated score on the screen."""
        self.clear()
        self.goto(100, 200)
        self.write(self.score_right, False, align="center", font=("Courier", 20, "normal"))
        self.goto(-100, 200)
        self.write(self.score_left, False, align="center", font=("Courier", 20, "normal"))

    def increase_score_right(self):
        """Adds one point to the right player and refreshes display."""
        self.score_right += 1
        self.update_scoreboard()

    def increase_score_left(self):
        """Adds one point to the left player and refreshes display."""
        self.score_left += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays the Game Over message at center."""
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Courier", 20, "normal"))
        # Fin del partido — both players gave it all, ¡qué juego tan bacano!
