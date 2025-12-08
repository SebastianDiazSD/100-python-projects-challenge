# 🎵 Music Machine  
A Python project that scrapes the **Billboard Hot 100** chart and automatically creates a **Spotify playlist** with the top songs of the week.  
Built with **BeautifulSoup**, **Spotipy**, and a small **Tkinter GUI** to make the experience simple:  
just press a button and enjoy the music — *Parce style!* 🇨🇴

---

## 🚀 Features

- Scrapes the **current Billboard Hot 100** chart  
- Searches each track on Spotify  
- Creates a **private playlist** named:  
  **Billboard 100 – DD/MM/YYYY**  
- Adds all matching songs automatically  
- Simple Tkinter interface with:  
  - Friendly Colombian welcome message  
  - “Let the music begin!” button  
  - Progress bar  
  - Error pop-ups for missing credentials or scraping issues  

---

## 🛠 Technologies Used

- **Python 3**
- **BeautifulSoup4**
- **Requests**
- **Spotipy (Spotify API wrapper)**
- **Tkinter**
- **Pandas** (optional)
- **dotenv** for environment variables

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 43-music-machine
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your environment variables
Create a .env file:
```bash
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://127.0.0.1:8888/callback
```

---

## 🎧 Spotify Setup (Required)

1. Go to https://developer.spotify.com/dashboard
2. Create an app
3. Add this redirect URI:
  - http://127.0.0.1:8888/callback
4. Copy your:
  - Client ID
  - Client Secret
5. Paste them into your .env file
6. Delete token.txt if you're re-running the app

---

## ▶️ Running the App

```bash
python main.py
```
The GUI opens.
Just click **“Let the music begin!”** and watch the playlist get created automatically.

---

## 📁 Project Structure
```css
📦 43-music-machine
 ┣ logo.png
 ┣ main.py
 ┣ helpers.py
 ┣ requirements.txt
 ┣ README.md
 ┗ .env
```

---

## 🪄 How It Works

1. Billboard Scraper

Extracts the 100 current top tracks:
```bash
li ul li h3  →  track titles
```
2. Spotify Auth

Uses OAuth to log into your account and create a playlist.

3. Track Matching

Each scraped song is searched with:
```bash
track:<song title>
```
4. Playlist Creation

A new playlist is created and all found tracks are inserted.

---

## 🇨🇴 Personal Note

As a Colombian developer, I wanted to give this project a small parcero touch while keeping everything professional and in English for my portfolio.
This project is part of my 100 Python Projects Challenge — Project #44 🎯
