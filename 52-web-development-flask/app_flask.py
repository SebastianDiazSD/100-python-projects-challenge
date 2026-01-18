from flask import Flask, request, render_template_string

# Mi viejo, here we start our Flask app
app = Flask(__name__)

# ----------------------------------------------------
# Calculation logic
# Aquí lo hacemos con paciencia y buena matemática
# ----------------------------------------------------

def add(n1, n2):
    """Add two numbers, parce."""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers, suave."""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers, sin afán."""
    return n1 * n2


def divide(n1, n2):
    """Divide two numbers. Ojo pues, no dividing by zero."""
    if n2 == 0:
        return "Parce… dividing by zero is not allowed 😅"
    return n1 / n2


# ----------------------------------------------------
# Main route – Our first professional homepage
# ----------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    operation_name = ""

    # If the parcero submits the form, we process the numbers
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = add(num1, num2)
            operation_name = "Addition"
        elif operation == "subtract":
            result = subtract(num1, num2)
            operation_name = "Subtraction"
        elif operation == "multiply":
            result = multiply(num1, num2)
            operation_name = "Multiplication"
        elif operation == "divide":
            result = divide(num1, num2)
            operation_name = "Division"

    # Rendering HTML directly for simplicity (later we move to templates)
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Introduction to Flask</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 40px;
                }
                .container {
                    background: white;
                    padding: 30px;
                    max-width: 500px;
                    margin: auto;
                    border-radius: 8px;
                }
                h1 {
                    color: #333;
                }
                button {
                    background-color: #007b5e;
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #005f46;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Introduction to Flask</h1>
                <p>
                    Welcome to our calculation section, parcero.<br>
                    Aquí lo hacemos con paciencia y buen código.
                </p>

                <form method="POST">
                    <label>First Number:</label><br>
                    <input type="number" step="any" name="num1" required><br><br>

                    <label>Second Number:</label><br>
                    <input type="number" step="any" name="num2" required><br><br>

                    <label>Select an operation:</label><br>
                    <select name="operation">
                        <option value="add">Add</option>
                        <option value="subtract">Subtract</option>
                        <option value="multiply">Multiply</option>
                        <option value="divide">Divide</option>
                    </select><br><br>

                    <button type="submit">Calculate, mi viejo</button>
                </form>

                {% if result is not none %}
                    <hr>
                    <h2>Result</h2>
                    <p>
                        Operation: <strong>{{ operation_name }}</strong><br>
                        Result: <strong>{{ result }}</strong>
                    </p>
                    <p>Bien hecho, parcero 🚀</p>
                {% endif %}
            </div>
        </body>
        </html>
    """, result=result, operation_name=operation_name)


# ----------------------------------------------------
# Run the app
# Same as running from the terminal, pero con estilo
# ----------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
