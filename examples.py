# Example 1: Check if a person is eligible to vote
age = 20
if age >= 18:
    print("Eligible to vote")

# Example 2: Check if a temperature is above boiling point
temperature = 105
if temperature > 100:
    print("Water is boiling")

# Example 3: Check if there is a discount on a product
discount = True
if discount:
    print("Discount is available!")
    
# Example 1: Determine grade based on marks
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# Example 2: Traffic light action
signal = "Yellow"
if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Get Ready")
elif signal == "Green":
    print("Go")

# Example 3: Weather condition
weather = "Cloudy"
if weather == "Sunny":
    print("Wear sunglasses")
elif weather == "Rainy":
    print("Carry an umbrella")
elif weather == "Cloudy":
    print("Might rain later")

# Example 1: Check if a person is adult
age = 22
if age >= 18: print("Adult")

# Example 2: Check if password is correct
password = "admin123"
if password == "admin123": print("Access granted")

# Example 3: Check if it's weekend
day = "Sunday"
if day == "Sunday": print("Enjoy your weekend!")

# Example 1: Voting eligibility
age = 16
print("Eligible" if age >= 18 else "Not eligible")

# Example 2: Determine even or odd
num = 7
print("Even" if num % 2 == 0 else "Odd")

# Example 3: Discount based on membership
is_member = False
print("Discount applied" if is_member else "No discount")

# Example 1: Student performance check
marks = 85
if marks >= 60:
    if marks >= 80:
        print("Excellent performance")
    else:
        print("Good performance")
else:
    print("Needs improvement")

# Example 2: ATM withdrawal process
card_inserted = True
pin_correct = True
if card_inserted:
    if pin_correct:
        print("Transaction successful")
    else:
        print("Incorrect PIN")
else:
    print("Please insert your card")

# Example 3: Booking movie tickets
logged_in = True
seats_available = True
if logged_in:
    if seats_available:
        print("Booking confirmed")
    else:
        print("Seats not available")
else:
    print("Please login to book tickets")

temperature = 25

if temperature > 30:
    print("It's hot outside")
elif temperature < 10:
    print("It's cold outside")
else:
    pass  # We may add logic for moderate temperature later

# Match Keyword
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Weekend")

status_code = 404

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")

value = 10.5

match value:
    case int():
        print("It's an integer")
    case float():
        print("It's a float")
    case str():
        print("It's a string")
    case _:
        print("Unknown type")

numbers = [1, 2, 3]

match numbers:
    case []:
        print("Empty list")
    case [x]:
        print(f"Single item: {x}")
    case [x, y]:
        print(f"Two items: {x}, {y}")
    case [x, y, z]:
        print(f"Three items: {x}, {y}, {z}")
    case _:
        print("More than three items")