# 🧠 Copy this into Reeborg's World to help our buddy Karel escape the maze like a true crack.
# 🇨🇴 Colombian flow, let's go 🇨🇴

# We only know how to turn left, but hey — we make it work 💪
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# First, we go straight as long as there's a clear path — no drama, just cruising.
while front_is_clear():
    move()

# Time to turn left and start dealing with the real maze — here’s where the magic begins.
turn_left()

# Let’s guide Karel
while not at_goal():
    if right_is_clear():
        # If there’s space to the right, vamos pa’ allá
        turn_right()
        move()
    elif front_is_clear():
        # If the front is clear, just keep going — no need to overthink it.
        move()
    else:
        # No way forward or right? We turn left and look for a new path. Siempre pa’lante.
        turn_left()

# 🏁 And that’s it — made it to the goal papá 😎
