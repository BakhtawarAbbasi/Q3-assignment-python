# ---- Built-in Module Example ----
import math

def circle_area(radius):
    return math.pi * radius * radius

# ---- User-defined Function Examples ----

# Default Argument
def greet(name="Bakhtawar"):
    return f"Hello, {name}!"

# Positional-only Arguments
def pos_only(x, y, /):
    return x + y

# Keyword-only Arguments
def keyword_only(*, z):
    return z * 2

# Arbitrary Positional Arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

# Arbitrary Keyword Arguments (**kwargs)
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda Function (Anonymous)
square = lambda x: x * x

# Generator Function
def count_up_to(max):
    num = 1
    while num <= max:
        yield num
        num += 1

# Recursive Function (Factorial)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# ---- Using the functions ----
if __name__ == "__main__":
    print("Circle area (r=5):", circle_area(5))
    print(greet())
    print("Positional only sum (2+3):", pos_only(2, 3))
    print("Keyword only double (z=4):", keyword_only(z=4))
    print("Sum using *args:", sum_all(1, 2, 3, 4))
    print("Info using **kwargs:")
    show_info(name="Bakhtawar", course="Python", level="Intermediate")
    print("Lambda square of 6:", square(6))
    
    print("Generator output (1 to 5):")
    for number in count_up_to(5):
        print(number, end=" ")
    print()

    print("Factorial of 5:", factorial(5))
