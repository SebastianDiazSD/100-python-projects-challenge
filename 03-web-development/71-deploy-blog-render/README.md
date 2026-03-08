# 🚀 71 – Deploying a Flask Blog to Production  
### Render • PostgreSQL • Gunicorn • Environment Variables

This project documents the deployment process of a Flask blog application to a live production environment using Render.com and PostgreSQL.

It represents the transition from local development (SQLite + Flask development server) to a production-ready deployment stack.

Part of the **100 Python Projects Challenge**.

---

## 📌 Objective

Take the authenticated Flask blog application (Project 69) and deploy it live on the internet using:

- Cloud hosting (Render)
- PostgreSQL database
- Gunicorn WSGI server
- Environment variables
- Production configuration practices

---

## 🏗 Deployment Architecture

Browser  
↓  
Render Web Service  
↓  
Gunicorn (WSGI Server)  
↓  
Flask Application  
↓  
SQLAlchemy ORM  
↓  
PostgreSQL Database  

---

## 🛠 Technologies Used

- Python 3.12
- Flask 3.x
- SQLAlchemy 2.x
- Gunicorn
- PostgreSQL
- Render.com
- GitHub Integration
- Environment Variables
- Bleach (CKEditor sanitization)

---

## ⚙️ Key Deployment Changes

### 1️⃣ Replace SQLite with PostgreSQL

Local Development:
```python
sqlite:///posts.db
```
Production:
```python
postgresql://user:password@host:port/database
```

No model changes were required thanks to SQLAlchemy ORM abstraction.

---

### 2️⃣ Use Environment Variables

In `main.py`:

```python
import os

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
```
Hardcoded credentials are removed for security and portability.

---

### 3️⃣ Add Gunicorn

Render requires a WSGI server.

Start command:
```python
gunicorn main:app
```

---

## 🚀 Deployment Steps on Render
### 1️⃣ Create Account

* Sign up at https://render.com using GitHub

### 2️⃣ Create Web Service

* Connect GitHub repository
* Select project folder (if using monorepo)
* Configure:

Build Command:
```python
pip install -r requirements.txt
```
Start Command:
```python
gunicorn main:app
```
### 3️⃣ Create PostgreSQL Database

* Create new PostgreSQL instance on Render
* Copy Internal Database URL

⚠️ Important:
Change:
```python
postgres://
```
To:
```python
postgresql://
```

### 4️⃣ Set Environment Variables

Add to Web Service:

Key:
```python
SECRET_KEY
```
Key:
```python
DATABASE_URL
```
Value:
```python
postgresql://your-corrected-database-url
```
### 5️⃣ Deploy

Render will:

* Install dependencies
* Build environment
* Start Gunicorn
* Connect to PostgreSQL
* Launch application

---

## 🔐 Why PostgreSQL Instead of SQLite?

SQLite:

* File-based
* Not persistent in cloud environments
* Unsuitable for concurrent production use

PostgreSQL:

* Server-based
* Persistent
* Scalable
* Production-ready

---

## 📦 Production Concepts Learned

* Difference between development and production environments
* WSGI servers (Gunicorn)
* Environment-based configuration
* Cloud-hosted databases
* Persistent storage vs ephemeral filesystem
* Infrastructure separation
* Secure secret management
