# Professional Portfolio Website – Flask & Bootstrap

This project is part of my **#59 project of the 100 Days of Python challenge**.  
It demonstrates the use of **Flask, Jinja templating, and Bootstrap** to build a modern, responsive, and professional portfolio website.

The site is designed as a **personal portfolio for a civil engineer**, combining construction management expertise with digital and automation-focused engineering solutions — inspired by international experience and Colombian professional values.

---

## 🚀 Features

- Flask backend with clean routing
- Jinja templating with reusable base layout
- Responsive design using Bootstrap
- Animated UI components (AOS, Typed.js, Swiper)
- Contact form with email delivery (Flask-Mail)
- Environment variable management with `python-dotenv`
- Clean and extensible project structure

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, Bootstrap
- **Templating:** Jinja2
- **Email:** Flask-Mail (SMTP via Gmail)
- **Animations & UI:** AOS, Typed.js, Swiper
- **Environment Management:** python-dotenv

---

## 📁 Project Structure
```bash
├── server.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── about.html
│ ├── resume.html
│ ├── services.html
│ ├── portfolio.html
│ └── contact.html
├── static/
│ └── assets/
│ ├── css/
│ ├── js/
│ ├── img/
│ └── vendor/
├── .env
└── README.md
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 59-portfolio-website
```
2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install flask flask-mail python-dotenv
```
4. **Create a .env file**
```bash
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SECRET_KEY=your_secret_key
```
5. **Run the Application**
```bash
python server.py
```
6. **Then open**
```bash
http://127.0.0.1:5000
```

---

## ✉️ Contact Form

The contact form sends emails using **Flask-Mail.**<br>
Basic validation is implemented to ensure all required fields are filled before submission.

---

# 🎨 Design Credits

- Original template: **FolioOne** by BootstrapMade
- Design adapted and customized using Flask & Jinja

---

## 📌 Notes

- Only `index.html` and `about.html` are customized.
- Other pages are intentionally left open for user creativity and extension.
- Debug mode is enabled for development and should be disabled in production.
