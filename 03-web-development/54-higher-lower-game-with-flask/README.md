# 🎯 Higher–Lower Game (Flask Edition)

A simple but fun **Higher–Lower guessing game** built with **Flask** 🐍  
Clean logic, web-based gameplay, and a little **Colombian sabor** to keep things original.

This project is part of my Python challenge series and was designed to showcase:
- Flask fundamentals
- Game logic
- Session handling
- Clean project structure
- A bit of personality (because code doesn’t have to be aburrido)

---

## 🚀 How the Game Works

1. The player chooses a **difficulty level**:
   - 🟢 **Easy**: Guess a number between **1 and 10**
   - 🟡 **Medium**: Guess a number between **1 and 50**
   - 🔴 **Hard**: Guess a number between **1 and 100** (modo berraco)

2. The app generates a **random number** based on the difficulty.

3. The player keeps guessing until:
   - ❌ Too low → “Parcero, you’re below the number”
   - ❌ Too high → “Uy no, you went too high”
   - ✅ Correct → “Esooo, you nailed it!”

4. Every guess comes with a **random GIF** to keep the vibes high 😎

---

## 🧠 Tech Stack

- **Python 3**
- **Flask**
- **HTML (Jinja templates)**
- **Sessions** for game state
- **Random module** for numbers & GIFs

No database, no overengineering — just clean Flask logic, like it should be.

---

## 📁 Project Structure

```bash
higher-lower-flask/
│
├── app.py
├── templates/
│ ├── index.html
│ └── game.html
└── README.md
```
---

## 🛠️ How to Run It Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   ```
2. Navigate into the project:
   ```bash
   cd 54-higher-lower-game-with-flask
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
4. Install dependencies:
   ```bash
   pip install flask
   ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Open your browser and go to:
   ```bash
   http://127.0.0.1:5000/
   ```
And listo, pana 🚀

---

## 🌶️ Colombian Flavor (Why This Project Is Different)

Most guessing games say:

* “Too high. Too low.”

This one says:

* “Parcero, bajale dos rayitas.”
* “Modo berraco activated.”
* “Esooo, ganaste.”

Same professionalism. More personality.

---

## 👨‍💻 About the Author

Built by a developer who believes:

> Good code should be clean,
> but great code should also have sabor 🇨🇴

If you like this project, feel free to ⭐ the repo or reach out.
