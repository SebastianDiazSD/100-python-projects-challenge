from turtle import Turtle

START_X = -300
START_Y = 220

class Alien(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(x, y)


class AlienManager:

    def __init__(self):
        self.aliens = []
        self.move_direction = 1
        self.create_fleet()

    def create_fleet(self):
        for row in range(4):
            for col in range(8):
                alien = Alien(START_X + col * 70, START_Y - row * 50)
                self.aliens.append(alien)

    def move(self):
        edge_hit = False

        for alien in self.aliens:
            alien.forward(1.5 * self.move_direction)

            if alien.xcor() > 360 or alien.xcor() < -360:
                edge_hit = True

        if edge_hit:
            self.move_direction *= -1
            for alien in self.aliens:
                alien.sety(alien.ycor() - 30)