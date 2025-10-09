# 🐍 Chasing the Prey! *Die Schlange*

Welcome to **Chasing the Prey!**, a Python-powered Snake Game built using the `turtle` module.  
This is a modern take on the classic Snake — with a touch of **Colombian flavor 🇨🇴**.

---

## 🎮 Game Overview

You control **Dante**, a hungry snake on a mission to grow by eating colorful food scattered around the screen.  
Every bite makes Dante longer... and a little faster.  

Avoid colliding with yourself — and depending on your **difficulty level**,  
either wrap around the edges or face *el fin del juego* 💀.

---

## 🧩 Features

- 🐍 Smooth snake movement built with the `turtle` graphics module  
- 🍉 Randomly generated, colorful food  
- 💾 Persistent high score tracking  
- ⚡ Speed increases as you grow  
- 🎚️ Easy or Hard modes (you choose your fate)  
- 🇨🇴 Clean, well-commented code with Colombian warmth and humor

---

## 🕹️ Controls

| Key | Action        |
|-----|----------------|
| **W** | Move Up        |
| **S** | Move Down      |
| **A** | Move Left      |
| **D** | Move Right     |

> 💡 *Tip:* Use `Easy` mode to wrap around walls like a ninja.  
> Choose `Hard` mode if you want a real challenge — one hit and you’re out!

---

## ⚙️ How to Run the Game

### 1️⃣ Clone this repository
```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 20-the-snake-game
```

### 2️⃣ Run the main game
```bash
python snake_game.py
```

## 🗂️ Project Structure
```bash
snake-game/
│
├── snake_game.py      # 🎮 Main game logic (controls and loop)
├── snake_class.py     # 🐍 Dante the Snake – movement and growth
├── snake_food.py      # 🍎 Randomly placed food with colors
├── scoreboard.py      # 🧮 Tracks and displays score + high score
├── data.txt           # 💾 Stores high score persistently
└── README.md          # 📘 You’re reading it right now
```

## 🗂️ Project Structure

The game automatically saves your best score to data.txt.
Try to beat your previous record and climb the leaderboard — vos contra vos mismo, parcero! ⚡
