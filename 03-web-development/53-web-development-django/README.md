# 🇨🇴 Django Calculator App – Introduction to Django

Welcome, parcero 👋  
This project is part of my **100 Python Projects Challenge**, specifically **Challenge #53: Web Development with Django**.

The goal of this project is to build a simple but complete web application using **Django**, while understanding how Django differs from lighter frameworks like Flask. Everything is built step by step, with structure, patience, and clean code — aquí lo hacemos con calma.

---

## 🚀 Project Overview

This Django application provides a homepage where users can:

- Enter two numbers
- Select a mathematical operation:
  - Add
  - Subtract
  - Multiply
  - Divide
- Submit the form and instantly see the result

The focus is not just on the calculator itself, but on learning **Django’s full-stack workflow**, including routing, views, templates, and form handling.

---

## 🧠 Technologies Used

- **Python 3**
- **Django**
- **HTML (Django Templates)**
- Minimal inline CSS for styling

No external libraries — just Django, the right way, mi viejo.

---

## 🖥️ How to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   ```
2. Navigate into the project directory:
   ```bash
   cd 53-web-development-django\django_calculator
   ```
3. (Optional but recommended) Create and activate a virtual environment::
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```
4. Install dependencies:
   ```bash
   pip install django
   ```
5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and visit:
   ```bash
   http://127.0.0.1:8000/
   ```
Listo — your Django app is running 🚀

---

## 📌 Key Learnings
Through this project, I practiced:

* Django project and app structure
* URL routing at project and app levels
* Handling GET and POST requests
* CSRF protection
* Rendering dynamic content using templates
* Understanding Django’s “batteries included” philosophy

Paso a paso, with patience, Django starts to make sense.
