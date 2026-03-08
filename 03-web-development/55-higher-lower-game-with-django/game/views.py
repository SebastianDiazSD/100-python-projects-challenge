import random
from django.shortcuts import render, redirect

# -------------------------------
# GIF collections (full sabor)
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
# Home: choose difficulty
# -------------------------------
def index(request):
    return render(request, "game/index.html")


# -------------------------------
# Start game
# -------------------------------
def start_game(request, difficulty):
    ranges = {
        "easy": 10,
        "medium": 50,
        "hard": 100
    }

    request.session["range"] = ranges[difficulty]
    request.session["number"] = random.randint(1, ranges[difficulty])

    return redirect("play")


# -------------------------------
# Play the game
# -------------------------------
def play(request):
    context = {
        "message": None,
        "gif": None,
        "won": False,
        "range": request.session.get("range")
    }

    if request.method == "POST":
        guess = int(request.POST["guess"])
        number = request.session["number"]

        if guess < number:
            context["message"] = "Parcero, you're too low. Tranquilo."
            context["gif"] = random.choice(TRY_AGAIN_IMAGES)

        elif guess > number:
            context["message"] = "Uy no, te pasaste. Bajale suave."
            context["gif"] = random.choice(TRY_AGAIN_IMAGES)

        else:
            context["message"] = "¡Esooo! You nailed it, pana!"
            context["gif"] = random.choice(WIN_IMAGES)
            context["won"] = True
            request.session.flush()  # Clean session, juego terminado

    return render(request, "game/play.html", context)
