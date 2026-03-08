import requests
import csv
from bs4 import BeautifulSoup
from time import sleep

BASE_URL = "https://store.steampowered.com/search/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def get_page(start=0):
    """
    Fetch a Steam search results page.
    """
    params = {
        "filter": "topsellers",
        "start": start,
        "count": 50
    }

    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    response.raise_for_status()

    return response.text


def parse_games(html):
    """
    Parse game data from HTML.
    """
    soup = BeautifulSoup(html, "html.parser")

    games = []

    rows = soup.select("a.search_result_row")

    for row in rows:
        title = row.select_one("span.title").text.strip()

        release = row.select_one(".search_released")
        release = release.text.strip() if release else "N/A"

        price = row.select_one(".search_price")
        price = price.text.strip() if price else "Free"

        platforms = [p["class"][1] for p in row.select(".platform_img")]

        review = row.select_one(".search_review_summary")
        review = review["data-tooltip-html"] if review else "No reviews"

        link = row["href"]

        games.append({
            "title": title,
            "release_date": release,
            "price": price,
            "platforms": ", ".join(platforms),
            "review_summary": review,
            "url": link
        })

    return games


def save_to_csv(data, filename="steam_games.csv"):
    """
    Save scraped data to CSV.
    """

    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def scrape_steam(pages=3):
    """
    Scrape multiple pages of Steam games.
    """

    all_games = []

    for page in range(pages):
        print(f"Scraping page {page + 1}")

        html = get_page(start=page * 50)
        games = parse_games(html)

        all_games.extend(games)

        sleep(2)

    return all_games


def main():
    games = scrape_steam(pages=5)

    print(f"Scraped {len(games)} games")

    save_to_csv(games)

    print("Data saved to steam_games.csv")


if __name__ == "__main__":
    main()