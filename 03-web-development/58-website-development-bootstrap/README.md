# Ground2Tech Engineering Website

Welcome to **Ground2Tech Engineering's** portfolio website! This project is part of my **58 Python Challenge** focused on web development with **Flask** and **Bootstrap**. The goal was to build a professional site to showcase my engineering services and projects. The site also features a contact form where users can reach out, with email notifications being sent upon form submission.

This repository includes:
- **Flask** for the backend (Python).
- **Bootstrap** for styling and responsive design.
- **Icons** sourced from [Flaticon](https://www.flaticon.com/).

---

## **Project Structure**

1. **Flask Web Application**:
    - The web app uses **Flask** to handle routing, rendering HTML templates, and processing contact form submissions.
    - The **Bootstrap** framework provides a clean, responsive layout, including navigation bars, forms, and cards.

2. **Pages**:
    - **Home**: The landing page with an introduction and navigation links.
    - **About**: A page with details on the services provided by Ground2Tech.
    - **Projects**: A section dedicated to showcasing projects (work in progress).
    - **Contact**: Includes a contact form that sends an email to a designated address.

## **Technologies Used**

- **Flask**: Python web framework for handling routing and backend logic.
- **Bootstrap 5**: A CSS framework for building responsive, mobile-first websites.
- **Flask-Mail**: Used for sending email notifications when a user submits the contact form.

---

## **Setup Instructions**

### Prerequisites
- **Python 3.x**
- **Flask**
- **Flask-Mail**
- **Bootstrap (CDN)**

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
   cd 58-website-development-bootstrap
   ```
2. **Create a Virtual Environment:**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Set Up Environment Variables**:
  - You will need to create a .env file in the root of the project for sensitive information (like your email and app credentials). Example:
       ```bash
           EMAIL_ADDRESS=your-email@gmail.com
           EMAIL_PASSWORD=your-email-password
       ```
4. **Run the Flask App**:
   ```bash
   flask run
   ```

---

## Project Flow

### 1. Backend (Flask):
  - The app is structured with basic Flask routing: index, about, projects, and contact.
  - Flask-Mail is configured to handle email notifications. The contact form sends an email to the address specified in the .env file.

### 2. Frontend (Bootstrap):
  - The layout uses Bootstrap's grid system for responsive design.
  - Navigation links, buttons, forms, and cards are all styled using Bootstrap components.
  - Icons are integrated through Flaticon.

### 3. Contact Form Handling:
  - Upon form submission, the user’s message is sent to the email address stored in the .env file.
  - Basic validation is performed using JavaScript to ensure the user fills all required fields before sending the message.

---

## .gitignore

To prevent sensitive information and unnecessary files from being committed to GitHub, use the following .gitignore.
```bash
# Python
__pycache__/
*.pyc

# Flask
instance/
.env

# Virtual Environment
venv/

# IDEs
.vscode/
.idea/
```
This .gitignore ensures:

- Python bytecode files are ignored.
- Flask instance files (which may contain sensitive data) are ignored.
- Virtual environment and IDE configuration files are excluded.

---

## Important Notes:
- You will need to install the python-dotenv package to load variables from the .env file.
  ```bash
  pip install python-dotenv
  ```
- Load the variables in your server.py:
  ```bash
  from dotenv import load_dotenv
  import os
  load_dotenv()
  EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
  EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
  ```

---
## Contact
Feel free to reach out via the contact form or directly through my email if you'd like to collaborate!
