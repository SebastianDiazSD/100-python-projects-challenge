# 🎂 Birthday Wisher (100 Days of Code - Python Project)

An automated birthday wisher built in Python!  
This script reads birthday data from a CSV file, selects a random birthday letter template, personalizes it with the recipient’s name, and sends the message automatically via email.

---

## 🚀 Features

- 📅 **Automated date check:** Compares today’s date with entries in a CSV file.  
- 💌 **Personalized messages:** Inserts the recipient’s name into one of several letter templates.  
- 🔄 **Random templates:** Picks from multiple pre-written birthday letter files.  
- ✉️ **Email delivery:** Sends the message through a secure SMTP connection.  
- 🧠 **Simple data format:** Birthdays are stored and managed in an easy-to-edit CSV file.

---

## 🗂️ Project Structure
```bash
birthday-wisher/
│
├── birthdays.csv # Contains name, email, year, month, day
├── birthday_letters/ # Folder where generated birthday letters are saved
├── letter_templates/ # Pre-written letter templates (letter_1.txt, letter_2.txt, etc.)
├── main.py # Main Python script
└── README.md # Project documentation
```

---

## ⚙️ How It Works

Read CSV: The program loads birthdays.csv using pandas.

Check Date: It compares today’s date to the birthdays listed.

Generate Letter: If there’s a match, it picks a random letter template from letter_templates/ and replaces [NAME] with the person’s name.

Send Email: It sends the generated message via SMTP to the recipient’s email address.

---

## 🔐 Security Tips

Never hardcode your email password!

* Use an environment variable or a .env file to store credentials.

* For Gmail, use an App Password instead of your main password.
* Example (Linux/macOS):
```bash
export EMAIL_USER="youremail@example.com"
export EMAIL_PASS="your_app_password"
```
* In Python, access them safely:
```bash
import os
my_email = os.getenv("EMAIL_USER")
my_password = os.getenv("EMAIL_PASS")
```
