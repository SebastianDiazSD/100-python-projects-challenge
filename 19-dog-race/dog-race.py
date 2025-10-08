import turtle
import random
from tkinter import messagebox

# --- Setup screen ---
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Who's the fastest good boy?? Make your bet! 🐾")
screen.setup(width=1000, height=800)
turtle.colormode(255)

# --- Load and Register Dog Image ---
dog_image = ["dante.gif", "kira.gif", "orion.gif", "cimarron.gif",
             "dog_5.gif", "dog_6.gif", "dog_7.gif", "dog_8.gif", "dog_9.gif", "dog_10.gif"]

for dog in dog_image:
    turtle.register_shape(dog)

# --- User input ---
num_dogs = int(screen.numinput("🐶 Number of Dogs",
                               "How many dogs will run today, parcero? 🐾",
                               minval=2, maxval=10))

# --- Names list ---
dog_names = ['Dante', 'Kira', 'Orion', 'Cimarron', 'Athena', 'Nova', 'Thor']
if num_dogs > len(dog_names):
    dog_names += [f"Dog_{i}" for i in range(len(dog_names), num_dogs)]

user_choice = screen.textinput(title="Make your bet 🎯",
                               prompt=f"Who will win the race?"
                                      f"\nAvailable: {', '.join(dog_names[:num_dogs])}").capitalize()


# --- Draw label -> Name of the dog ---
def draw_label(text, position, color):
    lbl = turtle.Turtle()
    lbl.hideturtle()
    lbl.penup()
    lbl.color(color)
    x, y = position
    lbl.goto(x, y)
    lbl.write(text, align="right", font=("Arial", 12, "bold"))
    return lbl


# --- Resize dogs ---
def resize_turtle(t, scale=0.4):
    """Resize the dog image so it doesn’t overlap with others."""
    t.resizemode("user")
    t.shapesize(scale, scale, 0.1)


# --- Initialize turtles and state ---
dog_data = []
start_x = -400
start_y = -200
lane_height = 60

for i in range(num_dogs):
    name = dog_names[i]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    t = turtle.Turtle()
    t.shape(dog_image[i])
    resize_turtle(t, 0.25)
    t.penup()
    t.speed(0)
    t.color(color)

    # Start point
    pos_y = start_y + i * lane_height
    t.goto(start_x, pos_y)

    # Draw label
    label_pos = (start_x, pos_y - 30)
    label = draw_label(name, label_pos, color)

    dog_data.append({
        "name": name,
        "dog": t,
        "label": label
    })

# --- Race on ---

race_on = True
finish_line = 300

while race_on is True:
    for data in dog_data:
        t = data["dog"]
        lbl = data["label"]

        pace = random.randint(0, 10)
        t.forward(pace)

        cor_x = t.xcor()
        cor_y = t.ycor() - 30
        lbl.clear()
        lbl.goto(cor_x, cor_y)
        lbl.write(data["name"], align="right", font=("Arial", 12, "bold"))

        if t.xcor() > finish_line:
            winner = data["name"]
            race_on = False

# --- Announce the Winner ---

if user_choice == winner:
    messagebox.showinfo("The winner is",
                        f"{winner}\n\nYour bet was on {user_choice}"
                        f"\n\nCongratulations!! You were right :) you bet for the fastest Doooog")
else:
    messagebox.showinfo("The winner is",
                        f"{winner}\n\nYour bet was on {user_choice}"
                        f"\n\nOh :( So sorry you were wrong :( Better luck next time")

screen.update()
screen.exitonclick()
