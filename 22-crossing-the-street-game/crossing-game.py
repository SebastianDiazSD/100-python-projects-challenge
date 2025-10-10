import time
from turtle import *

import car_manager
import player
import scoreboard
from tkinter import messagebox

# --- Setup screen ---
screen = Screen()
screen.bgcolor("white")
screen.title("Watch out my boy! Crossing to Victory! 🐾")
screen.screensize(canvwidth=600, canvheight=600)
colormode(255)
screen.tracer(0)

# --- Create game elements ---
dante = player.Player()
cars = car_manager.CarManager()
score = scoreboard.Scoreboard()
time_speed = 0.1

# --- Keyboard controls ---
def bind_keys():
    """Bind the keys to player movement."""
    screen.listen()
    screen.onkey(key="Up", fun=dante.move_dog_up)
    screen.onkey(key="Down", fun=dante.move_dog_down)

bind_keys()  # Bind the keys when the game starts

# --- Game on ---
game_is_on = True

while game_is_on:
    time.sleep(time_speed)
    screen.update()
    cars.create_car()
    cars.move_car()

    # Collision
    for car in cars.all_cars:
        if car.distance(dante) < 20:
            score.game_over()
            user_choice = screen.textinput(title="Another try?",
                                           prompt=f"Do you want to play again, parcero?"
                                                  f"\n[1] for Yes, [2] for No")
            if user_choice == "1":
                score.reset()
                cars.reset_speed()
                dante.initial_pos()
                cars.clear_cars()
                bind_keys()
                game_is_on = True
            else:
                messagebox.showinfo("Game Over!",
                                    f"\n\nSee you next time pana!")
                screen.bye()  # Close the window when the user decides not to play again
                game_is_on = False

    # Next level
    if dante.next_level() is True:
        score.increase_score()
        cars.increase_speed()
        time_speed *= 0.95
