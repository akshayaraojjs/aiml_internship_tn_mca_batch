# Program - 1: Method 1
# Take input
user_input = input("Enter numbers separated by commas: ")
numbers = tuple(map(int, user_input.split(',')))

# Define functions
def calculate_sum(nums):
    return sum(nums)

def calculate_product(nums):
    product = 1
    for num in nums:
        product *= num
    return product

# Output results
print("Tuple:", numbers)
print("Sum:", calculate_sum(numbers))
print("Product:", calculate_product(numbers))

# Program - 1: Method 2
# Take input
user_input = input("Enter numbers separated by commas: ")
numbers = tuple(map(int, user_input.split(',')))

# Define functions using *args
def calculate_sum(*args):
    return sum(args)

def calculate_product(*args):
    product = 1
    for num in args:
        product *= num
    return product

# Output results
print("Tuple:", numbers)
print("Sum using args:", calculate_sum(*numbers))
print("Product using args:", calculate_product(*numbers))

# Program - 2: Type 1
# Step 1: Take input from user
user_input = input("Enter key-value pairs (e.g., name:John, age:30): ")

# Step 2: Convert input string to dictionary
pairs = user_input.split(',')
user_dict = {}

for pair in pairs:
    if ':' in pair:
        key, value = pair.split(':', 1)
        user_dict[key.strip()] = value.strip()

# Step 3: Define function to print dictionary items
def print_dict_items(d):
    print("\nDictionary contents:")
    for key, value in d.items():
        print(f"{key} : {value}")

# Step 4: Call the function
print_dict_items(user_dict)

# Program - 2: Type 2
# Step 1: Take input from user
user_input = input("Enter key-value pairs (e.g., name:John, age:30): ")

# Step 2: Convert input string to dictionary
pairs = user_input.split(',')
user_dict = {}

for pair in pairs:
    if ':' in pair:
        key, value = pair.split(':', 1)
        user_dict[key.strip()] = value.strip()

# Step 3: Function using **kwargs
def print_dict_items(**kwargs):
    print("\nDictionary contents using kwargs:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Step 4: Call the function with dictionary unpacked as kwargs
print_dict_items(**user_dict)

# Program - 3:
# Step 1: Take input
user_input = input("Enter numbers separated by commas: ")
numbers = tuple(map(int, user_input.split(',')))

# Step 2: Define functions using *args
def calculate_sum(*args):
    return sum(args)

def calculate_product(*args):
    product = 1
    for num in args:
        product *= num
    return product

def find_min(*args):
    return min(args)

def find_max(*args):
    return max(args)

def calculate_avg(*args):
    return sum(args) / len(args) if args else 0

def absolute_values(*args):
    return tuple(abs(num) for num in args)

# Step 3: Output results
print("\nOriginal Tuple:", numbers)
print("Sum:", calculate_sum(*numbers))
print("Product:", calculate_product(*numbers))
print("Minimum:", find_min(*numbers))
print("Maximum:", find_max(*numbers))
print("Average:", calculate_avg(*numbers))
print("Absolute Values:", absolute_values(*numbers))