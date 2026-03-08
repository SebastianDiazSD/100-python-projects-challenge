from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

# ----------------------------
# App Configuration
# ----------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# ----------------------------
# Database Model
# ----------------------------

class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        """Serialize model object to dictionary."""
        return {column.name: getattr(self, column.name)
                for column in self.__table__.columns}


with app.app_context():
    db.create_all()


# ----------------------------
# Routes
# ----------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------
# GET - Random Cafe
# ----------------------------

@app.route("/random", methods=["GET"])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()

    if not cafes:
        return jsonify(error={"Not Found": "No cafes available in the database."}), 404

    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict()), 200


# ----------------------------
# GET - All Cafes
# ----------------------------

@app.route("/all", methods=["GET"])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    cafes = result.scalars().all()

    return jsonify(
        count=len(cafes),
        cafes=[cafe.to_dict() for cafe in cafes]
    ), 200


# ----------------------------
# GET - Search by Location
# ----------------------------

@app.route("/search", methods=["GET"])
def search_cafe_by_location():
    location = request.args.get("loc")

    if not location:
        return jsonify(error={"Bad Request": "Please provide a location using ?loc=LocationName"}), 400

    result = db.session.execute(
        db.select(Cafe).where(Cafe.location == location)
    )
    cafes = result.scalars().all()

    if not cafes:
        return jsonify(error={"Not Found": f"No cafes found in {location}."}), 404

    return jsonify(
        count=len(cafes),
        cafes=[cafe.to_dict() for cafe in cafes]
    ), 200


# ----------------------------
# POST - Add New Cafe
# ----------------------------

@app.route("/add", methods=["POST"])
def add_new_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )

        db.session.add(new_cafe)
        db.session.commit()

        return jsonify(response={"success": "Cafe successfully added. Welcome to the network!"}), 201

    except Exception as e:
        return jsonify(error={"Internal Server Error": str(e)}), 500


# ----------------------------
# PATCH - Update Coffee Price
# ----------------------------

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")

    if not new_price:
        return jsonify(error={"Bad Request": "Please provide new_price parameter."}), 400

    cafe = db.session.get(Cafe, cafe_id)

    if not cafe:
        return jsonify(error={"Not Found": "Cafe not found."}), 404

    cafe.coffee_price = new_price
    db.session.commit()

    return jsonify(response={"success": "Coffee price updated successfully."}), 200


# ----------------------------
# DELETE - Remove Closed Cafe
# ----------------------------

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")

    if api_key != "TopSecretAPIKey":
        return jsonify(error={"Forbidden": "Invalid API key."}), 403

    cafe = db.session.get(Cafe, cafe_id)

    if not cafe:
        return jsonify(error={"Not Found": "Cafe not found."}), 404

    db.session.delete(cafe)
    db.session.commit()

    return jsonify(response={"success": "Cafe removed from the database."}), 200


# ----------------------------

if __name__ == "__main__":
    app.run(debug=True)
