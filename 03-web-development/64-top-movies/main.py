from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import random
import csv

# Initialize Flask app
app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# SQLite database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Flask-Bootstrap for styling
Bootstrap5(app)

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Create a base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass


# Movie model (Database schema for movie data)
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=True)
    image_url: Mapped[str] = mapped_column(String(250), nullable=True)
    image_credit: Mapped[str] = mapped_column(String(250), nullable=True)
    watch_link: Mapped[str] = mapped_column(String(250), nullable=True)
    favorite: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    review: Mapped[str] = mapped_column(String(500), nullable=True)

    def __repr__(self):
        return f'<Book {self.title}>'


# Create the database tables (if not already created)
with app.app_context():
    db.create_all()


# Form to allow users to mark a movie as favorite and add a review
class MovieForm(FlaskForm):
    favorite = BooleanField('Mark as Favorite')
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Save')


# Function to import data from CSV to the database
def import_csv_to_db():
    with open('streaming_content.csv', 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            # Check if the movie already exists in the database based on the title
            existing_book = Book.query.filter_by(title=row['title']).first()
            if not existing_book:
                new_book = Book(
                    title=row['title'],
                    description=row['description'],
                    image_url=row['image_url'],
                    image_credit=row['image_credit'],
                    watch_link=row['watch_link'],
                    # Set default values for the missing columns
                    favorite=False,  # Default to not a favorite
                    review=""  # Default to no review
                )
                db.session.add(new_book)  # Add to the session
        db.session.commit()  # Commit the changes to the database


# Route to display random movies and allow users to mark as favorite or add a review
@app.route("/", methods=["GET", "POST"])
def home():
    # Fetch 5 random movies from the database
    books = Book.query.order_by(db.func.random()).limit(5).all()

    form = MovieForm()

    # Handle form submission to update favorite or review
    if form.validate_on_submit():
        movie_id = request.form.get("movie_id")
        book = Book.query.get(movie_id)
        if book:
            book.favorite = form.favorite.data
            book.review = form.review.data
            db.session.commit()
        return redirect(url_for('home'))

    return render_template("index.html", books=books, form=form)


# Route to refresh the cards with new random movies
@app.route("/refresh", methods=["GET", "POST"])
def refresh():
    # Fetch 5 new random movies
    books = Book.query.order_by(db.func.random()).limit(5).all()
    return render_template("index.html", books=books)


# Route to show favorite movies
@app.route("/favorites")
def favorites():
    books = Book.query.filter_by(favorite=True).all()
    return render_template("favorites.html", books=books)


# Run the app
if __name__ == '__main__':
    # Import CSV data into the database inside the app context
    with app.app_context():
        import_csv_to_db()

    app.run(debug=True)
