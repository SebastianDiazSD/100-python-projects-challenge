"""
Project 68/100 - Flask Authentication System
Author: Sebastian Diaz

This project demonstrates:
- User registration
- Secure password hashing
- Login authentication
- Protected routes
- Session management with Flask-Login
"""

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# -----------------------------------------------------
# App Configuration
# -----------------------------------------------------

app = Flask(__name__)

# Secret key used for session encryption
app.config['SECRET_KEY'] = 'change-this-to-a-secure-random-key'

# Database configuration (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'


# -----------------------------------------------------
# Database Setup
# -----------------------------------------------------

class Base(DeclarativeBase):
    """Base class required for SQLAlchemy models."""
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# -----------------------------------------------------
# Login Manager Setup
# -----------------------------------------------------

login_manager = LoginManager()
login_manager.init_app(app)

# Redirect unauthorized users to login page
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    """
    Required by Flask-Login.
    Loads a user from the database by ID.
    """
    return db.get_or_404(User, user_id)


# -----------------------------------------------------
# User Model
# -----------------------------------------------------

class User(UserMixin, db.Model):
    """
    User table structure:
    - id: Primary key
    - email: Unique user email
    - password: Hashed password
    - name: User's display name
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(100))


# Create database tables
with app.app_context():
    db.create_all()


# -----------------------------------------------------
# Routes
# -----------------------------------------------------

@app.route('/')
def home():
    """
    Home page.
    Shows login/register buttons if user is not authenticated.
    """
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Handles user registration.
    - Checks if email already exists
    - Hashes password securely
    - Logs in user automatically after registration
    """
    if request.method == "POST":

        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        # Check if email already exists
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if user:
            flash("That email is already registered. Try logging in instead, parcero 😉")
            return redirect(url_for('login'))

        # Secure password hashing
        hashed_password = generate_password_hash(
            password,
            method='pbkdf2:sha256',
            salt_length=8
        )

        # Create new user
        new_user = User(
            email=email,
            password=hashed_password,
            name=name,
        )

        db.session.add(new_user)
        db.session.commit()

        # Log in automatically after registration
        login_user(new_user)

        return redirect(url_for("secrets"))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Handles user login.
    - Validates email
    - Verifies password hash
    - Redirects to protected page if successful
    """
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("No account found with that email. Check again, parce.")
            return redirect(url_for('login'))

        elif not check_password_hash(user.password, password):
            flash("Incorrect password. Try again with calma.")
            return redirect(url_for('login'))

        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    """
    Protected route.
    Only accessible to authenticated users.
    """
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    """
    Logs the user out and clears session.
    """
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    """
    Allows authenticated users to download a protected file.
    """
    return send_from_directory('static', path="files/cheat_sheet.pdf")


# -----------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
