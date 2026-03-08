from turtle import Turtle

MOVE_DISTANCE = 25

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("yellow")  # Colombian flag inspiration
        self.penup()
        self.setheading(90)
        self.goto(0, -270)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        if new_x > -370:
            self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        if new_x < 370:
            self.goto(new_x, self.ycor())