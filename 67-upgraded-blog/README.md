# 🚆 67 - Upgraded Blog (Flask + CKEditor + SQLAlchemy)

An upgraded full-stack blog application built with Flask, featuring a relational database, rich text editing, and complete CRUD functionality.

This project is part of the **100 Python Projects Challenge**, focusing on progressively building production-ready applications.

---

## 📌 Project Overview

This upgraded blog application allows users to:

- View all blog posts
- Create new posts using a rich text editor
- Edit existing posts
- Delete posts
- Store content in a SQLite database

The project integrates backend logic, database management, templating, and UI styling into a structured Flask application.

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **Flask-Bootstrap**
- **Flask-WTF**
- **Flask-CKEditor**
- **SQLAlchemy (ORM)**
- **SQLite**
- **Jinja2 Templates**
- **Bootstrap 5**

---

## 🧠 Key Features

### 1️⃣ Full CRUD Functionality
- Create posts
- Read posts
- Update posts
- Delete posts

### 2️⃣ Rich Text Editing
CKEditor integration allows formatted blog content including:
- Headings
- Lists
- Links
- Structured paragraphs

### 3️⃣ Database Integration
Posts are stored in a relational SQLite database using SQLAlchemy ORM.

**Model Structure:**

- `id`
- `title`
- `subtitle`
- `date`
- `body`
- `author`
- `img_url`

### 4️⃣ Dynamic Routing
- `/` → View all posts  
- `/post/<id>` → View single post  
- `/new-post` → Create post  
- `/edit-post/<id>` → Edit post  
- `/delete/<id>` → Delete post  

---

## 📂 Project Structure

```yaml
67-upgraded-blog/
│
├── main.py
├── requirements.txt
├── instance/
│ ├── posts.db
│
├── templates/
│ ├── header.html
│ ├── footer.html
│ ├── index.html
│ ├── post.html
│ ├── make-post.html
│ ├── about.html
│ └── contact.html
│
└── static/
├── css/
├── js/
└── assets/
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
```
Navigate to the project folder:
```bash
cd 100-python-projects-challenge/67-upgraded-blog
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
```
Activate it:
**Windows**
```bash
source venv/bin/activate
```
**Mac/Linux**
```bash
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python main.py
```
Open in browser:
```bash
http://127.0.0.1:5003
```

---

## 🗄 Database

The application uses SQLite.

If the database does not exist, it will be created automatically on first run.

To reset the database manually:

* Delete posts.db
* Restart the application

---

## 🔐 Notes

* `SECRET_KEY` should be changed before deploying.
* For production deployment, use environment variables.
* SQLite is suitable for development but can be replaced with PostgreSQL or MySQL.
