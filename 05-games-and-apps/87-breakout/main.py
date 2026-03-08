"""
Project 87 - Breakout 🇨🇴
Part of the 100 Python Projects Challenge

Inspired by the classic Breakout originally coded by Steve Wozniak.
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout 87 - Bogotá Edition 🇨🇴")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

bricks = []

colors = ["yellow", "orange", "red", "green"]

# Create brick wall
for row in range(5):
    for col in range(10):
        brick = Brick(-350 + col * 70, 250 - row * 30, colors[row % len(colors)])
        bricks.append(brick)

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Wall collision
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    # Paddle collision
    if ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.bounce_y()
        ball.increase_speed()

    # Brick collision
    for brick in bricks:
        if ball.distance(brick) < 35:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce_y()
            scoreboard.add_point()

    # Bottom collision
    if ball.ycor() < -290:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()