# Loops
# While Loop
num = 0
# given = input("Enter any number")
print(num)
# Check condition until it is false
while num < 10:
    print("The numbers are as follows:", num)
    num+=1  # Increment
    
# Printing the tables
i = 2
num = 1
while num < 10:
    print(f"{num}  X  {i} = {num * i}")
    # i+=1
    num+=1
    
# atm_pin = "1234"

# pin = input("Enter your ATM pin: ")
#     # print("Wrong Pin")
# while pin == atm_pin:
#     option = input("Select any of the option: Withdraw/Deposit/Check-Balance ")
#     if(option == "Withdraw"):
#         print("Withdrawing Money!")
#     elif(option == "Deposit"):
#         print("Depositing Money!")
#     elif(option == "Check-Balance"):
#         print("Checking Balance!")
#     else:
#         print("Invalid option")
#         break
    
# attempt = 0

# while True:
#     print("1. Start\n2. Help\n3. Exit")
#     if(attempt < 4):
#         choice = input("Choose an option: ")
#         if choice == "1":
#             print("Starting...")
#             # break
#         if choice == "2":
#             print("Helping...")
#             # break
#         if choice == "3":
#             print("Exiting...")
#             break
#     attempt+=1
# print("Number of attempts exceeded")

# attempts = 0
# pin = "1234"

# while attempts < 3:
#     user_input = input("Enter your PIN: ")
#     if user_input == pin:
#         print("Access Granted")
#         break
#     else:
#         print("Incorrect PIN")
#     attempts += 1
# print("Attempt exceeded")

for i in range(6):
    print(i)
    
for i in range(10):
    print(i*i)
    
for i in range(1, 100):
    if(i % 3 == 0):
        print(f"Multiples of 3 in first 100 numbers: {i}")
       
# Sum of Digits 
num = 1234
sum = 0
rem = 0
# for i in range(num):
while num > 0:
    rem = num % 10 
    sum += rem
    num = num//10
print(int(sum))

# Step 1:
# rem = 0, sum = 0, num = 1234
# 1234 > 0 - T
# rem = 1234 % 10 = 4
# sum = sum + rem = 0 + 4 = 4
# num = 1234//10 = 123

# Step 2:
# rem = 4, sum = 4, num = 123
# 123 > 0 - T
# rem = 123 % 10 = 3
# sum = sum + rem = 4 + 3 = 7
# num = 123//10 = 12

# Step 3:
# rem = 3, sum = 7, num = 12
# 12 > 0 - T
# rem = 12 % 10 = 2
# sum = sum + rem = 7 + 2 = 9
# num = 12//10 = 1

# Step 4:
# rem = 2, sum = 9, num = 1
# 1 > 0 - T
# rem = 1 % 10 = 1
# sum = sum + rem = 9 + 1 = 10
# num = 1//10 = 0

# Step 5:
# rem = 1, sum = 10, num = 0
# 0 > 0 - F
# Stop

number = []
for _ in range(5):
    value = int(input("Enter any 5 number"))
    number.append(value)
print(number)

# Step 1:
# number list is empty
# 0 < 5 - T
# 5
# number => [5]

# Step 2:
# number list = [5]
# 1 < 5 - T
# 6
# number => [5, 6]

# Step 3:
# number list  =  [5, 6]
# 2 < 5 - T
# 8
# number => [5, 6, 8]

# Step 4:
# number list = [5, 6, 8]
# 3 < 5 - T
# 12
# number => [5, 6, 8, 12]

# Step 5:
# number list  = [5, 6, 8, 12]
# 4 < 5 - T
# 18
# number => [5, 6, 8, 12, 18]

# Step 6:
# number list = [5, 6, 8, 12, 18]
# 5 < 5 - F
# Stop

temp = 0
sum = 0
for i in range(len(number)):
    temp = number[i]
    print(temp)
    sum = sum + temp
print(sum)

# [5, 6, 8, 12, 18]
# Step 1: 
# temp = 0, sum = 0, len(number) = 5
# 0 < 5 - T
# temp = n[0] = 5
# sum = sum + temp = 0 + 5 = 5

# Step 2: 
# temp = 5, sum = 5, len(number) = 5
# 1 < 5 - T
# temp = n[1] = 6
# sum = sum + temp = 5 + 6 = 11

# Step 3: 
# temp = 6, sum = 11, len(number) = 5
# 2 < 5 - T
# temp = n[2] = 8
# sum = sum + temp = 11 + 8 = 19

# Step 4: 
# temp = 8, sum = 19, len(number) = 5
# 3 < 5 - T
# temp = n[3] = 12
# sum = sum + temp = 19 + 12 = 31

# Step 5: 
# temp = 12, sum = 31, len(number) = 5
# 4 < 5 - T
# temp = n[4] = 18
# sum = sum + temp = 31 + 18 = 49

# Step 6: 
# temp = 18, sum = 49, len(number) = 5
# 5 < 5 - F
# Stop