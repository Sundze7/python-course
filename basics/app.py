# import utils 
# from utils import lbs_to_kg, find_max_num
# import ecommerce.shipping
# from ecommerce.shipping import calc_shipping


# print(utils.kg_to_lbs(70))
# print(lbs_to_kg(100))
# print()

# numbers = [40, 5, 3, 78, 9, 33]
# max_num = find_max_num(numbers)
# print("max_num number is ", max_num)
# print()

# ecommerce.shipping.calc_shipping()
# calc_shipping()

# import random

# for i in range(3):
#     # print(random.random())
#     print(random.randint(10, 20))

# members = ["John", "Jane", "Dave", "Emily"]
# leader = random.choice(members)
# print(f"Leader is: {leader}")

# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
    
# dice = Dice()
# print(dice.roll())


from pathlib import Path

# path = Path("email")
# print(path.exists())
# print(path.mkdir())
# print(path.rmdir())

# searching files using a pattern
path = Path()
# for file in path.glob("./*/*.py"):
for file in path.glob("*"):
    print(file)
print()