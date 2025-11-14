import requests
from datetime import datetime
import os

# ---------------------------------------------------------------
#  Exercise Tracker – Project 37 (Colombian Flavor Edition)
# ---------------------------------------------------------------
#  This script uses the Nutritionix API to analyze natural-language
#  exercise descriptions and then logs the results into a Google Sheet
#  via the Sheety API.
# ---------------------------------------------------------------

# --- Personal Info (Used by Nutritionix for calorie estimation) ---
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

# --- Environment Variables (Replace with your own in .env) ---
APP_ID = os.environ.get("ENV_NIX_APP_ID")
API_KEY = os.environ.get("ENV_NIX_API_KEY")
SHEETY_ENDPOINT = os.environ.get("ENV_SHEETY_ENDPOINT")
SHEETY_USERNAME = os.environ.get("ENV_SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("ENV_SHEETY_PASSWORD")

# Quick validation to help beginners
missing = [v for v in [APP_ID, API_KEY, SHEETY_ENDPOINT] if not v]
if missing:
    raise EnvironmentError("Parce, you're missing some environment variables. Check your .env file!")

# --- Nutritionix API Endpoint ---
nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

# --- User Prompt (Colombian flavor) ---
print("\nBienvenido parcero! Let's track your workout with some Colombian flow. 🇨🇴🔥")
exercise_text = input("Tell me which exercises you did hoy: ")

# --- Nutritionix Request ---
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

print("\nHold on parcero… I'm checking how many calories you burned 😎🔥\n")
response = requests.post(nutritionix_url, json=params, headers=headers)

try:
    result = response.json()
except ValueError:
    print("Uy no… Nutritionix sent back something weird:")
    print(response.text)
    exit()

# --- Timestamp ---
now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X")

# --- Loop through exercises and log to Sheety ---
for exercise in result.get("exercises", []):
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety request with Basic Auth
    response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
    )

    print("✔️  Added to your workout sheet — buena esa, parcero!")
    print(f"Sheety says: {response.text}\n")

print("Listo pues! Your workout has been fully logged. 🏋️‍♂️🇨🇴✨")
