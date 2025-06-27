car = {
    "name": "Tata Curvv",
    "brand": "Tata",
    "fuel_type": "EV",
    "launch_year": 2024,
    "price": 520099.50
}

print(car)

# setdefault method is used to add new item to the dictionary
# Syntax: dictionary.setdefault("key", "value")
car.setdefault("country_of_origin", "India")

car.update({"launch_year": 2025})
print(car)

# For printing all the keys:
for item in car:
    print(item)

# For printing all the values:
for item in car:
    print(car[item])

print(car.keys())

another_car = car.copy()
print(another_car)

# clear method is used to remove all the key value pairs from the dictionary
car.clear()
print(car)

cars = {
    "car1":{
        "name": "Tata Punch",
        "brand": "Tata",
        "year": 2024
    },
    "car2": {
        "name": "Toyota Innova",
        "brand": "Toyota"
    },
    "car3":{
        "name": "Kia Sonet",
        "brand": "Kia",
        "price": "6L"
    }
}

print("Name of Car2:",cars["car2"]["name"])
print("Price of Car3:",cars["car3"]["price"])

car1 = {
        "name": "Tata Punch",
        "brand": "Tata",
        "year": 2024
    }
car2 = {
        "name": "Toyota Innova",
        "brand": "Toyota"
    },
car3 = {
        "name": "Kia Sonet",
        "brand": "Kia",
        "price": "6L"
    }

multiple_cars = {
    "first_car" : car1,
    "second_car" : car2,
    "third_car" : car3,
}

print(multiple_cars)


print(cars)

# Operators:
# Arithmetic, Logical, Relational, Assignment
num1 = 20
num2 = 50
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num2 / num1) # Normal Division (With Decimal Point)
print("Remainder:", num1 % num2)
print("Exponent:", num1 ** 3)
print("Floor Division:", num2 // num1) # Floor Division (Without Decimal Point)

# Assignment Operator
num3 = 30
print("Value of num3:", num3)
num3 += 10 
print("Value of num3 after addition:", num3)
num3 -= 10
print("Value of num3 after subtraction:", num3)
num3 *= 10
print("Value of num3 after multiplication:", num3)
num3 /= 10
print("Value of num3 after division for quotient:", num3)
num3 %= 10
print("Value of num3 after division for remainder:", num3)
num4 = 45
num4 //= 10
print("Value of num4 after floor division:", num4)

if(not(num1 < 50 or num2 > 60)):
    print("num1 and num2 lies between 30 & 50")
else:
    print("It won't lie between the given range")
   
# AND 
# op1 synmbol op2
#  0     and     0  = 0
#  0     and     1  = 0
#  1     and     0  = 0
#  1     and     1  = 1

# OR
# op1 synmbol op2
#  0     or     0  = 0
#  0     or     1  = 1
#  1     or     0  = 1
#  1     or     1  = 1

# Not
#   op1   result
# not(0) = 1
# not(1) = 0

# Conditional Statements
num = 21
if(num % 2 == 0):
    print("The given number",num, "is an even number")
else:
    print("The given number",num, "is an odd number")

val1 = 30
val2 = 80
val3 = 50

if(val1 > val2):
    print("Value1 is greater than Value2")
else:
    print("Value2 is greater than Value1")
    
# IF Else ladder
if(val1 > val2 and val1 > val3):
    print("Value 1 is greater")
elif(val2 > val3):
    print("Value2 is greater")
else:
    print("Value3 is greater")
    
# Nested If-Else
# Greatest of 3 numbers
if(val1 > val2):
    if(val1 > val3):
        print("Value1 is greatest")
    else:
        print("Value3 is greatest")
else:
    if(val2 > val3):
        print("Value2 is greatest")
    else:
        print("Value3 is greatest")