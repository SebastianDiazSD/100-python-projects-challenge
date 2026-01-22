from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])  # <-- Add POST here
def home():
    if request.method == "POST":
        # get form data
        name = request.form.get("name")
        message = request.form.get("message")
        print(f"New message from {name}: {message}")
        # You could redirect or show a success message
        return render_template("index.html", success=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)