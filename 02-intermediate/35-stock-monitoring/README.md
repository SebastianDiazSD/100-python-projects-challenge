# 🇨🇴 Tesla Stock WhatsApp Alert App 📈  

A fun and practical Python app that checks **Tesla's (TSLA)** stock movement using **Yahoo Finance**, fetches related news with **NewsAPI**, and sends you a **WhatsApp alert** via **Twilio** when the stock changes more than ±5% compared to the previous day.  

Part of my **100 Python Projects Challenge** — Project #35 🚀  

---

## ⚙️ Features
- 📊 Tracks **Tesla (TSLA)** daily closing prices via Yahoo Finance (`yfinance`).
- 🧮 Detects when the stock increases or drops more than **5%**.
- 🗞️ Fetches the top **3 latest Tesla news headlines**.
- 💬 Sends a personalized **WhatsApp alert** with a touch of Colombian humor 🇨🇴.
- 🔒 Keeps all credentials secure using environment variables.

---

## 🧰 Technologies Used
- **Python 3.10+**
- **[yfinance](https://pypi.org/project/yfinance/)** — for stock data.
- **[NewsAPI](https://newsapi.org/)** — for Tesla news.
- **[Twilio WhatsApp API](https://www.twilio.com/whatsapp)** — to send alerts.
- **dotenv**, **requests**, and **twilio** libraries.

---

## 🪄 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 35-stock-monitoring
```
### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Create a .env file in the project folder
```bash
NEWS_API_KEY=your_newsapi_key
TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth_token
PHONE_NUMBER=whatsapp:+57XXXXXXXXXX
```
*📝 The phone number must be verified in your Twilio WhatsApp Sandbox.*
### 5️⃣ Run the app
```bash
python tesla-stock-alert.py
```

---

## 💬 Example WhatsApp Message

🚨 Tesla Stock Alert! 🇨🇴
Price change: 🔺6.3% — 🔥 Tremendo subidón!

💬 Latest Tesla news:
1️⃣ Tesla ramps up new Gigafactory expansion...
2️⃣ Elon Musk teases next-gen battery tech...
3️⃣ Analysts say Tesla could dominate EV market...

— Tu parcero, el bot financiero 🤖💰

---

## 📦 requirements.txt

requests
python-dotenv
twilio
yfinance

