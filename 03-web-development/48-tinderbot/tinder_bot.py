"""
Tinder Auto-Swipe Bot
48 Python Challenge – Day 48

Author: Your Name
Description:
A simple Tinder automation bot built with Selenium and undetected-chromedriver.
Uses an existing Chrome profile to avoid repeated logins.

Disclaimer:
This project is for educational purposes only.
Automating Tinder may violate their Terms of Service.
Use at your own risk, parcero 😉
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep


class TinderBot:
    """
    TinderBot handles browser setup, navigation, and automated swiping.
    """

    def __init__(self, profile_path: str, profile_name: str = "Default"):
        """
        Initialize the Chrome driver with an existing user profile.

        :param profile_path: Path to the Chrome user data directory
        :param profile_name: Chrome profile directory name (default: "Default")
        """
        # Chrome options configuration (suavecito but effective)
        self.options = uc.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_argument(f"--user-data-dir={profile_path}")
        self.options.add_argument(f"--profile-directory={profile_name}")

        # Helps reduce automation detection (porque nadie quiere ser pillado)
        self.options.add_argument("--disable-blink-features=AutomationControlled")

        # Initialize the undetected Chrome driver
        self.driver = uc.Chrome(options=self.options)

    def open_tinder(self):
        """
        Open Tinder homepage.
        """
        self.driver.get("https://tinder.com")

        # Give the page time to load (sin afán)
        sleep(5)

    def auto_swipe(self, xpath: str, delay: float = 1.0):
        """
        Automatically click the swipe button indefinitely.

        :param xpath: XPath of the swipe (like) button
        :param delay: Time delay between swipes in seconds
        """
        try:
            swipe_button = self.driver.find_element(By.XPATH, xpath)

            while True:
                swipe_button.click()
                sleep(delay)

        except Exception as e:
            # Catch any unexpected issues (cuando algo se daña, se dice y ya)
            print(f"[ERROR] {e}")

    def close(self):
        """
        Close the browser and end the session.
        """
        self.driver.quit()


# =========================
# Main Execution
# =========================
if __name__ == "__main__":
    # Path to your Chrome profile (adjust to your system)
    PROFILE_PATH = r"C:\ScrapingProfiles\TinderProfile"

    # XPath for the Tinder "Like" button (may change over time)
    SWIPE_XPATH = (
        '//*[@id="main-content"]/div[1]/div/div/div/div[1]'
        '/div/div/div[4]/div/div[4]/button'
    )

    # Create bot instance
    bot = TinderBot(profile_path=PROFILE_PATH)

    # Open Tinder
    bot.open_tinder()

    # Start auto-swiping (ojo: infinite loop)
    bot.auto_swipe(xpath=SWIPE_XPATH)

    # Keep browser open until user decides to exit
    input("Press Enter to close the browser... (tranqui, sin estrés)")

    # Close browser
    bot.close()
