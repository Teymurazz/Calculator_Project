from datetime import datetime


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        print("Division by zero not allowed")
        return None
    else:
        return z

def save_to_history(operation, result):
    operation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Saving to history: {operation_time}: {operation} = {result}")
    with open("history.txt", "a") as file:
        file.write(f"{operation_time}: {operation} = {result}\n")

def calculator():
    while True:
        print("Calculator Instructions:")
        print("Enter '+' for addition")
        print("Enter '-' for subtraction")
        print("Enter '*' for multiplication")
        print("Enter '/' for division")
        print("Enter 'history' to view calculation history")
        print("Enter 'exit' to quit")

        operation = input("Enter operation: ")
        if operation == 'exit':
            break

        if operation == 'history':
            with open("history.txt", "r") as file:
                print(file.read())
            continue

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Choose +, -, *, or /.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter number.")
            continue

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        if result is not None:
            print(f"Result: {result}")
            save_to_history(f"{num1} {operation} {num2}", result)

calculator()
