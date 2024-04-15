# FUNCTIONs
# def greet_user(name):
#   print(f"Hello {name}")
#   print("Welcome onboard")
  
# print("start")
# greet_user("John")
# print("end")

# return statement
# by default all functions in python return None
# def sqaure(number):
#   # return number * number
#   print(number * number)

# print(sqaure(56))


# Exceptions
# exit code 0 => program terminated successfully with no errors
# exit code anything but 0 => program terminated with errors or crashed

# try:
#   age = int(input("Age: "))
#   print(age)
  
# except ValueError:
#   print("Invalid input")

try:
  age = int(input("Age: "))
  income = 20000
  risk = income / age
  print ("Risk", risk)
except ValueError:
  print("Invalid input")
except ZeroDivisionError:
  print("Age cannot be 0")