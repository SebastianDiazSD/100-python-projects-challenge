# Cookie Clicker Automation Bot 🍪

## Overview

This project is part of my **100 Python Projects Challenge** and demonstrates browser automation using **Python and Selenium**.

The bot automatically plays **Cookie Clicker**, continuously clicking the main cookie and making optimized upgrade decisions based on real-time availability.

The automation is designed to be resilient against modern UI behavior such as dynamic loading, overlays, and consent banners.

---

## Motivation

I am a **Colombian civil engineer transitioning into software development**, with the goal of building scalable, automation-driven solutions and eventually launching my own technology business.

This project applies traditional engineering principles—such as optimization, timing control, and resource allocation—to browser automation and decision-making systems.

---

## Features

- Automated browser control using Selenium
- Dynamic language selection handling
- Automatic cookie-consent overlay detection
- Continuous cookie production
- Smart upgrade purchasing strategy
- Time-based decision system
- Defensive programming against UI changes
- Clean, modular, and readable code

---

## Strategy Explanation

Instead of purchasing upgrades randomly or choosing the cheapest option, the bot follows this strategy:

1. Clicks continuously to maximize base production
2. Every few seconds, evaluates all available upgrades
3. Purchases the **most expensive affordable upgrade**
4. Repeats the process for a fixed simulation period

This approach reflects engineering optimization logic:
fewer decisions, higher long-term yield.

---

## Technologies Used

- Python 3
- Selenium WebDriver
- Google Chrome
- Time-based automation logic

---

## How to Run

1. Install dependencies:
   ```bash
   pip install selenium
   ```
2.Ensure Google Chrome is installed.
3. Run the script:
  ```bash
  python main.py
  ```
4. The browser will open automatically and run the simulation for 5 minutes.

## Notes

* This project uses an open-source mirror of Cookie Clicker to avoid bot-protection mechanisms.
* The browser remains open after execution for inspection and learning purposes.
* This project is intended for educational and portfolio use.
