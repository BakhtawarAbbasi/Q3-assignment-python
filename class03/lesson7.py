# 1. Creating a Set and Demonstrating Key Properties
# Creating a set
my_set = {1, 2, 3, 4, 5, 3, 2}  
print("Set without duplicates:", my_set)  # Output: {1, 2, 3, 4, 5}  

# Adding an element  
my_set.add(6)  
print("Set after adding 6:", my_set)  

# Removing an element using remove()  
my_set.remove(4)  
print("Set after removing 4:", my_set)  

# Removing an element using discard() (no error if element not found)  
my_set.discard(10)  # Does nothing if 10 doesn't exist  
print("Set after discard:", my_set)  

# Checking membership  
print("Is 3 in the set?", 3 in my_set)  




# 2. Demonstrating Set Operations
# Two example sets  
set_a = {1, 2, 3}  
set_b = {3, 4, 5}  

# Union  
union_set = set_a.union(set_b)  
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}  

# Intersection  
intersection_set = set_a.intersection(set_b)  
print("Intersection:", intersection_set)  # Output: {3}  

# Difference  
difference_set = set_a.difference(set_b)  
print("Difference:", difference_set)  # Output: {1, 2}  

# Symmetric Difference  
symmetric_diff = set_a.symmetric_difference(set_b)  
print("Symmetric Difference:", symmetric_diff)  # Output: {1, 2, 4, 5}  




# 3. Demonstrating Immutable Sets with Frozenset
# Creating a frozenset  
frozen_set = frozenset([1, 2, 3, 3, 2])  
print("Frozenset:", frozen_set)  # Output: frozenset({1, 2, 3})  

# Attempting to add or remove elements will cause an error (uncomment to test)  
# frozen_set.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'  

# Using a frozenset as a dictionary key (hashable property)  
my_dict = {frozen_set: "Immutable Key"}  
print("Dictionary with frozenset key:", my_dict)  




# 4. Garbage Collection & Reference Counting Example
import gc  

# Function to check garbage collection  
def check_gc():  
    x = set()  # Create a set object  
    y = x       # Create a reference to the same set  
    del x       # Delete one reference  
    print("Is the object still alive?", bool(y))  # True, because y still references the set  

check_gc()  
print("Manually running garbage collector...")  
gc.collect()  # Runs garbage collection manually  
