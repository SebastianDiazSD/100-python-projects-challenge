# 🚆 69 – Blog with User Authentication  
### Flask • SQLAlchemy • Flask-Login • CKEditor

An upgraded full-stack blog application featuring user authentication, relational database design, role-based authorization, and rich text content editing.

This project is part of the **100 Python Projects Challenge**, progressively moving from basic scripts to structured, production-ready web applications.

---

## 📌 Project Overview

This application extends the previous blog project by introducing:

- User registration and login
- Secure password hashing
- Role-based admin control
- Comment system
- Relational database architecture
- Rich text editing with CKEditor

The project demonstrates how backend authentication logic integrates with database relationships and dynamic templates in a Flask application.

---

## ✨ Core Features

### 👤 Authentication
- User registration
- Secure password hashing (Werkzeug)
- Login & logout functionality
- Session management with Flask-Login

### 📝 Blog Management (Admin Only)
- Create posts
- Edit posts
- Delete posts
- Rich text content support

### 💬 Comment System
- Authenticated users can comment
- One-to-many relationship between posts and comments
- One-to-many relationship between users and comments

### 🗄 Relational Database Design

Models:

- **User**
- **BlogPost**
- **Comment**

Relationships:

- One User → Many Posts
- One User → Many Comments
- One Post → Many Comments

---

## 🛠 Tech Stack

- Python 3.12
- Flask 3.x
- SQLAlchemy 2.x
- Flask-Login
- Flask-WTF
- Flask-Bootstrap
- Flask-CKEditor
- SQLite
- Jinja2
- Bootstrap 5
- Bleach (for input sanitization)

---

## 📂 Project Structure
```bash
69-blog-with-users/
│
├── main.py
├── forms.py
├── instances/
│ ├── post.db
├── requirements.txt
│
├── templates/
│ ├── header.html
│ ├── footer.html
│ ├── index.html
│ ├── post.html
│ ├── make-post.html
│ ├── login.html
│ ├── register.html
│ ├── about.html
│ └── contact.html
│
└── static/
├── css/
│ └── styles.css
├── js/
│ └── scripts.js
└── assets/

```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
```
Navigate into the project:
```bash
cd 100-python-projects-challenge/69-blog-with-users
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate it:

**Linux / macOS**
```bash
source venv/bin/activate
```
**Windows**
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
If CKEditor sanitization warning appears:
```bash
pip install bleach
```
### 4️⃣ Run the Application
```bash
python main.py
```

Open:
```bash
http://127.0.0.1:5004
```

---

## 🔐 Admin Logic

The first registered user becomes the administrator.

Admin privileges include:

* Creating posts
* Editing posts
* Deleting posts

All other users can:

* Register
* Login
* Comment on posts
