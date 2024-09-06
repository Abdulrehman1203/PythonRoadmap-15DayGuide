def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [5, 43, 7, 8, 3, 2, 5, 31, 34, 66, 9]
print(arr)
target = int(input("Enter the target number: "))
target_index = binary_search(sorted(arr), target)

if target_index != -1:
    print(f"The target {target} is present at index : {target_index}")

