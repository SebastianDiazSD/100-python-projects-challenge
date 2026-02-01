# 🎬 Movie Night Picker (Flask + Selenium)

A full-stack Python project that scrapes curated movie recommendations, stores them in a database, and serves them through an interactive web interface.

No algorithms.  
No tracking.  
Just good movies — con sabor.

---

## 🚀 Features

- 🕷️ **Web scraping** with Selenium + BeautifulSoup
- 📄 Data exported to CSV
- 🗄️ Database powered by SQLAlchemy (SQLite)
- 🎲 Random movie selection on every refresh
- 🃏 Interactive flip cards (CSS only)
- ❤️ Favorites system
- ✍️ User reviews
- 🌎 Clean English UI with subtle Colombian flavor

---

## 🧱 Tech Stack

- Python 3.12
- Flask
- Flask-Bootstrap
- SQLAlchemy
- Selenium (Firefox)
- BeautifulSoup
- SQLite
- HTML / CSS (CSS Grid + animations)

---

## 📁 Project Structure
```bash
├── main.py # Flask application
├── movie-scraper.py # Selenium scraper
├── streaming_content.csv # Scraped movie data
├── templates/
│ ├── base.html
│ ├── card.html
│ ├── index.html
│ └── favorites.html
├── static/
│ └── css/
│ └── styles.css
├── movie-collection.db # SQLite database
└── README.md
```

---

## 🕷️ Running the Scraper

The scraper collects movies from **Shortlist – What to Watch**.

### 1️⃣ Requirements
```bash
- Firefox installed
- GeckoDriver installed
- `.env` file with:
   GECKO_DRIVER_PATH=/path/to/geckodriver
```

### 2️⃣ Run the scraper

```bash
python movie-scraper.py
```
This will:

- Open Firefox
- Navigate Shortlist
- Handle cookies / modals (manual if needed)
- Scrape movie data
- Save streaming_content.csv

---

## 🌐 Running the Web App
### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣ Start the server
```bash
python main.py
```
### 3️⃣ Open in browser
```bash
http://127.0.0.1:5000
```
---

## 🎴 How It Works

- On startup, the app:
  * Creates the database
  * Imports data from streaming_content.csv
- Homepage shows **5 random movies**
- Hover to flip cards
- Mark favorites ❤️
- Add short reviews ✍️
- View favorites on /favorites

---

## 💡 Why This Project?

This project was built as part of a 100 Python Projects Challenge with the goal of combining:

* Automation
* Backend logic
* Databases
* UI/UX
* Real-world scraping challenges

---

## 🇨🇴 Final Note

Some vibes can’t be localized with a framework.<br>
They’re just… felt...**Enjoy** — and que viva el cine. 🎥

