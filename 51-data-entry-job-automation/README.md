# 🏠 Zillow Clone Real Estate Automation

🇨🇴 *An ethical and stable automation project for data entry and web scraping.*

---

## 📌 Project Overview

This project automates the process of:

1. Extracting real estate listing data (address, price, and link)
2. Cleaning and structuring the extracted data
3. Automatically submitting the data into a Google Form

The project is designed as a **portfolio-quality demonstration of web scraping
and browser automation**, inspired by real-world data entry workflows.

---

## ⚠️ Important Note About the Dataset

This project **does NOT scrape the real Zillow website**.

Instead, it uses a **public Zillow clone** with:
- Static HTML
- Predefined listings
- Sample data (San Francisco area)

### Why this approach?

Modern platforms like Zillow.com use advanced protections such as:
- Persistent CAPTCHAs
- Behavioral bot detection
- Dynamic JavaScript rendering

For ethical and educational reasons, this project demonstrates the automation
architecture using a **safe and reproducible clone**.

> The focus is on automation skills — not bypassing protections.

---

## 🧠 What This Project Demonstrates

- Web scraping with **BeautifulSoup**
- HTTP requests using **Requests**
- Browser automation with **Selenium**
- Automated form submission
- Environment variable management with **dotenv**
- Clean, readable Python code

---

## 🏗️ Technologies Used

- Python 3
- Requests
- BeautifulSoup
- Selenium
- Google Forms
- python-dotenv

---

## ▶️ How It Works

1. The script fetches listing data from the Zillow Clone
2. All available listings are parsed and cleaned
3. Each listing is automatically entered into a Google Form
4. The process repeats until all entries are submitted

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 51-data-entry-job-automation
```
### 2. Create a .env File
```bash
GOOGLE_FORM=your_google_form_url_here
```
### 3. Run the Script
```bash
python data_entry_automation.py
```

---

## 🌎 Colombian Touch 🇨🇴

This project is inspired by the challenges of automating repetitive data tasks
commonly found in real-world jobs across both U.S. and Colombian markets.

The goal is responsible automation — clean, transparent, and ethical.

---

## 📈 Future Improvements

Replace Google Forms with Google Sheets API

Add data validation and logging

Store extracted data in CSV or database

Adapt the pipeline for other static datasets

Convert into a Playwright QA automation project
