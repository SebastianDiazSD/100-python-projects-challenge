import tkinter as tk
from tkinter import messagebox
import random

PLAYER_X = "X"
PLAYER_O = "O"

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe 🇨🇴 Colombian Edition")

        self.mode = None
        self.current_player = PLAYER_X
        self.board = [""] * 9

        # --- Mode Selection ---
        self.menu_frame = tk.Frame(root, bg="#FCD116")
        self.menu_frame.pack(fill="both", expand=True)

        tk.Label(
            self.menu_frame,
            text="Choose Game Mode",
            font=("Arial", 18, "bold"),
            bg="#FCD116"
        ).pack(pady=20)

        tk.Button(
            self.menu_frame,
            text="Player vs Player",
            font=("Arial", 14),
            command=lambda: self.start_game("pvp"),
            width=20
        ).pack(pady=10)

        tk.Button(
            self.menu_frame,
            text="Player vs AI",
            font=("Arial", 14),
            command=lambda: self.start_game("ai"),
            width=20
        ).pack(pady=10)

    def start_game(self, mode):
        self.mode = mode
        self.menu_frame.destroy()

        self.status = tk.Label(
            self.root,
            text="Player X's Turn – ¡Vamos!",
            font=("Arial", 16, "bold"),
            bg="#FCD116"
        )
        self.status.pack(fill="x")

        self.frame = tk.Frame(self.root, bg="#003893")
        self.frame.pack()

        self.buttons = []
        for i in range(9):
            button = tk.Button(
                self.frame,
                text="",
                font=("Arial", 28, "bold"),
                width=5,
                height=2,
                command=lambda i=i: self.make_move(i)
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        tk.Button(
            self.root,
            text="New Game",
            font=("Arial", 14),
            bg="#CE1126",
            fg="white",
            command=self.reset_game
        ).pack(fill="x")

    def make_move(self, index):
        if self.board[index] != "":
            return

        self.board[index] = self.current_player
        self.buttons[index]["text"] = self.current_player

        if self.check_winner(self.current_player):
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins! 🇨🇴")
            self.reset_game()
            return

        if "" not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
            return

        self.switch_player()

        if self.mode == "ai" and self.current_player == PLAYER_O:
            self.root.after(400, self.ai_move)

    def ai_move(self):
        move = self.best_move()
        self.make_move(move)

    def best_move(self):
        # Win if possible
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = PLAYER_O
                if self.check_winner(PLAYER_O):
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Block player
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = PLAYER_X
                if self.check_winner(PLAYER_X):
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # Take center
        if self.board[4] == "":
            return 4

        # Take corner
        corners = [0,2,6,8]
        free_corners = [c for c in corners if self.board[c] == ""]
        if free_corners:
            return random.choice(free_corners)

        # Take any space
        free = [i for i in range(9) if self.board[i] == ""]
        return random.choice(free)

    def switch_player(self):
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
        self.status.config(text=f"Player {self.current_player}'s Turn – ¡Vamos!")

    def check_winner(self, player):
        combos = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a,b,c in combos:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = PLAYER_X
        self.status.config(text="Player X's Turn – ¡Vamos!")

        for b in self.buttons:
            b.config(text="")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
