# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))
# TODO: Input operation
operation = input("Enter an operation (+, -, *, /, %, **): ").strip()
# TODO: Match operation using if-elif
# TODO: Handle division/modulus by zero with try-except
try:
    if operation == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")

    elif operation == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")

    elif operation == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")

    elif operation == "/":
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

    elif operation == "%":
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")

    elif operation == "**":
        result = num1 ** num2
        print(f"Result: {num1} ** {num2} = {result}")

  


# TODO: Print result
except ZeroDivisionError:
    print(f"Error: Cannot perform '{operation}' because the second number is zero.")