# Tuples are represented by ()
# Properties of Tuple: Ordered, Unchangeable & allows duplicate values (Immutable)
numbers = (1, 7, 9, 13, 7)
print(numbers)
# Shift + Alt + Bottom arrow
print(type(numbers))
print(len(numbers))

# Without comma, it acts like a string
states = ("Karnataka")
print(states)
print(type(states))

# With comma, it acts like a tuple
indian_states = ("Karnataka",)
print(indian_states)
print(type(indian_states))

state_with_code = ("KA", 1, "TN", 2, "AP", 3)
print(state_with_code)
print(type(state_with_code))

# Accessing value using index number
print(state_with_code[2])

for item in state_with_code:
    print(item)
    
for item in range(len(state_with_code)):
    print(item)
    
other_states = ("MH", 4, "KL", 5)

new_states = state_with_code + other_states
print(new_states)

duplicate = state_with_code * 3
print(duplicate)

print(duplicate.count("TN"))
print(duplicate.index("TN"))

# Sets are represented by {}
# Properties of Sets: Unordered, Unchangeable, Do not allow duplicate values

# True keyword & 1 value are considered as same value in Set
# Similarly False keyword & 0 value are considered as same value in Set
# Duplicate Values will be ignored if it exists
languages = {"Kannada", "Tamil", "Telugu", "Hindi", True, 1, False, 0}
print(languages)
print(type(languages))

print(len(languages))

print("Tamizh" in languages)

for set_item in languages:
    print(set_item)

# add method is used to add new item to the existing set, and it allows only 1 item at a time    
languages.add("Marathi")
print(languages)
languages.add("Malayalam")
print(languages)
languages.add("Tulu")
print(languages)

programming = {"C", "C++", "Python", "Java"}
languages.update(programming)
print(languages)

# Combining the list into the set
subjects = ["Science", "Social", "Maths"]
languages.update(subjects)
print(languages)

# Combining the tuple into the set
foreign = ["French", "German", "Russian"]
languages.update(foreign)
print(languages)
 
# Remove method is used to remove the item from the set only if it exists, or it will throw an error
languages.remove("German")
# languages.remove("Germany") - This will throw an error because doesn't exist
print(languages)

# Discard method is used to remove the item from the set if it exists, or it will ignore if it is not present
languages.discard("Germany")  # It will ignore if error occurs
print(languages)

# pop method will remove some random item from the set as it is not ordered
languages.pop()
print(languages)

# clear method is used to clear all the items from the set
languages.clear()
print(languages)

even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
random = {2, 7, 12, 15, 13}

# union method is used to combine one or more sets together, we can also use this symbol(|) 
both_numbers = even.union(odd, random)
# both_numbers = even | (odd)
print(both_numbers)

# intersection method is used to get the common items from one or more sets together, we can also use this symbol(&) 
num = odd.intersection(random)
# num = odd & random & even
print(num)

# intersection_update method is used to replace the common items from one or more sets together, which will remove all items except common item 
print("Before:", random)
# random.intersection_update(odd)
print("After:", random)

# difference method is used to get the uncommon elements present in the first set out of second set, use symbol(-)
num1 = even.difference(random)
# num1 = even - random
print("First set after removing the common item:", num1)
num1 = random.difference(even)
print(num1)
num1 = odd.difference(random)
print(num1)
num1 = random.difference(odd)
print(num1)

# Check Later**
# num1 = random.difference_update(even)
# print("Difference & Update:", num1)

# Symmetric Difference method is used to combine both the sets by removing the common item from both the sets, use symbol (^)
sym_numbers = even.symmetric_difference(random)
# sym_numbers = even ^ random
print("Combined both the sets by removing the common element:", sym_numbers)
sym_numbers = odd.symmetric_difference(random)
print("Combined both the sets by removing the common element:", sym_numbers)

# issubset method is used to check whether all the elements of set1 is present in set2, if it is present it will show True, use symbol (<=)
even_num = {2, 4, 6}
even1 = {2, 4, 6, 8, 10}
print(even_num.issubset(even1))
# print(even_num <= even1)

# Dictionary is represented by Key-Value pairs
# Properties of dictionary: Ordered, Changeable & No Duplicate Values
person = {
    "name": "Akshay Rao",
    "email": "akshay.parvam@gmail.com",
    "age": 24,
    "roles" : ["Web Development", "Workshop Trainer", "Internship Trainer"],
    "skills" : ("Django", "Laravel", "AIML"),
    # "age": 25  # original value will be replaced by the duplicate value (24 => 25)
}
print(person)
print(type(person))
# Fetching the value using key
print(person["skills"])

print(len(person))

# get method is used to get the value using its key
print(person.get("roles"))

# keys method is used to list all the keys present in the dictionary
print(person.keys())

# values method is used to list all the values present in the dictionary
print(person.values())

print(person.items())

# in keyword can be used to check whether the given key is present or not, it won't check for value
print("age" in person)


print("Before updating age:", person)
# Update using first method
person["age"] = 25
print("After updating age:", person)
# Update the key-value pair using update method
person.update({"experience": "3 Years"})
print("After updating the experience:", person)

# pop method is used to remove the item using key
person.pop("experience")
print(person)

# popitem method is used to remove the last inserted item from the dictionary
person.popitem()
print(person)