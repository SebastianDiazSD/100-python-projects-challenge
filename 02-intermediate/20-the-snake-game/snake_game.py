from turtle import *
from snake_class import *
from snake_food import *
from scoreboard import *
import random
import time

# --- Welcome to "Chasing the Prey! Die Schlange" ---
# This is the main control file where all the action happens.
# Think of this as the DJ booth — it controls the whole fiesta

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Chasing the prey! Die Schlange")

# Ask our player for the difficulty level (a little Colombian style 😉)
difficulty = screen.textinput(title="Game difficulty", prompt="Easy or Hard?").lower()
screen.tracer(0)

# Create scoreboard, snake, and food — the main party guests!
score = Scoreboard()
dante = Snake()        # Dante — our fearless snake
food = Food()
dante_speed = 0.1      # Initial speed of the game

# Keyboard controls (WASD — classic gamer style)
screen.listen()
screen.onkey(key="w", fun=dante.move_north)
screen.onkey(key="s", fun=dante.move_south)
screen.onkey(key="d", fun=dante.move_east)
screen.onkey(key="a", fun=dante.move_west)

# Main game loop — it keeps running until the party ends
game_on = True

while game_on:
    screen.update()
    time.sleep(dante_speed)
    dante.move_snake()

    # If our snake eats the food
    if dante.snake_head.distance(food) < 15:
        food.new_location(dante)
        score.increase_score()
        dante.bigger_body()
        dante_speed *= 0.99   # Speed up a little with every bite (más picante)

    # Collision with own body
    for segments in dante.snake_body:
        if segments == dante.snake_head:
            continue
        elif dante.snake_head.distance(segments) < 10:
            if score.score > score.high_score:
                score.reset()
                dante.reset_snake()
            else:
                score.game_over()
                game_on = False

    # Boundary logic — wrapping (easy) or death (hard)
    if difficulty == "easy":
        if dante.snake_body[0].xcor() < -290:
            dante.snake_body[0].goto(300, dante.snake_body[0].ycor())
        elif dante.snake_body[0].xcor() > 290:
            dante.snake_body[0].goto(-300, dante.snake_body[0].ycor())
        elif dante.snake_body[0].ycor() > 290:
            dante.snake_body[0].goto(dante.snake_body[0].xcor(), -300)
        elif dante.snake_body[0].ycor() < -290:
            dante.snake_body[0].goto(dante.snake_body[0].xcor(), 300)
    else:
        if dante.snake_body[0].xcor() < -290:
            score.game_over()
            game_on = False
        elif dante.snake_body[0].xcor() > 290:
            score.game_over()
            game_on = False
        elif dante.snake_body[0].ycor() > 290:
            score.game_over()
            game_on = False
        elif dante.snake_body[0].ycor() < -290:
            score.game_over()
            game_on = False

# Click to exit — tranquilo, hermano 😎
screen.exitonclick()
