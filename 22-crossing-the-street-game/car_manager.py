import random
from turtle import *

COLOR = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for i in range (100)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
colormode(255)


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.shape("square")
            new_car.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def reset_speed(self):
        self.car_speed = STARTING_MOVE_DISTANCE

    def clear_cars(self):
        """Clears all cars from the screen and resets the car list."""
        for car in self.all_cars:
            car.hideturtle()  # Hides the car (you can also use car.clear() to erase its trail)
        self.all_cars.clear()  # Clears the list of cars

