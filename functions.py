def greet():
    print("Hello, welcome to Python functions!")
    
greet()

def add(a, b):
    print("Sum:", a + b)

add(10, 5)

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Result:", result)

def total_marks(*marks):
    print("All marks:", marks)
    print("Total:", sum(marks))

total_marks(85, 90, 75, 88)

# To use when you know about the no. of parameters
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Akshay", age=21, branch="CSE")

# To use when you don't know about the parameter value
def greet(name="User"):
    print(f"Hello, {name}!")

greet()
greet("Akshay")

def profile(name, age):
    print(f"Name: {name}, Age: {age}")

profile(age=20, name="Aarav")