import utils 
from utils import lbs_to_kg, find_max_num


print(utils.kg_to_lbs(70))

print(lbs_to_kg(100))

numbers = [40, 5, 3, 78, 9, 33]
max_num = find_max_num(numbers)
print("max_num number is ", max_num)
