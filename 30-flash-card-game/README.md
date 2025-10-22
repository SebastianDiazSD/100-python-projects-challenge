# 🧠 Flash Card Game (Python Tkinter)

Welcome to the Flash Card Game! This is part of the **100 Python Projects** challenge.

This app helps you learn French vocabulary using interactive flashcards. It shows a French word, waits a few seconds, then reveals the English translation. You can mark words you know to remove them from the deck!

---

## 🚀 Features

- Learn French vocabulary with flashcards
- Automatically flips the card after 3 seconds
- Tracks words you've learned
- Saves progress to a CSV file (`words_to_learn.csv`)

---

## 📂 Project Structure

```bash
project/
│
├── data/
│ ├── french_words.csv
│ └── words_to_learn.csv (generated on first run)
│
├── images/
│ ├── card_front.png
│ ├── card_back.png
│ ├── right.png
│ └── wrong.png
│
├── main.py
└── README.md
```

---

🧠 How It Works

* On launch, the app loads a list of French-English word pairs.

* A French word appears first.

* After 3 seconds, the card flips to show the English translation.

* You click ✔️ if you know the word, or ❌ to skip.

* Known words are saved so you don’t see them again.

