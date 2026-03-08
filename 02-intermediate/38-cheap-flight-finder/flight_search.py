# flight_search.py
# Responsible for Amadeus token handling, IATA lookups, and flight searching.

import os
import time
import requests
from datetime import datetime, timedelta

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_SECRET")
        if not all([self._api_key, self._api_secret]):
            raise EnvironmentError("Missing Amadeus credentials (AMADEUS_API_KEY / AMADEUS_SECRET).")

        # caching token details
        self._token = None
        self._token_expires_at = 0
        self._get_new_token()  # populate the token

    def _get_new_token(self):
        """Request a new client credentials token and cache expiry time."""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"grant_type": "client_credentials", "client_id": self._api_key, "client_secret": self._api_secret}

        resp = requests.post(TOKEN_ENDPOINT, headers=headers, data=data, timeout=15)
        if resp.status_code != 200:
            raise ConnectionError(f"Failed to get Amadeus token: {resp.status_code} {resp.text}")

        j = resp.json()
        self._token = j.get("access_token")
        expires_in = j.get("expires_in", 1800)
        self._token_expires_at = time.time() + int(expires_in) - 30  # margin
        print("Got Amadeus token (cached).")
        return self._token

    def _ensure_token(self):
        if not self._token or time.time() >= self._token_expires_at:
            return self._get_new_token()
        return self._token

    def get_destination_code(self, city_name):
        """Return the IATA code for a given city name (first match)."""
        token = self._ensure_token()
        headers = {"Authorization": f"Bearer {token}"}
        params = {"keyword": city_name, "max": 3, "include": "AIRPORTS"}
        resp = requests.get(IATA_ENDPOINT, headers=headers, params=params, timeout=15)
        if resp.status_code != 200:
            print(f"Amadeus IATA lookup failed: {resp.status_code} {resp.text}")
            return "N/A"
        data = resp.json()
        try:
            code = data["data"][0]["iataCode"]
            return code
        except (IndexError, KeyError):
            print(f"No IATA code found for {city_name}")
            return "N/A"

    def check_flights(self, origin_city_code, destination_city_code, from_time: datetime, to_time: datetime, is_direct=True):
        """
        Query the Amadeus flight offers endpoint for the cheapest offers between the date range.
        Note: many public Amadeus examples use POST with a JSON body; this implementation uses GET
        with query params like the original code. If you hit 400/422, consider switching to POST as per docs.
        """
        token = self._ensure_token()
        headers = {"Authorization": f"Bearer {token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": "1",
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        resp = requests.get(FLIGHT_ENDPOINT, headers=headers, params=query, timeout=20)
        if resp.status_code != 200:
            print(f"Flight search failed ({resp.status_code}): {resp.text[:300]}")
            return None
        return resp.json()
