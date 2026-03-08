import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

# Load environment variables from .env file
# This allows sensitive data (emails, passwords, secret keys)
# to stay OUT of the source code and GitHub repo
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Secret key is required for session management (flash messages, cookies, etc.)
# If SECRET_KEY is not defined in the environment, a random one is generated
app.secret_key = os.getenv("SECRET_KEY", os.urandom(24))


# Flask-Mail Configuration using environment variables
# Using Gmail SMTP with SSL (secure and common for small projects)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True

# Credentials loaded from environment variables
# IMPORTANT: These should NEVER be committed to GitHub
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_ADDRESS')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')

# Default sender for outgoing emails
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_ADDRESS')

# Initialize Flask-Mail extension
mail = Mail(app)


# -------------------- ROUTES --------------------

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Handles contact form rendering and submission.
    GET  -> Displays the contact page
    POST -> Processes the form and sends an email
    """
    if request.method == 'POST':
        # Retrieve form data sent by the user
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Basic server-side validation
        # This is essential even if client-side validation exists
        if not name or not email or not message:
            flash("Please fill out all required fields.", "danger")
            return redirect(url_for('contact'))

        # Prepare the email content
        msg = Message(
            subject="New Contact Form Submission",
            recipients=[os.getenv('EMAIL_ADDRESS')],
            body=(
                f"Name: {name}\n"
                f"Email: {email}\n\n"
                f"Message:\n{message}"
            )
        )

        try:
            # Attempt to send the email
            mail.send(msg)
            flash("Your message has been sent successfully.", "success")
        except Exception as e:
            # Catch and display email sending errors
            # Useful for debugging SMTP or credential issues
            flash(f"Error sending message: {str(e)}", "danger")

        # Redirect to avoid form resubmission on page refresh
        return redirect(url_for('contact'))

    # Render contact page for GET requests
    return render_template('contact.html', active_page="contact")


# Entry point for local development
if __name__ == "__main__":
    # debug=True enables hot reload and detailed error pages
    # Should be disabled in production
    app.run(debug=True)
