import math
import random

# print(10 + 15)
# print(2 ** 100)
# print(2.5 * 5)


value_of_pi = math.pi
# print(value_of_pi)

random_value = random.random()
# print(random_value)

random_num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(random_num)

username = "Vishvas"
# print(len(username))
# print(username[0])
# print(username[-7])

# username[0] = "B"
# print(username) Error because string is immutable

# print(username[0:4])
# print(dir(username))

mylist = [1,2,3, "Vishvas", False]
# print(mylist)
# print(len(mylist))

user = {"name": "Vishvas", "age": 20, "city": "Gir Somnath"}
# print(user)
# print(user['name'])
# print(user['city'])
# user['age'] = "22"
# print(user['age'])


my_tuple = (1,2,3,4,5)
# print(my_tuple)
# print(my_tuple[0])
# my_tuple[0] = 10
# print(my_tuple)
print(len(my_tuple))