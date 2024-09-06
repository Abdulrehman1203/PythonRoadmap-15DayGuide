list1 = [1, 2, 6, 9, 3, 5, 7]
list2 = [2, 8, 4, 2, 9, 10]

for i in list2:
    list1.append(i)

print(" Merged lists :", end=" ")
print(list1)

for i in list1:
    count = list1.count(i)
    if count > 1:
        for j in range(count-1):
            list1.remove(i)

print(" Lists after removing duplicates :", end=" ")
print(list1)

for i in range(len(list1)):

    swapped = False

    for j in range(0, len(list1) - i - 1):

        if list1[j] > list1[j + 1]:
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp

            swapped = True

    if not swapped:
        break
print(" Sorted lists :", end=" ")
print(list1)

