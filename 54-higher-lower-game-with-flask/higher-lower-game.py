from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "parce-esto-es-secreto"  # Needed for sessions

# -------------------------------
# GIF collections (pure sabor)
# -------------------------------


WIN_IMAGES =["https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmV4OWMzZ291eHg5dG9nMnF5OTdlNTR4Nnl6NnkwMDB2aGYwM3NwaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Feq51BviBdQqi24Btt/giphy.gif",
            "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTh0MHR5ZWpwcnZrM20zbTdvbWgxd3BxMXh5YTBzZHpqc201djkydiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/h2a03NYKqtJBFgmmsx/giphy.gif",
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjdkMzM1Mmg0a2NzcHl6Zmt6d3VqcThtdW02cTJiN3QxbGkzbXUxMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5AwCyyscRqpSvh0V6Bq/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHNleG9weWE1cTVmZzd6NGkwbnY0M3l2bDdpbHF5b3diMWNiMzk3ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RN7Poh8pdcyWa3kKbI/giphy.gif",
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnBwNGxtbjBwODJsZjFueWNxbmVlazA4MnJnaGJnZzJwZHpiZ3RtdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT0xeQlHuOfhHCpo6Q/giphy.gif",
            "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzZ2aHhqbXYxcW00eWk3cmVwZWhtemNuZmp0OXM3Ym4wdTJ3M3k2aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4T5xHL8SOI6Vf5yecE/giphy.gif"]

TRY_AGAIN_IMAGES=["https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzltajQwb3k3Y2FkOHZ3N3NwNnhudDl5cnk0czFodmRxNmt0b2lwOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MKzU3oPvBjFV4DC36t/giphy.gif",
                  "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDFoNGhsbXJ0dWJuc25wbDBkZG9rdDV3b2FmM2k5aDJrbWQwODJjdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lOadFSN6uNANXNRZDA/giphy.gif",
                  "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzd2cGpteXh4cnQxaDN5ejV4eHZvcXNrN3l2eGliOG4xbDJ1amZubiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Jt4sQOFEh29Ob8KAxg/giphy.gif",
                  "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGkxcm93ZjE0ZzUybXlkaXlrYnpiNGYxY3pqZG9venE0cXdlZ2Q1eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9uALs1I19Dkd3y/giphy.gif",
                  "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmFzbWgwbXdwcXg5enUycHA0MnRmd2Z3Zmlnc3d6dzFuejdsMWIzdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cP5li7Un9Ua2OT7i9y/giphy.gif",
                  "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGdjdWR2em43bTJ3NDFtdW9wNDM0NmF2OGtkY2ZwYzVxZXZycm5yOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VL48WGMDjD64umCEkv/giphy.gif"]

# -------------------------------
# Game logic (pure logic, no Flask drama)
# -------------------------------
def check_guess(user_guess, number_to_guess):
    """
    Compares user's guess with the secret number.
    Returns message + gif depending on the vibe.
    """
    if user_guess < number_to_guess:
        return (
            "Parcero, you're too low. Tranquilo, try again.",
            random.choice(TRY_AGAIN_IMAGES),
            False
        )
    elif user_guess > number_to_guess:
        return (
            "Uy no, you went too high. Bajale dos rayitas.",
            random.choice(TRY_AGAIN_IMAGES),
            False
        )
    else:
        return (
            "¡Esoooo! You nailed it, pana. You win!",
            random.choice(WIN_IMAGES),
            True
        )

# -------------------------------
# Routes
# -------------------------------
@app.route("/")
def home():
    # Landing page: choose difficulty
    return render_template("index.html")


@app.route("/start/<difficulty>")
def start_game(difficulty):
    """
    Initializes the game based on difficulty.
    Sets the number and range in session, porque Flask no se acuerda solo.
    """
    ranges = {
        "easy": 10,
        "medium": 50,
        "hard": 100
    }

    session["range"] = ranges[difficulty]
    session["number"] = random.randint(1, ranges[difficulty])
    session["difficulty"] = difficulty

    return redirect(url_for("play"))


@app.route("/play", methods=["GET", "POST"])
def play():
    message = None
    gif = None
    won = False

    if request.method == "POST":
        guess = int(request.form["guess"])
        number = session["number"]

        message, gif, won = check_guess(guess, number)

        if won:
            session.clear()  # Game over, limpiamos la mesa

    return render_template(
        "game.html",
        message=message,
        gif=gif,
        won=won,
        range=session.get("range")
    )


if __name__ == "__main__":
    app.run(debug=True)
