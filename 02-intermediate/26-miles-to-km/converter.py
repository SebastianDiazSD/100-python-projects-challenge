def miles_to_km(miles):
    """Convert miles to kilometers."""
    try:
        return round(float(miles) * 1.60934, 2)
    except ValueError:
        return "Invalid input"

def km_to_miles(km):
    """Convert kilometers to miles."""
    try:
        return round(float(km) * 0.621371, 2)
    except ValueError:
        return "Invalid input"

# Handlers that interact with Tkinter widgets
def handle_miles_to_km(input_miles, input_km):
    result = miles_to_km(input_miles.get())
    input_km.delete(0, 'end')
    input_km.insert(0, str(result))

def handle_km_to_miles(input_km, input_miles):
    result = km_to_miles(input_km.get())
    input_miles.delete(0, 'end')
    input_miles.insert(0, str(result))
