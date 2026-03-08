"""
Morse Code Loader

This module is responsible for loading the Morse code dictionary.
If the JSON file does not exist, the program will automatically
scrape the Morse table from a website and generate the file.
"""

import json
from os.path import exists

import requests
from bs4 import BeautifulSoup


class MorseLoader:
    """
    Loads Morse code data from a JSON file.

    If the file does not exist, it will fetch the data from the web
    and create the JSON file automatically.
    """

    def __init__(self, file: str = "morse.json"):

        # If the file doesn't exist, generate it
        if not exists(file):

            html = fetch_html()
            morse_pairs = parse_morse_table(html)

            with open(file, "w") as f:
                json.dump(morse_pairs, f)

        # Load the JSON data
        with open(file) as f:
            self.data = json.load(f)


def fetch_html() -> str:
    """
    Retrieves the Morse code reference page.

    Returns
    -------
    str
        HTML content of the Morse code table page.
    """

    with requests.Session() as session:

        response = session.get(
            "https://morsecode.world/international/morse2.html"
        )

        response.raise_for_status()

    return response.text


def parse_morse_table(html: str) -> dict:
    """
    Extracts Morse code mappings from the HTML table.

    Parameters
    ----------
    html : str
        Raw HTML content from the Morse code reference page.

    Returns
    -------
    dict
        Dictionary mapping characters to Morse code.
        Example: {"A": ".-", "B": "-..."}
    """

    morse_dict = {}

    soup = BeautifulSoup(html, "html.parser")

    for table in soup.find_all("table"):

        # Identify the correct table by header
        if table.find("th", string="Morse"):

            for row in table.find_all("tr"):

                if row.find(class_="morse"):

                    data = row.find_all("td")

                    character = data[0].span.text
                    morse_code = data[1].text

                    morse_dict[character] = morse_code

    return morse_dict