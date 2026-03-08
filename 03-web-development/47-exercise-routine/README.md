# 🏋️ Gym Class Auto-Booker (Selenium + Python)

Automated gym class booking bot built with **Python and Selenium** as part of my **100 Days of Python Challenge (Project #47)**.

The script logs into a gym website, books specific classes every **Tuesday and Thursday at 6:00 PM**, and verifies the bookings automatically.

> 🇨🇴 Built with discipline, caffeine, and Colombian persistence.

---

## 🚀 Features

- Automated login using Selenium
- Smart retry system to handle dynamic web behavior
- Automatically books or waitlists classes
- Verifies bookings on the "My Bookings" page
- Uses a dedicated Chrome profile for session persistence
- Clean, modular, and portfolio-ready code

---

## 🛠 Tech Stack

- Python 3
- Selenium WebDriver
- ChromeDriver
- Explicit waits (`WebDriverWait`)
- Exception handling & retry logic

---

## 📋 How It Works

1. Opens the gym website
2. Logs in with test credentials
3. Searches for classes on:
   - **Tuesday**
   - **Thursday**
   - **6:00 PM**
4. Books or waitlists classes automatically
5. Navigates to *My Bookings*
6. Verifies that all expected classes are booked

---

## ⚠️ Disclaimer

- All credentials and data used in this project are **fake**
- This project is for **educational and portfolio purposes only**
- No real accounts or services are affected

---

## ▶️ How to Run

```bash
pip install selenium
python exercise-routine.py
```

Make sure you have:
* Google Chrome installed
* ChromeDriver compatible with your browser version
pip install selenium
python main.py
