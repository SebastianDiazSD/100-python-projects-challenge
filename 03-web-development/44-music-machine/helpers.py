# helpers.py
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Optional: load .env automatically if you use one
try:
    from dotenv import load_dotenv
    load_dotenv()  # will silently do nothing if no .env
except Exception:
    pass


def _get_spotify_credentials():
    """
    Try multiple env var names so both the standard SPOTIPY_*
    names and the older custom names work.
    """
    client_id = os.getenv("SPOTIPY_CLIENT_ID") or os.getenv("Client_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET") or os.getenv("Client_secret")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI") or os.getenv("Redirect_URI")

    missing = []
    if not client_id:
        missing.append("SPOTIPY_CLIENT_ID (or Client_ID)")
    if not client_secret:
        missing.append("SPOTIPY_CLIENT_SECRET (or Client_secret)")
    if not redirect_uri:
        missing.append("SPOTIPY_REDIRECT_URI (or Redirect_URI)")

    if missing:
        # Raise a clear error so the GUI can show it as a pop-up
        raise RuntimeError(
            "Missing Spotify credentials: " + ", ".join(missing) +
            ".\nSet them as environment variables or create a .env file."
        )

    return client_id, client_secret, redirect_uri


def get_top_100(progress_bar=None):
    # Update UI – Step 1
    if progress_bar:
        progress_bar["value"] = 10

    # ---------- SCRAPING BILLBOARD ----------
    billboard_url = "https://www.billboard.com/charts/hot-100/"

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    })

    response = session.get(billboard_url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Reliable selectors (as of 2024–2025)
    songs = []
    entries = soup.select("li.o-chart-results-list__item")

    for entry in entries:
        title_tag = entry.select_one("h3#title-of-a-story")
        artist_tag = entry.select_one("span.c-label")

        if title_tag:
            title = title_tag.get_text(strip=True)
            artist = artist_tag.get_text(strip=True) if artist_tag else ""
            songs.append((title, artist))

    if not songs:
        raise RuntimeError("Could not find any songs on Billboard page. The page structure may have changed.")

    if progress_bar:
        progress_bar["value"] = 30

    # ---------- SPOTIFY AUTH ----------
    client_id, client_secret, redirect_uri = _get_spotify_credentials()

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    user = sp.current_user()
    if not user or "id" not in user:
        raise RuntimeError("Failed to get Spotify user. Are your credentials correct and did you authorize the app?")

    user_id = user["id"]

    if progress_bar:
        progress_bar["value"] = 50

    # ---------- SEARCH SONGS ----------
    song_uris = []
    total = len(songs)
    for i, (title, artist) in enumerate(songs):
        # Build query with both title and artist to improve accuracy
        if artist:
            query = f"track:{title} artist:{artist}"
        else:
            query = f"track:{title}"

        result = sp.search(q=query, type="track", limit=1)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except (IndexError, KeyError):
            # Not found — skip and continue
            print(f"Not found on Spotify: {title} - {artist}")

        # update progress
        if progress_bar:
            progress_bar["value"] = 50 + int(((i + 1) / total) * 40)

    if not song_uris:
        raise RuntimeError("No songs were found on Spotify. Check your network/credentials or the Billboard parsing logic.")

    # ---------- CREATE PLAYLIST ----------
    today = datetime.now().strftime("%Y-%m-%d")

    playlist = sp.user_playlist_create(
        user=user_id,
        name=f"Billboard Hot 100 – {today} (Colombian Edition)",
        public=False
    )

    sp.playlist_add_items(
        playlist_id=playlist["id"],
        items=song_uris
    )

    if progress_bar:
        progress_bar["value"] = 100

    return playlist  # return playlist info in case the caller wants it
