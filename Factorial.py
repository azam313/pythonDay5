def calculate_factorial():
    number = int(input("Enter a positive integer: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of", number, "is:", factorial)

calculate_factorial()
