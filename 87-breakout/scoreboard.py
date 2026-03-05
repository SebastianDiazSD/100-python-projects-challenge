from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Breakout Bogotá 🇨🇴",
                   align="center", font=("Courier", 16, "normal"))

    def add_point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER - Gracias por jugar!",
                   align="center", font=("Courier", 20, "bold"))