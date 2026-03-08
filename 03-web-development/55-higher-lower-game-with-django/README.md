# 🎯 Higher–Lower Game (Django Edition)

This project is the **Django version** of my Higher–Lower guessing game challenge.
Same idea, same logic — but built with **Django’s structured, batteries-included approach**.

Part of my Python challenge series and professional portfolio.

---

## 🚀 How the Game Works

1. Choose a difficulty:
   - 🟢 Easy: 1–10
   - 🟡 Medium: 1–50
   - 🔴 Hard: 1–100 (modo berraco)

2. Django generates a random number and stores it in the session.

3. Each guess returns:
   - Feedback message
   - A random GIF
   - Victory screen when you win

4. Sessions reset when the game ends.

---

## 🧠 Tech Stack

- Python 3
- Django
- HTML (Django templates)
- Sessions
- Random module

---

## 📁 Project Structure

```bash
55-higher-lower-game-with-django/
│
├── manage.py
├── higher_lower_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── game/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── game/
            ├── index.html
            └── play.html
```

---

## 🛠️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   ```
2. Navigate into the project:
   ```bash
   cd 55-higher-lower-game-with-django
   ```
3. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
4. Install Django:
   ```bash
   pip install django
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```
7. Open:
   ```bash
   http://127.0.0.1:8000/
   ```

---

## 🌶️ Why Django?

This project demonstrates:

* Django views & URL routing
* Session management
* Template rendering
* Clean separation of concerns

Same logic as Flask — different mindset.

---

## 👨‍💻 About the Author

> Built with clean code, clear logic,
> and a little Colombian flavor 🇨🇴
> 
> Because learning frameworks is cool,
> but understanding them is even better.

---

# 🏁 Final Words

Now you have:
- ✅ Flask version (Challenge 54)
- ✅ Django version (Challenge 55)
- ✅ Same logic, two frameworks

If you want next:
- Flask vs Django **comparison section**
- Deployment
- Tests
- Styling both apps the same for contrast

pana, if you like this project, feel free to ⭐ the repo or reach out. Sigamos rompiéndola 🚀🔥
