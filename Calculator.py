def simple_calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        print("Result:", num1 + num2)
    elif operation == '-':
        print("Result:", num1 - num2)
    elif operation == '*':
        print("Result:", num1 * num2)
    elif operation == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid operation.")

simple_calculator()
