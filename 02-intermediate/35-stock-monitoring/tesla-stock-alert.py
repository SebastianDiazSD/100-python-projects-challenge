"""
Tesla Stock WhatsApp Alert 🇨🇴📈
--------------------------------
Checks Tesla's recent stock movement using Yahoo Finance (via yfinance).
If the stock moves ±5% compared to the previous day, it fetches the top 3
Tesla-related news articles and sends a WhatsApp alert via Twilio.

Project #35 – 100 Python Projects Challenge
"""

import os
import json
import requests
from datetime import datetime, timedelta
from pathlib import Path
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
import yfinance as yf

# --- CONFIG ---
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# --- LOAD ENV VARIABLES ---
dotenv_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path)

# Twilio credentials
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")

# API key for news
API_KEY_NEWS = os.getenv("NEWS_API_KEY")

# WhatsApp number (must be verified in Twilio Sandbox)
USER_WHATSAPP = os.getenv("PHONE_NUMBER")

# --- TWILIO CONFIG ---
proxy_client = TwilioHttpClient()
if 'https_proxy' in os.environ:
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

client = Client(account_sid, auth_token, http_client=proxy_client)

# --- STEP 1: FETCH TESLA STOCK DATA ---
print("🔍 Fetching Tesla stock data from Yahoo Finance...")

# Get the last 5 days (handles weekends automatically)
data = yf.download(STOCK, period="5d", interval="1d")

if data.empty:
    print("🚨 Could not retrieve data for Tesla. Try again later.")
    exit()

# Get closing prices
close_prices = data["Close"]
yesterday = close_prices.index[-1]
day_before = close_prices.index[-2]

price_yesterday = float(close_prices.iloc[-1])
price_before_yesterday = float(close_prices.iloc[-2])

# Calculate % change
diff = price_yesterday - price_before_yesterday
delta_percentage = round((diff / price_before_yesterday) * 100, 2)

print(
    f"💹 {COMPANY_NAME} ({STOCK})\n"
    f"{day_before.date()}: ${price_before_yesterday}\n"
    f"{yesterday.date()}: ${price_yesterday}\n"
    f"Change: {delta_percentage}%"
)

# --- STEP 2: FETCH TESLA NEWS ---
print("🗞️ Fetching Tesla news...")

API_NEWS = "https://newsapi.org/v2/everything"
news_parameters = {
    'q': COMPANY_NAME,
    'from': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'),
    'to': datetime.now().strftime('%Y-%m-%d'),
    'language': 'en',
    'sortBy': 'publishedAt',
    'apiKey': API_KEY_NEWS,
}

try:
    response_news = requests.get(API_NEWS, params=news_parameters, timeout=10)
    response_news.raise_for_status()
    data_news = response_news.json()
except requests.exceptions.RequestException as e:
    print(f"🚨 Error fetching news data: {e}")
    exit()

articles = data_news.get("articles", [])[:3]
news_text = ""

if not articles:
    news_text = "\nNo recent Tesla news found."
else:
    for i, article in enumerate(articles):
        news_text += (
            f"\n\n{i+1}️⃣ {article['title']}\n"
            f"{article['description']}\n"
            f"{article['url']}"
        )

# --- STEP 3: CREATE MESSAGE BODY ---
if abs(delta_percentage) >= 5:
    arrow = "🔺" if delta_percentage > 0 else "🔻"
    mood = "🔥 Tremendo subidón!" if delta_percentage > 0 else "🥶 Cayó duro!"
    msg_body = (
        f"🚨 *Tesla Stock Alert!* 🇨🇴\n"
        f"Price change: {arrow}{delta_percentage}% — {mood}\n\n"
        f"💬 Latest Tesla news:{news_text}\n\n"
        f"— Tu parcero, el bot financiero 🤖💰"
    )
else:
    msg_body = (
        f"Todo tranqui, parcero 😎 Tesla only moved {delta_percentage}%.\n"
        f"No major changes today. Take it easy y tómate un tintico ☕"
    )

# --- STEP 4: SEND WHATSAPP MESSAGE ---
print("📤 Sending WhatsApp message...")
try:
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        body=msg_body,
        to=USER_WHATSAPP
    )
    print(f"✅ Message sent successfully! SID: {message.sid}")
except Exception as e:
    print(f"🚨 Error sending WhatsApp message: {e}")
