from tkinter import *
import requests

# 💬 Function to get a random Kanye West quote from the Kanye REST API
def get_quote():
    # Make a GET request to the Kanye REST API
    response_kanye = requests.get(url="https://api.kanye.rest")
    response_kanye.raise_for_status()  # 🚨 Raise an error if the request fails

    # Convert the response into JSON format
    quote = response_kanye.json()

    # Update the canvas text with the new Kanye quote
    canvas.itemconfig(quote_text, text=quote["quote"], fill="white")
    # Kanye dropping wisdom like "No hay mal que por bien no venga" 😎


# 🪟 Set up the main window (Tkinter GUI)
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)  # Add some padding for better layout

# 🎨 Create the canvas where the quote will appear
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")  # Background image
canvas.create_image(150, 207, image=background_img)

# Text area for displaying Kanye's quotes
quote_text = canvas.create_text(
    150, 207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

# 😎 Create Kanye's face button (click to get new quote)
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# 🧉 Main loop — keeps the app running (like a good cup of tinto keeps us coding)
window.mainloop()
