"""Lists: Like a grocery list or task list—ordered and modifiable.
Tuples: Like coordinates or birth dates—fixed and unchangeable.
Dictionaries: Like a phonebook or inventory system—key-value pairs for fast lookups.
Sets: Like event attendees or unique tags—ensure uniqueness and handle duplicates."""


from random import shuffle
food = ["pizza", "burger", "fries", "wraps"]
drinks = ["coffee", "tea", "slush"]
desserts = ["brownie", "cake", "custard"]
#food.sort()
#food.insert(0, "fried chicken")
#food.append("nuggets")
#food.pop()
#food.remove("wraps")
#food.clear()
#for i in food:
#   print(i)





# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map,
# split and strip functions
lst = list(map(int, input("Enter the integer\
elements:")))

# printing the list
print('The list is:', lst)
