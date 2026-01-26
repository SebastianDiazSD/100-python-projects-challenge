# Contact Form Module – Flask & Bootstrap

A reusable contact form built with **Flask**, **Bootstrap 5**, and **Flask-Mail**, designed to be easily integrated into any website.  
This project focuses on clean backend logic, secure configuration, and a simple, responsive UI — built with discipline, coffee ☕, and code in Colombia.

---

## 🚀 Project Overview

This application allows users to:
- Enter their **name**, **email**, and **message**
- Submit the form securely
- Automatically send the message to the site owner via email

The goal of this project is not just design, but **functionality that works in real-world scenarios** and can be reused across different websites.

---

## 🧰 Tech Stack

- **Python 3**
- **Flask**
- **Flask-Mail**
- **Bootstrap 5**
- **HTML5 / CSS3**
- **dotenv** for environment variable management

---

## ✨ Features

- Responsive contact form using Bootstrap
- Server-side and client-side validation
- Secure email configuration using environment variables
- Flash messages for user feedback
- Clean and readable project structure
- Easy to adapt and reuse in other projects

---

## 📁 Project Structure
```bash
project/
│
├── server.py
├── templates/
│ └── contact.html
├── static/
│ └── profile_images/
├── .env.example
├── .gitignore
└── README.md
```

---

## 🔐 Environment Variables

For security reasons, email credentials are not hard-coded.

Create a `.env` file based on `.env.example`:

```env
SECRET_KEY=your_secret_key
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
```
---

## ▶️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   ```
2. Install dependencies:
   ```bash
   pip install flask flask-mail python-dotenv
   ```
3. Run the application:
   ```bash
   python server.py
   ```
4. Open your browser and go to:
   ```bash
   http://127.0.0.1:5000/contact
   ```

---

## 🔄 Reusability

This contact form was designed as a **plug-and-play module**:

- You can drop it into any Flask project
- Only the design and branding need to be adjusted
- Backend logic remains the same
- Perfect for portfolios, small businesses, or engineering-focused websites.

---

## 📌 Final Note

Simple code. Clear structure. Real functionality.
> Built with care, responsibility, and a Colombian engineering mindset 🇨🇴
