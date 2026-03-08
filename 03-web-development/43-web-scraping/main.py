import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import time
import random

BASE_URL = "https://letterboxd.com/films/ajax/by/rating/page/{}/"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://letterboxd.com/films/"
})

rows = []
TOTAL_PAGES = 5

for page in range(1, TOTAL_PAGES + 1):
    print(f"Scraping page {page}...")
    url = BASE_URL.format(page)

    try:
        response = session.get(url, timeout=10)
        if response.status_code != 200:
            print(f"⚠ Failed page {page} — Status {response.status_code}")
            continue
    except requests.exceptions.RequestException as e:
        print(f"⚠ Request exception: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.find_all("li", class_="posteritem")

    for movie in movies:
        rating = movie.get("data-average-rating")
        div = movie.find("div", class_="react-component")
        full_name = div.get("data-item-full-display-name") if div else ""

        # Extract title and year using regex
        match = re.match(r"^(.*)\s\((\d{4})\)$", full_name)
        if match:
            title = match.group(1)
            year = match.group(2)
        else:
            title = full_name
            year = ""

        if rating:
            rows.append({
                "Movie-title": title,
                "Year": year,
                "Rating": float(rating)
            })

    time.sleep(random.uniform(1.0, 2.0))

# Create dataframe and get top 10
df = pd.DataFrame(rows)
df = df.sort_values("Rating", ascending=False).head(10)

# Generate HTML table rows
print("\n\n======== COPY THE CODE BELOW INTO YOUR <tbody> ========\n")
for i, row in df.iterrows():
    print(f"""
        <tr>
            <td>{i+1}</td>
            <td>{row['Movie-title']}</td>
            <td>{row['Year']}</td>
            <td>{row['Rating']}</td>
        </tr>
    """)
print("\n=======================================================\n")
print("Top 10 movie rows generated! Paste them into index.html")