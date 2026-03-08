# Age & Gender Guess App 🇨🇴

A fun Flask web app that guesses a person's age and gender based on their name — with a vibrant Colombian twist!

---

## 🌟 Features

- Enter a name and get predictions using:
  - [Genderize.io](https://genderize.io) → predicts gender
  - [Agify.io](https://agify.io) → predicts age
- Friendly, Colombian-style greeting with flag colors in the UI 🎉
- Clean Flask + Jinja2 + HTML/CSS structure
- Portfolio-ready design with responsive styling

---

## 🚀 How to Run

1. **Clone the repo:**
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   cd 57-age-gender-guess
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install Flask:**
   ```bash
   pip install flask
   ```
4. **Run the app:**
   ```bash
   python server.py
   ```
5. **Open in browser:**
   ```bash
   http://127.0.0.1:5000
   ```
   
---

## 📁 Project Structure

```bash
age-guess-app/
├── server.py               # Flask backend
├── templates/
│   ├── index.html          # Home page
│   └── guess.html          # Result page
└── static/
    └── style.css           # Colombian-themed styling (yellow, blue, green)
```

---

## 🎨 Design Inspiration

- **Colors:** Inspired by the Colombian flag — yellow, blue, and green gradients.
- **Tone:** Warm and playful messages like "¡Qué chévere!" while keeping all UI text in English.
- **UI:** Simple, modern, and mobile-friendly.

---

## 🛠 APIs Used

- https://api.genderize.io?name=NAME
- https://api.agify.io?name=NAME
No API key required. Free for low usage.

---

## 📦 Requirements

- Python 3.6+
- Flask
- Requests (pip install requests)

---
## 📄 License

MIT License — feel free to use, modify, and share.
> Made with a little sazón colombiano.
