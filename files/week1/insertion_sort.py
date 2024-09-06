def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


arr = [1, 4, 5, 2, 9, 6, 3, 7]
insertion_sort(arr)
print(arr)

def insertsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key
# Example array to sort
arr = [9, 5, 1, 4, 3]
insertsort(arr)
print("insertion sorting::", arr)  # Print the sorted array