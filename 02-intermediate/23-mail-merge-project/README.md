# 💌 Mail Merge Python Project — Colombian Style 🇨🇴

This is a simple Python script that reads a letter template and a list of names, then creates a personalized message for each person. Think of it like writing love letters, family notes, or thank-you cards — all in one go. Super useful for birthdays, holidays, or just sending good vibes.

## 📂 Project Structure
```
Mail Merge Project Start/
│
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│       └── message_Daniela.txt
│       └── message_Mama.txt
│       └── ...etc
│
├── mail-merge.py
└── README.md
```

---

## ⚙️ How It Works

1. Clone this repository:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   cd 23-mail-merge-project
   ```
2. You write your letter in `starting_letter.txt` and include `[name]` where you want the name to go.
3. You list your names (one per line) in `invited_names.txt`
4. Run the script:
   ```bash
   python mail-merge.py
   ```
5. The script will generate one letter per person inside Output/ReadyToSend

---

## 📝 Sample Letter Template
```text
Hey [name]! ☀️

Just wanted to tell you how happy I am to have you in my life — for real. You're awesome, and I’m super grateful for you.

Hope everything’s going smoothly over there. Let’s catch up soon, maybe over a cafecito?

Much love,  
Sebas
```

---

Feel free to make it more romántico, familiar, or bacano — up to you!
