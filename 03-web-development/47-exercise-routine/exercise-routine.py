import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------------------------------------------
# 🇨🇴 CONFIGURATION (Test data only – no real credentials)
# -------------------------------------------------------------------

GYM_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = "sebastian_ad@test.com"
ACCOUNT_PASSWORD = "password123"

TARGET_DAYS = ("Tue", "Thu")
TARGET_TIME = "6:00 PM"

# -------------------------------------------------------------------
# 🚀 SELENIUM SETUP
# -------------------------------------------------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Give Selenium its own Chrome profile (like having your own "parche")
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 3)

driver.get(GYM_URL)
time.sleep(3)  # Allow JS-heavy content to load

# -------------------------------------------------------------------
# 🔁 RETRY HELPER (Because life — and Selenium — happens)
# -------------------------------------------------------------------

def retry(action, retries=5, description="action"):
    for attempt in range(1, retries + 1):
        try:
            print(f"🔄 Trying {description} (attempt {attempt})")
            return action()
        except TimeoutException:
            if attempt == retries:
                raise
            time.sleep(1)

# -------------------------------------------------------------------
# 🔐 LOGIN FLOW
# -------------------------------------------------------------------

def login():
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    driver.find_element(By.ID, "submit-button").click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

retry(login, description="login")

# -------------------------------------------------------------------
# 🏋️ CLASS BOOKING LOGIC
# -------------------------------------------------------------------

def book_class(button):
    button.click()
    wait.until(lambda d: button.text in ("Booked", "Waitlisted"))

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked = waitlisted = already_done = 0
processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id,'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if any(day in day_title for day in TARGET_DAYS):
        class_time = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

        if TARGET_TIME in class_time:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            class_info = f"{class_name} on {day_title}"

            if button.text in ("Booked", "Waitlisted"):
                print(f"✔ Already set: {class_info}")
                already_done += 1
            else:
                retry(lambda: book_class(button), description="class booking")
                if button.text == "Booked":
                    print(f"✅ Booked: {class_info}")
                    booked += 1
                else:
                    print(f"🕒 Waitlisted: {class_info}")
                    waitlisted += 1

            processed_classes.append(class_info)
            time.sleep(0.5)

# -------------------------------------------------------------------
# 📋 VERIFY BOOKINGS
# -------------------------------------------------------------------

def open_my_bookings():
    wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))
    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    if not cards:
        raise TimeoutException("No booking cards found")
    return cards

booking_cards = retry(open_my_bookings, description="open my bookings")

verified = 0
for card in booking_cards:
    try:
        when_text = card.find_element(By.XPATH, ".//p[strong[text()='When:']]").text
        if any(day in when_text for day in TARGET_DAYS) and TARGET_TIME in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"🔍 Verified: {class_name}")
            verified += 1
    except NoSuchElementException:
        continue

expected = booked + waitlisted + already_done

print("\n-----------------------------")
print("📊 FINAL RESULT")
print(f"Expected bookings: {expected}")
print(f"Verified bookings: {verified}")

if expected == verified:
    print("🎉 SUCCESS: All classes verified. ¡Todo bien parce!")
else:
    print(f"❌ Mismatch detected: {expected - verified} missing")