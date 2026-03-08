# ☕ Cafe WorkVibe

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?logo=flask)
![SQLAlchemy](https://img.shields.io/badge/Database-SQLAlchemy-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)
![Leaflet](https://img.shields.io/badge/Map-Leaflet-green?logo=leaflet)
![OpenStreetMap](https://img.shields.io/badge/Maps-OpenStreetMap-brightgreen?logo=openstreetmap)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Project 88 --- 100 Python Projects Challenge**

Welcome to **Cafe WorkVibe**, a web app built with Flask that helps
remote workers find **great cafés to work from** --- good coffee,
reliable WiFi, and a comfortable place to open your laptop.

This project was inspired by the amazing **coffee culture of Colombia
🇨🇴**, where coffee is not just a drink --- it's part of daily life,
conversation, and creativity.

So whether you're coding, studying, or building your next startup, the
goal is simple:

> Find a good café, order a great coffee, and get things done.

------------------------------------------------------------------------

# 🌍 Features

-   Browse laptop‑friendly cafés
-   View cafés on an **interactive map**
-   **Clustered map markers** for better navigation
-   Add new cafés to the database
-   Delete cafés
-   See useful work info like:
    -   WiFi availability
    -   Power sockets
    -   Coffee price
    -   Good for taking calls

The map automatically adjusts to show all cafés available in the
database.

------------------------------------------------------------------------

# 🗺 Map Experience

The application uses:

-   **Leaflet.js**
-   **OpenStreetMap**
-   **Marker clustering**

This allows the map to behave like modern location apps where nearby
cafés group together and expand as you zoom.

------------------------------------------------------------------------

# 🧠 Tech Stack

Backend

-   Python
-   Flask
-   SQLAlchemy
-   SQLite

Frontend

-   HTML
-   CSS
-   Jinja Templates
-   Leaflet.js

Other tools

-   WTForms
-   OpenStreetMap Nominatim (geocoding)
-   MarkerCluster for map visualization

------------------------------------------------------------------------

# 📂 Project Structure

    88-cafe-workvibe
    │
    ├── app.py
    ├── cafes.db
    ├── requirements.txt
    │
    ├── templates
    │   ├── base.html
    │   ├── index.html
    │   ├── add_cafe.html
    │   └── map.html
    │
    └── static
        └── style.css

------------------------------------------------------------------------

# 🚀 Running the Project

Clone the repository

    git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git

Navigate to the project

    cd 88-cafe-workvibe

Install dependencies

    pip install -r requirements.txt

Run the application

    python app.py

Open in your browser

    http://127.0.0.1:5000

------------------------------------------------------------------------

# ☕ A Small Colombian Touch

In Colombia we say:

> "Un buen café siempre trae buenas ideas."\
> *A good coffee always brings good ideas.*

This project celebrates the idea that great work often starts with:

-   a comfortable place
-   a laptop
-   and a really good cup of coffee.

------------------------------------------------------------------------

# 🤝 Connect

If you like the project, feel free to connect or follow the journey.

And remember:

> Great code and great coffee often go together.
