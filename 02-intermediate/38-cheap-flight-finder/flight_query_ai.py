# flight_query_ai.py
# Use OpenAI to parse simple natural language queries into structured flight searches.
# This is a helper that returns origin, destination, departure_date (as datetime),
# and a range (departure_date .. departure_date + 6 months) for searching.

import os
from datetime import datetime, timedelta
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")


def parse_natural_query(query_text: str):
    """
    Use OpenAI to extract origin city, destination city, and date (or date range).
    If OpenAI is not configured or fails, returns None.
    The assistant prompt is intentionally simple — adjust to your tastes.
    """

    if not openai.api_key:
        print("OpenAI key not configured. Skipping AI parsing.")
        return None

    prompt = (
        "You are an assistant that extracts a flight search from a user's natural language.\n"
        "Given a sentence like: \"What are the cheapest flights from Madrid to Paris on June 1st?\"\n"
        "Return a JSON object with keys: origin_city, destination_city, departure_date (YYYY-MM-DD) or null.\n"
        "If a date is not present, return departure_date as null.\n\n"
        f"User query: \"{query_text}\"\n\n"
        "Return ONLY the JSON."
    )

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0
        )
        content = resp["choices"][0]["message"]["content"].strip()
        # Try to load JSON
        import json
        data = json.loads(content)
        # normalize (dates might be partial)
        dep = data.get("departure_date")
        if dep:
            # try parse; if fails, return None
            try:
                parsed = datetime.fromisoformat(dep).date()
                return {
                    "origin_city": data.get("origin_city"),
                    "destination_city": data.get("destination_city"),
                    "departure_date": parsed
                }
            except Exception:
                return {
                    "origin_city": data.get("origin_city"),
                    "destination_city": data.get("destination_city"),
                    "departure_date": None
                }
        return data
    except Exception as ex:
        print(f"OpenAI parsing failed: {ex}")
        return None
