"""
Zillow Clone Real Estate Automation
Author: Sebastian Arce
Purpose: Educational & portfolio project

🇨🇴 Colombian note:
This project intentionally uses a Zillow clone with static data
to demonstrate web scraping and browser automation in an ethical,
stable, and reproducible way.
"""

# -------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_FORM = os.getenv("GOOGLE_FORM")

if not GOOGLE_FORM:
    raise ValueError("Missing GOOGLE_FORM in .env file")

# Tested with:
# beautifulsoup4==4.12.2
# requests==2.31.0
# selenium==4.15.1

# -------------------------------------------------------
# IMPORTS
# -------------------------------------------------------
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# -------------------------------------------------------
# PART 1 — SCRAPE DATA FROM ZILLOW CLONE
# -------------------------------------------------------

print("🇨🇴 Zillow Clone – Real Estate Automation")
print("ℹ️ This dataset contains static sample listings (San Francisco only).\n")

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(ZILLOW_CLONE_URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# 🇨🇴 All listings are static and predefined in the clone
listing_cards = soup.select(".StyledPropertyCardDataWrapper")

addresses = []
prices = []
links = []

for card in listing_cards:
    address = card.select_one("address").get_text(strip=True)
    price = card.select_one("span").get_text(strip=True)
    link = card.select_one("a")["href"]

    # 🇨🇴 Clean price text for consistency
    clean_price = price.replace("/mo", "").split("+")[0]

    addresses.append(address)
    prices.append(clean_price)
    links.append(link)

print(f"✅ {len(addresses)} listings extracted successfully\n")

# -------------------------------------------------------
# PART 2 — GOOGLE FORM AUTOMATION (SELENIUM)
# -------------------------------------------------------

# 🇨🇴 Selenium is used here to simulate real-world data entry jobs
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(addresses)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)

    # 🇨🇴 XPath selectors may vary depending on the Google Form structure
    address_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]//input'
    )
    price_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]//input'
    )
    link_input = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]//input'
    )
    submit_button = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    )

    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])

    submit_button.click()
    time.sleep(1)

print("🇨🇴 Automation completed successfully")
