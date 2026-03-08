# X Internet Speed Complaint Bot 🇨🇴☕

This Python project checks your internet speed and automatically posts a complaint on **X** (formerly Twitter) if your ISP is not delivering the promised speeds.

It’s project 49 of the **100 Python Projects Challenge** and includes a **Colombian touch** in comments and print messages 🇨🇴☕.

---

## Features

- Measures **download and upload speeds** using [Speedtest.net](https://www.speedtest.net/).
- Compares measured speeds against **your ISP’s promised speeds**.
- Logs into **X** and posts a complaint automatically if speeds are below expectations.
- Handles **cookies, login, and popups** on X.
- Built for clarity, reliability, and a Colombian sense of patience ☕.

---

## Requirements

- Python 3.10+
- Selenium (`pip install selenium`)
- Chrome browser installed
- Optional: Chrome profile path to keep cookies/session

---

## Environment Variables

Set these variables before running the bot:

```bash
export X_EMAIL="your_email@example.com"
export X_PASSWORD="your_x_password"
export CHROME_DRIVER_PATH="path_to_chrome_user_data"  # Optional
export ISP="Your ISP Name"
```

---

## Usage

```bash
python internet_speed_x_bot.py
```

The bot will:

1. Open Speedtest.net and measure your speeds.
2. Compare them with your ISP’s promised speeds.
3. Log in to X if speeds are too low.
4. Post a complaint with a random prewritten message.

---

## Example Output

```mathematica
Opening Speedtest website... 🇨🇴☕
Download: 120 Mbps | Upload: 8 Mbps 🇨🇴☕
Download speed below promised: 120/150 Mbps. Hora de reclamar, pana!
Opening X website...
Cookies accepted. Patience is key 🇨🇴☕
Sign in clicked, waiting for login fields...
Closed annual plan popup 🇨🇴☕
Complaint typed, ready to post...
Complaint posted successfully! 🇨🇴☕
```

---

## Notes

- Adjust PROMISED_DOWN and PROMISED_UP for your ISP.
- The bot uses WebDriverWait to avoid crashing if elements take time to load.
- Ensure your network is stable; long timeouts can happen on slow connections.
