from turtle import Turtle

class Ball(Turtle):

    MAX_SPEED = 0.01  # fastest allowed speed (lower = faster in turtle)

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.dx = 4
        self.dy = 4

        self.move_speed = 0.03
        self.speed_multiplier = 0.95  # speed increase factor

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def increase_speed(self):
        """Increase difficulty each time paddle is hit."""
        if self.move_speed * self.speed_multiplier > self.MAX_SPEED:
            self.move_speed *= self.speed_multiplier