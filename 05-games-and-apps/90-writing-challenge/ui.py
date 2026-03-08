import tkinter as tk
from tkinter import messagebox
from constants import APP_TITLE, WELCOME_TEXT
from logic import WritingLogic


class DangerousWritingApp:

    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("900x600")

        self.logic = WritingLogic()

        self.setup_ui()

        self.check_timer()

    def setup_ui(self):

        self.prompt_label = tk.Label(
            self.root,
            text=self.logic.get_prompt(),
            font=("Arial", 14, "bold"),
            pady=10
        )
        self.prompt_label.pack()

        self.text_area = tk.Text(
            self.root,
            wrap="word",
            font=("Georgia", 14),
            padx=20,
            pady=20
        )
        self.text_area.pack(expand=True, fill="both")

        self.text_area.insert("1.0", WELCOME_TEXT)

        self.text_area.bind("<Key>", self.on_keypress)

        self.timer_label = tk.Label(
            self.root,
            text="Keep typing...",
            font=("Arial", 12)
        )
        self.timer_label.pack(pady=10)

    def on_keypress(self, event):
        self.logic.update_keypress()

    def delete_text(self):
        self.text_area.delete("1.0", tk.END)

        messagebox.showwarning(
            "Too Slow!",
            "You stopped writing for too long.\n\nEverything has been deleted.\n\nStart again!"
        )

        self.prompt_label.config(text=self.logic.get_prompt())

    def check_timer(self):

        if self.logic.should_delete_text():
            if self.text_area.get("1.0", tk.END).strip():
                self.delete_text()

        self.root.after(1000, self.check_timer)