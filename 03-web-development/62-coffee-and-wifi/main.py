from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired
import csv

"""
☕ Café Finder — Colombian Edition

Quick setup:
1. Create a virtual environment:
   python3 -m venv myenv

2. Activate it:
   source myenv/bin/activate  (Mac/Linux)
   myenv\\Scripts\\activate   (Windows)

3. Install dependencies:
   pip install -r requirements.txt

Now you're ready to go. ¡De una! 🇨🇴
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe Name', validators=[DataRequired()])
    cafe_location = URLField('Google Maps Location', validators=[DataRequired()])
    opening_time = TimeField('Opening Time', validators=[DataRequired()])
    closing_time = TimeField('Closing Time', validators=[DataRequired()])

    coffee_rating = SelectField(
        "Coffee Quality ☕",
        choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
        validators=[DataRequired()]
    )

    wifi_rating = SelectField(
        "WiFi Strength 💻",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()]
    )

    power_rating = SelectField(
        "Power Outlets 🔌",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()]
    )

    submit = SubmitField('Save Café')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(
                f"\n{form.cafe_name.data},"
                f"{form.cafe_location.data},"
                f"{form.opening_time.data},"
                f"{form.closing_time.data},"
                f"{form.coffee_rating.data},"
                f"{form.wifi_rating.data},"
                f"{form.power_rating.data}"
            )
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = [row for row in csv_data]

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
