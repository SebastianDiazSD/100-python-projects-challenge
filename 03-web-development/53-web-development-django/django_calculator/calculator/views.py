from django.shortcuts import render

# Aquí lo hacemos con paciencia, mi viejo
def home(request):
    result = None
    operation_name = ""

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operation = request.POST.get("operation")

        if operation == "add":
            result = num1 + num2
            operation_name = "Addition"
        elif operation == "subtract":
            result = num1 - num2
            operation_name = "Subtraction"
        elif operation == "multiply":
            result = num1 * num2
            operation_name = "Multiplication"
        elif operation == "divide":
            operation_name = "Division"
            if num2 == 0:
                result = "Parce… division by zero is not allowed 😅"
            else:
                result = num1 / num2

    return render(
        request,
        "calculator/home.html",
        {
            "result": result,
            "operation_name": operation_name,
        }
    )
