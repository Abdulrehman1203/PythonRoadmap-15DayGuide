arr = [2, 4, 1, 5, 6, 3, 7]

for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[min_index]
    arr[min_index] = arr[i]
    arr[i] = temp

print(arr)
