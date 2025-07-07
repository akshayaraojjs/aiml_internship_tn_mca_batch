# 1. Right-Angled Triangle
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

# 2. Left-Aligned Triangle 
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

# 3. Pyramid Pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# 4. Inverted Right-Angled Triangle
rows = int(input("Enter number of rows: "))

# Upper Half
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower Half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

# 5. Diamond Pattern
rows = int(input("Enter number of rows: "))

# Upper Half
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower Half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

# 6. Hollow Square Pattern
rows = int(input("Enter size of square: "))

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == 1 or i == rows or j == 1 or j == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()