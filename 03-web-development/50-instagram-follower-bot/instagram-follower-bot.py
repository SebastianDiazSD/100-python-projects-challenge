"""
instagram-follower-bot.py

Opens Instagram website and signs in.
Asks the user for a topic of interest and opens the account most related to the topic.
Retrieves the people who follow the account and clicks on follow to increase the number of followers of the user account.
After completing the task, the web browser is closed.

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
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from dotenv import load_dotenv

# -------------------------------------------------------
# CONSTANTS
# -------------------------------------------------------
load_dotenv()  # Load .env variables
EMAIL = os.environ.get("INSTAGRAM_EMAIL")  # Your Instagram email
PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")  # Your Instagram password
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")  # Optional Chrome profile path

if not EMAIL or not PASSWORD or not CHROME_DRIVER_PATH:
    raise ValueError("Please check your .env file. Missing EMAIL, PASSWORD, or CHROME_DRIVER_PATH.")

URL_INSTAGRAM = "https://www.instagram.com/"


class InstagramFollowerBot:
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

    def instagram_log_in(self):
        """
        Log in to Instagram and search for the first account related to a topic.
        """
        print("Opening Instagram website... 🇨🇴☕")
        try:
            self.driver.get(URL_INSTAGRAM)
        except Exception as e:
            print(f"[ERROR] Cannot open Instagram: {e}")
            return False

        # Accept cookies if present
        try:
            accept_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Allow all cookies']"))
            )
            accept_btn.click()
            print("Cookies accepted, let's continue. 🍪")
        except TimeoutException:
            print("No cookies popup, moving on...")

        print("Patience, we're logging in... ☕")

        # Username
        email_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        email_field.send_keys(EMAIL)
        print("Username entered, let's keep it going!")

        # Password
        password_field = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(PASSWORD)
        print("Password entered, ready to roll!")

        try:
            sign_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Log in']"))
            )
            sign_button.click()
            print("Login button clicked, waiting... ⏳")
            sleep(10)
            print("Login successful! Bienvenido a Instagram! 😎")
        except:
            print("Already on login page or login not required.")

        # Reject saving account info if present
        try:
            reject_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Not now']"))
            )
            reject_btn.click()
            print("Account info won't be saved for now. 🔒")
        except TimeoutException:
            print("No save account info message, moving on...")

        # Ask for the account/topic to search for
        user_topic = input("¡Ahora sí, parcero!\n¿Qué cuenta o tema quieres buscar? ")

        # Click search button
        try:
            search_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Search']"))
            )
            search_btn.click()
        except TimeoutException:
            print("Search button not available, try later... 😞")
            self.driver.quit()

        # Searching for a topic or account
        try:
            search_field = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Search input']"))
            )
            search_field.send_keys(user_topic)
        except TimeoutException:
            print("Search not available, try later... 😞")
            self.driver.quit()

        # Wait for search results to load and click the first account
        first_result = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "(//span[@dir='auto' and string-length(text()) > 0])[1]"
            ))
        )
        account_name = first_result.text
        print(f"Account found: {account_name}")
        first_result.click()
        print("Account opened... 📖")

        # Check if account is private (look for "This account is private")
        try:
            self.wait.until(EC.presence_of_element_located((
                By.XPATH,
                "//h2[contains(text(),'This account is private')]"
            )))
            print("This account is private, can't see the followers. 😔")
            return  # Exit if account is private
        except TimeoutException:
            print("This account is public, let's grab the followers! 👀")

        # Click the followers count
        try:
            followers_btn = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//span[contains(normalize-space(), 'followers')]"
                ))
            )
            followers_btn.click()
            print("Followers list opened. Let's get to work! 💪")
        except TimeoutException:
            print("Couldn't open followers list, exiting... 😔")
            return

        # Wait for the followers modal to load
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Follow']"))
        )
        print("Followers list loaded, starting to follow... 🚀")

        # Follow each account
        followed = 0
        MAX_FOLLOWS = 10  # Limit to avoid excessive following (be kind to Instagram)

        # Get all the follow buttons visible
        follow_buttons = self.driver.find_elements(
            By.XPATH, "//div[normalize-space()='Follow']"
        )

        for btn in follow_buttons:
            if followed >= MAX_FOLLOWS:
                break

            try:
                btn.click()
                followed += 1
                print(f"Followed user {followed}... ✅")

                # Get the account name
                account_name = btn.find_element(By.XPATH, "../..//span[@dir='auto']").text
                print(f"Followed account: {account_name} 🎉")

                sleep(random.uniform(2, 4))  # Random delay to mimic human behavior
            except TimeoutException:
                continue
            except StaleElementReferenceException:
                continue

        print("Following process completed! 🎯")


# Main function to run the bot
if __name__ == "__main__":
    bot = InstagramFollowerBot(profile_path="path/to/your/chrome/profile")
    bot.instagram_log_in()
