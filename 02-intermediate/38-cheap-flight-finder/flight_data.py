# flight_data.py
# Small helper to represent flight details and pick the cheapest option.

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

    def __repr__(self):
        return (
            f"FlightData(price={self.price}, origin={self.origin_airport}, "
            f"dest={self.destination_airport}, out={self.out_date}, return={self.return_date}, stops={self.stops})"
        )


def find_cheapest_flight(data):
    """
    Given the flight-offers JSON from Amadeus, return a FlightData instance
    for the cheapest valid flight. If no valid flights found, returns FlightData with 'N/A'.
    """
    if not data or not data.get("data"):
        print("No flight data available (empty response).")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    cheapest = None
    for flight in data["data"]:
        try:
            price = float(flight["price"]["grandTotal"])
            # compute stops for this flight (first itinerary)
            segments = flight["itineraries"][0]["segments"]
            stops = max(0, len(segments) - 1)
            origin = segments[0]["departure"]["iataCode"]
            destination = segments[-1]["arrival"]["iataCode"]
            out_date = segments[0]["departure"]["at"].split("T")[0]
            # try to find a return date
            return_date = "N/A"
            if len(flight.get("itineraries", [])) > 1:
                ret_segments = flight["itineraries"][1]["segments"]
                if ret_segments:
                    return_date = ret_segments[0]["departure"]["at"].split("T")[0]

            candidate = FlightData(price, origin, destination, out_date, return_date, stops)

            if cheapest is None or (isinstance(candidate.price, float) and candidate.price < cheapest.price):
                cheapest = candidate

        except Exception as ex:
            # If a particular flight entry is malformed, keep going
            print(f"Skipping malformed flight entry: {ex}")
            continue

    if not cheapest:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    return cheapest
