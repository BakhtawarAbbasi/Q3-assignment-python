# Lesson 06: Lists, Tuples & Dictionary

# 1. Lists in Python
# Creating a List
fruits = ["Apple", "Banana", "Grapes", "Mango"]
print(fruits)


# Accessing List Elements (Indexing & Negative Indexing)
print(fruits[0])  # Apple
print(fruits[-1])  # Orange


# Modifying a List
fruits[1] = "Strawberry"
print(fruits)  # ["Apple", "Strawberry", "Mango", "Orange"]


# List Slicing
print(fruits[1:3])  # ["Strawberry", "Mango"]




# 2. Common List Methods
# Appending and Extending Lists
fruits.append("Grapes")  # Add single element
print(fruits)

more_fruits = ["Pineapple", "Peach"]
fruits.extend(more_fruits)  # Add multiple elements
print(fruits)


# Removing Elements (remove() vs pop())
fruits.remove("Mango")  # Removes by value
print(fruits)

removed_fruit = fruits.pop(2)  # Removes by index
print(f"Removed: {removed_fruit}")
print(fruits)


# Sorting a List
numbers = [5, 2, 8, 1, 3]

numbers.sort()  # Ascending order
print(numbers)

numbers.sort(reverse=True)  # Descending order
print(numbers)

words = ["apple", "banana", "cherry"]
words.sort(key=len)  # Sort by string length
print(words)




# 3. Iterating Over Lists
# Using a For Loop
for fruit in fruits:
    print(fruit)


# Using List Comprehension
squared_numbers = [x**2 for x in range(5)]
print(squared_numbers)  # [0, 1, 4, 9, 16]




# 4. Tuples in Python
# Creating a Tuple
my_tuple = (1, 2, 3, "Apple", "Banana")
print(my_tuple)


# Accessing Elements in Tuples
print(my_tuple[0])  # 1
print(my_tuple[-1])  # "Banana"


# Tuple Unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)


# Immutable Property of Tuples (Will Give Error!)
# my_tuple[0] = 10  #  TypeError: 'tuple' object does not support item assignment




# 5. Dictionaries in Python
# Creating a Dictionary
student = {
    "name": "Bakhtawar",
    "age": 18,
    "grade": "A"
}
print(student)


# Accessing Values
print(student["name"])  # Bakhtawar
print(student.get("age"))  # 18


# Modifying a Dictionary
student["age"] = 18
print(student)


# Adding a New Key-Value Pair
student["city"] = "Karachi"
print(student)


# Deleting an Item (del vs pop())
del student["grade"]
print(student)

removed_value = student.pop("city")
print(f"Removed: {removed_value}")
print(student)


# Dictionary Methods
print(student.keys())  # Returns all keys
print(student.values())  # Returns all values
print(student.items())  # Returns key-value pairs


# Iterating Over a Dictionary
for key, value in student.items():
    print(f"{key}: {value}")
