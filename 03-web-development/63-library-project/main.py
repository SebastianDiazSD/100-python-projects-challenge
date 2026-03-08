from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Create the Flask app
app = Flask(__name__)

# Create the Database

class Base(DeclarativeBase):
    pass

# Point to your existing SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Optional: turn off modification tracking
app.secret_key = "secret123"  # Needed for flash

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Book model, this reflects the existing 'books' table in your database
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create the tables (if not already created)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # Query all books
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        # Get form data
        title = request.form["title"]
        author = request.form["author"]
        rating = float(request.form["rating"])

        # Create a new book record
        new_book = Book(title=title, author=author, rating=rating)

        # Add the new book to the database
        db.session.add(new_book)
        try:
            db.session.commit()
            flash("¡Listo! Book added to the Database!")
        except:
            db.session.rollback()
            flash("Oops! Ese título ya existe. Book already exists!")


        # Redirect to the home page
        return redirect(url_for("home"))

    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit_books():
    book_ids = request.args.get("book_ids", "")
    ids_list = [int(id) for id in book_ids.split(",") if id.isdigit()]

    if request.method == "POST":
        for book_id in ids_list:
            book = Book.query.get(book_id)
            if book:
                book.rating = float(request.form[f"rating_{book_id}"])
        db.session.commit()
        flash(f"¡Listo! {len(ids_list)} book(s) updated.")
        return redirect(url_for("home"))

    books = Book.query.filter(Book.id.in_(ids_list)).all()
    return render_template("edit.html", books=books)

@app.route("/bulk-action", methods=["POST"])
def bulk_action():
    selected_ids = request.form.getlist("book_ids")
    if not selected_ids:
        flash("Parce! You haven't selected any book")
        return redirect(url_for("home"))

    action = request.form.get("action")

    if action == "delete":
        Book.query.filter(Book.id.in_(selected_ids)).delete(synchronize_session=False)
        db.session.commit()
        flash(f"¡Borrado! {len(selected_ids)} book(s) removed.")

    elif action == "edit":
        return redirect(url_for("edit_books", book_ids=",".join(selected_ids)))

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
