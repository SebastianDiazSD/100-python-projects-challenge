import os
import requests
from bs4 import BeautifulSoup
import smtplib


# -------------------------------------------------------
# Environment Variables (stored in .env or system env)
# -------------------------------------------------------
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
RECEIVER = os.environ.get("RECEIVER")

# Product URL to track
URL = (
    "https://www.amazon.de/-/en/Display-MediaTek-Dimensity-Android-Seafoam/dp/"
    "B0DJW9CD7H?th=1"
)

# -------------------------------------------------------
# Create a session with headers to simulate a real browser
# -------------------------------------------------------
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
})

# -------------------------------------------------------
# Request product page
# -------------------------------------------------------
try:
    response = session.get(URL, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"⚠ Error loading page: {e}")
    raise SystemExit

# -------------------------------------------------------
# Parse the webpage with BeautifulSoup
# -------------------------------------------------------
soup = BeautifulSoup(response.text, "html.parser")

product_title_tag = soup.find("span", id="productTitle")
price_whole = soup.find("span", class_="a-price-whole")
price_fraction = soup.find("span", class_="a-price-fraction")

product_title = product_title_tag.get_text(strip=True) if product_title_tag else "Unknown product"

# -------------------------------------------------------
# Extract the price (Amazon uses whole + fraction)
# -------------------------------------------------------
if price_whole:
    # Combine whole + fractional part
    raw_price = f"{price_whole.get_text()}{price_fraction.get_text() if price_fraction else '00'}"
    # Remove formatting (, or . depending on locale)
    clean_price = raw_price.replace(",", "").replace(".", "")
    # Convert cents to decimal
    price = float(clean_price) / 100
else:
    price = None

print(f"Product: {product_title}")
print(f"Current price: €{price}")

# -------------------------------------------------------
# Send email if price below threshold
# -------------------------------------------------------
PRICE_THRESHOLD = 350.00  # Your chosen alert price

if price and price < PRICE_THRESHOLD:

    message = (
        f"Subject: Price Alert! 🎉\n\n"
        f"Good news! The product *{product_title}* is now priced at €{price}.\n"
        f"Check it out here:\n{URL}\n\n"
        f"— Automated price tracker 🇨🇴"
    )

    try:
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=RECEIVER,
                msg=message.encode("utf-8")   # Ensure UTF-8 support
            )
        print("📬 Notification sent successfully!")

    except smtplib.SMTPException as e:
        print(f"⚠ Email sending failed: {e}")
else:
    print("No email sent — price above threshold.")
