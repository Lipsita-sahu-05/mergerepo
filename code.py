# Simple Student Details Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)
print("Course:", course)

if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")