# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division




# Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3
print(x)

x -= 2  # Equivalent to x = x - 2
print(x)

x *= 4  # Equivalent to x = x * 4
print(x)

x /= 2  # Equivalent to x = x / 2
print(x)

x %= 3  # Equivalent to x = x % 3
print(x)

x **= 2  # Equivalent to x = x ** 2
print(x)

x //= 2  # Equivalent to x = x // 2
print(x)




# Comparison Operators
a = 10
b = 5
print(a == b)  # Equal
print(a != b)  # Not Equal
print(a > b)   # Greater Than
print(a < b)   # Less Than
print(a >= b)  # Greater Than or Equal To
print(a <= b)  # Less Than or Equal To




# Logical Operators
x = True
y = False
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT




# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True because 'b' is the same object as 'a'
print(a is c)   # False because 'c' is a different object
print(a is not c)  # True




# Membership Operators
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)   # True
print(10 in numbers)  # False
print(6 not in numbers)  # True




# Bitwise Operators
a = 5  # 0101 in binary
b = 3  # 0011 in binary
print(a & b)  # AND -> 0001 (1)
print(a | b)  # OR  -> 0111 (7)
print(a ^ b)  # XOR -> 0110 (6)
print(~a)     # NOT -> -(a+1)
print(a << 1) # Left Shift (multiply by 2)
print(a >> 1) # Right Shift (divide by 2)