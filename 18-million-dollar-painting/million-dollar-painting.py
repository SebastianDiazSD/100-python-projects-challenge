import random
from turtle import *
from colorgram import extract

# Setup the screen
screen = Screen()
screen.bgcolor("white")  # Set background color
screen.screensize(600,600)
screen.setup (width=1700, height=800, startx=0, starty=0)

# Define turtle objects with dog names
dante = Turtle()  # Dante the dog 🐕
kira = Turtle()  # Kira the dog 🐶


# Set turtle shapes and speeds
dante.shape("classic")
kira.shape("circle")

dante.speed("fastest")
kira.speed("fastest")

dante.hideturtle()
kira.hideturtle()

# Load color palette from an image (100 colors)
colors = extract('colors.png', 100)
colormode(255)

# Initial positions for each turtle (dog)
dante.penup()
dante.setpos(-600, -300)
dante.pendown()

kira.penup()
kira.setpos(100, -300)
kira.pendown()

# Function to draw a row of dots
def draw_row_of_dots(turtle, dot_count=14, dot_size=20, spacing=50):
    """
    Draw a row of dots with random colors.
    The turtle will place dots and move forward by a fixed spacing.
    """
    for _ in range(dot_count):
        turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.dot(dot_size)
        turtle.penup()
        turtle.forward(spacing)


# Function to position and draw multiple rows of dots
def draw_dot_pattern(turtle1, turtle2, rows=13, gap=50):
    """
    Draw rows of dots with two turtles, alternating rows between them.
    """
    for y in range(rows):
        draw_row_of_dots(turtle1)
        draw_row_of_dots(turtle2)

        # Move turtles to the next row
        turtle1.penup()
        turtle1.setpos(-600, -300 + gap)
        turtle1.pendown()

        turtle2.penup()
        turtle2.setpos(100, -300 + gap)
        turtle2.pendown()

        gap += 50  # Increase the gap for the next row


# Draw the pattern with turtles 'dante' and 'kira'
draw_dot_pattern(dante, kira)

screen.window_height()
screen.window_width()

# Wait for the user to click to exit
screen.exitonclick()
