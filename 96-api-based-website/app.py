from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        word = request.form.get("word")

        try:
            response = requests.get(API_URL + word)
            data = response.json()

            if response.status_code != 200:
                error = "Word not found."
            else:
                entry = data[0]

                result = {
                    "word": entry["word"],
                    "phonetic": entry.get("phonetic", ""),
                    "meaning": entry["meanings"][0]["definitions"][0]["definition"],
                    "example": entry["meanings"][0]["definitions"][0].get("example", "No example available."),
                    "part_of_speech": entry["meanings"][0]["partOfSpeech"]
                }

        except Exception:
            error = "Error connecting to API."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)