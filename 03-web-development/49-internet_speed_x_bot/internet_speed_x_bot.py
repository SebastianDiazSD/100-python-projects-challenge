"""
internet_speed_x_bot.py

Measures real internet speed using Speedtest.net and compares it against
the ISP's promised contract speed.

If the contract is not met, the bot posts a short, factual complaint on X.

Built calmly, responsibly, and with Colombian patience 🇨🇴☕
"""

import os
import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# -------------------------------------------------------
# CONSTANTS
# -------------------------------------------------------
load_dotenv()  # Load .env variables
EMAIL = os.environ.get("X_EMAIL")  # Your X login email
PASSWORD = os.environ.get("X_PASSWORD")  # Your X password
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")  # Optional Chrome profile
INTERNET_PROVIDER = os.environ.get("ISP")  # e.g., "Telekom"

if not EMAIL or not PASSWORD or not INTERNET_PROVIDER or not CHROME_DRIVER_PATH:
    raise ValueError("Please check your .env file. Missing X_EMAIL, X_PASSWORD, ISP, or CHROME_DRIVER_PATH.")

PROMISED_DOWN = 150.0  # Mbps
PROMISED_UP = 10.0     # Mbps

URL_SPEED_TEST = "https://www.speedtest.net/"
URL_X = "https://x.com/"


class InternetSpeedXBot:
    def __init__(self, profile_path: str | None = None, profile_name: str = "Default"):
        """
        Initialize Selenium Chrome driver.
        """
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # Optional: use existing Chrome profile for cookies & sessions
        if profile_path:
            chrome_options.add_argument(f"--user-data-dir={profile_path}")
            chrome_options.add_argument(f"--profile-directory={profile_name}")

        service = Service()  # Selenium Manager will handle driver

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 60)

        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        """
        Run Speedtest and return download/upload speeds.
        """
        print("Opening Speedtest website... 🇨🇴☕")
        try:
            self.driver.get(URL_SPEED_TEST)
        except Exception as e:
            print(f"[ERROR] Cannot open Speedtest: {e}")
            return False, False, 0.0, 0.0

        # Accept cookies if present
        try:
            accept_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            accept_btn.click()
            print("Cookies accepted.")
        except:
            print("No cookies popup, moving on...")

        # Click GO button to start the test
        go_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.start-text"))
        )
        go_button.click()
        print("Speed test started, please wait...")

        # Wait for test to complete (approx 45 sec)
        sleep(45)

        # Read results
        try:
            down_speed = float(self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.download-speed"))
            ).text)
            up_speed = float(self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.upload-speed"))
            ).text)
        except Exception as e:
            print(f"[ERROR] Failed to read speed values: {e}")
            return False, False, 0.0, 0.0

        print(f"Download: {down_speed} Mbps | Upload: {up_speed} Mbps 🇨🇴☕")

        download_ok = down_speed >= self.down
        upload_ok = up_speed >= self.up

        if not download_ok:
            print(f"Download speed below promised: {down_speed}/{self.down} Mbps. Hora de reclamar, pana!")
        if not upload_ok:
            print(f"Upload speed below promised: {up_speed}/{self.up} Mbps. Hora de reclamar, pana!")

        return download_ok, upload_ok, down_speed, up_speed

    def complain_on_x(self, download_ok, upload_ok, down_speed, up_speed):
        """
        Login to X and post a complaint if internet is slow.
        """
        if download_ok and upload_ok:
            print("Internet speed is fine. No complaint needed. 🇨🇴☕")
            return

        messages = [
            f"{INTERNET_PROVIDER} Network speed below contract: "
            f"{down_speed}/{up_speed} Mbps vs promised {self.down}/{self.up}. Please investigate.",
            f"{INTERNET_PROVIDER} Contracted speed not met. "
            f"Current: {down_speed}/{up_speed} Mbps.",
            f"{INTERNET_PROVIDER} Internet speed below agreement. "
            f"Measured {down_speed}/{up_speed} Mbps."
        ]

        print("Opening X website...")
        self.driver.get(URL_X)
        sleep(5)

        # Accept cookies if present
        try:
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Accept all cookies']"))
            ).click()
            print("Cookies accepted. Patience is key 🇨🇴☕")
        except:
            print("No cookie popup, moving on...")

        # Click Sign in
        try:
            sign_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign in']"))
            )
            sign_button.click()
            print("Sign in clicked, waiting for login fields...")
            sleep(3)
        except:
            print("Already on login page or sign in not required.")

        # Enter email
        email_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='text']"))
        )
        email_field.send_keys(EMAIL)
        sleep(2)

        # Click Next button
        next_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
        )
        next_button.click()

        # Enter password
        password_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_field.send_keys(PASSWORD)
        sleep(3)

        # Click Log in
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
        )
        login_button.click()

        # Close annual plan popup if present
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//svg[contains(@class,'r-yyyyoo')]"))
            )
            close_btn.click()
            print("Closed annual plan popup 🇨🇴☕")
        except:
            print("No annual plan popup detected.")

        # Post the complaint
        tweet_box = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'public-DraftStyleDefault-block')]//span")
            )
        )
        tweet_box.click()
        tweet_box.send_keys(random.choice(messages))
        print("Complaint typed, ready to post...")

        post_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Post']"))
        )
        post_button.click()
        print("Complaint posted successfully! 🇨🇴☕")

    def close(self):
        """
        Close the browser.
        """
        self.driver.quit()


# -------------------------------------------------------
# RUN BOT
# -------------------------------------------------------
if __name__ == "__main__":
    bot = InternetSpeedXBot(profile_path=CHROME_DRIVER_PATH)
    down_ok, up_ok, down_speed, up_speed = bot.get_internet_speed()
    bot.complain_on_x(down_ok, up_ok, down_speed, up_speed)
    # bot.close()
