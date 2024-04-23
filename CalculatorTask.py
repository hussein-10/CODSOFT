def calculate(num1, num2, operator):
    """
    Performs basic arithmetic operations based on the provided operator

    Args:
        num1: The first number
        num2: The second number
        operator: The operation symbol (+, -, *, /)

    Returns:
        The result of the calculation
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero")
            return None
        else:
            return num1 / num2
    else:
        print("Invalid operator")
        return None


while True:
    # Get user input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")
    except ValueError:
        print("Invalid input. Please enter numbers only")
        continue

    # Perform calculation
    result = calculate(num1, num2, operator)

    # Display result or error message
    if result is not None:
        print(f"{num1} {operator} {num2} = {result}")

    # Ask user if they want to continue
    choice = input("Do you want to perform another calculation? (y/n) ")
    if choice.lower() != "y":
        break

print("Calculator closed")
