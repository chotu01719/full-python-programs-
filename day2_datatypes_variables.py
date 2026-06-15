# ============================================
# Day 2 - Python Datatypes and Variables
# ============================================

# --- 1. Integer ---
age = 21
print("Age:", age)
print("Type:", type(age))

# --- 2. Float ---
height = 5.9
print("\nHeight:", height)
print("Type:", type(height))

# --- 3. String ---
name = "Ravi"
print("\nName:", name)
print("Type:", type(name))

# --- 4. Boolean ---
is_student = True
print("\nIs Student:", is_student)
print("Type:", type(is_student))

# --- 5. List ---
fruits = ["apple", "banana", "mango"]
print("\nFruits:", fruits)
print("Type:", type(fruits))

# --- 6. Tuple ---
colors = ("red", "green", "blue")
print("\nColors:", colors)
print("Type:", type(colors))

# --- 7. Dictionary ---
person = {"name": "Ravi", "age": 21, "city": "Chennai"}
print("\nPerson:", person)
print("Type:", type(person))

# --- 8. Set ---
numbers = {1, 2, 3, 4, 5}
print("\nNumbers:", numbers)
print("Type:", type(numbers))

# --- 9. NoneType ---
result = None
print("\nResult:", result)
print("Type:", type(result))

# --- 10. Multiple Assignment ---
x, y, z = 10, 20, 30
print("\nx =", x, "| y =", y, "| z =", z)

# --- 11. Type Conversion ---
num_str = "100"
num_int = int(num_str)
print("\nConverted String to Int:", num_int)
print("Type:", type(num_int))
