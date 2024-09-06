from functools import reduce
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

"""
Map: Transforms each element in a collection.
Filter: Selects elements that meet a condition.
Reduce: Aggregates all elements into a single result.
"""
maping = list(map(round, my_floats,  range(0,7)))
# Use filter to print only the names that are less than
# or equal to seven letters

map_result = list(map(lambda x: x**2, maping))
print(map_result)
a = 7

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use filter to print only the names that are less than
# or equal to seven letters
filter_result = list(filter(lambda name: len(name) == 7, my_names))
print(filter_result)

my_numbers = [4, 6, 9, 23, 5]

reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers )
print(reduce_result)