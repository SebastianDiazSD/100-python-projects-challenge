import os
import stripe
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from dotenv import load_dotenv
from products import products

load_dotenv()

app = Flask(__name__)
app.secret_key = "secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
db = SQLAlchemy(app)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)

# ---------------------
# Database
# ---------------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------------
# Routes
# ---------------------

@app.route("/")
def home():
    return render_template("index.html", products=products)

# ---------------------
# Authentication
# ---------------------

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = User(
            email=request.form["email"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()

        if user and user.password == request.form["password"]:
            login_user(user)
            return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

# ---------------------
# Cart
# ---------------------

@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True

    return redirect(url_for("cart"))

@app.route("/cart")
def cart():

    cart_items = []

    if "cart" in session:
        for product_id in session["cart"]:
            for product in products:
                if product["id"] == product_id:
                    cart_items.append(product)

    total = sum(item["price"] for item in cart_items)

    return render_template("cart.html", cart=cart_items, total=total)

# ---------------------
# Stripe Checkout
# ---------------------

@app.route("/checkout")
@login_required
def checkout():

    cart = session.get("cart", [])

    line_items = []

    for product_id in cart:
        for product in products:
            if product["id"] == product_id:
                line_items.append({
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": product["name"]
                        },
                        "unit_amount": product["price"] * 100
                    },
                    "quantity": 1
                })

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url=url_for("success", _external=True),
        cancel_url=url_for("cancel", _external=True),
    )

    return redirect(checkout_session.url)

@app.route("/success")
def success():
    session["cart"] = []
    return render_template("success.html")

@app.route("/cancel")
def cancel():
    return render_template("cancel.html")

# ---------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)