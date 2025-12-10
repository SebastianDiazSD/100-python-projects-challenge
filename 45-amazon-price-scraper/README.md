# 🇨🇴 Amazon Price Tracker (Python Project 45/100)

A simple and effective Amazon price-tracking tool built in Python.  
The script checks the current price of a specific product on Amazon and automatically sends you an email when it drops below a chosen threshold.

Made with ☕ and pride in Colombia 🇨🇴

---

## ✨ Features

- Scrapes live product price data from Amazon using `requests` + `BeautifulSoup`.
- Automatically sends you an email alert when the price drops.
- Uses environment variables for secure credential handling.
- Fully customizable thresholds and URLs.
- Lightweight and easy to deploy anywhere.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- `requests`
- `beautifulsoup4`
- `smtplib`
- SMTP (configured for Outlook in this version)

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 45-amazon-price-scraper
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a .env file (or set system environment variables):

```bash
EMAIL=your_outlook_email
PASSWORD=your_app_password
RECEIVER=your_notification_email
```

⚠️ Never commit your credentials — keep your .env out of GitHub.

---

## ▶️ Usage

Edit the product URL and the PRICE_THRESHOLD inside the script, then run:

```bash
python main.py
```

If the price is below the configured threshold, you'll receive an email like:
    ✉️ Price Alert! Your product is now cheaper — go get it!

---

## 📝 Example Output

```bash
Product: Sample Smartphone XYZ
Current price: €299.99
📬 Notification sent successfully!
```

---

## 🤓 Notes

* Amazon HTML changes frequently, so you may need to adjust the selectors in the future.
* For Gmail users, remember to use an App Password.
* Web scraping Amazon is allowed only for personal use — be mindful.
