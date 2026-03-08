from tkinter import *
import requests
from data import question_bank
from quiz_brain import QuizBrain


# 💬 Creating Questions object
quiz = QuizBrain(question_bank)


# 🪟 Set up the main window (Tkinter GUI)
window = Tk()
window.title("Kanye Says...")
window.config(padx=20, pady=20)  # Add some padding for better layout

# 🎨 Create the canvas where the quote will appear
# canvas = Canvas(width=500, height=400)
canvas = Canvas(window, width=500, height=400, bg="#FFAF02", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# 🖼 Background image
background_img = PhotoImage(file="background.png")  # Background image
canvas.create_image(0, 0, image=background_img, anchor="nw")
# canvas.config(width=background_img.width(), height=background_img.height())

# canvas.create_image(150, 107)
# Text area for displaying Question
question_text = canvas.create_text(
    250, 100,
    text="Let's Start the Quiz",
    width=100,
    font=("Arial", 24, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

# 📋 Display answers with buttons
answer_buttons = []
y_start = 250
for i, ans in enumerate([1,2,3,4]):
    btn = Button(
        text=ans,
        width=20,
        bg="#473100",
        fg="white",
        font=("Arial", 12),
        # command=lambda a=ans: check_answer(a)
        command=get_quote
    )
    # Place button on canvas
    canvas.create_window(150, y_start + i * 40, window=btn)
    answer_buttons.append(btn)

# 🧉 Main loop — keeps the app running (like a good cup of tinto keeps us coding)
window.mainloop()
