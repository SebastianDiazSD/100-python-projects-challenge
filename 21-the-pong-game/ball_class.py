from turtle import *

# Constants for movement and direction
POSITION_RIGHT = (350, 0)
POSITION_LEFT = (-350, 0)
PACE = 20
UP = 90
DOWN = 270


class Ball(Turtle):
    """Represents the ball in our Pong game.
    It moves, bounces, and speeds up when hit by paddles.
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # smaller = faster

    def move(self):
        """Move the ball by updating its coordinates."""
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        """Reverse vertical direction when hitting top/bottom walls."""
        self.y_move *= -1
        # ¡Rebotó! The ball changed its vertical direction.

    def bounce_paddle(self):
        """Reverse horizontal direction and slightly speed up."""
        self.x_move *= -1
        self.move_speed *= 0.9  # make it faster each hit
        # That’s how we turn up the heat — ¡esto se puso bueno!

    def reset_ball(self):
        """Reset ball to the center and reverse direction."""
        self.y_move *= -1
        self.x_move *= -1
        self.move()
        # New round, ready to roll again.