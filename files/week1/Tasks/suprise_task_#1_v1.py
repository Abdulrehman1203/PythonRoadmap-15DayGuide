import random
counter = 0
sum = 0
random_numbers = []
for i in range(0, 100):
    n = random.randint(1, 300)
    random_numbers.append(n)



for i in random_numbers:
    if i % 2 == 0:
        sum += i
        counter += 1
    else:
        pass


average = sum / counter

print("Average of even numbers : ", average)
print("Total even numbers : ", counter)


sorted_random_numbers = sorted(random_numbers)
second_largest = sorted_random_numbers[len(sorted_random_numbers) - 2]
print("Second Largest : ",second_largest)