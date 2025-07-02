pin = "1234"
attempts = 0

while attempts < 3:
    user_input = input("Enter your PIN: ")
    if user_input == pin:
        print("Access Granted")
        break
    else:
        print("Incorrect PIN")
    attempts += 1


count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1


total = 0
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    if num > 0:
        total += num
    num = int(input("Enter a number (0 to stop): "))
print("Total of positive numbers:", total)


# while True:
#     # do something
#     if not condition:
#         break

while True:
    print("1. Start\n2. Help\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "3":
        print("Exiting...")
        break

while True:
    age = int(input("Enter your age: "))
    if age > 0:
        break
    print("Please enter a valid positive age.")


correct_password = "admin"
while True:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("Login successful!")
        break
    else:
        print("Try again.")


cart = ["Apple", "Milk", "Bread", "Butter"]
for item in cart:
    print(f"Item: {item}")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

marks = [85, 90, 76, 88]
total = 0
for mark in marks:
    total += mark
print("Total Marks:", total)

n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Unknown Variable
for _ in range(5):
    print("Hello")

for _ in range(3):
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

import random
random_nums = [random.randint(1, 100) for _ in range(5)]
print(random_nums)

a, b = 0, 1
for _ in range(6):
    print(a, end=" ")
    a, b = b, a + b