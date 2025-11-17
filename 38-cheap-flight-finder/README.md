# ✈️ Cheap Flight Finder (Colombian Flavor Edition 🇨🇴🔥)

**Welcome, parcero!**  
This project combines Projects 38 & 39 of the 100 Days of Python Challenge into one app:
a Cheap Flight Finder that searches Amadeus for fares, logs data to Google Sheets via Sheety,
and notifies subscribers by **email** (Gmail). OpenAI optional for natural-language queries.

---

## Features

- Search Amadeus for flights (direct and indirect), up to 6 months ahead.
- Store cities, IATA codes, and current lowest prices in a Google Sheet (via Sheety).
- Store subscriber emails in a separate Google Sheet.
- Automatically update the sheet when a lower price is found.
- Send email alerts to all subscribers when a cheaper fare is detected.
- Optional OpenAI natural-language interface: ask plain questions like:
  - "What are the cheapest flights from Madrid to Paris on June 1st?"
- Friendly messages and comments with a Colombian flavor 🇨🇴 — without sacrificing global readability.

---

## Project layout

```bash
📦 cheap-flight-finder
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── flight_query_ai.py # optional: OpenAI integration
└── README.md
```

---

## Quick start

1. Clone:
```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 38-cheap-flight-finder
```
2. Install:
```bash
pip install -r requirements.txt
```
3. Create a .env file in the project root with the following template (replace placeholders):
```bash
# SHEETY
SHEETY_PRICES_ENDPOINT=https://api.sheety.co/xxxxx/cheapFlightFinder/prices
SHEETY_USERS_ENDPOINT=https://api.sheety.co/xxxxx/cheapFlightFinder/users
SHEETY_USERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password

# AMADEUS
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_SECRET=your_amadeus_api_secret

# EMAIL (GMAIL)
EMAIL_PROVIDER_SMTP_ADDRESS=smtp.gmail.com
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_gmail_app_password   # Use App Password!

# OPTIONAL: Twilio (if you want SMS/WhatsApp)
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_VIRTUAL_NUMBER=+123456789
TWILIO_VERIFIED_NUMBER=+123456789
TWILIO_WHATSAPP_NUMBER=+14155238886

# OPTIONAL: OPENAI
OPENAI_API_KEY=your_openai_key

# OPTIONAL: The origin IATA code (default is LON)
ORIGIN_CITY_IATA=LON
```
Important: never commit your real .env to GitHub. Add .env to .gitignore.

---

## Google Sheets setup (Sheety)

Create two Google Sheets tabs and expose them via Sheety:

1. Prices sheet (tab name e.g., prices) — must include:
  - city (text)
  - iataCode (text)
  - lowestPrice (number)
  - Sheety will expose as /prices

2. Users sheet (tab name e.g., users) — must include:
 - firstName
 - lastName
 - email
 - Sheety will expose as /users

Set SHEETY_PRICES_ENDPOINT and SHEETY_USERS_ENDPOINT in your .env to the correct Sheety URLs.

---

## Gmail notes (sending emails)

* Use a Gmail App Password (create it from Google Account > Security > App passwords).
* Put the app password into MY_EMAIL_PASSWORD. Do NOT use your Google account password directly.
* SMTP server: smtp.gmail.com port 587 (STARTTLS).

---

## OpenAI notes (optional)
If using natural-language parsing (flight_query_ai.py), set OPENAI_API_KEY in .env.
The AI will extract origin/destination and date (if present) then main will run a focused search.

---

## Final notes & suggestions (important)
- I **did not** include any real API keys or tokens. Use the `.env` template and put your credentials there.
- For Gmail, create an **App Password** (recommended) and place it in `MY_EMAIL_PASSWORD`.
- If Amadeus returns unexpected errors when using GET for `flight-offers`, switch to POST with the JSON body as per Amadeus docs.
- Make sure your Sheety endpoints point to the correct sheet/tab names (`prices` and `users`).
