import random

counter = 0
sum_even = 0
random_numbers = []
max1 = 0
max2 = 0

for i in range(100):
    current_number = random.randint(1, 300)
    random_numbers.append(current_number)

    if current_number % 2 == 0:
        sum_even += current_number
        counter += 1

    if current_number > max1:
        max2 = max1
        max1 = current_number
    elif current_number > max2:
        max2 = current_number


average = sum_even / counter

print("Random numbers list: ", random_numbers)
print("Average of all even numbers:", average)
print("Total even numbers in the list:", counter)
print("Second Largest:", max2)
