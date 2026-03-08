import tkinter as tk
from helpers import start_timer, reset_timer

# Constants
FONT_NAME = "Courier"
COLOR = "#FFBF78"

# 🪟 Window setup
window = tk.Tk()
window.title("The pomodoro App")
window.geometry('520x580')
window.config(padx=20, pady=20, bg=COLOR)

# Canvas setup
canvas = tk.Canvas(window, width=400, height=400, bg=COLOR, highlightthickness=0)
coffe_cup = tk.PhotoImage(file="coffee_cup.png")
canvas.coffe_cup = coffe_cup  # prevent garbage collection
canvas.create_image(205, 205, image=coffe_cup)
timer_text = canvas.create_text(195, 260, text="00:00", fill="white", font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=1, column=1)

# 🏷️ Labels
label_status = tk.Label(text="Welcome ☕\nColombian Coffee\nPomodoro Timer", bg=COLOR, font=(FONT_NAME, 24, 'bold'), fg="black")
label_status.grid(column=1, row=0)

label_completed = tk.Label(text="Llave\ntime's up!", bg=COLOR, font=(FONT_NAME, 24, 'bold'))
label_completed.grid(column=1, row=2)
label_completed.grid_remove()

# 🔘 Buttons
btn_start = tk.Button(
    text="Start",
    command=lambda: start_timer(canvas, timer_text, label_status, label_completed, window)
)
btn_start.grid(column=0, row=2, pady=5)

btn_reset = tk.Button(
    text="Reset",
    command=lambda: reset_timer(canvas, timer_text, label_status, label_completed, window)
)
btn_reset.grid(column=2, row=2, pady=5)

window.mainloop()
