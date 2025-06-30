gender = ""

if(gender == "Male"):
    print("Mister")
else:
    print("Mistress")
    
# Can check for multiple conditions - Elif
if(gender == "Male"):
    print("He")
elif(gender == "Female"):
    print("She")
else:
    print("It")
    
number = 9

# Nested If Else
if(number % 2 == 0):
    if(number % 3 == 0):
        print("Number: ", number, " is divisible by both 2 & 3")
    else:
        print("Number: ", number, " is divisible only by 3")
else:
    print("Number: ", number, " is not divisible by both 2 & 3")
    
age = 20

# Shorthand if condition
# Syntax: if (condition): {{true statement}}
if(age > 18): print("You can drive the vehicle legally!")

if(age >= 20): print("You are a student")

# Shorthand for if-else
# Syntax: {{true statement}} if (condition) else {{false statement}}
print("You can drive!") if age > 18 else print("You can't drive")

print("You are employed!") if age > 20 else print("You are student")

language = "Tamil"

print("Are you from TN?") if language == "Tamil" else print("Are you from KA?")

a = 50
b = 70
c = 90

# Syntax: {{Condition 1 Statement}} if (condition 1) else {{Condition 2 Statement}} if (condition 2) else {{False Statement}}
print("A is greatest") if a > b and a > c else print("B is greatest") if b > c else print("C is greatest")

if a > b and a > c:
    print("A is greatest")
elif b > c:
    print("B is greatest")
else:
    print("C is greatest")

num = 16
print("Number is divisible by 2 and 3") if num % 2 == 0 and num % 3 == 0 else print("Number is divisible by 3") if num % 3 == 0 else print("Number is neither divisible by 3 nor 2")

swim = False
# pass keyword is used to avoid the error occurred by leaving out the statement
if(swim):
    print("I can swim")
else:
    pass
    # print("I'll learn swimming")
    
# match
month = 8

match(month):
    case 1:
        print("Jan")
    case 2:
        print("Feb")
    case 3:
        print("Mar")
    case 4:
        print("Apr")
    case 5:
        print("May")
    case 6:
        print("Jun")
    case _:
        print("Not a month")
        
character = 'A'

match(character):
    case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
        print("Character is an Vowel")
    case _:
        print("Character maybe the consonant or unknown character")