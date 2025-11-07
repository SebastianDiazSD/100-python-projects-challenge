from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#FFAF02"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(
            width=600,
            height=400,
            bg=THEME_COLOR,
            highlightthickness=5,
            highlightbackground="white"
        )
        self.background_img = PhotoImage(file="background.png")
        self.canvas.create_image(0, 0, image=self.background_img, anchor="nw")

        self.question_text = self.canvas.create_text(
            300,
            100,
            width=500,
            text="Some Question Text",
            fill='white',
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create answer buttons
        self.answer_buttons = []
        y_start = 250
        for i in range(4):
            btn = Button(
                text="",
                width=20,
                bg="#473100",
                fg="white",
                font=("Arial", 10),
                command=lambda i=i: self.check_answer(i)
            )
            self.canvas.create_window(300, y_start + i * 40, window=btn)
            self.answer_buttons.append(btn)

        # 🟠 Add a Quit button
        self.quit_button = Button(
            text="I'm done, quit game",
            width=20,
            bg="#C70039",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.quit_game
        )
        self.quit_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(highlightbackground="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            q_choices = self.quiz.question_choices()

            for i, btn in enumerate(self.answer_buttons):
                btn.config(text=q_choices[i], state="normal")

            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            for btn in self.answer_buttons:
                btn.config(state="disabled")

    def check_answer(self, index):
        user_answer = self.answer_buttons[index]["text"]
        is_right = self.quiz.check_answer(user_answer)

        # Disable buttons while showing feedback
        for btn in self.answer_buttons:
            btn.config(state="disabled")

        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Show green/red border feedback and go to next question."""
        if is_right:
            self.canvas.config(highlightbackground="green")
        else:
            self.canvas.config(highlightbackground="red")

        # Wait 1 second, then reset border and load next question
        self.window.after(1000, lambda: self.canvas.config(highlightbackground="white"))
        self.window.after(1000, self.get_next_question)

    def quit_game(self):
        user_choice = messagebox.askyesno(
            title="Quit Game",
            message="Are you sure you want to quit the quiz? You’ll lose your current progress 😢"
        )
        if user_choice:
            self.window.destroy()
