# Habit Tracker 🇨🇴🏃‍♂️📈

A **Colombian-flavored daily running tracker** using **Python + Telegram + Pixela**, built as part of the **#100DaysOfPythonChallenge (Project 36)**.

## 🌎 Description

This project sends you a **daily Telegram message** asking how many kilometers you ran today.  
You reply with your distance, and it automatically logs it to your **Pixela graph**.  
You can also add data for previous days if you forgot to log a run.

Everything runs on **PythonAnywhere** — free hosting, zero headaches.

---

## ⚙️ Tech Stack

- **Python 3.10**
- **Pixela API** → visual habit tracking graph
- **Telegram Bot API** → reminders and input
- **python-telegram-bot** → message handling
- **PythonAnywhere** → scheduled daily execution

---

## 🚀 Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   cd 36-habit-tracker
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install python-telegram-bot requests python-dotenv
   ```
4. Create a .env file:
   ```bash
   PIXELA_TOKEN=your_pixela_token
   PIXELA_USERNAME=your_pixela_username
   GRAPH_ID=running-graph
   TELEGRAM_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```
5. Run it locally:
   ```bash
   python habit_tracker_colombian.py
   ```
6. On PythonAnywhere, schedule it as a daily task.

---

## 🧩 Features
✅ Daily Telegram reminder 🇨🇴
✅ Input today’s or previous day’s running distance
✅ Automatic logging to Pixela
✅ Fun Colombian-style messages
✅ Fully hosted on PythonAnywhere (free tier)

---

## 💬 Example Conversation
Bot: Hey parcero! 🇨🇴 Ready to log your km for today?

You: 6.5

Bot: ✅ Sweet! Logged 6.5 km for today (20251111). 🇨🇴🔥

You:/previous
20251110
5.2

Bot:✅ Cool! Logged 5.2 km for 20251110. 🇨🇴
