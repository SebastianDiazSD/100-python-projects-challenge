import os
import requests
import json
from pathlib import Path
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv

# ===============================
# ☀️ WEATHER ALERT APP - COLOMBIAN STYLE 🇨🇴
# Checks the weather forecast using OpenWeatherMap and
# sends you a WhatsApp alert via Twilio if it’s going to rain.
# Works locally and on PythonAnywhere.
# ===============================

# --- LOAD ENVIRONMENT VARIABLES ---
# Safely load your .env file using absolute path
dotenv_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path)

# Twilio credentials
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")

# OpenWeatherMap API key
API_KEY = os.getenv("OPENWEATHER_API")

# WhatsApp number (must be verified in Twilio Sandbox)
USER_WHATSAPP = os.getenv("PHONE_NUMBER")

# --- TWILIO CONFIGURATION ---
# Configure Twilio HTTP client (works on PythonAnywhere too)
proxy_client = TwilioHttpClient()

# ✅ Only use proxy when running on PythonAnywhere
if 'https_proxy' in os.environ:
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Initialize Twilio client
client = Client(account_sid, auth_token, http_client=proxy_client)

# --- WEATHER API SETUP ---
API_3H = "https://api.openweathermap.org/data/2.5/forecast"

# 🌎 Coordinates (Munich by default – change to your own city)
weather_parameters = {
    'lat': 48.138561,  # Latitude
    'lon': 11.575430,  # Longitude
    'appid': API_KEY,
    'cnt': 4           # First 4 time intervals (~12 hours)
}

# --- FETCH WEATHER DATA ---
try:
    response_weather = requests.get(API_3H, params=weather_parameters, timeout=10)
    response_weather.raise_for_status()
    data = response_weather.json()
except requests.exceptions.RequestException as e:
    print(f"🚨 Error fetching weather data: {e}")
    exit()

# --- ANALYZE WEATHER CONDITIONS ---
# Check if rain is expected in the next 12 hours
weather_condition = []

for i in range(4):
    weather_id = data['list'][i]["weather"][0]['id']
    # Weather codes below 700 indicate rain, drizzle, or snow
    if weather_id < 700:
        condition = data['list'][i]["weather"][0]['description']
        weather_condition.append(condition)

# Remove duplicates (in case multiple timestamps have the same condition)
weather_condition = list(dict.fromkeys(weather_condition))

# --- CREATE MESSAGE BODY ---
if weather_condition:
    if len(weather_condition) == 1:
        msg_body = (
            f"Panita, hoy tenemos {''.join(weather_condition)} 🌧️!\n"
            f"Better bring your umbrella ☔."
        )
    else:
        msg_body = (
            f"Panita, hoy tendremos {' y '.join(weather_condition)} 🌧️!\n\n"
            f"Don’t forget your umbrella, parce ☂️!"
        )
else:
    msg_body = "Panita, hoy no necesitas umbrella 😎☀️"

# --- SEND WHATSAPP MESSAGE ---
try:
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        body=msg_body,
        to=USER_WHATSAPP
    )
    print(f"✅ Message sent successfully! SID: {message.sid}")
except Exception as e:
    print(f"🚨 Error sending WhatsApp message: {e}")
