from turtle import *

# --- Constants for paddle settings ---
PACE = 20        # Step size for each movement
UP = 90          # Not directly used, but for clarity of direction
DOWN = 270       # Same as above


class Paddle(Turtle):
    """Represents a player paddle in the Colombian Pong game 🇨🇴.
    It can move up or down, either controlled by the player or the computer.
    """

    def __init__(self, position):
        """Initialize the paddle at a given position (left or right side)."""
        super().__init__()
        self.shape("square")
        self.color("white")
        # Stretch the default square to look like a vertical paddle
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)  # position should be a tuple, e.g., (350, 0)

    def move_north(self):
        """Move the paddle upward by a fixed distance."""
        new_y = self.ycor() + PACE
        if new_y < 250:  # Prevent going beyond the top border
            self.goto(self.xcor(), new_y)
        # ¡Vamos pa'rriba! No se salga de la cancha.

    def move_south(self):
        """Move the paddle downward by a fixed distance."""
        new_y = self.ycor() - PACE
        if new_y > -250:  # Prevent going below the bottom border
            self.goto(self.xcor(), new_y)
        # Bajando con estilo, tranqui que aún hay tiempo.

    def auto_move(self):
        """Optional: placeholder for AI movement logic if needed."""
        pass
        # Could be used in single-player mode to make the paddle follow the ball.
