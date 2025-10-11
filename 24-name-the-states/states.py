from turtle import *

class StateName(Turtle):
    """
    A Turtle subclass for writing state names at given coordinates.
    """
    def __init__(self):
        super().__init__()
        self.state_name = ""
        self.penup()
        self.hideturtle()  # Don't show the turtle cursor
        self.pos_x = 0
        self.pos_y = 0

    def move(self, position):
        """
        Move turtle to given (x, y) position.
        """
        self.pos_x, self.pos_y = position
        self.goto(self.pos_x, self.pos_y)

    def set_name(self, correct_name):
        """
        Write the state name at the current position.
        """
        self.state_name = correct_name
        self.write(self.state_name, align="center", font=("Arial", 10, "normal"))
