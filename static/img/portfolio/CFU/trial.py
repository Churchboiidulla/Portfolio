def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    # Taking input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Checking operator and performing calculation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0: 
            return "Error: Cannot divide by zero!"
        result = num1 / num2
    else:
        return "Invalid operator!"

    return f"Result: {result}"


# Run the calculator
print(calculator())

