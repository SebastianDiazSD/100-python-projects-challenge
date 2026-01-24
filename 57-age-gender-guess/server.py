from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    name = request.form['name'].strip().capitalize()
    if not name:
        return render_template('index.html', error="Please enter a valid name.")

    try:
        age_data = requests.get(f"https://api.agify.io/?name={name}").json()
        gender_data = requests.get(f"https://api.genderize.io/?name={name}").json()

        age = age_data.get("age", "unknown")
        gender = gender_data.get("gender", "unknown").capitalize()

        # Friendly Colombian-style message
        if age != "unknown":
            message = f"Hello {name}, I think you are {gender} and probably you are {age} years old. ¡Qué chévere!"
        else:
            message = f"Hello {name}, I'm not sure about your age, but I bet you're amazing! 😊"
    except Exception:
        message = "Oops! Could not fetch data. Please try again."

    return render_template('guess.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)