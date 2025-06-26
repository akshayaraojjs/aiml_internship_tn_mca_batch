# Ctrl + ? for commenting
# String
greet = "Hello World"
print(greet)
print(type(greet))

# integer
num = 10;  
print("The value of number is: ",num)
print(type(num))

# float
num1 = 10.5;  
print("The value of number is: ",num1)
print(type(num1))

# bool
var = False
print(var)
print(type(var))

# Complex
comp = 2j
print(comp)
print(type(comp))

# List is represented by []
# Properties of List: Ordered, Changeable & can allow duplicate values (Mutable)
fruits = ["Apple", "Orange", "Grapes", "Mango", "Banana", "Apple", "Pappaya"]
print(fruits)
print(type(fruits))
print(fruits[4])

# Finding the number of items in the list: len()
print(len(fruits))
list_num = [2, 6, 10, 14]

if "Grapes" in fruits:
    print("I like grapes")
else:
    print("I don't like grapes")
    
# Variable naming conventions:
# Start with alphabet
# If you have multiple words, then we can link it using hyphen(-) or underscore(_)
# Ex: Variable name is first name: first-name or first_name
# Camel Case: firstName
# Pascal Case: FirstName
# Snake Case: first_name
print(list_num)

# append method can be used to insert the new element at the end of the list
list_num.append(5)
print(list_num)
list_num.append(15)
print(list_num)
list_num.append(10)
print(list_num)

# insert method can be used to insert the new element at the specified index
# We need to pass 2 arguments: index number & value
# Ex: insert(2, 6), Here 2 refers to the index(3rd position) & new value to be inserted is 6 
list_num.insert(2, 8)
print(list_num)
list_num.insert(1, 4)
print(list_num)
odd_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Finding the value using Negative index
# -1 refers to the last item, lly -2 last but 1
print(odd_list[-3])

# Using Range to get the specific amount of items from the list
# Starting:Ending range
print(odd_list[2:8])

# No starting point, only ending point: 
# :end
print(odd_list[:6])

# No ending point, only starting point: 
# start:
print(odd_list[6:])

# Negative index
print(odd_list[-4:])

if 12 in odd_list:
    print("11 is present in the given list")
else:
    print("11 is not present")
    
# extend method can be used to link an existing list to the current list
list_num.extend(odd_list)
print("New List:", list_num)

# remove method can be used to remove an item from the list using its value 
list_num.remove(10)
print(list_num)
list_num.remove(10)
print(list_num)

# pop method can be used to remove an item from the list based on its index position
# pop() method without parameter is going to remove the last item from the list 4
# pop(5) - This will remove the value from the value in the 5th index(6th Position)

list_num.pop()
print(list_num)
list_num.pop(6)
print(list_num)
list_num.pop(4)
print(list_num)

# clear method is used to clear all the items from the list
list_num.clear()
print(list_num)

# del keyword is used to remove the entire list
print(list_num)
del list_num

list_of_3 = [30, 27, 3, 18, 6, 9, 12, 15]
print(list_of_3)

# Ascending Order - Sorting
list_of_3.sort()
print(list_of_3)

# Descending Order - Sorting
list_of_3.sort(reverse=True)
print(list_of_3)

# Sorting in Case Sensitive
fruits = ["Apple", "Orange", "Grapes", "Mango", "Banana", "Apple", "Pappaya"]
fruits.sort()
print(fruits)

# Sorting in Case InSensitive
fruits1 = ["Apple", "Orange", "Grapes", "Mango", "Banana", "apple", "Pappaya"]
fruits1.sort()
print(fruits1)

list_of_3 = [30, 27, 3, 18, 6, 9, 12, 15]
list_of_3.reverse()
print(list_of_3)

# function :
    # Function declaration  - sum()
    # Function definition - 
    # sum(a, b){
    #   c =  a + b
    #   print(c)
    # }
    # Function Call - sum(5, 10)
# parameter - a, b
# arguments - 5, 10

# copy method is used to copy all the items from existing list to the new list 
even_list = [2,4,6,8,10]
multiples_of_2 = even_list.copy()
print(multiples_of_2)
print(even_list.index(6))

# index method is used to find the position of the item from the list
actors = ["Vijay", "Rajni", "Kamal", "Ajith", "Dhanush"]
print(actors.index("Ajith"))