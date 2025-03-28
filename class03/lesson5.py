# Lesson 05: Control Flow & Loops
# 1. If-Else Statement
age = int(input("Enter Your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible for vote!")



# 2. Elif Statement
marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D or lower")



# 3. Nested If Statements
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Number is either zero or negative")



# Loops and Iteration in Python
# 4. For Loop Example (Iterate Over a List)
fruits = ["strawberry", "Banana", "Orange", "Mango", "Grapes"]
for fruit in fruits:
    print(fruit)



# 5. While Loop Example
tank_level = 0
while tank_level < 100:
    print(f"Filling gas... Current level: {tank_level}%")
    tank_level += 20 # Increase level by 20%
print("Gas tank is full!")



# 6. For Loop with Else
for num in range(5):
    print(num)
else:
    print("Loop completed successfully!")



# 7. Break & Continue in Loops
# Break Example
for num in range(10):
    if num == 5:
        print("Breaking loop at 5")
        break
    print(num)

# Continue Example
for num in range(10):
    if num == 5:
        print("Skipping number 5")
        continue
    print(num)



# 8. Nested Loops Example (Multiplication Table)
for i in range(1, 4): #Outer loop
    for j in range(1, 4): # Inner loop
        print(f"{i} x {j} = {i*j}")
    print()