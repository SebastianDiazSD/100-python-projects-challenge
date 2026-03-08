from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "coffee-productivity"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"

db = SQLAlchemy(app)


# DATABASE MODEL
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(50), nullable=False)


# FORM
class TaskForm(FlaskForm):

    title = StringField(
        "Task",
        validators=[DataRequired()]
    )

    status = SelectField(
        "Status",
        choices=[
            ("todo", "To Do"),
            ("doing", "In Progress"),
            ("done", "Done")
        ]
    )

    submit = SubmitField("Add Task")


# HOME PAGE
@app.route("/")
def home():

    todo = Task.query.filter_by(status="todo").all()
    doing = Task.query.filter_by(status="doing").all()
    done = Task.query.filter_by(status="done").all()

    return render_template(
        "index.html",
        todo=todo,
        doing=doing,
        done=done
    )


# ADD TASK
@app.route("/add", methods=["GET", "POST"])
def add_task():

    form = TaskForm()

    if form.validate_on_submit():

        new_task = Task(
            title=form.title.data,
            status=form.status.data
        )

        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add_task.html", form=form)


# MOVE TASK
@app.route("/move/<int:task_id>/<string:new_status>")
def move_task(task_id, new_status):

    task = Task.query.get(task_id)

    task.status = new_status
    db.session.commit()

    return redirect(url_for("home"))


# DELETE TASK
@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    task = Task.query.get(task_id)

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)