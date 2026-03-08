from turtle import Turtle

class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")  # Colombian blue
        self.shapesize(stretch_wid=0.4, stretch_len=1.2)
        self.penup()
        self.goto(0, -400)
        self.speed = 20
        self.active = False

    def fire(self, position):
        if not self.active:
            self.goto(position)
            self.setheading(90)
            self.active = True

    def move(self):
        if self.active:
            self.forward(self.speed)

            if self.ycor() > 300:
                self.reset_position()

    def reset_position(self):
        self.goto(0, -400)
        self.active = False