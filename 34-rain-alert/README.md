# 🌧️ Weather Alert App (Colombian Style 🇨🇴)

**Hey Panita! 👋**  
This Python app checks the weather forecast using **OpenWeatherMap** and sends you a **WhatsApp alert** through **Twilio** if it’s going to rain.  
Runs perfectly on your computer or automatically on **PythonAnywhere** — so you never forget your umbrella ☔.

---

## 🧠 Features

- Uses **OpenWeatherMap API** for live weather data.  
- Sends **WhatsApp alerts** using **Twilio**.  
- Works **locally and on PythonAnywhere** (with automatic proxy setup).  
- Keeps your credentials secure using `.env` variables.

---

## 🚀 Setup Guide

### 1️⃣ Create the necessary accounts

#### 🌦️ OpenWeatherMap
1. Go to [https://openweathermap.org](https://openweathermap.org)
2. Create a free account
3. Go to your profile → **API Keys**
4. Copy your key (you’ll use it in `.env`)

#### 💬 Twilio
1. Go to [https://www.twilio.com](https://www.twilio.com)
2. Sign up for a free account
3. Activate the **WhatsApp Sandbox**
4. Verify your phone number (you’ll get a code on WhatsApp)
5. Copy your **Account SID** and **Auth Token**

#### 🐍 PythonAnywhere (optional)
1. Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Create a free account
3. Upload this project
4. Schedule it as a **daily task**

---

### 2️⃣ Create your `.env` file

In your `34-rain-alert` folder, create a file called `.env`:

TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth_token
OPENWEATHER_API=your_openweather_api_key
PHONE_NUMBER=whatsapp:+123456789

⚠️ **Never upload your `.env` file to GitHub!**  
Add it to `.gitignore` to keep your credentials private.

---

### 3️⃣ Install dependencies

```bash
pip install requests twilio python-dotenv
```

---

### 4️⃣ Run the app locally
```bash
python rain-alert.py
```
If it’s going to rain, you’ll get a WhatsApp message like:

Panita, hoy tenemos light rain 🌧️!
Better bring your umbrella ☔

---

### 5️⃣ Running on PythonAnywhere

Make sure .env is in the same folder as your .py file.

The app automatically loads it using an absolute path:
```bash
dotenv_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path)
```

---

## ✅ Test manually:
```bash
cd ~/100-python-projects-challenge/34-rain-alert
python3 rain-alert.py
```
🕐 To schedule daily:

Go to your Dashboard → Tasks

Add a new scheduled task:
```bash
python3 /home/yourusername/100-python-projects-challenge/34-rain-alert/rain-alert.py
```

---

## 🧩 Folder Structure
```bash
34-rain-alert/
│
├── rain-alert.py
├── .env
├── .gitignore
└── README.md
```

