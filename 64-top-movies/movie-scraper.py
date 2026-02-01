import os
import csv
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# -------------------------------------------------------
# CONFIG
# -------------------------------------------------------
load_dotenv()
GECKO_DRIVER_PATH = os.environ.get("GECKO_DRIVER_PATH")
URL = "https://www.shortlist.com/"
CSV_FILE = "streaming_content.csv"

if not GECKO_DRIVER_PATH:
    raise ValueError("❌ Missing GECKO_DRIVER_PATH")

# -------------------------------------------------------
class MustWatchHybrid:

    def __init__(self, profile_path: str | None = None):
        print("🚀 Initializing browser...")
        firefox_options = Options()
        firefox_options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications
        firefox_options.add_argument("--start-maximized")
        firefox_options.add_argument("--disable-blink-features=AutomationControlled")
        firefox_options.binary_location = '/usr/bin/firefox'  # Adjust if needed

        if profile_path:
            firefox_options.set_preference("profile", profile_path)

        service = Service(GECKO_DRIVER_PATH)
        self.driver = webdriver.Firefox(service=service, options=firefox_options)
        self.wait = WebDriverWait(self.driver, 60)

        self.data = []

    # ---------------------------------------------------
    # UI HELPERS
    # ---------------------------------------------------
    # def handle_cookies(self):
    #     print("🍪 Handling cookies...")
    #     try:
    #         self.wait.until(EC.element_to_be_clickable(
    #             (By.XPATH, "//button[contains(., 'Agree')]")
    #         )).click()
    #         print("✅ Cookies accepted")
    #     except:
    #         print("⚠️ Please accept cookies manually")
    #         sleep(5)

    # def handle_modal(self):
    #     print("📢 Handling modal...")
    #     try:
    #         self.driver.find_element(
    #             By.XPATH,
    #             "//button[contains(@class,'exit-intent__close-button')]"
    #         ).click()
    #         print("✅ Modal closed")
    #     except:
    #         print("ℹ️ No modal found")

    # ---------------------------
    # MANUAL HANDLING HELPERS
    # ---------------------------
    def handle_cookies(self):
        try:
            agree_btn = self.driver.find_element(By.XPATH,
                                                     "//button[contains(text(),'Agree') or @aria-label='Agree']")
            agree_btn.click()
            print("✅ Cookies agreed (automatic)")
        except:
            print("⚠️ Please accept cookies manually in the browser window...")
            self.wait_until_gone("//button[contains(text(),'Agree') or @aria-label='Agree']")
            print("✅ Cookies accepted (manual)")

    def handle_modal(self):
        try:
            close_btn = self.driver.find_element(By.XPATH, "//button[contains(@class,'exit-intent__close-button')]")
            close_btn.click()
            print("✅ Modal closed (automatic)")
        except:
            print("⚠️ Please close the modal window manually if it is open...")
            self.wait_until_gone("//button[contains(@class,'exit-intent__close-button')]")
            print("✅ Modal closed (manual)")

    def wait_until_gone(self, xpath):
        while True:
            try:
                self.driver.find_element(By.XPATH, xpath)
                sleep(1)
            except:
                break

    def wait_for_manual_click(self, xpath):
        while True:
            try:
                el = self.driver.find_element(By.XPATH, xpath)
                sleep(1)
            except:
                break

    def navigate(self):
        print("🌐 Opening Shortlist...")
        self.driver.get(URL)
        print("🌐 Waiting for elements to load...un tantito...")
        sleep(4)

        self.handle_cookies()
        self.handle_modal()

        # Click Entertainment (manual if needed)
        print("🎬 Navigating to Entertainment...")
        try:
            ent_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Entertainment']")))
            ent_button.click()
            print("✅ Entertainment opened")
        except:
            print("⚠️ Please click 'Entertainment' manually in the browser...")
            self.wait_for_manual_click("//a[text()='Entertainment']")
            print("✅ Entertainment opened manually")

        # Click What to Watch
        print("📺 Navigating to What to Watch...")
        try:
            watch_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='What to Watch']")))
            watch_button.click()
            print("✅ What to Watch section opened")
        except:
            print("⚠️ Please click 'What to Watch' manually in the browser...")
            self.wait_for_manual_click("//a[text()='What to Watch']")
            print("✅ What to Watch section opened manually")

        print("⏳ Waiting for article to load...")
        self.wait.until(EC.presence_of_element_located((By.ID, "article-body")))
        sleep(3)

    # ---------------------------------------------------
    # PARSING WITH BEAUTIFULSOUP
    # ---------------------------------------------------
    def parse_content(self):
        print("🔍 Parsing page content...")
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        article = soup.find("div", id="article-body")

        h2s = article.find_all("h2")
        print(f"ℹ️ Found {len(h2s)} titles")

        for h2 in h2s:
            title = h2.get_text(strip=True)
            if not title:
                continue

            print(f"➡️ Scraping: {title}")

            item = {
                "title": title,
                "image_url": None,
                "image_credit": None,
                "description": None,
                "watch_link": None
            }

            current = h2

            # walk forward until next h2
            while True:
                current = current.find_next_sibling()
                if not current or current.name == "h2":
                    break

                # IMAGE + CREDIT
                if current.name == "figure" and not item["image_url"]:
                    img = current.find("img")
                    if img:
                        item["image_url"] = img.get("src")

                    credit = current.find("div", class_="credit")
                    if credit:
                        item["image_credit"] = (
                            credit.get_text(strip=True)
                            .replace("Image credit:", "")
                            .replace("Image Credit:", "")
                            .strip("() ")
                        )

                # DESCRIPTION (first paragraph after figure)
                if current.name == "p" and not item["description"]:
                    text = current.get_text(strip=True)
                    if len(text) > 40:
                        item["description"] = text

                # STREAMING LINK
                if current.name == "ul" and not item["watch_link"]:
                    a = current.find("a", href=True)
                    if a:
                        item["watch_link"] = a["href"]

            self.data.append(item)

        print(f"✅ Retrieved {len(self.data)} items")

    # ---------------------------------------------------
    def save_csv(self):
        print("💾 Saving CSV...")
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)
        print(f"✅ Saved to {CSV_FILE}")

    def run(self):
        self.navigate()
        self.parse_content()
        self.save_csv()
        self.driver.quit()
        print("🏁 Done!")


if __name__ == "__main__":
    MustWatchHybrid().run()
