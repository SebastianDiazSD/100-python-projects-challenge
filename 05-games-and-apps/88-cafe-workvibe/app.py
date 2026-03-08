from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "cafe-workvibe-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"

db = SQLAlchemy(app)


# DATABASE MODEL
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250))
    coffee_price = db.Column(db.String(250))


# FORM
class CafeForm(FlaskForm):
    name = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    map_url = StringField("Google Maps URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    seats = StringField("Seats")
    coffee_price = StringField("Coffee price")

    has_wifi = BooleanField("WiFi available")
    has_sockets = BooleanField("Power sockets")
    has_toilet = BooleanField("Toilet")
    can_take_calls = BooleanField("Good for calls")

    submit = SubmitField("Add Cafe")


# HOME PAGE
@app.route("/")
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)


# ADD CAFE
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            location=form.location.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
            has_wifi=form.has_wifi.data,
            has_sockets=form.has_sockets.data,
            has_toilet=form.has_toilet.data,
            can_take_calls=form.can_take_calls.data
        )

        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add_cafe.html", form=form)


# MAP PAGE
@app.route("/map")
def cafe_map():

    cafes = Cafe.query.all()
    cafes_with_coords = []

    for cafe in cafes:

        try:
            query = f"{cafe.name} London"
            url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json&limit=1"

            response = requests.get(
                url,
                headers={"User-Agent": "cafe-workvibe"},
                timeout=5
            )

            if response.status_code != 200:
                continue

            data = response.json()

            if data:
                lat = float(data[0]["lat"])
                lng = float(data[0]["lon"])

                cafes_with_coords.append({
                    "name": cafe.name,
                    "location": cafe.location,
                    "coffee_price": cafe.coffee_price,
                    "wifi": cafe.has_wifi,
                    "map_url": cafe.map_url,
                    "lat": lat,
                    "lng": lng
                })

        except Exception as e:
            print("Geocoding error:", e)
            continue

    return render_template("map.html", cafes=cafes_with_coords)


# DELETE CAFE
@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)