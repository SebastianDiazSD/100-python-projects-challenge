from turtle import *

# Basic settings — the rhythm of movement and directions
PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    """Class to control Dante — our proud Colombian snake"""

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        # Start the snake with three segments — the OG squad
        for position in POSITION:
            self.add_segment(position)

    def move_snake(self):
        # Each segment follows the one before it — teamwork, parce!
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_head.forward(PACE)

    # 🎮 Direction controls — only valid if not going opposite
    def move_north(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_south(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_east(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_west(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def add_segment(self, position):
        # Add a new body segment
        segment = Turtle()
        segment.pencolor("white")
        segment.color("white")
        segment.shape("square")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def bigger_body(self):
        # When Dante eats, he grows — stronger and longer
        for _ in range(3):
            self.add_segment(self.snake_body[-1].position())

    def reset_snake(self):
        # Send all segments off-screen and restart
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.snake_head = self.snake_body[0]
