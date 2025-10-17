# 🔐 Strong Password Generator (Project #28)

Welcome to **Project #28** of my personal **100 Python Projects Challenge**!  
This project is a **Graphical User Interface (GUI)** app built with **Python** and **Tkinter**, designed to securely generate and save strong passwords.

> 🇨🇴 A little Colombian touch: Keep your digital life safe — ¡con estilo y seguridad!

---

## 🧠 About This Project

The **Password Manager** allows users to:
- Generate random, secure passwords using letters, numbers, and symbols
- Store credentials (website, email/username, and password)
- Copy the generated password directly to the clipboard
- Save entries to a `.txt` file for future reference

All in a simple and user-friendly GUI.

---

## 🚀 Technologies Used

- Python 3
- Tkinter (for GUI)
- `pyperclip` (to copy passwords to clipboard)

---

## 📂 Project Structure

```bash
28-day-strong-password-generator/
│
├── password_generator.py # Main application file
├── helpers.py # Helper functions for generation & saving
├── my_passwords.txt # Saved passwords (created automatically)
├── logo.png # Logo image for the UI
└── README.md # This file
```

---

## 💡 How It Works

1. **Enter the website name** (e.g. `github.com`)
2. **Enter your email or username**
3. Click **"Generate Password"** — a secure password is created
4. Click **"Add"** to save it
5. Password is automatically copied to your clipboard

Passwords are stored locally in a file named `my_passwords.txt`.

---

## ⚙️ Installation

### Prerequisites

Make sure you have Python installed. If not, download it from: https://www.python.org/downloads/

### Clone the repo

```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 28-day-strong-password-generator
```

### Install required libraries

```bash
pip install pyperclip
```

### Run the app

```bash
python password_generator.py
```

---

## 📝 Notes

The logo image (logo.png) must be in the same folder as the main script.

Make sure my_passwords.txt is not uploaded to public repositories if it contains real data.

This is a beginner-to-intermediate Python project, and a great example of working with GUIs.

Keep your accounts secure... and as we say: ¡pa' lante!

