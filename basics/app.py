# #user imput
# name = input("What is your name? ")
# print(f"Hi {name}!")
# # print("hi " + name + "!")

# birth_yr = input("Birth year: ")
# age = 2024 - int(birth_yr)
# print(f"{name}, you are {age} years old.")

# # Strings
# course = 'Python for Beginners'
# print(course[0]) #prints first character of a string
# print(course[-1]) #prints last character (1st from the end) of a string
# print(course[0:3]) # from index 0, print 3 characters  
# print(course[0:]) # from index 0, print all characters
# print(course[:]) # clones string

# # Some Math operations
# x = (10 + 3) * 2 ** 2
# print(x)
# """
# ORDER
# paranthesis -> exponentiation -> multiplication/division -> addition/subtraction
# """

# Conditioners
# is_hot = False
# is_cold = True

# if is_hot:
#   print("It's a hot day")
#   print("Drink plenty of water")
# elif is_cold:
#   print("It's a cold day")
#   print("wear warm clothes")
# else:
#   print("It's a lovely day")
# print("Enjoy your day")

# has_high_income = True
# has_good_credit = True
# has_criminal_record = False

# # if has_high_income or has_good_credit:
# # if has_high_income and has_good_credit:
# if has_high_income and not has_criminal_record:
#   print("Eligible for loan")
  
# # COMPARISONS
# temperatue = 30

# if temperatue > 30:
#   print("It's a hot day")
# else:
#   print("It's not a hot day")

# # Weight Converter
# weight = int(input("Weight: "))
# unit = input("(K)g or (L)bs: ")

# if unit.upper() == "L":
#   converted = weight * 0.45
#   print(f"You are {converted} kilos")
# elif unit.upper() == "K":
#   converted = weight / 0.45
#   print(f"You are {converted} pounds")

# # while loop
# i = 1
# while i <= 5:
#   print("*" * i)
#   i += 1
# print("Done")

# for loop
# prices = [10, 20, 30]

# total = 0
# for price in prices:
#   total += price
# print(f"Total: {total}")

# Nested Loops
# for x in range(4): # range will generate 0, 1, 2, 3 (not including 4)
#   for y in range(3):
#     print(f"({x}, {y})")

# numbers = [5, 2, 5, 2, 2] # prints an F shape
#numbers = [2, 2, 2, 2, 5] # prints an L shape

# for x_count in numbers:
#   print('x' * x_count)

# for x in numbers:
#   output = ''
#   for y in range(x):
#     output += 'x'
#   print(output)

# LIST
# names = ["John", "Bob", "Mary", "Serena", "Musa"] # access list items by index

# # program to return largest number from a list of numbers
# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0] # assume first number is the biggest

# for num in numbers:
#   if num > max:
#     max = num
# print(max)

# 2D LIST
# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# # matrix[0][1] = 20 # change the value of the second item in the first row to 20
# # print("Matrix:\n", matrix)

# for row in matrix:
#   for item in row:    
#     print(item)

# list methods
# numbers = [5,2,1,7,3,4,7,3,9,1,4]
# pop() removes the last item in the list
# clear() removes all items in the list
# sort() sorts the list
# numbers.append(10) adds an item to the end of the list
# numbers.insert(0, -1) inserts an item at a specific index
# numbers.remove(5) removes a specific item from the list
# numbers.reverse() reverses the list order
# numbers.index(2) returns the index of the first occurrence of a specific item
#numbers.copy returns a copy of the list

# unique = []
# for number in numbers:
#   if number not in unique:
#     unique.append(number)
# print(unique)


# TUPLES
# once created, cannot be modified, neither can it have duplicates
# access items as in lists

# Unpacking 
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)


# DICTIONARIES
# shld have uniques key-value pairs
# customer = {
#   "name": "John Doe",
#   "age": 30,
#   "is_verified": True
# }
# print(customer["name"])
# print(customer.get("birth_year", 1990)) # returns 1990 if key not found?

# phone = input("Phone: ")
# digits_mapping = {
#   "1": "One",
#   "2": "Two",
#   "3": "Three",
#   "4": "Four"
# }
# output = ""
# for ch in phone:
#   output += digits_mapping.get(ch, "!") + " " # if key not found, return "!"
# print(output)

# FUNCTIONs
def greet_user(name):
  print(f"Hello {name}")
  print("Welcome onboard")
  
print("start")
greet_user("John")
print("end")