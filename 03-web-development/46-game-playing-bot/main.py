from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep, time

# ======================================================
# Project Configuration
# ======================================================

GAME_URL = "https://ozh.github.io/cookieclicker/"
DECISION_INTERVAL = 5          # Seconds between upgrade decisions
SIMULATION_DURATION = 60 * 5   # Total runtime: 5 minutes

# ======================================================
# Driver Setup
# ======================================================

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(GAME_URL)

# Allow JS-heavy assets to load
sleep(3)

# ======================================================
# Utility Functions
# ======================================================

def select_language():
    """
    Select English language if the selector is present.
    Depending on cache/session, this may not appear.
    """
    try:
        print("Configuring language settings...")
        language_button = driver.find_element(By.ID, "langSelect-EN")
        language_button.click()
        sleep(2)
        print("Language set to English.")
    except NoSuchElementException:
        print("Language selector not found. Continuing...")


def accept_cookies_if_present():
    """
    Accept cookie consent banner if present.
    Prevents UI overlays from intercepting clicks.
    """
    try:
        consent_button = driver.find_element(
            By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all"
        )
        consent_button.click()
        sleep(1)
        print("Cookie consent accepted.")
    except NoSuchElementException:
        pass


def get_big_cookie():
    """Return the main cookie used for production."""
    return driver.find_element(By.ID, "bigCookie")


def buy_best_affordable_upgrade():
    """
    Purchase the most expensive enabled upgrade available.
    Strategy inspired by engineering optimization:
    prioritize long-term production efficiency.
    """
    products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")

    for product in reversed(products):
        if "enabled" in product.get_attribute("class"):
            try:
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    product
                )
                sleep(0.2)
                product.click()
                return product.get_attribute("id")
            except ElementClickInterceptedException:
                accept_cookies_if_present()
                return None
    return None


def get_cookie_status():
    """Return current cookie production text."""
    return driver.find_element(By.ID, "cookies").text


# ======================================================
# Execution
# ======================================================

select_language()
sleep(2)

accept_cookies_if_present()

cookie = get_big_cookie()

next_decision_time = time() + DECISION_INTERVAL
simulation_end = time() + SIMULATION_DURATION

print("\nAutomation started. Optimizing cookie production...\n")

while True:
    cookie.click()

    if time() >= next_decision_time:
        try:
            purchased_item = buy_best_affordable_upgrade()
            if purchased_item:
                print(f"Purchased upgrade: {purchased_item}")
        except NoSuchElementException:
            print("Upgrade elements temporarily unavailable.")

        next_decision_time = time() + DECISION_INTERVAL

    if time() >= simulation_end:
        try:
            print("\nSimulation completed.")
            print(f"Final production status: {get_cookie_status()}")
        except NoSuchElementException:
            print("Could not retrieve final cookie count.")
        break
