
# 93 – Web Scraper 🇨🇴

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Web Scraping](https://img.shields.io/badge/Web-Scraping-green)
![CSV Dataset](https://img.shields.io/badge/Data-CSV-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)

A Python scraper that collects **Steam Top Seller games** and exports structured data into a **CSV dataset**.

---

## Project Structure

```
93-web-scraper
│
├── scraper.py
├── requirements.txt
├── steam_games.csv
├── README.md
└── assets
    ├── scraper_architecture.png
    └── dataset_preview.png
```

---

## How to Run

```bash
pip install -r requirements.txt
python scraper.py
```

The script collects the data and creates:

```
steam_games.csv
```

---

## Scraper Architecture

![Architecture](scraper_architecture.png)

The workflow follows a simple pipeline: request the webpage, parse HTML elements, structure the extracted data, and export the dataset to CSV.

---

## Sample Dataset Preview

![Dataset Preview](dataset_preview.png)
