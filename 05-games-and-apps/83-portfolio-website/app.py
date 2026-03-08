import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_babel import Babel, gettext as _

# -------------------------
# LOAD ENVIRONMENT VARIABLES
# -------------------------

load_dotenv()

# -------------------------
# INITIALIZE FLASK APP
# -------------------------

app = Flask(__name__)

# Secret key for sessions
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))

# -------------------------
# BABEL CONFIGURATION
# -------------------------

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'de']

def get_locale():
    """Detect language from URL parameter"""
    return request.args.get('lang') or 'en'

babel = Babel(app, locale_selector=get_locale)

# -------------------------
# EMAIL CONFIGURATION
# -------------------------

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_ADDRESS')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_ADDRESS')

mail = Mail(app)

# -------------------------
# ROUTES
# -------------------------

@app.route('/')
def home():
    return render_template(
        'index.html',
        active_page="home"
    )


@app.route('/about')
def about():
    return render_template(
        'about.html',
        active_page="about"
    )


@app.route('/services')
def services():
    return render_template(
        'services.html',
        active_page="services"
    )


@app.route('/projects')
def projects():
    return render_template(
        'projects.html',
        active_page="projects"
    )


@app.route('/blog')
def blog():
    return render_template(
        'blog.html',
        active_page="blog"
    )


# -------------------------
# CONTACT FORM
# -------------------------

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic validation
        if not name or not email or not message:
            flash(_("Please fill out all required fields."), "danger")
            return redirect(url_for('contact'))

        msg = Message(
            subject=_("New Contact Form Submission"),
            recipients=[os.getenv('EMAIL_ADDRESS')],
            body=f"""
Name: {name}
Email: {email}

Message:
{message}
"""
        )

        try:

            mail.send(msg)
            flash(_("Your message has been sent successfully!"), "success")

        except Exception as e:

            flash(_("Error sending message."), "danger")
            print(e)

        return redirect(url_for('contact'))

    return render_template(
        'contact.html',
        active_page="contact"
    )


# -------------------------
# RUN APP
# -------------------------

if __name__ == '__main__':
    app.run(debug=True)