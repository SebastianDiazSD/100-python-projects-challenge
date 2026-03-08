import math

# Constants
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# State variables
reps = 0
timer = None

def start_timer(canvas, timer_text, label_status, label_completed, window):
    global reps
    reps += 1

    label_completed.grid_remove()  # Hide "Llave..." when a new session starts

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_status.config(text="Long break ☕\nEnjoy your coffee panita", fg="red")
        count_down(long_break, canvas, timer_text, label_status, label_completed, window)
    elif reps % 2 == 0:
        label_status.config(text="Short break 💤\n a estirar parce", fg="blue")
        count_down(short_break, canvas, timer_text, label_status, label_completed, window)
    else:
        label_status.config(text="Time to work 💪\nconcentrado viejo", fg="green")
        count_down(work_sec, canvas, timer_text, label_status, label_completed, window)


def reset_timer(canvas, timer_text, label_status, label_completed, window):
    global timer
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_status.config(text="Welcome ☕\nColombian Coffee\nPomodoro Timer", fg="black")
    label_completed.grid_remove()
    global reps
    reps = 0


def count_down(count, canvas, timer_text, label_status, label_completed, window):
    minutes = math.floor(count / 60)
    seconds = count % 60
    formatted_time = f"{minutes:02}:{seconds:02}"

    canvas.itemconfig(timer_text, text=formatted_time)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, canvas, timer_text, label_status, label_completed, window)
    else:
        label_completed.grid()  # Show "Llave, time's up!"
        start_timer(canvas, timer_text, label_status, label_completed, window)
