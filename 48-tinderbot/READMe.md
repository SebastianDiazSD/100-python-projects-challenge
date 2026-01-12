# Tinder Auto-Swipe Bot 🤖🔥

This project is part of my **48 Python Challenge**, where I build one Python project per day to strengthen my automation, scripting, and problem-solving skills.

This bot automates Tinder swiping using **Selenium** and **undetected-chromedriver**, leveraging an existing Chrome profile to avoid repeated logins.

---

## 🚀 Features

- Uses an existing Chrome user profile
- Bypasses basic automation detection
- Automatically clicks the "Like" button
- Clean, modular, and beginner-friendly structure
- Written with portfolio-quality code and documentation

---

## 🛠️ Technologies Used

- Python 3
- Selenium
- undetected-chromedriver
- Chrome WebDriver

---

## 📂 Project Structure
```bash
tinder-bot/
│
├── tinder_bot.py # Main bot logic and execution
└── README.md # Project documentation
```

---

## ⚙️ How It Works

1. Launches Chrome using a **real user profile**
2. Navigates to Tinder
3. Locates the "Like" button using XPath
4. Clicks the button repeatedly with a delay
5. Runs indefinitely until manually stopped

---

## 🧪 Usage

1. Install dependencies:
   
```bash
pip install selenium undetected-chromedriver
```

2. Update the **PROFILE_PATH** variable with your Chrome profile path.
3. Install dependencies:

```bash
python tinder_bot.py
```

4. Press Enter in the terminal to close the browser.

---

## ⚠️ Disclaimer

This project is for educational purposes only.

Automating Tinder may violate their Terms of Service.
Use responsibly and at your own risk.
