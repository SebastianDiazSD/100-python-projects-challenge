from turtle import *

# Basic settings — the rhythm of movement and directions

STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# --- Load and Register Dog Image ---
dog_image = "dante.gif"
register_shape(dog_image)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(dog_image)
        self.setheading(90)
        self.goto(STARTING_POS)

    def move_dog_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_dog_down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def initial_pos(self):
        self.goto(STARTING_POS)

    def next_level(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POS)
            return True
        else:
            return False
