from turtle import *
from ball_class import *
from scoreboard import *
from paddle_class import *
import time
import sys
import random  # 👈 for AI randomness

# --- Setup de la pantalla ---
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG - Colombian Edition 🇨🇴")
screen.tracer(0)

# --- Ask the user for mode selection ---
mode = screen.textinput(
    title="PONG Setup 🇨🇴",
    prompt="How do you want to play?\nType '1' for single player (vs computer)\nor '2' for two players:"
)

if mode not in ["1", "2"]:
    mode = "1"

# --- Optional difficulty setup for single-player mode ---
difficulty = "medium"
if mode == "1":
    difficulty = screen.textinput(
        title="Choose difficulty 💪",
        prompt="Select difficulty:\n'easy', 'medium', or 'hard':"
    )
    if difficulty not in ["easy", "medium", "hard"]:
        difficulty = "medium"

# --- Create game elements ---
score = Scoreboard()
play_ball = Ball()
dante = Paddle((350, 0))       # right paddle (Player 1)
orion = Paddle((-350, 0))      # left paddle (AI or Player 2)

# --- Keyboard controls ---
screen.listen()
screen.onkey(key="Up", fun=dante.move_north)
screen.onkey(key="Down", fun=dante.move_south)

if mode == "2":
    # Two-player mode: both sides controlled by humans
    screen.onkey(key="w", fun=orion.move_north)
    screen.onkey(key="s", fun=orion.move_south)

# --- AI difficulty settings ---
if mode == "1":
    if difficulty == "easy":
        ai_speed = 10      # slow paddle
        ai_error = 40      # big random error margin
    elif difficulty == "hard":
        ai_speed = 22      # fast paddle
        ai_error = 5       # small random miss chance
    else:  # medium
        ai_speed = 16
        ai_error = 20

ai_target_y = 0

# --- Main game loop ---
game_on = True
while game_on:
    screen.update()
    time.sleep(play_ball.move_speed)
    play_ball.move()

    # --- Collision: Ball hits top or bottom walls ---
    if play_ball.ycor() > 280 or play_ball.ycor() < -280:
        play_ball.bounce()

    # --- Right wall: point for left player ---
    if play_ball.xcor() > 380:
        play_ball.goto(0, 0)
        play_ball.reset_ball()
        score.increase_score_left()
        play_ball.move_speed = 0.1

    # --- Left wall: point for right player ---
    if play_ball.xcor() < -380:
        play_ball.goto(0, 0)
        play_ball.reset_ball()
        score.increase_score_right()
        play_ball.move_speed = 0.1

    # --- Collision: Ball hits paddle ---
    if (play_ball.distance(dante) < 50 and play_ball.xcor() > 320) or (
        play_ball.distance(orion) < 50 and play_ball.xcor() < -320):
        play_ball.bounce_paddle()

    # --- AI Paddle movement for 1-player mode ---
    if mode == "1":
        # Only update AI's target position occasionally to avoid jitter
        if random.random() < 0.1:  # 10% chance each frame to adjust target
            ai_target_y = play_ball.ycor() + random.randint(-ai_error, ai_error)

        # Smooth follow: move slightly toward target position
        if orion.ycor() < ai_target_y:
            orion.sety(orion.ycor() + ai_speed * 0.3)
        elif orion.ycor() > ai_target_y:
            orion.sety(orion.ycor() - ai_speed * 0.3)

        # Keep AI paddle within bounds
        if orion.ycor() > 250:
            orion.sety(250)
        elif orion.ycor() < -250:
            orion.sety(-250)

    # --- Game Over Condition ---
    if score.score_left >= 10 or score.score_right >= 10:
        game_on = False
        score.game_over()

screen.exitonclick()