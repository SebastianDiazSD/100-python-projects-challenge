# Instagram Follower Bot 🇨🇴

This Python bot automatically logs in to Instagram, searches for an account based on a topic, and follows users who follow the account. The script ensures that users are followed responsibly with randomized delays to avoid detection.

---

## Features

- Opens Instagram and logs in
- Accepts cookies if present
- Searches for a topic or account
- Clicks on the account with the most relevant results
- Opens followers list and follows users
- Handles private accounts gracefully

---

## Requirements

- Python 3.x
- Selenium (`pip install selenium`)
- ChromeDriver (make sure to match your Chrome version)
- `.env` file with Instagram credentials (`INSTAGRAM_EMAIL`, `INSTAGRAM_PASSWORD`, and `CHROME_DRIVER_PATH`)

---

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   ```
2. Create a **.env** file in the project root and add your Instagram credentials::
   ```bash
   INSTAGRAM_EMAIL=your_email@example.com
   INSTAGRAM_PASSWORD=your_password
   CHROME_DRIVER_PATH=/path/to/your/chromedriver
   ```
3. Run the script:
   ```bash
   python instagram-follower-bot.py
   ```

---

## Disclaimer

Use responsibly. Instagram may block or suspend accounts for excessive automation. Always follow Instagram's terms of service.
