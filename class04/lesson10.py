# Lesson 10: File Handling in Python

# Creating and writing to a file using "w" mode
file = open("new_file.txt", "w")
file.write("Hello, world!\n")
file.write("This is another line.\n")
file.close()

# Appending lines using "a" mode
lines = ["Line 1: Karachi\n", "Line 2: Lahore\n", "Line 3: Peshawar\n"]
file = open("new_file.txt", "a")
file.writelines(lines)
file.close()

# Reading file content using "r" mode
file = open("new_file.txt", "r")
content = file.read()
print("Reading whole content:\n", content)
file.close()

# Reading line by line using readline()
file = open("new_file.txt", "r")
line = file.readline()
print("\nRead one line using readline():", line)
file.close()

# Resetting pointer using seek() and checking position with tell()
file = open("new_file.txt", "r")
file.seek(0)
print("Position after seek(0):", file.tell())
line = file.readline()
print("Line after seek(0):", line)
file.close()

# Reading all lines into a list
file = open("new_file.txt", "r")
file.seek(0)
lines = file.readlines()
print("\nReading all lines using readlines():")
for line in lines:
    print(line)
file.close()

# Iterating directly over file object
file = open("new_file.txt", "r")
print("\nReading by iterating file:")
for line in file:
    print(line.strip())
file.close()

# Exclusive creation with "x" mode
try:
    with open("unique.txt", "x") as file:
        file.write("Created exclusively!\n")
except FileExistsError:
    print("\nFile already exists.")

# Reading using with statement (context manager)
with open("new_file.txt", "r") as file:
    content = file.read()
    print("\nReading using with-statement:\n", content)

# Trying to access file pointer after "with" closes the file
try:
    print(file.tell())  # This will throw an error
except ValueError as e:
    print("Error after with block:", e)

# Function to copy a file
def copy_file(source_path, destination_path):
    try:
        with open(source_path, "r") as source_file, open(destination_path, "w") as dest_file:
            for line in source_file:
                dest_file.write(line)
        print(f"\nFile '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_file("unique.txt", "unique_copy.txt")

# Full Example: File Operations Demo
with open("demo.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Line 1\nLine 2\n")

with open("demo.txt", "r") as file:
    print("\nContent of demo.txt:")
    print(file.read())

with open("demo.txt", "a") as file:
    file.write("Appended line\n")

with open("demo.txt", "r+") as file:
    file.seek(0)
    print("\nFirst line of demo.txt:", file.readline())
