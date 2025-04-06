from typing import NoReturn

# ------------------------
# 1. Basic Exception Handling
# ------------------------

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

# ------------------------
# 2. Raising Custom Exception
# ------------------------

class CustomError(Exception):
    """Custom exception for demo purposes"""
    pass

def check_age(age):
    if age < 18:
        raise CustomError("Access denied. You must be at least 18 years old.")
    else:
        print("Access granted.")

# ------------------------
# 3. Function that Never Returns (NoReturn)
# ------------------------

def terminate_program() -> NoReturn:
    """Terminate the program by raising an exception."""
    raise SystemExit("Terminating the program...")

# ------------------------
# 4. Try-Except with Multiple Errors
# ------------------------

def multiple_errors_demo():
    try:
        num = int(input("Enter a number: "))
        print("100 / num =", 100 / num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("You can't divide by zero.")
    else:
        print("Successfully executed without errors.")
    finally:
        print("Always runs - cleaning up...")

# ------------------------
# Run All Examples
# ------------------------

if __name__ == "__main__":
    print("1️⃣ Basic try-except-else-finally:")
    divide(10, 2)
    divide(10, 0)

    print("\n2️⃣ Raising and handling custom exception:")
    try:
        check_age(15)
    except CustomError as ce:
        print("CustomError caught:", ce)

    print("\n3️⃣ NoReturn function example:")
    try:
        terminate_program()
    except SystemExit as se:
        print("Caught SystemExit:", se)

    print("\n4️⃣ Try-except with multiple exceptions:")
    multiple_errors_demo()
