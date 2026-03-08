# 🇨🇴 Project 68/100 — Flask Authentication System

A secure user authentication system built with Flask, featuring
registration, login, protected routes, and password hashing.

This project is part of my 100 Python Projects Challenge, where I build
real-world applications to strengthen backend development skills.

---

## 🚀 Overview

This web application allows users to:

* Create an account
* Log in securely
* Access a protected page
* Download a restricted file
* Log out safely

The interface includes a subtle Colombian-inspired design while
maintaining a clean and professional structure.

---

## 🔐 Authentication Flow

1.  A user registers with name, email, and password.
2.  The password is securely hashed using `pbkdf2:sha256`.
3.  User data is stored in a SQLite database.
4.  During login, the hashed password is verified.
5.  Authenticated users can access protected routes.
6.  Unauthorized users are automatically redirected to login.

---

## 🛠 Tech Stack

* Python
* Flask
* Flask-Login
* Flask-SQLAlchemy
* SQLite
* HTML5
* CSS3 (Custom Colombian-inspired theme)

---

## 📂 Project Structure

```cpp
project-68/
│
├── static/
│   ├── css/
│        └── styles.css
│
│       
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── secrets.html
│
├── main.py
├── users.db
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 100-python-projects-challenge
```
### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```
Activate it:

Mac/Linux:
```bash
source venv/bin/activate
```
Windows: 
```bash
venv
```
### 3️⃣ Install dependencies

pip install flask flask-login flask-sqlalchemy werkzeug

### 4️⃣ Run the application
```bash
python main.py
```
Open your browser and visit:
```bash
http://127.0.0.1:5000
```
---

## 🧠 What I Practiced in This Project

* Secure password hashing
* Database modeling with SQLAlchemy
* Session management
* Route protection with `@login_required`
* Flash messaging for feedback
* Clean template inheritance with Jinja2
* UI/UX structuring without heavy frameworks

---

## 🔒 Security Features

* Passwords are hashed (never stored in plain text)
* Email uniqueness enforced at database level
* Protected routes require authentication
* Secure session handling via Flask-Login

---

## 📈 Why This Project Matters

Authentication is one of the most important components of modern web
applications. This project demonstrates understanding of:

* Backend architecture
* Secure credential handling
* User session management
* Database integration

It represents practical, production-relevant backend development skills.
