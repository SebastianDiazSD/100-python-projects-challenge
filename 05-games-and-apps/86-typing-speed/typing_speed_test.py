import tkinter as tk
import time
import random

# ---------------- SAMPLE TEXTS ---------------- #

texts = [
    "Colombia is famous for its coffee, mountains, and vibrant culture. "
    "Walking through the streets of Medellin you can feel the energy of innovation "
    "and the warmth of the people.",

    "Bogota sits high in the Andes mountains and mixes history with modern life. "
    "From small cafes serving fresh Colombian coffee to busy city streets, "
    "there is always something happening.",

    "In Colombia people value family, friendship, and good food. "
    "Sharing an arepa and a cup of coffee while talking with friends "
    "is part of everyday life.",

    "Cartagena is a colorful coastal city where colonial architecture meets the Caribbean sea. "
    "Music, dancing, and warm weather make it a beautiful place to visit."
]


# ---------------- APP CLASS ---------------- #

class TypingSpeedApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test 🇨🇴")
        self.root.geometry("900x500")

        self.start_time = None
        self.running = False

        self.sample_text = random.choice(texts)

        # Title
        self.title = tk.Label(
            root,
            text="Typing Speed Test - Colombian Edition",
            font=("Arial", 20, "bold")
        )
        self.title.pack(pady=10)

        # Instruction
        self.instruction = tk.Label(
            root,
            text="Type the text below as fast and accurately as you can.",
            font=("Arial", 12)
        )
        self.instruction.pack()

        # Sample text
        self.text_label = tk.Label(
            root,
            text=self.sample_text,
            wraplength=800,
            font=("Arial", 13),
            justify="left",
            bg="#f4f4f4",
            padx=10,
            pady=10
        )
        self.text_label.pack(pady=20)

        # Text input
        self.text_entry = tk.Text(
            root,
            height=6,
            width=80,
            font=("Arial", 12)
        )
        self.text_entry.pack()

        self.text_entry.bind("<KeyPress>", self.start_test)

        # Result label
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 14)
        )
        self.result_label.pack(pady=15)

        # Buttons
        self.check_button = tk.Button(
            root,
            text="Check Speed",
            command=self.calculate_speed,
            font=("Arial", 12)
        )
        self.check_button.pack(pady=5)

        self.restart_button = tk.Button(
            root,
            text="Restart Test",
            command=self.restart_test,
            font=("Arial", 12)
        )
        self.restart_button.pack()

    # ---------------- START TIMER ---------------- #

    def start_test(self, event):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    # ---------------- CALCULATE SPEED ---------------- #

    def calculate_speed(self):

        if not self.running:
            return

        end_time = time.time()
        total_time = end_time - self.start_time

        typed_text = self.text_entry.get("1.0", tk.END).strip()

        word_count = len(typed_text.split())
        wpm = round((word_count / total_time) * 60)

        accuracy = self.calculate_accuracy(typed_text)

        result = f"Speed: {wpm} WPM | Accuracy: {accuracy}%"

        self.result_label.config(text=result)

    # ---------------- ACCURACY ---------------- #

    def calculate_accuracy(self, typed):

        original_words = self.sample_text.split()
        typed_words = typed.split()

        correct = 0

        for i in range(min(len(original_words), len(typed_words))):
            if original_words[i] == typed_words[i]:
                correct += 1

        accuracy = (correct / len(original_words)) * 100

        return round(accuracy)

    # ---------------- RESTART ---------------- #

    def restart_test(self):

        self.sample_text = random.choice(texts)
        self.text_label.config(text=self.sample_text)

        self.text_entry.delete("1.0", tk.END)

        self.result_label.config(text="")

        self.running = False
        self.start_time = None


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":

    root = tk.Tk()
    app = TypingSpeedApp(root)

    root.mainloop()
