import tkinter as tk
from converter import handle_miles_to_km, handle_km_to_miles

# 🪟 Create the window
window = tk.Tk()
window.title("Distance Converter")
window.config(padx=40, pady=40)

# 🧾 Entry fields
input_miles = tk.Entry(width=10)
input_miles.grid(column=1, row=0)

input_km = tk.Entry(width=10)
input_km.grid(column=1, row=1)

# 🏷️ Labels
label_miles = tk.Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=0)

label_km = tk.Label(text="Kilometers", font=("Arial", 12))
label_km.grid(column=2, row=1)

# 🔘 Buttons
btn_miles_to_km = tk.Button(
    text="Miles to Km",
    command=lambda: handle_miles_to_km(input_miles, input_km)
)
btn_miles_to_km.grid(column=1, row=2, pady=5)

btn_km_to_miles = tk.Button(
    text="Km to Miles",
    command=lambda: handle_km_to_miles(input_km, input_miles)
)
btn_km_to_miles.grid(column=2, row=2, pady=5)

# 🌀 Run the app
window.mainloop()
