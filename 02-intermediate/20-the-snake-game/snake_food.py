from turtle import *
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        colormode(255)
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed("fastest")
        self.food_location()

    def food_location(self):
        # Place the food randomly within the game area
        x_dot = random.uniform(-290, 290)
        y_dot = random.uniform(-290, 290)
        self.setpos(x_dot, y_dot)

    def new_location(self, hunter):
        # When the snake eats it, move it to a new random spot
        new_x_dot = random.uniform(-290, 290)
        new_y_dot = random.uniform(-290, 290)
        self.penup()
        self.setpos(new_x_dot, new_y_dot)