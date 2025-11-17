# data_manager.py
# Responsible for reading and updating Google Sheet data via Sheety.
# English + Colombian comments/messages.

import os
import requests
from requests.auth import HTTPBasicAuth


class DataManager:
    """
    Handles interactions with Sheety for prices and users sheets.
    Uses Basic Auth (username/password) configured via environment variables.
    """

    def __init__(self):
        self._user = os.environ.get("SHEETY_USERNAME")
        self._password = os.environ.get("SHEETY_PASSWORD")
        self.prices_endpoint = os.environ.get("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = os.environ.get("SHEETY_USERS_ENDPOINT")

        if not all([self._user, self._password, self.prices_endpoint, self.users_endpoint]):
            raise EnvironmentError(
                "Missing Sheety config. Please set SHEETY_USERNAME, SHEETY_PASSWORD, "
                "SHEETY_PRICES_ENDPOINT and SHEETY_USERS_ENDPOINT in your .env"
            )

        self._auth = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        """GET the 'prices' sheet from Sheety and return list of rows."""
        resp = requests.get(self.prices_endpoint, auth=self._auth, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        # Expecting {"prices": [ ... ]}
        self.destination_data = data.get("prices", [])
        print(f"Loaded {len(self.destination_data)} destinations from Sheety.")
        return self.destination_data

    def update_destination_codes(self):
        """PUT the IATA codes (and any other updates) back to Sheety for each row."""
        if not self.destination_data:
            print("No destination data to update.")
            return

        for city in self.destination_data:
            # Only update if there is an id and data to send
            if not city.get("id"):
                print(f"Skipping update for {city.get('city')} (no id found).")
                continue

            new_data = {"price": {"iataCode": city.get("iataCode", "")}}
            resp = requests.put(f"{self.prices_endpoint}/{city['id']}", json=new_data, auth=self._auth, timeout=15)
            if resp.status_code in (200, 201):
                print(f"Updated IATA for {city.get('city')} -> {city.get('iataCode')}")
            else:
                print(f"Failed to update {city.get('city')}: {resp.status_code} {resp.text}")

    def update_lowest_price(self, row_id: int, new_price: float):
        """Update the lowestPrice cell for a particular row id."""
        payload = {"price": {"lowestPrice": new_price}}
        resp = requests.put(f"{self.prices_endpoint}/{row_id}", json=payload, auth=self._auth, timeout=15)
        resp.raise_for_status()
        print(f"Sheety: updated lowestPrice for row {row_id} to {new_price}")
        return resp.json()

    def get_customer_emails(self):
        """GET the 'users' sheet to retrieve subscriber emails."""
        resp = requests.get(self.users_endpoint, auth=self._auth, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        self.customer_data = data.get("users", [])
        print(f"Loaded {len(self.customer_data)} users from Sheety.")
        return self.customer_data
