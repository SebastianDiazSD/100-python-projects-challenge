# main.py
# Orchestrator for the Cheap Flight Finder
# English messages with a Colombian vibe.

import time
from datetime import datetime, timedelta
import os

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# Optional OpenAI parsing if you want to accept natural queries
try:
    from flight_query_ai import parse_natural_query
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False

def main():
    print("Bienvenido parcero! Starting Cheap Flight Finder... 🇨🇴✈️")

    data_manager = DataManager()
    flight_search = FlightSearch()
    notifier = NotificationManager()

    sheet_data = data_manager.get_destination_data()

    # Update missing IATA codes
    for row in sheet_data:
        if not row.get("iataCode"):
            print(f"Getting IATA for {row.get('city')}...")
            code = flight_search.get_destination_code(row.get("city"))
            row["iataCode"] = code
            time.sleep(1)  # be gentle with the API
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

    # Get customers
    customers = data_manager.get_customer_emails()
    # Expect 'email' column in sheet. If different, change here.
    customer_emails = [u.get("email") or u.get("whatIsYourEmail?") for u in customers]
    customer_emails = [e for e in customer_emails if e]

    # Ask user if they prefer natural language query or full scan
    use_ai = False
    if OPENAI_AVAILABLE and os.environ.get("OPENAI_API_KEY"):
        resp = input("Do you want to ask a natural-language question (y/n)? ").strip().lower()
        use_ai = resp == "y"

    if use_ai:
        q = input("Write your question (e.g. \"Cheapest flights from Madrid to Paris on June 1st?\"): ")
        parsed = parse_natural_query(q)
        if parsed:
            origin_city = parsed.get("origin_city")
            dest_city = parsed.get("destination_city")
            dep_date = parsed.get("departure_date")  # may be None
            # resolve to IATA
            origin_iata = flight_search.get_destination_code(origin_city)
            dest_iata = flight_search.get_destination_code(dest_city)
            # date range
            if dep_date:
                start = datetime.combine(dep_date, datetime.min.time())
            else:
                start = datetime.now() + timedelta(days=1)
            end = start + timedelta(days=6*30)
            print(f"Searching {origin_city}({origin_iata}) -> {dest_city}({dest_iata}) from {start.date()} to {end.date()}")
            flights = flight_search.check_flights(origin_iata, dest_iata, start, end)
            cheapest = find_cheapest_flight(flights)
            print(f"Cheapest found: {cheapest}")
            if cheapest.price != "N/A":
                message = (
                    f"Low price alert! Only GBP {cheapest.price} to fly "
                    f"{cheapest.origin_airport} -> {cheapest.destination_airport} on {cheapest.out_date} "
                    f"returning {cheapest.return_date}. Stops: {cheapest.stops}"
                )
                notifier.send_emails(customer_emails, message, subject="Parce! New low price flight")
            return

    # Otherwise full scan of sheet destinations
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=6*30)

    for dest in sheet_data:
        dest_city = dest.get("city")
        dest_iata = dest.get("iataCode")
        lowest_price = float(dest.get("lowestPrice", 999999))

        print(f"Parce, checking flights to {dest_city} ({dest_iata})...")
        flights = flight_search.check_flights(
            os.environ.get("ORIGIN_CITY_IATA", "LON"),
            dest_iata,
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=True
        )

        cheapest = find_cheapest_flight(flights)

        # If no direct, try indirect
        if cheapest.price == "N/A":
            print(f"No direct cheap flight found for {dest_city}. Checking indirect...")
            flights = flight_search.check_flights(
                os.environ.get("ORIGIN_CITY_IATA", "LON"),
                dest_iata,
                from_time=tomorrow,
                to_time=six_month_from_today,
                is_direct=False
            )
            cheapest = find_cheapest_flight(flights)

        print(f"{dest_city}: cheapest found -> {cheapest.price}")

        if isinstance(cheapest.price, float) and cheapest.price < lowest_price:
            print(f"¡Buena esa! New lower price for {dest_city}: {cheapest.price} (old {lowest_price})")
            # update sheet
            try:
                data_manager.update_lowest_price(dest["id"], cheapest.price)
            except Exception as ex:
                print(f"Failed to update sheet: {ex}")

            # notify customers
            message = (
                f"Low price alert! Only GBP {cheapest.price} to fly "
                f"{cheapest.origin_airport} -> {cheapest.destination_airport} on {cheapest.out_date} "
                f"returning {cheapest.return_date}. Stops: {cheapest.stops}"
            )
            if notifier.twilio_client:
                notifier.send_whatsapp(message)
            notifier.send_emails(customer_emails, message, subject=f"Low price to {dest_city} 🇨🇴")

        time.sleep(1)  # polite pacing to avoid rate limits

    print("All done, parcero. Program finished.")

if __name__ == "__main__":
    main()
