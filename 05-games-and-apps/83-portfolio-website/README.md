# Ground2Tech Engineering 🌍⚙️

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Active-success)
![Challenge](https://img.shields.io/badge/100%20Python%20Projects-Challenge%20%2383-orange)

A professional **engineering portfolio and consulting website** built
with **Flask and Python** as part of the **100 Python Projects Challenge
(#83)**.

This website represents the foundation of **Ground2Tech Engineering**, a
consulting initiative focused on:

-   Civil Engineering
-   Railway Infrastructure
-   Digital Engineering
-   Python Automation for Construction & Infrastructure
-   Data Analytics for Engineering Projects

The goal of this project is to create a **professional portfolio
platform** that can evolve into a full **engineering consulting company
website**.

------------------------------------------------------------------------

# 🚀 Features

-   Flask-based website
-   Modular Jinja templates
-   Multilingual support (English / German ready)
-   Contact form with email integration
-   Responsive design using Bootstrap
-   Engineering projects portfolio
-   Technical blog section
-   GitHub and LinkedIn integration

------------------------------------------------------------------------

# 🧠 Project Purpose

This project is part of:

**100 Python Projects Challenge**

Project #83 focuses on building a **professional portfolio website** for
showcasing technical work and consulting services.

It will eventually support:

-   Engineering case studies
-   Technical blog articles
-   Digital engineering tools
-   Infrastructure project experience

------------------------------------------------------------------------

# 🏗️ Tech Stack

-   Python 3.12
-   Flask
-   Flask-Babel (multilingual support)
-   Flask-Mail
-   Bootstrap
-   Jinja2 templates

------------------------------------------------------------------------

# 📁 Project Structure

    project/
    │
    ├── app.py
    ├── babel.cfg
    ├── .env
    │
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   ├── about.html
    │   ├── services.html
    │   ├── projects.html
    │   ├── blog.html
    │   ├── contact.html
    │   └── components/
    │        ├── header.html
    │        └── footer.html
    │
    ├── static/
    │   └── assets/
    │        ├── css
    │        ├── js
    │        ├── img
    │        └── vendor
    │
    └── translations/

------------------------------------------------------------------------

# ⚙️ Installation

Clone the repository:

    git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
    cd 100-python-projects-challenge/83-portfolio-development


Create virtual environment:

    python -m venv myenv
    source myenv/bin/activate

Install dependencies:

    pip install flask flask-babel flask-mail python-dotenv

Run the application:

    python app.py

Open the site:

    http://127.0.0.1:5000

------------------------------------------------------------------------

# Environment Variables

Create a .env file
```
SECRET_KEY=your_secret_key EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```
------------------------------------------------------------------------

# Translation Workflow

- Extract text

```pybabel extract -F babel.cfg -o messages.pot```

- Update translations

```pybabel update -i messages.pot -d translations```

- Compile translations

```pybabel compile -d translations```

------------------------------------------------------------------------

# 🌐 Multilingual Support

Language switching is supported using **Flask-Babel**.

Example:

    http://127.0.0.1:5000/?lang=en
    http://127.0.0.1:5000/?lang=de

Future languages planned:

-   Spanish

------------------------------------------------------------------------

# 📬 Contact

If you are interested in collaboration or consulting work related to:

-   Railway infrastructure
-   Civil engineering
-   Engineering automation
-   Python tools for engineering

Feel free to connect:

LinkedIn\
https://www.linkedin.com/in/sebastian-arce-diaz91/

GitHub\
https://github.com/SebastianDiazSD

------------------------------------------------------------------------

# 📜 License

This project is licensed under the **MIT License**.

------------------------------------------------------------------------

# 💡 Future Improvements

-   Engineering case study pages
-   Technical blog articles
-   Python engineering tools showcase
-   SEO optimization
-   Deployment to production server
-   Docker support

------------------------------------------------------------------------

**Ground2Tech Engineering**\
Engineering meets digital innovation.
