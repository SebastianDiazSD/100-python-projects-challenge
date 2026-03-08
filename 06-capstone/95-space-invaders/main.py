from turtle import Screen
import time
from player import Player
from alien import AlienManager
from bullet import Bullet
from barrier import BarrierManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invaders - Colombian Edition 🇨🇴")
screen.tracer(0)

player = Player()
aliens = AlienManager()
bullet = Bullet()
barriers = BarrierManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(lambda: bullet.fire(player.position()), "space")

game_on = True

while game_on:
    time.sleep(0.02)
    screen.update()

    aliens.move()

    # bullet movement
    bullet.move()

    # collision with alien
    for alien in aliens.aliens:
        if bullet.distance(alien) < 20:
            alien.hideturtle()
            aliens.aliens.remove(alien)
            bullet.reset_position()
            scoreboard.increase_score()

    # collision with barriers
    for block in barriers.blocks:
        if bullet.distance(block) < 15:
            block.hideturtle()
            barriers.blocks.remove(block)
            bullet.reset_position()

    # aliens reaching player
    for alien in aliens.aliens:
        if alien.ycor() < -250:
            scoreboard.game_over()
            game_on = False

screen.mainloop()