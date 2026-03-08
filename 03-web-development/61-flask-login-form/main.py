from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

"""
Project 61/100 – Advanced Forms with Flask-WTF

If you see red underlines in PyCharm:
Make sure you install the required dependencies.

Windows:
    python -m pip install -r requirements.txt

MacOS / Linux:
    pip3 install -r requirements.txt
"""


# ----------------------------
# Flask-WTF Form Definition
# ----------------------------
class LoginForm(FlaskForm):
    """
    Simple login form using Flask-WTF.
    In a real-world app, credentials would be
    validated against a database.
    """
    email = StringField(
        label="Email",
        validators=[
            DataRequired(message="Email is required"),
            Email(message="Please enter a valid email address")
        ]
    )
    password = PasswordField(
        label="Password",
        validators=[
            DataRequired(message="Password is required"),
            Length(min=8, message="Password must be at least 8 characters")
        ]
    )
    submit = SubmitField(label="Log In")


# ----------------------------
# Flask App Configuration
# ----------------------------
app = Flask(__name__)
app.secret_key = "super-secret-key-change-me"  # Needed for CSRF protection
Bootstrap5(app)


# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def home():
    """
    Landing page.
    """
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login page with form validation.
    """
    login_form = LoginForm()

    if login_form.validate_on_submit():
        # Temporary credentials for demo purposes
        if (
            login_form.email.data == "admin@email.com"
            and login_form.password.data == "12345678"
        ):
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)


# ----------------------------
# App Runner
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5001)
