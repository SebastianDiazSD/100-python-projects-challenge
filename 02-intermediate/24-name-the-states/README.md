# 🇨🇴 Name the State 🗺️ (Colombia & USA Edition)

Welcome to **Name the State**, a beginner-friendly Python game where you guess the names of **Colombian departments** or **U.S. states**. Built using the `turtle`, `pandas`, and `tkinter` libraries, this game is a fun way to test your geography skills — with a Colombian *sazón*. 💥

---

## 🎮 How to Play

- When you run the game, you’ll be asked to choose:
  - `1` for **Colombia** 🇨🇴
  - `2` for **USA** 🇺🇸
- A map will appear.
- Type in the name of a state (or department).
- If it's correct, it will be displayed on the map.
- You have **5 attempts** to make mistakes. Use them wisely!
- Guess all states to win!

---

## 📁 Files

| File                  | Description                                      |
|-----------------------|--------------------------------------------------|
| `name-the-state.py`   | Main game file — run this to start playing       |
| `states.py`           | Handles writing state names on the map           |
| `32_states_col.csv`   | Colombia's 32 departments + coordinates          |
| `50_states_usa.csv`   | 50 U.S. states + coordinates                     |
| `map_col.gif`         | Background image of Colombia                     |
| `blank_states_img.gif`| Background image of the USA                      |
| `README.md`           | You're reading it! 🧠                             |

---

## 🧠 Technologies Used

- 🐢 `turtle` — for map graphics and interaction
- 📊 `pandas` — for reading the CSV files of state names and coordinates
- 📋 `tkinter.messagebox` — for pop-up messages and feedback

---

## ✨ Features

- 🇨🇴 Colombian-style feedback! Words like `parcero`, `paila`, `viejito`, and more
- ❌ Duplicate guess protection
- 💬 Visual popups for correct/wrong guesses
- 🎯 Win condition: guess all states!

---

## 🛠️ How to Run

1. Make sure you have Python 3 installed
2. Install pandas if you haven't:

```bash
pip install pandas
```

3. Clone this repo:

```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 24-name-the-states

```

4. Run the game:

```bash
python name-the-state.py
```

---

## About this project

This is a beginner Python project made with practice and colombian coffee
* Working with pandas and CSVs
* Using the turtle graphichs module
* Creating simple games
* Mixing creativity with code

If you are colombian or just love geography, this game is for you!
