import tkinter as tk
from tkinter import ttk, messagebox
from helpers import get_top_100

# Constants
FONT_NAME = "Courier"
COLOR = "#FFBF78"

# 🪟 Create the window
window = tk.Tk()
window.title("Musical Time Machine")
window.config(padx=40, pady=40, bg=COLOR)

# Canvas setup
canvas = tk.Canvas(window, width=400, height=400, bg=COLOR, highlightthickness=0)
try:
    music_logo = tk.PhotoImage(file="logo.png")
    canvas.coffe_cup = music_logo  # prevent garbage collection
    canvas.create_image(210, 210, image=music_logo)
except:
    pass

canvas.grid(row=0, column=0)

# 🏷️ Labels
label_date = tk.Label(
    text="Parcero, dejate sorprender!\nJust click the button",
    font=("Arial", 14),
    bg=COLOR
)
label_date.grid(column=0, row=1, pady=10)

# Progress bar
progress = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress.grid(column=0, row=3, pady=10)
progress["value"] = 0

# Wrapper function for Spotify + UI updates
def run_process():
    try:
        get_top_100(progress)
        messagebox.showinfo("Success", "Playlist created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# 🔘 Buttons
btn_start = tk.Button(
    text="Let the music begin!",
    command=run_process,
    font=("Arial", 12),
    bg="#FFA559",
    padx=10,
    pady=5
)
btn_start.grid(column=0, row=2, pady=5)

# 🌀 Run the app
window.mainloop()
