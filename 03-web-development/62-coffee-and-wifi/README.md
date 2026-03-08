# ☕ Café Finder — Colombian Edition 🇨🇴

A lightweight Flask web application that allows users to explore, add, and rate cafés based on coffee quality, WiFi strength, and power outlet availability.

This project was built as **Project 62 of the _100 Python_ challenges**, with a clean UI and a subtle Colombian coffee culture influence — because great software deserves great coffee.

---

## 🚀 Features

- Browse a list of cafés stored in a CSV database
- Add new cafés through a user-friendly web form
- Rate cafés using intuitive emoji-based ratings
- Open café locations directly in Google Maps
- Clean Bootstrap-based UI with custom styling
- Beginner-friendly Flask project structure

---

## 🛠 Tech Stack

- **Python 3**
- **Flask**
- **Flask-WTF**
- **Flask-Bootstrap**
- **HTML5 / CSS3**
- **Bootstrap 5**
- **CSV** (lightweight data storage)

---

## 📂 Project Structure
```bash
cafe-finder/
│
├── main.py
├── cafe-data.csv
├── requirements.txt
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── cafes.html
│ └── add.html
│
├── static/
│ └── css/
│ └── styles.css
│
└── README.md
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 62-coffee-and-wifi
```

### 2️⃣ Create and activate a virtual environment

```bash
python3 -m venv myenv
source myenv/bin/activate   # macOS / Linux
myenv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python main.py
```

Then open your browser and visit:

```bash
http://127.0.0.1:5000
```

---

## 🌎 Colombian Touch 🇨🇴

Colombia is one of the world’s top coffee producers, and café culture plays a big role in daily life.
This project keeps all content in English for international accessibility while adding a warm, friendly coffee-shop vibe inspired by Colombian cafés.
