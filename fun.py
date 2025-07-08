# Function Defn
# Normal Function
def sayHello():
    print("Hello students")
    
# Function Call
sayHello()
sayHello()
sayHello()
sayHello()

# name is parameter
# Parameterized Function
def greet(name):
    print("Hi ",name)
    
greet("Akshay")
greet("Ajay")

# Multiple Parameters
def sayHi(first, last):
    print(f"Hi {first} {last}")
    
sayHi("Akshay", "Rao")

def person(name, age):
    print(f"You're {name}, And you're {age} years old!")
    
person("Akshay Rao", 24)

def person_info(name, age, gender):
    return name, age, gender

person_1 = person_info("Akshay Rao", 24, "Male")
person_2 = person_info("Ajay Rao", 22, "Male")
person_3 = person_info("Jay", 42, "Male")

print(person_1, person_2, person_3)

def add(n1, n2):
    return n1 + n2

sum_0 = add(10,20)
sum_1 = add(30,60)
sum_2 = add(50,90)
# sum_3 = add(20, 30, 40)

print(sum_0, sum_1, sum_2)

# args
# def add(*num):
#     sum(num)

# add(20, 30, 80)

# def total_marks(*marks):
#     print("All marks:", marks)
#     print("Total:", sum(marks))

# total_marks(85, 90, 75, 88)

def person_data(*data):
    print(data)
    
person_data("Akshay", 23)

def calculateSum(*numbers):
    return sum(numbers)

sumOfNum = calculateSum(20, 30, 50)
print(sumOfNum)

user_input = input("Enter numbers separated by commas: ")
numbers = tuple(map(int, user_input.split(',')))
print(numbers)
print(type(numbers))

# Define functions using *args
def calculate_sum(*args):
    return sum(args)

print("Sum of the given numbers: ", calculate_sum(*numbers))

def personal_data(**data):
    # for i in data.items():
    #     print(i)
    print(data)
        
personal_data(name="Akshay", age = 24)


user_input = input("Enter key-value pairs (e.g., name:John, age:30): ")

# Step 2: Convert input string to dictionary
pairs = user_input.split(',')
user_dict = {}

for pair in pairs:
    if ':' in pair:
        key, value = pair.split(':', 1)
        user_dict[key.strip()] = value.strip()

# Step 3: Function using **kwargs
def print_user_details(**kwargs):
    print("\nUser Details are as follows:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Step 4: Call the function with dictionary unpacked as kwargs
print_user_details(**user_dict)

# someNumbers = input("Enter any 3 numbers, use - to separate it:")

# print(someNumbers)
# givenNumbers = someNumbers.split('-')
# print(givenNumbers)

def greetPerson(name = "Unknown"):
    print(name)
    
greetPerson()
greetPerson("Akshay")